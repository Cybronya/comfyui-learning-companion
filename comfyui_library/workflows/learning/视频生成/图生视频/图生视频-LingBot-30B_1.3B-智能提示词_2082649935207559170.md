---
key: 视频生成/图生视频/图生视频-LingBot-30B_1.3B-智能提示词_2082649935207559170.json
name: 图生视频-LingBot-30B_1.3B-智能提示词_2082649935207559170.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频-LingBot-30B_1.3B-智能提示词_2082649935207559170.json
hash: 044d54ab6137d3f4
coverage: 0.638889
learned_at: 2026-10-15 22:42:33
nodes: [LingBotTextEncode, easy clearCacheAll, easy clearCacheAll, CR Prompt Text, CR Prompt Text, easy int, easy int, LoadImage, SetNode, SetNode, RH_Captioner_Pro, ImageResizeKJv2, easy int, SaveVideo, easy cleanGpuUsed, GetNode, SimpleMath+, SetNode, easy int, SetNode, GetNode, CreateVideo, GetNode, easy showAnything, PreviewImage, LingBotMoELoaderGGUF, LingBotLoader, easy cleanGpuUsed, easy anythingIndexSwitch, easy cleanGpuUsed, easy clearCacheAll, easy showAnything, GetNode, GetNode, GetNode, LingBotSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频-LingBot-30B_1.3B-智能提示词_2082649935207559170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2082649935207559170.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（36 个）：
- `LingBotTextEncode`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `CR Prompt Text`
- `CR Prompt Text`
- `easy int`
- `easy int`
- `LoadImage`
- `SetNode`
- `SetNode`
- `RH_Captioner_Pro`
- `ImageResizeKJv2`
- `easy int`
- `SaveVideo`
- `easy cleanGpuUsed`
- `GetNode`
- `SimpleMath+`
- `SetNode`
- `easy int`
- `SetNode`
- `GetNode`
- `CreateVideo`
- `GetNode`
- `easy showAnything`
- `PreviewImage`
- `LingBotMoELoaderGGUF`
- `LingBotLoader`
- `easy cleanGpuUsed`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `LingBotSampler` ★核心

## 知识

覆盖率 **64%**（23/36）

**有卡**：`LingBotTextEncode`、`easy clearCacheAll`、`CR Prompt Text`、`easy int`、`LoadImage`、`RH_Captioner_Pro`、`ImageResizeKJv2`、`SaveVideo`、`easy cleanGpuUsed`、`SimpleMath+`、`CreateVideo`、`LingBotMoELoaderGGUF`、`LingBotLoader`、`easy anythingIndexSwitch`、`LingBotSampler`

**用到的条目**：LoadImage、LingBotSampler、LingBotTextEncode、CR Prompt Text、ImageResizeKJv2、SaveVideo、CreateVideo、RH_Captioner_Pro
