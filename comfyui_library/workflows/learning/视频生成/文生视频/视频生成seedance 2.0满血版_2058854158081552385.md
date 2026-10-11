---
key: 视频生成/文生视频/视频生成seedance 2.0满血版_2058854158081552385.json
name: 视频生成seedance 2.0满血版_2058854158081552385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/视频生成seedance 2.0满血版_2058854158081552385.json
hash: 4674a52785978eff
coverage: 0.964286
learned_at: 2026-10-11 19:49:51
nodes: [RH_SparkVideoAssetCreate, RH_SparkVideoAssetCreate, RH_SparkVideoAssetCreate, RH_SparkVideoAssetCreate, RH_SparkVideoAssetCreate, RH_SparkVideoAssetCreate, LoadImage, LoadImage, LoadImage, LoadImage, RH_SparkVideoAssetCreate, RH_SparkVideoAssetCreate, RH_SparkVideoAssetCreate, RH_SparkVideoAssetIdsMerge, SaveVideo, LoadImage, CR Prompt Text, LoadVideo, LoadVideo, LoadVideo, LoadAudio, LoadAudio, LoadAudio, LoadImage, LoadImage, LoadImage, LoadImage, RH_RhartVideoSparkvideo20MultimodalVideo]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/视频生成seedance 2.0满血版_2058854158081552385.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/视频生成seedance 2.0满血版_2058854158081552385.json`

## 结构

**生成流程**：Output → Other

**节点**（28 个）：
- `RH_SparkVideoAssetCreate`
- `RH_SparkVideoAssetCreate`
- `RH_SparkVideoAssetCreate`
- `RH_SparkVideoAssetCreate`
- `RH_SparkVideoAssetCreate`
- `RH_SparkVideoAssetCreate`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `RH_SparkVideoAssetCreate`
- `RH_SparkVideoAssetCreate`
- `RH_SparkVideoAssetCreate`
- `RH_SparkVideoAssetIdsMerge`
- `SaveVideo`
- `LoadImage`
- `CR Prompt Text`
- `LoadVideo`
- `LoadVideo`
- `LoadVideo`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `RH_RhartVideoSparkvideo20MultimodalVideo`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`RH_SparkVideoAssetCreate`、`LoadImage`、`RH_SparkVideoAssetIdsMerge`、`SaveVideo`、`LoadVideo`、`LoadAudio`、`RH_RhartVideoSparkvideo20MultimodalVideo`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：LoadImage、SaveVideo、LoadAudio、LoadVideo、RH_RhartVideoSparkvideo20MultimodalVideo、RH_SparkVideoAssetCreate、RH_SparkVideoAssetIdsMerge、sd15-t2i-basic

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
