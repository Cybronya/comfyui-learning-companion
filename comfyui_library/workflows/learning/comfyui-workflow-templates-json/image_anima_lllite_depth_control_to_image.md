---
key: comfyui-workflow-templates-json/image_anima_lllite_depth_control_to_image.json
name: image_anima_lllite_depth_control_to_image
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_anima_lllite_depth_control_to_image.json
hash: d46cfa6b0a7784f1
official: true
coverage: 0.555556
learned_at: 2026-10-10 22:47:24
nodes: [MarkdownNote, SaveImage, GetImageSize, ImageCompare, 147b517e-5ea6-4fba-84f7-46851be6e4ce, LoadImage, PreviewImage, 28eb0ec0-5d35-42e9-8cb3-d1161dc5a231, ResizeImageMaskNode]
patterns: []
missing: [147b517e-5ea6-4fba-84f7-46851be6e4ce, 28eb0ec0-5d35-42e9-8cb3-d1161dc5a231]
discoveries: [次要节点 `147b517e-5ea6-4fba-84f7-46851be6e4ce` 知识库中没有该节点类型的任何知识, 次要节点 `28eb0ec0-5d35-42e9-8cb3-d1161dc5a231` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_anima_lllite_depth_control_to_image.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_anima_lllite_depth_control_to_image.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `MarkdownNote`
- `SaveImage`
- `GetImageSize`
- `ImageCompare`
- `147b517e-5ea6-4fba-84f7-46851be6e4ce`
- `LoadImage`
- `PreviewImage`
- `28eb0ec0-5d35-42e9-8cb3-d1161dc5a231`
- `ResizeImageMaskNode`

## 知识

覆盖率 **56%**（5/9）

**有卡**：`SaveImage`、`GetImageSize`、`ImageCompare`、`LoadImage`、`ResizeImageMaskNode`

**缺卡**（2）：`147b517e-5ea6-4fba-84f7-46851be6e4ce`、`28eb0ec0-5d35-42e9-8cb3-d1161dc5a231`

**用到的条目**：LoadImage、GetImageSize、ResizeImageMaskNode、GetImageSize、SaveImage、ImageCompare、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `147b517e-5ea6-4fba-84f7-46851be6e4ce` 知识库中没有该节点类型的任何知识
- 次要节点 `28eb0ec0-5d35-42e9-8cb3-d1161dc5a231` 知识库中没有该节点类型的任何知识
