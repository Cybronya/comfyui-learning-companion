---
key: 视频生成/文生视频/pipi-Seedance2.0 mini-多图多视频参考_2080957986448691202.json
name: pipi-Seedance2.0 mini-多图多视频参考_2080957986448691202
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/pipi-Seedance2.0 mini-多图多视频参考_2080957986448691202.json
hash: 807337ed9a81da9e
coverage: 0.875
learned_at: 2026-10-11 20:38:44
nodes: [SaveVideo, CR Text, LoadImage, LoadImage, LoadVideo, LoadVideo, RH_BytedanceSeedance20GlobalMiniMultimodalVideo, LoadAudio]
patterns: []
missing: [CR Text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/pipi-Seedance2.0 mini-多图多视频参考_2080957986448691202.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/pipi-Seedance2.0 mini-多图多视频参考_2080957986448691202.json`

## 结构

**生成流程**：Output → Other

**节点**（8 个）：
- `SaveVideo`
- `CR Text`
- `LoadImage`
- `LoadImage`
- `LoadVideo`
- `LoadVideo`
- `RH_BytedanceSeedance20GlobalMiniMultimodalVideo`
- `LoadAudio`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`SaveVideo`、`LoadImage`、`LoadVideo`、`RH_BytedanceSeedance20GlobalMiniMultimodalVideo`、`LoadAudio`

**缺卡**（1）：`CR Text`

**用到的条目**：LoadImage、RH_BytedanceSeedance20GlobalMiniMultimodalVideo、SaveVideo、LoadAudio、LoadVideo、sd15-t2i-basic、sd15-t2i-lora、Seed

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
