---
key: 视频生成/文生视频/全能视频S图生视频openai最新模型0.5元_次（国庆前5次免费）_1973570458102665218.json
name: 全能视频S图生视频openai最新模型0.5元_次（国庆前5次免费）_1973570458102665218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/全能视频S图生视频openai最新模型0.5元_次（国庆前5次免费）_1973570458102665218.json
hash: c3cecf668261876d
coverage: 0.375
learned_at: 2026-10-10 23:11:05
nodes: [LoadImage, RH_Sora2_I2V, easy showAnything, easy showAnything, CR Prompt Text, SaveVideo, Text Concatenate, CR Prompt Text]
patterns: []
missing: [Text Concatenate, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/全能视频S图生视频openai最新模型0.5元_次（国庆前5次免费）_1973570458102665218.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/全能视频S图生视频openai最新模型0.5元_次（国庆前5次免费）_1973570458102665218.json`

## 结构

**生成流程**：Output → Other

**节点**（8 个）：
- `LoadImage`
- `RH_Sora2_I2V`
- `easy showAnything`
- `easy showAnything`
- `CR Prompt Text`
- `SaveVideo`
- `Text Concatenate`
- `CR Prompt Text`

## 知识

覆盖率 **38%**（3/8）

**有卡**：`LoadImage`、`RH_Sora2_I2V`、`SaveVideo`

**缺卡**（3）：`Text Concatenate`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：LoadImage、SaveVideo、RH_Sora2_I2V、sd15-t2i-basic、sd15-t2i-lora、Text、CLIPTextEncode、CLIPLoader

## 学习发现

- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
