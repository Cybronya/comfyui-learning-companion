---
key: 平台全量/MiniCPM4.5视频反推_2015017383466901505.json
name: MiniCPM4.5视频反推_2015017383466901505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/MiniCPM4.5视频反推_2015017383466901505.json
hash: 91c94dd1ac7a7a50
coverage: 0.615385
learned_at: 2026-11-14 00:40:39
nodes: [WanVideoLoraSelect, PrimitiveInt, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, INTConstant, MarkdownNote, PrimitiveInt, MarkdownNote, ShellAgentPluginOutputText, LoadVideo, AILab_MiniCPM_4_V_Advanced, ShowText|pysssss, easy saveText]
patterns: []
missing: []
---

# 平台全量/MiniCPM4.5视频反推_2015017383466901505.json

> 来源文件 `comfyui_library/workflows/平台全量/MiniCPM4.5视频反推_2015017383466901505.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（13 个）：
- `WanVideoLoraSelect`
- `PrimitiveInt`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `INTConstant`
- `MarkdownNote`
- `PrimitiveInt`
- `MarkdownNote`
- `ShellAgentPluginOutputText`
- `LoadVideo`
- `AILab_MiniCPM_4_V_Advanced`
- `ShowText|pysssss`
- `easy saveText`

## 知识

覆盖率 **62%**（8/13）

**有卡**：`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`INTConstant`、`ShellAgentPluginOutputText`、`LoadVideo`、`AILab_MiniCPM_4_V_Advanced`、`easy saveText`

**用到的条目**：LoadWanVideoT5TextEncoder、WanVideoLoraSelect、easy saveText、ShellAgentPluginOutputText、AILab_MiniCPM_4_V_Advanced、INTConstant、LoadVideo、image_to_image_controlnet_face_detailer_lora
