Quickstart
==========
1. **Create a virtual environment**

   Create a virtual environment and enter it with commands
   .. code-block:: bash
      
      python -m venv venv

   .. code-block:: bash

      source venv/bin/activate
      
2. **Install Dependencies:**

   Install the required dependencies by running:

   .. code-block:: bash

      pip install -r requirements.txt

2. **Prepare File JSON with questions:**

   Create a JSON file containing the test questions and options, called `questions.json`. JSON file must be such structure:
   ``"Question text": ["First option", "Second option", ..]``

3. **Run the test:**

   Execute the test by running the following command:

   .. code-block:: bash

      python main.py

   Follow the on-screen instructions to answer the questions. The test will calculate and display the final result.
