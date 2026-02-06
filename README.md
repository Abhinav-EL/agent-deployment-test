# Agentic Deployment Testing Project

Test AI Agent deployment using Google GCP and ADK. This is based on the Kaggle course.


## Setup

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Google Cloud:
    Agent Engine is needed to confirm agent deployment.
    ```bash
    brew update && brew install --cask google-cloud-sdk
    pip install --upgrade "google-cloud-aiplatform[agent_engines,adk]"
    ```

5. Login account
    ```bash
    gcloud auth application-default login
    ```


## Agent

1. Build a new Agent. This example uses Weather App agent using fake data.

2. Push the Agent to GCP:
    ```bash
    adk deploy agent_engine --project=$PROJECT_ID --region=us-east4 weather-agent/weather_agent --agent_engine_config_file=weather-agent/weather_agent/agent_engine_config.json --trace_to_cloud
    ```
    Once the deployment is complete, confirm on the gcp web console.

3. Test Deployment Using Python:
    Use google-cloud-sdk to test the deployment. This test finds the last deployed Agent using agent_engines. https://console.cloud.google.com/vertex-ai/agents/agent-engines
    ```bash
    python agentic-tests/test_main.py
    ```

    Method to run
    ```python
    await test_deployment.test_agent_deployment()
    ```

4. Cleanup Deployment:
    Must cleanup otherwise potential for charge.
    ```bash
    python agentic-tests/test_main.py
    ```
    Method
    ```python
    await test_deployment.cleanup_deployed_agents()
    ```

5. Evaluate Agent repsonses:
    Using data in weather_agent_eval_v2.test.json. Built using (some outdated info), https://google.github.io/adk-docs/evaluate/#first-approach-using-a-test-file
    ```bash
    pytest weather-agent/eval/test_eval.py
    ```