---
key: 视频生成/文生视频/全能视频S视频（rh-api版本）0.05_10秒_1973594617805451266.json
name: 全能视频S视频（rh-api版本）0.05_10秒_1973594617805451266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/全能视频S视频（rh-api版本）0.05_10秒_1973594617805451266.json
hash: fc6ecabe8ede014b
coverage: 0.333333
learned_at: 2026-10-10 23:11:44
nodes: [easy showAnything, SaveVideo, RH_Sora2_I2V, easy showAnything, SaveVideo, RH_Sora2_T2V, Text Concatenate, easy showAnything, easy showAnything, ImpactSwitch, CR Prompt Text, LoadImage, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, Text Concatenate, ImpactSwitch, LoadImage, SaveImage]
patterns: []
missing: [Text Concatenate, Text Concatenate, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/全能视频S视频（rh-api版本）0.05_10秒_1973594617805451266.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/全能视频S视频（rh-api版本）0.05_10秒_1973594617805451266.json`

## 结构

**生成流程**：Output → Other

**节点**（21 个）：
- `easy showAnything`
- `SaveVideo`
- `RH_Sora2_I2V`
- `easy showAnything`
- `SaveVideo`
- `RH_Sora2_T2V`
- `Text Concatenate`
- `easy showAnything`
- `easy showAnything`
- `ImpactSwitch`
- `CR Prompt Text`
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `Text Concatenate`
- `ImpactSwitch`
- `LoadImage`
- `SaveImage`

## 知识

覆盖率 **33%**（7/21）

**有卡**：`SaveVideo`、`RH_Sora2_I2V`、`RH_Sora2_T2V`、`LoadImage`、`SaveImage`

**缺卡**（8）：`Text Concatenate`、`Text Concatenate`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：LoadImage、SaveImage、SaveVideo、RH_Sora2_I2V、RH_Sora2_T2V、sd15-t2i-basic、sd15-t2i-lora、Text

## 学习发现

- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
