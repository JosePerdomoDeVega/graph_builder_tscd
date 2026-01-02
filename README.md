### Graph Service Query (GSQ)

Graph Service Query (GSQ) is the public-facing module of the system. It exposes a REST API that allows users to submit graph-related queries over a word-based graph.

This module is responsible for handling all external interactions and acts as an orchestration layer between clients and the internal processing services. GSQ validates incoming requests, persists request metadata for auditing and analysis purposes, and delegates computationally intensive tasks to asynchronous workers through a message queue.

To avoid blocking clients during long-running operations, GSQ follows an asynchronous request model. Each request includes a callback URL where the final result will be delivered once processing is complete. GSQ ensures that results returned by internal services are correctly associated with the original request and forwarded to the appropriate callback endpoint.

GSQ also stores both requests and responses in a datalake, enabling traceability, debugging, and future analytical use cases. As the single externally exposed component, it centralizes concerns such as input validation, error handling, and request tracking.
