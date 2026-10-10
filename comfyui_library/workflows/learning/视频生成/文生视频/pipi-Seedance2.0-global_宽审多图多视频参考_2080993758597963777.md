---
key: 视频生成/文生视频/pipi-Seedance2.0-global_宽审多图多视频参考_2080993758597963777.json
name: pipi-Seedance2.0-global_宽审多图多视频参考_2080993758597963777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/pipi-Seedance2.0-global_宽审多图多视频参考_2080993758597963777.json
hash: 25cc9cc025c95b28
coverage: 0.875
learned_at: 2026-10-10 23:09:14
nodes: [SaveVideo, LoadImage, LoadImage, LoadVideo, LoadVideo, LoadAudio, CR Text, RH_BytedanceSeedance20GlobalMultimodalVideo]
patterns: []
missing: [CR Text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/pipi-Seedance2.0-global_宽审多图多视频参考_2080993758597963777.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/pipi-Seedance2.0-global_宽审多图多视频参考_2080993758597963777.json`

## 结构

**生成流程**：Output → Other

**节点**（8 个）：
- `SaveVideo`
- `LoadImage`
- `LoadImage`
- `LoadVideo`
- `LoadVideo`
- `LoadAudio`
- `CR Text`
- `RH_BytedanceSeedance20GlobalMultimodalVideo`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`SaveVideo`、`LoadImage`、`LoadVideo`、`LoadAudio`、`RH_BytedanceSeedance20GlobalMultimodalVideo`

**缺卡**（1）：`CR Text`

**用到的条目**：LoadImage、RH_BytedanceSeedance20GlobalMultimodalVideo、SaveVideo、LoadAudio、LoadVideo、sd15-t2i-basic、sd15-t2i-lora、Seed

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
