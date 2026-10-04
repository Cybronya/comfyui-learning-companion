from .models import (
    Lesson,
    LessonSection
)


from .templates import (
    NODE_LESSON_TEMPLATES
)



class LessonGenerator:



    def generate(
        self,
        workflow
    ):


        sections=[]



        for node in workflow.nodes:


            template = (
                NODE_LESSON_TEMPLATES
                .get(
                    node.node_type
                )
            )


            if template:


                sections.append(

                    LessonSection(

                        title=
                        template["title"],


                        content=
                        template["content"],


                        exercises=
                        template["exercise"]

                    )

                )



        return Lesson(

            title=

            self.create_title(
                workflow
            ),


            workflow_type=
            workflow.task_type,


            sections=sections,


            learning_topics=
            workflow.learning_topics

        )




    def create_title(
        self,
        workflow
    ):


        return (

            f"{workflow.task_type}"
            " Workflow 学习课程"

        )
