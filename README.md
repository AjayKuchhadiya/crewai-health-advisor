### README

# Health Advisor Agents

This project implements a system of AI agents designed to assist in healthcare tasks, such as summarizing medical reports, finding relevant medical articles, and providing health recommendations based on extracted data. The project uses the `crewai` library to define agents and tasks, and the `langchain_groq` library for natural language processing capabilities.

## Approach

1. **Agent Definition**:
    - Three main agents are defined: `Pathologist`, `Medical Researcher`, and `Doctor`.
    - Each agent is assigned a specific role, goal, and backstory, and is powered by the `ChatGroq` language model.
    - The agents can perform tasks sequentially, retaining memory and context across tasks.

2. **Task Definition**:
    - Tasks are defined in the `tasks.py` file and include:
        - **Reading and summarizing the blood test report**.
        - **Finding relevant health articles**.
        - **Providing health recommendations**.

3. **PDF Text Extraction**:
    - The project includes functionality to extract text from a PDF document, representing a medical report.

4. **Crew Execution**:
    - A crew is formed with the defined agents and tasks, and the execution process is managed in `main.py`.


### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-repo/health-advisor-agents.git
    cd health-advisor-agents
    cd assignment 
    ```

2. **Install Dependencies**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
    - Create a `.env` file in the root directory of the project.
    - Add your API keys and other configurations:
      ```
      GROQ_API_KEY=your_groq_api_key
      SERPER_API_KEY=your_serper_api_key
      ```

### Running the Application

1. **Prepare a PDF File**:
    - Ensure you have a PDF file containing the blood test report. You can place it in the root directory or specify its path.

2. **Execute the Script**:
    ```bash
    python main.py path_to_your_pdf_file.pdf
    ```

    Replace `path_to_your_pdf_file.pdf` with the path to your PDF file.

3. **Output**:
    - The script will print the results, including the summary of the blood test report, relevant articles, and health recommendations. It will also save the outputs to specified files (`blood_report_summary.txt`, `health_articles_urls.txt`, `health_recommendations.txt`).
