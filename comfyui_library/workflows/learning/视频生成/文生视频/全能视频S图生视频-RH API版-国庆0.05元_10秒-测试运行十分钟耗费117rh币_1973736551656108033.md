---
key: 视频生成/文生视频/全能视频S图生视频-RH API版-国庆0.05元_10秒-测试运行十分钟耗费117rh币_1973736551656108033.json
name: 全能视频S图生视频-RH API版-国庆0.05元_10秒-测试运行十分钟耗费117rh币_1973736551656108033
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/全能视频S图生视频-RH API版-国庆0.05元_10秒-测试运行十分钟耗费117rh币_1973736551656108033.json
hash: d8f383083d9ec599
coverage: 0.3
learned_at: 2026-10-10 23:11:04
nodes: [easy showAnything, Text Concatenate, CR Prompt Text, CR Prompt Text, ImpactSwitch, SaveVideo, CR Prompt Text, LoadImage, RH_Sora2_I2V, easy showAnything]
patterns: []
missing: [Text Concatenate, CR Prompt Text, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/全能视频S图生视频-RH API版-国庆0.05元_10秒-测试运行十分钟耗费117rh币_1973736551656108033.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/全能视频S图生视频-RH API版-国庆0.05元_10秒-测试运行十分钟耗费117rh币_1973736551656108033.json`

## 结构

**生成流程**：Output → Other

**节点**（10 个）：
- `easy showAnything`
- `Text Concatenate`
- `CR Prompt Text`
- `CR Prompt Text`
- `ImpactSwitch`
- `SaveVideo`
- `CR Prompt Text`
- `LoadImage`
- `RH_Sora2_I2V`
- `easy showAnything`

## 知识

覆盖率 **30%**（3/10）

**有卡**：`SaveVideo`、`LoadImage`、`RH_Sora2_I2V`

**缺卡**（4）：`Text Concatenate`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：LoadImage、SaveVideo、RH_Sora2_I2V、sd15-t2i-basic、sd15-t2i-lora、Text、Switch、CLIPTextEncode

## 学习发现

- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
