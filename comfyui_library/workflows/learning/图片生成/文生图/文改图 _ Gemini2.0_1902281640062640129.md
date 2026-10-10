---
key: 文改图 _ Gemini2.0_1902281640062640129.json
name: 文改图 _ Gemini2.0_1902281640062640129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文改图 _ Gemini2.0_1902281640062640129.json
hash: 15edbac06a801260
coverage: 0.461538
learned_at: 2026-10-10 20:59:45
nodes: [LoadImage, easy imageSize, DeepTranslatorTextNode, ShowText|pysssss, Google-Gemini-PL, Textbox, ShowText|pysssss, CR Text Concatenate, Textbox, easy imageSize, PreviewImage, SaveImage, Gemini_Flash_200_Exp]
patterns: []
missing: [CR Text Concatenate, Google-Gemini-PL, easy imageSize, easy imageSize]
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Google-Gemini-PL` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 文改图 _ Gemini2.0_1902281640062640129.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文改图 _ Gemini2.0_1902281640062640129.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（13 个）：
- `LoadImage`
- `easy imageSize`
- `DeepTranslatorTextNode`
- `ShowText|pysssss`
- `Google-Gemini-PL`
- `Textbox`
- `ShowText|pysssss`
- `CR Text Concatenate`
- `Textbox`
- `easy imageSize`
- `PreviewImage`
- `SaveImage`
- `Gemini_Flash_200_Exp`

## 知识

覆盖率 **46%**（6/13）

**有卡**：`LoadImage`、`DeepTranslatorTextNode`、`Textbox`、`SaveImage`、`Gemini_Flash_200_Exp`

**缺卡**（4）：`CR Text Concatenate`、`Google-Gemini-PL`、`easy imageSize`、`easy imageSize`

**用到的条目**：LoadImage、SaveImage、Textbox、DeepTranslatorTextNode、TextBox、Gemini_Flash_200_Exp、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Google-Gemini-PL` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
