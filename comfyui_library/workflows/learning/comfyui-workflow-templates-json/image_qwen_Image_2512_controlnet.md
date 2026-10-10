---
key: comfyui-workflow-templates-json/image_qwen_Image_2512_controlnet.json
name: image_qwen_Image_2512_controlnet
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_Image_2512_controlnet.json
hash: 1fdfa3828059a771
official: true
coverage: 0.555556
learned_at: 2026-10-10 22:48:26
nodes: [ResizeImageMaskNode, GetImageSize, LoadImage, MarkdownNote, 3f445b89-990a-4475-aec8-84ce536527f7, SaveImage, MarkdownNote, PreviewImage, Canny]
patterns: []
missing: [3f445b89-990a-4475-aec8-84ce536527f7]
discoveries: [次要节点 `3f445b89-990a-4475-aec8-84ce536527f7` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_qwen_Image_2512_controlnet.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_Image_2512_controlnet.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `ResizeImageMaskNode`
- `GetImageSize`
- `LoadImage`
- `MarkdownNote`
- `3f445b89-990a-4475-aec8-84ce536527f7`
- `SaveImage`
- `MarkdownNote`
- `PreviewImage`
- `Canny`

## 知识

覆盖率 **56%**（5/9）

**有卡**：`ResizeImageMaskNode`、`GetImageSize`、`LoadImage`、`SaveImage`、`Canny`

**缺卡**（1）：`3f445b89-990a-4475-aec8-84ce536527f7`

**用到的条目**：LoadImage、Canny、GetImageSize、ResizeImageMaskNode、GetImageSize、SaveImage、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `3f445b89-990a-4475-aec8-84ce536527f7` 知识库中没有该节点类型的任何知识
