---
key: 视频生成/文生视频/SeeDance 2.0爆款视频分析高级版V1_2020740263819350017.json
name: SeeDance 2.0爆款视频分析高级版V1_2020740263819350017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/SeeDance 2.0爆款视频分析高级版V1_2020740263819350017.json
hash: 7dd3ce5ba7df2403
coverage: 0.636364
learned_at: 2026-10-11 03:16:49
nodes: [easy showAnything, ShellAgentPluginOutputText, easy showAnything, CR Prompt Text, Comfly_LLm_API, RH_LLMAPI_Pro_Node, LoadVideo, SaveImage, LoadImage, CR Prompt Text, ShellAgentPluginOutputText]
patterns: []
missing: [CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/SeeDance 2.0爆款视频分析高级版V1_2020740263819350017.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/SeeDance 2.0爆款视频分析高级版V1_2020740263819350017.json`

## 结构

**生成流程**：Output → Other

**节点**（11 个）：
- `easy showAnything`
- `ShellAgentPluginOutputText`
- `easy showAnything`
- `CR Prompt Text`
- `Comfly_LLm_API`
- `RH_LLMAPI_Pro_Node`
- `LoadVideo`
- `SaveImage`
- `LoadImage`
- `CR Prompt Text`
- `ShellAgentPluginOutputText`

## 知识

覆盖率 **64%**（7/11）

**有卡**：`ShellAgentPluginOutputText`、`Comfly_LLm_API`、`RH_LLMAPI_Pro_Node`、`LoadVideo`、`SaveImage`、`LoadImage`

**缺卡**（2）：`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：SaveImage、LoadImage、ShellAgentPluginOutputText、LoadVideo、RH_LLMAPI_Pro_Node、Comfly_LLm_API、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
