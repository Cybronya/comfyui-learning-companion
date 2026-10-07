---
key: comfyui-workflow-templates-json/image_qwen_image_layered.json
name: image_qwen_image_layered
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_layered.json
hash: c93da5dffc492d73
official: true
coverage: 0.444444
learned_at: 2026-10-07 21:36:02
nodes: [MarkdownNote, LoadImage, SaveImage, ImageScaleToMaxDimension, PrimitiveStringMultiline, MarkdownNote, SaveImage, f754a936-daaf-4b6e-9658-41fdc54d301d, 1ea4fa01-a81b-4420-a03c-f60019e69a92]
patterns: []
missing: [1ea4fa01-a81b-4420-a03c-f60019e69a92, f754a936-daaf-4b6e-9658-41fdc54d301d]
discoveries: [次要节点 `1ea4fa01-a81b-4420-a03c-f60019e69a92` 知识库中没有该节点类型的任何知识, 次要节点 `f754a936-daaf-4b6e-9658-41fdc54d301d` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_qwen_image_layered.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_qwen_image_layered.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `MarkdownNote`
- `LoadImage`
- `SaveImage`
- `ImageScaleToMaxDimension`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `SaveImage`
- `f754a936-daaf-4b6e-9658-41fdc54d301d`
- `1ea4fa01-a81b-4420-a03c-f60019e69a92`

## 知识

覆盖率 **44%**（4/9）

**有卡**：`LoadImage`、`SaveImage`、`ImageScaleToMaxDimension`

**缺卡**（2）：`1ea4fa01-a81b-4420-a03c-f60019e69a92`、`f754a936-daaf-4b6e-9658-41fdc54d301d`

**用到的条目**：LoadImage、SaveImage、ImageScaleToMaxDimension、sd15-t2i-basic、sd15-t2i-lora、ImageScale、scale、String

## 学习发现

- 次要节点 `1ea4fa01-a81b-4420-a03c-f60019e69a92` 知识库中没有该节点类型的任何知识
- 次要节点 `f754a936-daaf-4b6e-9658-41fdc54d301d` 知识库中没有该节点类型的任何知识
