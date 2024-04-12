import pandas as pd
import openai
import time
import re
import numpy as np

def extract_wait_time(error_message):
    # Example to extract wait time from the message, adjust according to the actual format
    match = re.search(r"Please try again in ([\d.]+)s", str(error_message))
    if match:
        return float(match.group(1))
    else:
        return 1  # Default wait time if not specified


def safe_api_call(call_function, *args, **kwargs):
    try:
        return call_function(*args, **kwargs)
    except Exception as e:
        if "Rate limit reached" in str(e):
            wait_time = extract_wait_time(e) + 1  # Adding a small buffer time
            print(f"Rate limit reached. Waiting for {wait_time} seconds before retrying...")
            time.sleep(wait_time)
            return safe_api_call(call_function, *args, **kwargs)  # Retry the function call with the same arguments
        else:
            print(f"An error occurred: {e}")
            return "Error: Unable to analyze"



# Setup OpenAI API key
openai.api_key = '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'

# The list of specific emotions to consider
emotions_list = [
    "Inspired", "Amused", "Informed", "Curious", "Hopeful"
    , "Moved", "Surprised", "Impressed", "Fulfilled", "Sad"
]


def analyze_text_emotion_chat(text):
    # Create a prompt that includes the specific list of emotions
    emotions_prompt = ", ".join([f'"{emotion}"' for emotion in emotions_list[:-1]]) + ", or " + f'"{emotions_list[-1]}"'
    prompt = f"""Given the following text excerpt, evaluate the likelihood of each of the following emotions being conveyed to the audience: {emotions_prompt}. Assign a score from 0.0 to 1.0 to each emotion based on its relevance, where 1.0 represents the highest likelihood of being evoked. Then, list the top three emotions with their scores in descending order of likelihood in JSON format.

    Make sure you only use the emotions provided in the list: ["Inspired", "Amused", "Informed", "Curious", "Hopeful"
    , "Moved", "Surprised", "Impressed", "Fulfilled", "Sad"]
    And give me the top three emotions and their scores in the following JSON format:
    {{"Inspired": 0.9, "Curious": 0.75, "Amused": 0.5}}
    Do not include any other information in the response.

    Text excerpt: \"{text}\""""
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        # Assuming the model returns a well-structured response, parse it here
        # This step might need to be adjusted based on the actual response format
        return response.choices[0].message['content']
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error: Unable to analyze"

# Load the CSV file into a DataFrame
# df = pd.read_csv('data/data_transcript_fully_processed.csv')
df = pd.read_csv('/Users/taeeunkwon/Downloads/vscode_projects/data/data_transcript_fully_processed.csv')

# Define the output CSV path
# output_csv_path = 'data/updated_transcripts_with_emotions_v2.csv'
output_csv_path = '/Users/taeeunkwon/Downloads/vscode_projects/data/updated_transcripts_with_emotions_v2_pt.3.csv'

# Initialize the CSV file with the current DataFrame structure if the file doesn't exist
df[:0].to_csv(output_csv_path, index=False)  # Save only the header initially

# Process the DataFrame in chunks of 30 rows
chunk_size = 10
for start in range(2000, len(df), chunk_size):
    end = start + chunk_size
    print(f"Processing rows {start} to {end}")
    for index, row in df.iloc[start:end].iterrows():
        if pd.isna(row['processed_transcript']):
            df.at[index, 'detected_emotion'] = np.nan  # Using numpy's NaN representation
        else:
            emotion_analysis = safe_api_call(analyze_text_emotion_chat, row['processed_transcript'])
            df.at[index, 'detected_emotion'] = emotion_analysis

    # Save the processed chunk to the CSV file
    # Use mode='a' to append and header=False to not repeat the header
    df.iloc[start:end].to_csv(output_csv_path, mode='a', header=False, index=False)
    print(f"Saved rows {start} to {end} to {output_csv_path}")

    # Optional: Wait a bit before processing the next chunk
    time.sleep(10)  # Adjust based on your needs and rate limits

print(f"Processing complete. Data saved to {output_csv_path}")