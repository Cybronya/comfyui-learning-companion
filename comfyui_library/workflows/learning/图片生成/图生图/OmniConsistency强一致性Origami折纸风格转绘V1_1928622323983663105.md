---
key: 图片生成/图生图/OmniConsistency强一致性Origami折纸风格转绘V1_1928622323983663105.json
name: OmniConsistency强一致性Origami折纸风格转绘V1_1928622323983663105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/OmniConsistency强一致性Origami折纸风格转绘V1_1928622323983663105.json
hash: 81d3a39353d6c426
coverage: 1
learned_at: 2026-10-23 11:10:16
nodes: [ImageConcanate, SaveImage, easy promptConcat, SaveImage, JWInteger, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, RunningHub OmniConsistency LoraLoader, RunningHub OmniConsistency Sampler, LoadImage, CR Prompt Text]
patterns: []
missing: []
---

# 图片生成/图生图/OmniConsistency强一致性Origami折纸风格转绘V1_1928622323983663105.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/OmniConsistency强一致性Origami折纸风格转绘V1_1928622323983663105.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（11 个）：
- `ImageConcanate`
- `SaveImage`
- `easy promptConcat`
- `SaveImage`
- `JWInteger`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RunningHub OmniConsistency LoraLoader` ★核心
- `RunningHub OmniConsistency Sampler` ★核心
- `LoadImage`
- `CR Prompt Text`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`ImageConcanate`、`SaveImage`、`easy promptConcat`、`JWInteger`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`RunningHub OmniConsistency LoraLoader`、`RunningHub OmniConsistency Sampler`、`LoadImage`

**用到的条目**：LoadImage、RunningHub OmniConsistency Sampler、RunningHub OmniConsistency LoraLoader、CR Prompt Text、easy promptConcat、SaveImage、ImageConcanate、JWInteger
