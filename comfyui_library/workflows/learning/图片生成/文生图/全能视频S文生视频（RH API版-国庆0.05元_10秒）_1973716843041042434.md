---
key: 全能视频S文生视频（RH API版-国庆0.05元_10秒）_1973716843041042434.json
name: 全能视频S文生视频（RH API版-国庆0.05元_10秒）_1973716843041042434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/全能视频S文生视频（RH API版-国庆0.05元_10秒）_1973716843041042434.json
hash: 1d2443bf80c61525
coverage: 0.2
learned_at: 2026-10-10 20:59:36
nodes: [easy showAnything, easy showAnything, RH_Sora2_T2V, SaveVideo, Text Concatenate, CR Prompt Text, ImpactSwitch, CR Prompt Text, CR Prompt Text, Note]
patterns: []
missing: [Text Concatenate, CR Prompt Text, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 全能视频S文生视频（RH API版-国庆0.05元_10秒）_1973716843041042434.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/全能视频S文生视频（RH API版-国庆0.05元_10秒）_1973716843041042434.json`

## 结构

**生成流程**：Output → Other

**节点**（10 个）：
- `easy showAnything`
- `easy showAnything`
- `RH_Sora2_T2V`
- `SaveVideo`
- `Text Concatenate`
- `CR Prompt Text`
- `ImpactSwitch`
- `CR Prompt Text`
- `CR Prompt Text`
- `Note`

## 知识

覆盖率 **20%**（2/10）

**有卡**：`RH_Sora2_T2V`、`SaveVideo`

**缺卡**（4）：`Text Concatenate`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：SaveVideo、RH_Sora2_T2V、sd15-t2i-basic、sd15-t2i-lora、Text、Switch、CLIPTextEncode、CLIPLoader

## 学习发现

- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
