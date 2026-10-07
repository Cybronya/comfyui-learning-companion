---
key: comfyui-workflow-templates-json/api_minimax_h3_max_turbo_i2v.json
name: api_minimax_h3_max_turbo_i2v
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_minimax_h3_max_turbo_i2v.json
hash: b3fa1b8011c03cea
official: true
coverage: 0.6
learned_at: 2026-10-07 21:34:19
nodes: [SaveVideo, MinimaxHailuo03ContextIRNode, SaveText, MinimaxHailuo03RegenerateNode, SaveVideo, ComfySwitchNode, ComfySwitchNode, PrimitiveStringMultiline, MarkdownNote, PrimitiveBoolean, PrimitiveBoolean, MarkdownNote, MinimaxHailuo03FirstLastFrameNode, LoadImage, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_minimax_h3_max_turbo_i2v.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_minimax_h3_max_turbo_i2v.json`

## 结构

**生成流程**：Output → Other

**节点**（15 个）：
- `SaveVideo`
- `MinimaxHailuo03ContextIRNode`
- `SaveText`
- `MinimaxHailuo03RegenerateNode`
- `SaveVideo`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `MarkdownNote`
- `MinimaxHailuo03FirstLastFrameNode`
- `LoadImage`
- `MarkdownNote`

## 知识

覆盖率 **60%**（9/15）

**有卡**：`SaveVideo`、`MinimaxHailuo03ContextIRNode`、`SaveText`、`MinimaxHailuo03RegenerateNode`、`PrimitiveBoolean`、`MinimaxHailuo03FirstLastFrameNode`、`LoadImage`

**用到的条目**：LoadImage、SaveText、SaveVideo、PrimitiveBoolean、MinimaxHailuo03ContextIRNode、MinimaxHailuo03FirstLastFrameNode、MinimaxHailuo03RegenerateNode、sd15-t2i-basic
