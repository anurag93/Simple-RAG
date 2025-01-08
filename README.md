# Simple-RAG
Building a Simple RAG

We will create a sentence search and retrieval system:
1) Every sentence will be identified with the Capital letters in them
2) When the user inserts data, the data will be in this form
    {
        data: {
            page_no: [sentences]
        }
    }
3) This data would then get annotated as per the criteria in point 1
4) The system will then serve and listen for the user input for finding the relevant data

Phase 1:
1) We will look for sentences where the word occurs and the associated page number


Phase 2:
1) Find me the page in which the word occurs the most