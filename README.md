# DaTatra - Data Analytics Tool

## Functionalities:

### <a href="[Main_Page.py](Main_Page.py)">Main Page</a>:
### <a href="[Data Analysis.py](Pages%2FData%20Analysis.py)">Data Analysis</a>:
### <a href="[Personal Buddy.py](Pages%2FPersonal%20Buddy.py)">Personal Buddy</a>:


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