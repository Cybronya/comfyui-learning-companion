---
key: 视频生成/文生视频/全能视频S一键黑白线稿生成广告视频（api版本）0.05_10秒_1981939164268634113.json
name: 全能视频S一键黑白线稿生成广告视频（api版本）0.05_10秒_1981939164268634113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/全能视频S一键黑白线稿生成广告视频（api版本）0.05_10秒_1981939164268634113.json
hash: 52d8a2ad14500fcd
coverage: 0.3
learned_at: 2026-10-11 02:45:04
nodes: [easy showAnything, ImpactSwitch, Text Concatenate, easy showAnything, RH_Sora2_I2V, CR Prompt Text, CR Prompt Text, LoadImage, CR Prompt Text, SaveVideo]
patterns: []
missing: [Text Concatenate, CR Prompt Text, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/全能视频S一键黑白线稿生成广告视频（api版本）0.05_10秒_1981939164268634113.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/全能视频S一键黑白线稿生成广告视频（api版本）0.05_10秒_1981939164268634113.json`

## 结构

**生成流程**：Output → Other

**节点**（10 个）：
- `easy showAnything`
- `ImpactSwitch`
- `Text Concatenate`
- `easy showAnything`
- `RH_Sora2_I2V`
- `CR Prompt Text`
- `CR Prompt Text`
- `LoadImage`
- `CR Prompt Text`
- `SaveVideo`

## 知识

覆盖率 **30%**（3/10）

**有卡**：`RH_Sora2_I2V`、`LoadImage`、`SaveVideo`

**缺卡**（4）：`Text Concatenate`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：LoadImage、SaveVideo、RH_Sora2_I2V、sd15-t2i-basic、sd15-t2i-lora、Text、Switch、CLIPTextEncode

## 学习发现

- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
