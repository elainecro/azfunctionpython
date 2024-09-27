import azure.functions as func
import logging

app = func.FunctionApp()

@app.function_name(name="FilaPowerAutomate")
@app.queue_trigger(arg_name="azqueue", queue_name="queuepowerautomate",  connection="AzureWebJobsStorage") 
def azfpowerautomatequeue(azqueue: func.QueueMessage):
    logging.info('Python Queue trigger processed a message: %s', azqueue.get_body().decode('utf-8'))

@app.function_name(name="FilaHttp")
@app.route(route="req")
def main(req: func.HttpRequest) -> str:
    user = req.params.get("user")
    return f"Hello, {user}!"