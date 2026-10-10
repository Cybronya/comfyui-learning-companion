---
key: 视频生成/文生视频/全能视频S文生视频openai最新模型0.5元_次（国庆前5次免费）_1973577884017233922.json
name: 全能视频S文生视频openai最新模型0.5元_次（国庆前5次免费）_1973577884017233922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/全能视频S文生视频openai最新模型0.5元_次（国庆前5次免费）_1973577884017233922.json
hash: 8ab63dc0c3d660f1
coverage: 0.285714
learned_at: 2026-10-10 23:11:32
nodes: [easy showAnything, RH_Sora2_T2V, easy showAnything, CR Prompt Text, Text Concatenate, CR Prompt Text, SaveVideo]
patterns: []
missing: [Text Concatenate, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/全能视频S文生视频openai最新模型0.5元_次（国庆前5次免费）_1973577884017233922.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/全能视频S文生视频openai最新模型0.5元_次（国庆前5次免费）_1973577884017233922.json`

## 结构

**生成流程**：Output → Other

**节点**（7 个）：
- `easy showAnything`
- `RH_Sora2_T2V`
- `easy showAnything`
- `CR Prompt Text`
- `Text Concatenate`
- `CR Prompt Text`
- `SaveVideo`

## 知识

覆盖率 **29%**（2/7）

**有卡**：`RH_Sora2_T2V`、`SaveVideo`

**缺卡**（3）：`Text Concatenate`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：SaveVideo、RH_Sora2_T2V、sd15-t2i-basic、sd15-t2i-lora、Text、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 学习发现

- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
