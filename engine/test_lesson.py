from workflow_parser.parser import (
    WorkflowParser
)

from workflow_parser.analyzer import (
    WorkflowAnalyzer
)

from workflow_parser.knowledge_loader import (
    NodeKnowledgeLoader
)

from lesson_generator.generator import (
    LessonGenerator
)

from pathlib import Path

# 用 __file__ 定位项目根目录，保证从任意工作目录运行都能找到文件。
root = Path(__file__).resolve().parent.parent



loader = NodeKnowledgeLoader(

    root
    / "comfyui_library"
    / "knowledge"

)



parser = WorkflowParser(

    loader

)



workflow = parser.parse(

    str(
        root
        / "comfyui_library"
        / "workflows"
        / "sd1.5"
        / "basic.json"
    )

)



workflow = WorkflowAnalyzer().analyze(

    workflow

)



lesson = LessonGenerator().generate(
    workflow
)



print(
    lesson.title
)



for section in lesson.sections:


    print(
        "\n##",
        section.title
    )


    print(
        section.content
    )


    print(
        "练习:"
    )


    for e in section.exercises:

        print(
            "-",
            e
        )


print("\nLearning Topics:")

for topic in lesson.learning_topics:

    print("-", topic)
