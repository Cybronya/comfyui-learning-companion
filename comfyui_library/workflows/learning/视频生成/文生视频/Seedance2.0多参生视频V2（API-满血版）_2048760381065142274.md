---
key: 视频生成/文生视频/Seedance2.0多参生视频V2（API-满血版）_2048760381065142274.json
name: Seedance2.0多参生视频V2（API-满血版）_2048760381065142274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Seedance2.0多参生视频V2（API-满血版）_2048760381065142274.json
hash: bb8b044b60580845
coverage: 0.75
learned_at: 2026-10-11 19:49:42
nodes: [SaveVideo, Comfly_Doubao_Seedance2_0, CR Prompt Text, LoadImage, LoadAudio, LoadImage, CR Prompt Text, Comfly_api_set]
patterns: []
missing: [CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Seedance2.0多参生视频V2（API-满血版）_2048760381065142274.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Seedance2.0多参生视频V2（API-满血版）_2048760381065142274.json`

## 结构

**生成流程**：Output → Other

**节点**（8 个）：
- `SaveVideo`
- `Comfly_Doubao_Seedance2_0`
- `CR Prompt Text`
- `LoadImage`
- `LoadAudio`
- `LoadImage`
- `CR Prompt Text`
- `Comfly_api_set`

## 知识

覆盖率 **75%**（6/8）

**有卡**：`SaveVideo`、`Comfly_Doubao_Seedance2_0`、`LoadImage`、`LoadAudio`、`Comfly_api_set`

**缺卡**（2）：`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：LoadImage、Comfly_Doubao_Seedance2_0、SaveVideo、LoadAudio、Comfly_api_set、sd15-t2i-basic、sd15-t2i-lora、Seed

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
