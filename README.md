# DaTatra - Data Analytics Tool

## Functionalities:

### <a href="Main_Page.py">Main Page</a>:

Data analysis dashboard for building and evaluating a Random Forest regression model, allowing users to upload a CSV dataset, adjust model hyperparameters, and visualize performance metrics.

### <a href="Pages%2FData%20Analysis.py">Data Analysis</a>:

Dashboard where users can upload a CSV file, select parameters, and choose chart types to generate interactive visualizations (line, bar, area, scatter, pie) using Plotly Express, with the ability to filter data and view statistics for the filtered dataset.

### <a href="Pages%2FPersonal%20Buddy.py">Personal Buddy</a>:

ChatBot using OpenAI's GPT-3.5-turbo model. Users can input messages in a chat interface, and the ChatBot responds by making calls to the OpenAI Chat API, updating the conversation history and displaying the assistant's replies in real-time.


## Instruction to run:

After installing all require libraries run this command

```text
streamlit run Main_Page.py
```

__Note__: To be able to run the `Personal Buddy`tab, you have to create an `OPENAI_API_KEY` from OpenAI webstite,
once you created a key, create in the project directory called `.streamlit` and within this directory file called `secrets.toml` with this line in it:

```toml
OPENAI_API_KEY = "<YOUR_PRIVATE_KEY>"
```