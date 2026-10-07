---
key: comfyui-workflow-templates-json/image_z_image_turbo_fun_union_controlnet.json
name: image_z_image_turbo_fun_union_controlnet
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_z_image_turbo_fun_union_controlnet.json
hash: 617c27df391c122b
official: true
coverage: 0.5
learned_at: 2026-10-07 21:36:06
nodes: [ImageScaleToMaxDimension, LoadImage, PreviewImage, MarkdownNote, Canny, SaveImage, e87b26c4-6b14-4040-bad6-063536f6fbea, MarkdownNote]
patterns: []
missing: [e87b26c4-6b14-4040-bad6-063536f6fbea]
discoveries: [次要节点 `e87b26c4-6b14-4040-bad6-063536f6fbea` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_z_image_turbo_fun_union_controlnet.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_z_image_turbo_fun_union_controlnet.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（8 个）：
- `ImageScaleToMaxDimension`
- `LoadImage`
- `PreviewImage`
- `MarkdownNote`
- `Canny`
- `SaveImage`
- `e87b26c4-6b14-4040-bad6-063536f6fbea`
- `MarkdownNote`

## 知识

覆盖率 **50%**（4/8）

**有卡**：`ImageScaleToMaxDimension`、`LoadImage`、`Canny`、`SaveImage`

**缺卡**（1）：`e87b26c4-6b14-4040-bad6-063536f6fbea`

**用到的条目**：LoadImage、Canny、SaveImage、ImageScaleToMaxDimension、sd15-t2i-basic、sd15-t2i-lora、ImageScale、scale

## 学习发现

- 次要节点 `e87b26c4-6b14-4040-bad6-063536f6fbea` 知识库中没有该节点类型的任何知识
