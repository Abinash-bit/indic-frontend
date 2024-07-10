# import streamlit as st
# import requests
# import os

# # List of major Indian languages plus English
# languages = ["English", "Hindi", "Bengali", "Telugu", "Marathi", "Tamil", "Urdu", "Gujarati", "Malayalam", "Kannada", "Odia", "Punjabi", "Assamese", "Maithili", "Sanskrit"]

# # Title of the app
# st.title("Indian Languages File Uploader")

# # Create columns with spaces between them
# col1, col_space1, col2, col_space2, col3 = st.columns([2, 0.5, 6, 0.5, 3])

# # Column 1: Language selection
# with col1:
#     st.header("Language")
#     language = st.selectbox("Language", languages)

# # Column 2: File uploaders
# with col2:
#     st.header("Upload Files")
    
#     # File uploader for audio files
#     uploaded_audio = st.file_uploader("Upload an audio file", type=["wav"])
    
#     # File uploader for text files
#     uploaded_text = st.file_uploader("Upload a text file", type=["txt"])

# # Column 3: Output display
# with col3:
#     st.header("Output")
    
#     if st.button("Submit"):
#         if uploaded_audio and uploaded_text:
#             # Save uploaded files temporarily
#             audio_path = os.path.join("/tmp", uploaded_audio.name)
#             text_path = os.path.join("/tmp", uploaded_text.name)
            
#             with open(audio_path, "wb") as f:
#                 f.write(uploaded_audio.getbuffer())
            
#             with open(text_path, "wb") as f:
#                 f.write(uploaded_text.getbuffer())
            
#             try:
#                 # Call the Flask API
#                 files = {
#                     'audio': open(audio_path, 'rb'),
#                     'text': open(text_path, 'rb')
#                 }
#                 response = requests.post("http://localhost:5000/align", files=files)
                
#                 if response.status_code == 200:
#                     srt_path = "/tmp/output.srt"
#                     with open(srt_path, "wb") as f:
#                         f.write(response.content)
                    
#                     with open(srt_path, "r", encoding='utf-8') as f:
#                         srt_content = f.read()
                    
#                     st.success("Alignment completed successfully!")
#                     st.text_area("SRT Content", srt_content, height=400)
#                 else:
#                     st.error(f"Error: {response.json().get('error', 'Unknown error')}")
#             except Exception as e:
#                 st.error(f"An error occurred: {str(e)}")
#         else:
#             st.error("Please upload both audio and text files.")


# import streamlit as st
# import os
# import shutil
# import subprocess

# # Paths for dictionary and acoustic model
# dictionary_path = "/home/abinash/Documents/MFA/pretrained_models/dictionary/tamil_cv.dict"
# acoustic_model_path = "/home/abinash/Documents/MFA/pretrained_models/acoustic/tamil_cv.zip"
# output_directory = "/home/abinash/Desktop/vayu/output"

# # Function to clear and create a directory
# def clear_and_create_dir(path):
#     if os.path.exists(path):
#         shutil.rmtree(path)
#     os.makedirs(path)

# # Function to run MFA aligner within a specific conda environment
# def run_mfa_alignment(corpus_dir, dictionary_path, acoustic_model_path, output_directory):
#     command = [
#         "conda", "run", "-n", "aligner", "mfa", "align",
#         corpus_dir, dictionary_path, acoustic_model_path, output_directory
#     ]
#     result = subprocess.run(command, capture_output=True, text=True)
#     return result

# # Function to read the contents of the TextGrid file
# def read_textgrid_file(output_directory):
#     for file_name in os.listdir(output_directory):
#         if file_name.endswith(".TextGrid"):
#             with open(os.path.join(output_directory, file_name), "r") as file:
#                 return file.read()
#     return None

# # Main function for the Streamlit app
# def main():
#     st.title("File Upload and MFA Alignment")
    
#     st.write("Upload an audio file and a text file")

#     # File upload widgets
#     audio_file = st.file_uploader("Upload Audio File", type=["wav", "mp3", "m4a"])
#     text_file = st.file_uploader("Upload Text File", type=["txt"])

#     if st.button("Upload and Align Files"):
#         if audio_file is not None and text_file is not None:
#             # Clear and create the corpus directory
#             corpus_dir = "corpus"
#             clear_and_create_dir(corpus_dir)
            
#             # Save the uploaded files
#             audio_path = os.path.join(corpus_dir, audio_file.name)
#             text_path = os.path.join(corpus_dir, text_file.name)

#             with open(audio_path, "wb") as f:
#                 f.write(audio_file.getbuffer())
            
#             with open(text_path, "wb") as f:
#                 f.write(text_file.getbuffer())
            
#             st.success(f"Files uploaded successfully to {corpus_dir}")

#             # Clear the output directory
#             clear_and_create_dir(output_directory)

#             # Run the MFA alignment
#             result = run_mfa_alignment(corpus_dir, dictionary_path, acoustic_model_path, output_directory)
            
#             if result.returncode == 0:
#                 st.success("Alignment completed successfully.")
#                 st.text(result.stdout)

#                 # Read and display the contents of the TextGrid file
#                 textgrid_contents = read_textgrid_file(output_directory)
#                 if textgrid_contents:
#                     st.subheader("Output TextGrid File")
#                     st.text(textgrid_contents)
#                 else:
#                     st.error("TextGrid file not found.")
#             else:
#                 st.error("Alignment failed.")
#                 st.text(result.stderr)
#         else:
#             st.error("Please upload both an audio file and a text file")

# if __name__ == "__main__":
#     main()


# this code works fine
# import streamlit as st
# import os
# import shutil
# import subprocess
# import textgrid

# # Paths for dictionary and acoustic model
# dictionary_path = "/home/abinash/Documents/MFA/pretrained_models/dictionary/tamil_cv.dict"
# acoustic_model_path = "/home/abinash/Documents/MFA/pretrained_models/acoustic/tamil_cv.zip"
# output_directory = "/home/abinash/Desktop/vayu/output"

# # Function to clear and create a directory
# def clear_and_create_dir(path):
#     if os.path.exists(path):
#         shutil.rmtree(path)
#     os.makedirs(path)

# # Function to run MFA aligner within a specific conda environment
# def run_mfa_alignment(corpus_dir, dictionary_path, acoustic_model_path, output_directory):
#     command = [
#         "conda", "run", "-n", "aligner", "mfa", "align",
#         corpus_dir, dictionary_path, acoustic_model_path, output_directory
#     ]
#     result = subprocess.run(command, capture_output=True, text=True)
#     return result

# # Function to read the contents of the TextGrid file
# def read_textgrid_file(output_directory):
#     for file_name in os.listdir(output_directory):
#         if file_name.endswith(".TextGrid"):
#             with open(os.path.join(output_directory, file_name), "r") as file:
#                 return file.read(), os.path.join(output_directory, file_name)
#     return None, None

# # Function to convert TextGrid to SRT
# def convert_textgrid_to_srt(textgrid_file_path):
#     tg = textgrid.TextGrid.fromFile(textgrid_file_path)
#     srt_content = []
#     index = 1
#     for interval in tg[0]:
#         start_time = interval.minTime
#         end_time = interval.maxTime
#         text = interval.mark.strip()

#         if text:  # Only add intervals with text
#             start_srt = f"{int(start_time // 60):02}:{int(start_time % 60):02},{int(start_time * 1000 % 1000):03}"
#             end_srt = f"{int(end_time // 60):02}:{int(end_time % 60):02},{int(end_time * 1000 % 1000):03}"
#             srt_content.append(f"{index}\n{start_srt} --> {end_srt}\n{text}\n")
#             index += 1

#     return "\n".join(srt_content)

# # Main function for the Streamlit app
# def main():
#     st.title("File Upload and MFA Alignment")
    
#     st.write("Upload an audio file and a text file")

#     # File upload widgets
#     audio_file = st.file_uploader("Upload Audio File", type=["wav", "mp3", "m4a"])
#     text_file = st.file_uploader("Upload Text File", type=["txt"])

#     if st.button("Upload and Align Files"):
#         if audio_file is not None and text_file is not None:
#             # Clear and create the corpus directory
#             corpus_dir = "corpus"
#             clear_and_create_dir(corpus_dir)
            
#             # Save the uploaded files
#             audio_path = os.path.join(corpus_dir, audio_file.name)
#             text_path = os.path.join(corpus_dir, text_file.name)

#             with open(audio_path, "wb") as f:
#                 f.write(audio_file.getbuffer())
            
#             with open(text_path, "wb") as f:
#                 f.write(text_file.getbuffer())
            
#             st.success(f"Files uploaded successfully to {corpus_dir}")

#             # Clear the output directory
#             clear_and_create_dir(output_directory)

#             # Run the MFA alignment
#             result = run_mfa_alignment(corpus_dir, dictionary_path, acoustic_model_path, output_directory)
            
#             if result.returncode == 0:
#                 st.success("Alignment completed successfully.")
#                 st.text(result.stdout)

#                 # Read and display the contents of the TextGrid file
#                 textgrid_contents, textgrid_file_path = read_textgrid_file(output_directory)
#                 if textgrid_contents:
#                     st.subheader("Output TextGrid File")
#                     st.text(textgrid_contents)

#                     # Convert TextGrid to SRT
#                     srt_contents = convert_textgrid_to_srt(textgrid_file_path)
#                     st.subheader("Converted SRT File")
#                     st.text(srt_contents)
#                 else:
#                     st.error("TextGrid file not found.")
#             else:
#                 st.error("Alignment failed.")
#                 st.text(result.stderr)
#         else:
#             st.error("Please upload both an audio file and a text file")

# if __name__ == "__main__":
#     main()





# This code works perfectly fine
# import streamlit as st
# import os
# import shutil
# import subprocess
# import re

# # Paths for dictionary and acoustic model
# dictionary_path = "/home/abinash/Documents/MFA/pretrained_models/dictionary/tamil_cv.dict"
# acoustic_model_path = "/home/abinash/Documents/MFA/pretrained_models/acoustic/tamil_cv.zip"
# output_directory = "/home/abinash/Desktop/vayu/output"

# # Function to clear and create a directory
# def clear_and_create_dir(path):
#     if os.path.exists(path):
#         shutil.rmtree(path)
#     os.makedirs(path)

# # Function to run MFA aligner within a specific conda environment
# def run_mfa_alignment(corpus_dir, dictionary_path, acoustic_model_path, output_directory):
#     command = [
#         "conda", "run", "-n", "aligner", "mfa", "align",
#         corpus_dir, dictionary_path, acoustic_model_path, output_directory
#     ]
#     result = subprocess.run(command, capture_output=True, text=True)
#     return result

# # Function to read the contents of the TextGrid file
# def read_textgrid_file(output_directory):
#     for file_name in os.listdir(output_directory):
#         if file_name.endswith(".TextGrid"):
#             with open(os.path.join(output_directory, file_name), "r") as file:
#                 return file.read(), os.path.join(output_directory, file_name)
#     return None, None

# # Parsing TextGrid and converting it to SRT
# def parse_textgrid(textgrid_data):
#     intervals = []
#     words_tier_pattern = re.compile(r'item \[\d+\]:\s*class = "IntervalTier"\s*name = "words"[\s\S]*?intervals: size = \d+\s*([\s\S]*?)item \[\d+\]:', re.MULTILINE)
#     interval_pattern = re.compile(r"intervals \[\d+\]:\s*xmin = ([\d.]+)\s*xmax = ([\d.]+)\s*text = \"(.*?)\"", re.DOTALL)
#     words_tier = words_tier_pattern.search(textgrid_data)
#     if words_tier:
#         for match in interval_pattern.finditer(words_tier.group(1)):
#             xmin = float(match.group(1))
#             xmax = float(match.group(2))
#             text = match.group(3).strip()
#             if text:  # Only add intervals with text
#                 intervals.append((xmin, xmax, text))
#     return intervals

# def convert_to_srt_time(time_seconds):
#     hours = int(time_seconds // 3600)
#     minutes = int((time_seconds % 3600) // 60)
#     seconds = int(time_seconds % 60)
#     milliseconds = int((time_seconds % 1) * 1000)
#     return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

# def write_srt(intervals, srt_path):
#     with open(srt_path, 'w', encoding='utf-8') as srt_file:
#         for index, (start, end, text) in enumerate(intervals, start=1):
#             srt_file.write(f"{index}\n")
#             srt_file.write(f"{convert_to_srt_time(start)} --> {convert_to_srt_time(end)}\n")
#             srt_file.write(f"{text}\n\n")

# def textgrid_to_srt(textgrid_content, srt_path):
#     intervals = parse_textgrid(textgrid_content)
#     write_srt(intervals, srt_path)

# # Main function for the Streamlit app
# def main():
#     st.title("File Upload and MFA Alignment")
    
#     st.write("Upload an audio file and a text file")

#     # File upload widgets
#     audio_file = st.file_uploader("Upload Audio File", type=["wav", "mp3", "m4a"])
#     text_file = st.file_uploader("Upload Text File", type=["txt"])

#     if st.button("Upload and Align Files"):
#         if audio_file is not None and text_file is not None:
#             # Clear and create the corpus directory
#             corpus_dir = "corpus"
#             clear_and_create_dir(corpus_dir)
            
#             # Save the uploaded files
#             audio_path = os.path.join(corpus_dir, audio_file.name)
#             text_path = os.path.join(corpus_dir, text_file.name)

#             with open(audio_path, "wb") as f:
#                 f.write(audio_file.getbuffer())
            
#             with open(text_path, "wb") as f:
#                 f.write(text_file.getbuffer())
            
#             st.success(f"Files uploaded successfully to {corpus_dir}")

#             # Clear the output directory
#             clear_and_create_dir(output_directory)

#             # Run the MFA alignment
#             result = run_mfa_alignment(corpus_dir, dictionary_path, acoustic_model_path, output_directory)
            
#             if result.returncode == 0:
#                 st.success("Alignment completed successfully.")
#                 st.text(result.stdout)

#                 # Read the contents of the TextGrid file
#                 textgrid_contents, textgrid_file_path = read_textgrid_file(output_directory)
#                 if textgrid_contents:
#                     # Convert TextGrid to SRT
#                     srt_path = os.path.join(output_directory, "output.srt")
#                     textgrid_to_srt(textgrid_contents, srt_path)

#                     # Read and display the SRT file
#                     with open(srt_path, "r", encoding="utf-8") as srt_file:
#                         srt_contents = srt_file.read()
#                     st.subheader("Converted SRT File")
#                     st.text(srt_contents)
#                 else:
#                     st.error("TextGrid file not found.")
#             else:
#                 st.error("Alignment failed.")
#                 st.text(result.stderr)
#         else:
#             st.error("Please upload both an audio file and a text file")

# if __name__ == "__main__":
#     main()

# this code is working
# import streamlit as st
# import os
# import shutil
# import subprocess
# import re
# from collections import OrderedDict

# # Paths for dictionary and acoustic model
# dictionary_path = "/home/abinash/Documents/MFA/pretrained_models/dictionary/tamil_cv.dict"
# acoustic_model_path = "/home/abinash/Documents/MFA/pretrained_models/acoustic/tamil_cv.zip"
# output_directory = "/home/abinash/Desktop/vayu/output"

# # Function to clear and create a directory
# def clear_and_create_dir(path):
#     if os.path.exists(path):
#         shutil.rmtree(path)
#     os.makedirs(path)

# # Function to run MFA aligner within a specific conda environment
# def run_mfa_alignment(corpus_dir, dictionary_path, acoustic_model_path, output_directory):
#     command = [
#         "conda", "run", "-n", "aligner", "mfa", "align",
#         corpus_dir, dictionary_path, acoustic_model_path, output_directory
#     ]
#     result = subprocess.run(command, capture_output=True, text=True)
#     return result

# # Function to read the contents of the TextGrid file
# def read_textgrid_file(output_directory):
#     for file_name in os.listdir(output_directory):
#         if file_name.endswith(".TextGrid"):
#             with open(os.path.join(output_directory, file_name), "r") as file:
#                 return file.read(), os.path.join(output_directory, file_name)
#     return None, None

# # Parsing TextGrid and converting it to SRT
# def parse_textgrid(textgrid_data):
#     intervals = []
#     words_tier_pattern = re.compile(r'item \[\d+\]:\s*class = "IntervalTier"\s*name = "words"[\s\S]*?intervals: size = \d+\s*([\s\S]*?)item \[\d+\]:', re.MULTILINE)
#     interval_pattern = re.compile(r"intervals \[\d+\]:\s*xmin = ([\d.]+)\s*xmax = ([\d.]+)\s*text = \"(.*?)\"", re.DOTALL)
#     words_tier = words_tier_pattern.search(textgrid_data)
#     if words_tier:
#         for match in interval_pattern.finditer(words_tier.group(1)):
#             xmin = float(match.group(1))
#             xmax = float(match.group(2))
#             text = match.group(3).strip()
#             if text:  # Only add intervals with text
#                 intervals.append((xmin, xmax, text))
#     return intervals

# def convert_to_srt_time(time_seconds):
#     hours = int(time_seconds // 3600)
#     minutes = int((time_seconds % 3600) // 60)
#     seconds = int(time_seconds % 60)
#     milliseconds = int((time_seconds % 1) * 1000)
#     return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

# def write_srt(intervals, srt_path):
#     with open(srt_path, 'w', encoding='utf-8') as srt_file:
#         for index, (start, end, text) in enumerate(intervals, start=1):
#             srt_file.write(f"{index}\n")
#             srt_file.write(f"{convert_to_srt_time(start)} --> {convert_to_srt_time(end)}\n")
#             srt_file.write(f"{text}\n\n")

# def textgrid_to_srt(textgrid_content, srt_path):
#     intervals = parse_textgrid(textgrid_content)
#     write_srt(intervals, srt_path)

# # Parse SRT file to extract timestamps and words
# def parse_srt(srt_file):
#     with open(srt_file, 'r', encoding='utf-8') as file:
#         content = file.read()

#     pattern = re.compile(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+?)(?=\n\d+\n|\Z)', re.DOTALL)
#     matches = pattern.findall(content)

#     words_data = []
#     for match in matches:
#         index, start_time, end_time, word = match
#         words_data.append((start_time, end_time, word.strip()))

#     return words_data

# # Parse TXT file to extract sentences
# def parse_txt(txt_file):
#     with open(txt_file, 'r', encoding='utf-8') as file:
#         sentences = file.readlines()

#     sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
#     return sentences

# # Generate sentence timestamps based on word timestamps
# def generate_sentence_timestamps(words_data, sentences):
#     word_index = 0
#     sentence_data = []

#     for sentence in sentences:
#         words = sentence.split()
#         num_words = len(words)

#         if num_words == 0:
#             continue

#         start_time = words_data[word_index][0]
#         end_time = words_data[word_index + num_words - 1][1]

#         sentence_data.append((start_time, end_time, sentence))
#         word_index += num_words

#     return sentence_data

# # Write the new SRT file with sentence timestamps
# def write_new_srt(sentence_data, output_file):
#     with open(output_file, 'w', encoding='utf-8') as file:
#         for index, (start_time, end_time, sentence) in enumerate(sentence_data, start=1):
#             file.write(f"{index}\n")
#             file.write(f"{start_time} --> {end_time}\n")
#             file.write(f"{sentence}\n\n")

# # Main function for the Streamlit app
# def main():
#     st.title("File Upload and MFA Alignment")
    
#     st.write("Upload an audio file and a text file")

#     # File upload widgets
#     audio_file = st.file_uploader("Upload Audio File", type=["wav", "mp3", "m4a"])
#     text_file = st.file_uploader("Upload Text File", type=["txt"])

#     if st.button("Upload and Align Files"):
#         if audio_file is not None and text_file is not None:
#             # Clear and create the corpus directory
#             corpus_dir = "corpus"
#             clear_and_create_dir(corpus_dir)
            
#             # Save the uploaded files
#             audio_path = os.path.join(corpus_dir, audio_file.name)
#             text_path = os.path.join(corpus_dir, text_file.name)

#             with open(audio_path, "wb") as f:
#                 f.write(audio_file.getbuffer())
            
#             with open(text_path, "wb") as f:
#                 f.write(text_file.getbuffer())
            
#             st.success(f"Files uploaded successfully to {corpus_dir}")

#             # Clear the output directory
#             clear_and_create_dir(output_directory)

#             # Run the MFA alignment
#             result = run_mfa_alignment(corpus_dir, dictionary_path, acoustic_model_path, output_directory)
            
#             if result.returncode == 0:
#                 st.success("Alignment completed successfully.")
#                 st.text(result.stdout)

#                 # Read the contents of the TextGrid file
#                 textgrid_contents, textgrid_file_path = read_textgrid_file(output_directory)
#                 if textgrid_contents:
#                     # Convert TextGrid to SRT
#                     srt_path = os.path.join(output_directory, "output.srt")
#                     textgrid_to_srt(textgrid_contents, srt_path)

#                     # Read the SRT file and the TXT file
#                     words_data = parse_srt(srt_path)
#                     sentences = parse_txt(text_path)

#                     # Generate sentence timestamps
#                     sentence_data = generate_sentence_timestamps(words_data, sentences)

#                     # Write the new SRT file
#                     new_srt_path = os.path.join(output_directory, "aligned_output.srt")
#                     write_new_srt(sentence_data, new_srt_path)

#                     # Read and display the new SRT file
#                     with open(new_srt_path, "r", encoding="utf-8") as srt_file:
#                         srt_contents = srt_file.read()
#                     st.subheader("Aligned SRT File")
#                     st.text(srt_contents)
#                 else:
#                     st.error("TextGrid file not found.")
#             else:
#                 st.error("Alignment failed.")
#                 st.text(result.stderr)
#         else:
#             st.error("Please upload both an audio file and a text file")

# if __name__ == "__main__":
#     main()


import streamlit as st
import os
import shutil
import subprocess
import re
from collections import OrderedDict

# Paths for dictionary and acoustic model
pretrained_models_path = "/home/abinash/Documents/MFA/pretrained_models"
languages = {
    "Tamil": {
        "dictionary": os.path.join(pretrained_models_path, "dictionary/tamil_cv.dict"),
        "acoustic_model": os.path.join(pretrained_models_path, "acoustic/tamil_cv.zip"),
    }
}
output_directory = "/home/abinash/Desktop/wds2.0"

# Function to clear and create a directory
def clear_and_create_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

# Function to run MFA aligner within a specific conda environment
def run_mfa_alignment(corpus_dir, dictionary_path, acoustic_model_path, output_directory):
    command = [
        "conda", "run", "-n", "aligner", "mfa", "align",
        corpus_dir, dictionary_path, acoustic_model_path, output_directory
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    return result

# Function to read the contents of the TextGrid file
def read_textgrid_file(output_directory):
    for file_name in os.listdir(output_directory):
        if file_name.endswith(".TextGrid"):
            with open(os.path.join(output_directory, file_name), "r") as file:
                return file.read(), os.path.join(output_directory, file_name)
    return None, None

# Parsing TextGrid and converting it to SRT
def parse_textgrid(textgrid_data):
    intervals = []
    words_tier_pattern = re.compile(r'item \[\d+\]:\s*class = "IntervalTier"\s*name = "words"[\s\S]*?intervals: size = \d+\s*([\s\S]*?)item \[\d+\]:', re.MULTILINE)
    interval_pattern = re.compile(r"intervals \[\d+\]:\s*xmin = ([\d.]+)\s*xmax = ([\d.]+)\s*text = \"(.*?)\"", re.DOTALL)
    words_tier = words_tier_pattern.search(textgrid_data)
    if words_tier:
        for match in interval_pattern.finditer(words_tier.group(1)):
            xmin = float(match.group(1))
            xmax = float(match.group(2))
            text = match.group(3).strip()
            if text:  # Only add intervals with text
                intervals.append((xmin, xmax, text))
    return intervals

def convert_to_srt_time(time_seconds):
    hours = int(time_seconds // 3600)
    minutes = int((time_seconds % 3600) // 60)
    seconds = int(time_seconds % 60)
    milliseconds = int((time_seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

def write_srt(intervals, srt_path):
    with open(srt_path, 'w', encoding='utf-8') as srt_file:
        for index, (start, end, text) in enumerate(intervals, start=1):
            srt_file.write(f"{index}\n")
            srt_file.write(f"{convert_to_srt_time(start)} --> {convert_to_srt_time(end)}\n")
            srt_file.write(f"{text}\n\n")

def textgrid_to_srt(textgrid_content, srt_path):
    intervals = parse_textgrid(textgrid_content)
    write_srt(intervals, srt_path)

# Parse SRT file to extract timestamps and words
def parse_srt(srt_file):
    with open(srt_file, 'r', encoding='utf-8') as file:
        content = file.read()

    pattern = re.compile(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+?)(?=\n\d+\n|\Z)', re.DOTALL)
    matches = pattern.findall(content)

    words_data = []
    for match in matches:
        index, start_time, end_time, word = match
        words_data.append((start_time, end_time, word.strip()))

    return words_data

# Parse TXT file to extract sentences
def parse_txt(txt_file):
    with open(txt_file, 'r', encoding='utf-8') as file:
        sentences = file.readlines()

    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return sentences

# Generate sentence timestamps based on word timestamps
def generate_sentence_timestamps(words_data, sentences):
    word_index = 0
    sentence_data = []

    for sentence in sentences:
        words = sentence.split()
        num_words = len(words)

        if num_words == 0:
            continue

        start_time = words_data[word_index][0]
        end_time = words_data[word_index + num_words - 1][1]

        sentence_data.append((start_time, end_time, sentence))
        word_index += num_words

    return sentence_data

# Write the new SRT file with sentence timestamps
def write_new_srt(sentence_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for index, (start_time, end_time, sentence) in enumerate(sentence_data, start=1):
            file.write(f"{index}\n")
            file.write(f"{start_time} --> {end_time}\n")
            file.write(f"{sentence}\n\n")

# Main function for the Streamlit app
def main():
    st.title("File Upload and MFA Alignment")
    
    st.write("Upload an audio file and a text file")

    # Dropdown for language selection
    language = st.selectbox("Select Language", options=list(languages.keys()))
    
    # File upload widgets
    audio_file = st.file_uploader("Upload Audio File", type=["wav", "mp3", "m4a"])
    text_file = st.file_uploader("Upload Text File", type=["txt"])

    if st.button("Upload and Align Files"):
        if audio_file is not None and text_file is not None:
            # Clear and create the corpus directory
            corpus_dir = "corpus"
            clear_and_create_dir(corpus_dir)
            
            # Save the uploaded files
            audio_path = os.path.join(corpus_dir, audio_file.name)
            text_path = os.path.join(corpus_dir, text_file.name)

            with open(audio_path, "wb") as f:
                f.write(audio_file.getbuffer())
            
            with open(text_path, "wb") as f:
                f.write(text_file.getbuffer())
            
            st.success(f"Files uploaded successfully to {corpus_dir}")

            # Clear the output directory
            clear_and_create_dir(output_directory)

            # Get the dictionary and acoustic model paths based on the selected language
            dictionary_path = languages[language]["dictionary"]
            acoustic_model_path = languages[language]["acoustic_model"]

            # Run the MFA alignment
            result = run_mfa_alignment(corpus_dir, dictionary_path, acoustic_model_path, output_directory)
            
            if result.returncode == 0:
                st.success("Alignment completed successfully.")
                st.text(result.stdout)

                # Read the contents of the TextGrid file
                textgrid_contents, textgrid_file_path = read_textgrid_file(output_directory)
                if textgrid_contents:
                    # Convert TextGrid to SRT
                    srt_path = os.path.join(output_directory, "output.srt")
                    textgrid_to_srt(textgrid_contents, srt_path)

                    # Read the SRT file and the TXT file
                    words_data = parse_srt(srt_path)
                    sentences = parse_txt(text_path)

                    # Generate sentence timestamps
                    sentence_data = generate_sentence_timestamps(words_data, sentences)

                    # Write the new SRT file
                    new_srt_path = os.path.join(output_directory, "aligned_output.srt")
                    write_new_srt(sentence_data, new_srt_path)

                    # Read and display the new SRT file
                    with open(new_srt_path, "r", encoding="utf-8") as srt_file:
                        srt_contents = srt_file.read()
                    st.subheader("Aligned SRT File")
                    st.text(srt_contents)
                else:
                    st.error("TextGrid file not found.")
            else:
                st.error("Alignment failed.")
                st.text(result.stderr)
        else:
            st.error("Please upload both an audio file and a text file")

if __name__ == "__main__":
    main()




