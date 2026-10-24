---
key: 图片生成/图生图/OmniConsistency强一致性Snoopy风格转绘V1_1928658509313818625.json
name: OmniConsistency强一致性Snoopy风格转绘V1_1928658509313818625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/OmniConsistency强一致性Snoopy风格转绘V1_1928658509313818625.json
hash: 724394a16b5b49c8
coverage: 1
learned_at: 2026-10-23 11:10:18
nodes: [ImageConcanate, easy promptConcat, JWInteger, CR Prompt Text, LoadImage, RunningHub OmniConsistency LoraLoader, CR Prompt Text, SaveImage, RunningHub OmniConsistency Sampler, LayerUtility: ImageScaleByAspectRatio V2, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/OmniConsistency强一致性Snoopy风格转绘V1_1928658509313818625.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/OmniConsistency强一致性Snoopy风格转绘V1_1928658509313818625.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（11 个）：
- `ImageConcanate`
- `easy promptConcat`
- `JWInteger`
- `CR Prompt Text`
- `LoadImage`
- `RunningHub OmniConsistency LoraLoader` ★核心
- `CR Prompt Text`
- `SaveImage`
- `RunningHub OmniConsistency Sampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`ImageConcanate`、`easy promptConcat`、`JWInteger`、`CR Prompt Text`、`LoadImage`、`RunningHub OmniConsistency LoraLoader`、`SaveImage`、`RunningHub OmniConsistency Sampler`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoadImage、RunningHub OmniConsistency Sampler、RunningHub OmniConsistency LoraLoader、CR Prompt Text、easy promptConcat、SaveImage、ImageConcanate、JWInteger
