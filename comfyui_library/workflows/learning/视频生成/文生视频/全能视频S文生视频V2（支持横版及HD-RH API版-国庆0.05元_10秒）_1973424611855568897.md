---
key: 视频生成/文生视频/全能视频S文生视频V2（支持横版及HD-RH API版-国庆0.05元_10秒）_1973424611855568897.json
name: 全能视频S文生视频V2（支持横版及HD-RH API版-国庆0.05元_10秒）_1973424611855568897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/全能视频S文生视频V2（支持横版及HD-RH API版-国庆0.05元_10秒）_1973424611855568897.json
hash: 466f1cd05483312f
coverage: 0.333333
learned_at: 2026-10-10 23:11:28
nodes: [easy showAnything, SaveVideo, CR Prompt Text, RH_Sora2_T2V, PrimitiveNode, easy showAnything]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/全能视频S文生视频V2（支持横版及HD-RH API版-国庆0.05元_10秒）_1973424611855568897.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/全能视频S文生视频V2（支持横版及HD-RH API版-国庆0.05元_10秒）_1973424611855568897.json`

## 结构

**生成流程**：Output → Other

**节点**（6 个）：
- `easy showAnything`
- `SaveVideo`
- `CR Prompt Text`
- `RH_Sora2_T2V`
- `PrimitiveNode`
- `easy showAnything`

## 知识

覆盖率 **33%**（2/6）

**有卡**：`SaveVideo`、`RH_Sora2_T2V`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：SaveVideo、RH_Sora2_T2V、sd15-t2i-basic、sd15-t2i-lora、node、Text、CLIPTextEncode、CLIPLoader

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
