---
key: 视频生成/文生视频/(贞贞AI工坊)Vidu Q2文生视频（基准约等于0.984元_5S-具体根据官方积分计算）_1995088415303643138.json
name: (贞贞AI工坊)Vidu Q2文生视频（基准约等于0.984元_5S-具体根据官方积分计算）_1995088415303643138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/(贞贞AI工坊)Vidu Q2文生视频（基准约等于0.984元_5S-具体根据官方积分计算）_1995088415303643138.json
hash: 9d4b96c2f88a7016
coverage: 0.272727
learned_at: 2026-10-11 02:57:34
nodes: [easy showAnything, easy showAnything, easy showAnything, SaveVideo, Note, Note, CR Prompt Text, Comfly_vidu_text2video, Note, Comfly_api_set, Note]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/(贞贞AI工坊)Vidu Q2文生视频（基准约等于0.984元_5S-具体根据官方积分计算）_1995088415303643138.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/(贞贞AI工坊)Vidu Q2文生视频（基准约等于0.984元_5S-具体根据官方积分计算）_1995088415303643138.json`

## 结构

**生成流程**：Output → Other

**节点**（11 个）：
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `SaveVideo`
- `Note`
- `Note`
- `CR Prompt Text`
- `Comfly_vidu_text2video`
- `Note`
- `Comfly_api_set`
- `Note`

## 知识

覆盖率 **27%**（3/11）

**有卡**：`SaveVideo`、`Comfly_vidu_text2video`、`Comfly_api_set`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：SaveVideo、Comfly_api_set、Comfly_vidu_text2video、sd15-t2i-basic、sd15-t2i-lora、Text、CLIPTextEncode、CLIPLoader

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
