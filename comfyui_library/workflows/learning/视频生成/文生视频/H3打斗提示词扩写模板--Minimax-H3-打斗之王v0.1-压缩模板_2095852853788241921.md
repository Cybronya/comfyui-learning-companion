---
key: 视频生成/文生视频/H3打斗提示词扩写模板--Minimax-H3-打斗之王v0.1-压缩模板_2095852853788241921.json
name: H3打斗提示词扩写模板--Minimax-H3-打斗之王v0.1-压缩模板_2095852853788241921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/H3打斗提示词扩写模板--Minimax-H3-打斗之王v0.1-压缩模板_2095852853788241921.json
hash: 0b54a510acde957b
coverage: 0.7
learned_at: 2026-10-11 21:30:18
nodes: [RH_LLMAPI_Pro_Node, SaveImage, ShellAgentPluginOutputText, easy showAnything, VHS_LoadVideo, LoadImage, RHMiniMaxH3T2VATextEncode, CR Prompt Text, LoadImage, CR Prompt Text]
patterns: []
missing: [CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/H3打斗提示词扩写模板--Minimax-H3-打斗之王v0.1-压缩模板_2095852853788241921.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/H3打斗提示词扩写模板--Minimax-H3-打斗之王v0.1-压缩模板_2095852853788241921.json`

## 结构

**生成流程**：Output → Other

**节点**（10 个）：
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `ShellAgentPluginOutputText`
- `easy showAnything`
- `VHS_LoadVideo`
- `LoadImage`
- `RHMiniMaxH3T2VATextEncode`
- `CR Prompt Text`
- `LoadImage`
- `CR Prompt Text`

## 知识

覆盖率 **70%**（7/10）

**有卡**：`RH_LLMAPI_Pro_Node`、`SaveImage`、`ShellAgentPluginOutputText`、`VHS_LoadVideo`、`LoadImage`、`RHMiniMaxH3T2VATextEncode`

**缺卡**（2）：`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：SaveImage、LoadImage、RHMiniMaxH3T2VATextEncode、ShellAgentPluginOutputText、RH_LLMAPI_Pro_Node、VHS_LoadVideo、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
