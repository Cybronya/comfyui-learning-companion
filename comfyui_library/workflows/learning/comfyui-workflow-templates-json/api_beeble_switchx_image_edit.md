---
key: comfyui-workflow-templates-json/api_beeble_switchx_image_edit.json
name: api_beeble_switchx_image_edit
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_beeble_switchx_image_edit.json
hash: 563a38dfa391bef3
official: true
coverage: 0.888889
learned_at: 2026-10-10 22:43:10
nodes: [BeebleSwitchXImageEdit, SaveImage, JoinImageWithAlpha, LoadImage, SaveImage, InvertMask, ImageCompare, LoadImage, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_beeble_switchx_image_edit.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_beeble_switchx_image_edit.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（9 个）：
- `BeebleSwitchXImageEdit`
- `SaveImage`
- `JoinImageWithAlpha`
- `LoadImage`
- `SaveImage`
- `InvertMask`
- `ImageCompare`
- `LoadImage`
- `MarkdownNote`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`BeebleSwitchXImageEdit`、`SaveImage`、`JoinImageWithAlpha`、`LoadImage`、`InvertMask`、`ImageCompare`

**用到的条目**：LoadImage、SaveImage、InvertMask、JoinImageWithAlpha、BeebleSwitchXImageEdit、ImageCompare、sd15-t2i-basic、sd15-t2i-lora
