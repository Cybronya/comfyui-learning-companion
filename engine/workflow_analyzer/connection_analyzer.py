class ConnectionAnalyzer:



    def analyze(
        self,
        graph
    ):


        connections=[]



        for edge in graph.edges:


            source = graph.nodes.get(
                edge.source
            )


            target = graph.nodes.get(
                edge.target
            )


            if not source or not target:

                continue



            connections.append(

            {

            "from":

            source.node_type,


            "to":

            target.node_type,


            "data":

            edge.data_type

            }

            )



        return connections
