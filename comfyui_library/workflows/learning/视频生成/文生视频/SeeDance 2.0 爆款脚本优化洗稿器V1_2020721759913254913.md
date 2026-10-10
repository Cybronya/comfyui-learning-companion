---
key: 视频生成/文生视频/SeeDance 2.0 爆款脚本优化洗稿器V1_2020721759913254913.json
name: SeeDance 2.0 爆款脚本优化洗稿器V1_2020721759913254913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/SeeDance 2.0 爆款脚本优化洗稿器V1_2020721759913254913.json
hash: 7673361980d4fa79
coverage: 0.5
learned_at: 2026-10-11 03:16:49
nodes: [easy showAnything, SaveImage, LoadImage, CR Prompt Text, RH_LLMAPI_Pro_Node, Comfly_LLm_API, Note, CR Prompt Text, ShellAgentPluginOutputText, CR Prompt Text]
patterns: []
missing: [CR Prompt Text, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/SeeDance 2.0 爆款脚本优化洗稿器V1_2020721759913254913.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/SeeDance 2.0 爆款脚本优化洗稿器V1_2020721759913254913.json`

## 结构

**生成流程**：Output → Other

**节点**（10 个）：
- `easy showAnything`
- `SaveImage`
- `LoadImage`
- `CR Prompt Text`
- `RH_LLMAPI_Pro_Node`
- `Comfly_LLm_API`
- `Note`
- `CR Prompt Text`
- `ShellAgentPluginOutputText`
- `CR Prompt Text`

## 知识

覆盖率 **50%**（5/10）

**有卡**：`SaveImage`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`Comfly_LLm_API`、`ShellAgentPluginOutputText`

**缺卡**（3）：`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：SaveImage、LoadImage、ShellAgentPluginOutputText、RH_LLMAPI_Pro_Node、Comfly_LLm_API、sd15-t2i-basic、sd15-t2i-lora、node

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
