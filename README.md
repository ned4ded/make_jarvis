**Title:** Build Your Own Jarvis

**Objectives:**

Basic Solution (60 points):

* **Understanding Language Models Integration** - Learn how to incorporate and manage language models in your project to process and understand user input (10 points).
* **Handling Dialogue** - Develop the capability to manage and sustain interactive dialogues with users (20 points).
* **Voice Recognition Integration** - Integrate voice recognition technologies to interpret spoken commands (20 points).
* **Voice Generation Integration** - Enable your system to respond audibly using synthesized speech (20 points).

Further Enhancements:

* **Voice Cloning** - Implement voice cloning to personalize the system’s voice to the user or to mimic other voices (30 points).
* **Video Generation with Lip Sync** - Create video outputs that include lip-syncing to make interactions appear more natural and engaging  (30 points).
* **Add Long-term Memory with PEFT** - Implement Predictive Efficiently Indexed Feature Tracking (PEFT) for a more robust and scalable memory system  (30 points).
* **Add Long-term Memory with an Updatable Database** - Incorporate a dynamic database system to retain and recall past interactions and information  (20 points).
* **Add Short-term Memory** - Develop short-term memory capabilities to remember the context of ongoing sessions  (10 points).
* **Add Routing and Tools** - Implement systems to manage and route tasks to appropriate tools or sub-systems  (10 points).
* **Add Routing and Actions** - Develop routing logic to direct actions based on user commands or system decisions  (10 points).
* **Add Planning and Goals** - Integrate planning capabilities to set, manage, and achieve short-term and long-term goals  (20 points).

Homework involves assembling your constructor from various parts and making it all work together by scripting in Python. Your main challenge will focus on optimizing for performance and determining which features to prioritize for speed.

Starting article with theory: [Agent Foundations](https://lilianweng.github.io/posts/2023-06-23-agent/)

**Project Structure**

Recommended Constructor Details:

1) **LLM Deployment:** It's convenient to use `llama.cpp` (https://github.com/ggerganov/llama.cpp) or `ollama` (https://ollama.com/). APIs from Replicate or OpenAI can also be explored, or you can set up your own model. Starting with simpler models like Gemma-2b or quantized 7b or 13b is advisable due to their lower computational demands. Remember to balance API speed and cost.
2) **A Wake Word:** Utilize [Choosing a Wake Word](https://picovoice.ai/docs/tips/choosing-a-wake-word/) with options like Athena in Italian model for consistent voice recognition. Whisper could also be an alternative for wake word detection.
3) **Voice Recognition:** Employ various versions of Whisper for efficient and robust voice recognition capabilities:
   - https://github.com/ggerganov/whisper.cpp
   - https://github.com/Vaibhavs10/insanely-fast-whisper
   - https://replicate.com/vaibhavs10/incredibly-fast-whisper?input=cog
   Ensure you check out installation guides for necessary codecs.
4) **Voice Generation:** Explore voice synthesis technologies to create natural-sounding speech:
   - https://replicate.com/cjwbw/openvoice
   - https://replicate.com/lucataco/xtts-v2
5) **Dialogue Logic:** Writing your own logic or using platforms like LangChain (https://www.langchain.com/) can enhance conversational capabilities.
6) **Memory Organization:** Use tools like LlamaIndex (https://www.llamaindex.ai/) for memory organization or again, LangChain for integrating memory into dialogue systems.
7) **Lip Sync:** Use technologies like wav2lip for lip-syncing. Consider recent forks for improved performance.

**Assessment**

* **Video with Demonstration:** Submit your video demonstrating your Jarvis.
* **Project Code:** Submit your code demonstrating the implementation.

**Tips**

* **Start Simple:** Begin with a small set of functions. E.g., start only with LLM chat or only STT.
* **Iterate:** Gradually introduce more complex parts.

**Important Notes**

* **Computational Resources:** Whisper LLM and Gemma-2b can be computationally light, but other parts probably can be heavy.

Let me know if you'd like adjustments in difficulty level or would like to focus on specific aspects of these technologies!

Later I will share the reference implementation.

### Setup
Install ffmpeg globally. 

### About
A short description of the project.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
