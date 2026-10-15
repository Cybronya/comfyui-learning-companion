---
key: comfyui-workflow-templates-json/image_qwen_Image_2512_controlnet.json
name: image_qwen_Image_2512_controlnet
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_Image_2512_controlnet.json
hash: 1fdfa3828059a771
official: true
coverage: 0.666667
learned_at: 2026-10-15 22:24:54
nodes: [ResizeImageMaskNode, GetImageSize, LoadImage, MarkdownNote, 3f445b89-990a-4475-aec8-84ce536527f7, SaveImage, MarkdownNote, PreviewImage, Canny]
patterns: []
missing: []
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

覆盖率 **67%**（6/9）

**有卡**：`ResizeImageMaskNode`、`GetImageSize`、`LoadImage`、`3f445b89-990a-4475-aec8-84ce536527f7`、`SaveImage`、`Canny`

**用到的条目**：LoadImage、Canny、GetImageSize、ResizeImageMaskNode、GetImageSize、SaveImage、3f445b89-990a-4475-aec8-84ce536527f7、sd15-t2i-basic
