---
key: comfyui-workflow-templates-json/image_mage_flow_t2i_int8.json
name: image_mage_flow_t2i_int8
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/image_mage_flow_t2i_int8.json
hash: 0a1eb40810d2a6f7
official: true
coverage: 0.4
learned_at: 2026-10-07 21:35:50
nodes: [SaveImageAdvanced, d069257b-0abc-4d5a-9a19-579e0fe5bd8d, MarkdownNote, MarkdownNote, ResolutionSelector]
patterns: []
missing: [d069257b-0abc-4d5a-9a19-579e0fe5bd8d]
discoveries: [次要节点 `d069257b-0abc-4d5a-9a19-579e0fe5bd8d` 知识库中没有该节点类型的任何知识]
---

# comfyui-workflow-templates-json/image_mage_flow_t2i_int8.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/image_mage_flow_t2i_int8.json`

## 结构

**生成流程**：Latent → Output → Other

**节点**（5 个）：
- `SaveImageAdvanced`
- `d069257b-0abc-4d5a-9a19-579e0fe5bd8d`
- `MarkdownNote`
- `MarkdownNote`
- `ResolutionSelector`

## 知识

覆盖率 **40%**（2/5）

**有卡**：`SaveImageAdvanced`、`ResolutionSelector`

**缺卡**（1）：`d069257b-0abc-4d5a-9a19-579e0fe5bd8d`

**用到的条目**：ResolutionSelector、SaveImageAdvanced、sd15-t2i-basic、sd15-t2i-lora、SaveImage、EmptyLatentImage、height 调整经验、width 调整经验

## 学习发现

- 次要节点 `d069257b-0abc-4d5a-9a19-579e0fe5bd8d` 知识库中没有该节点类型的任何知识
