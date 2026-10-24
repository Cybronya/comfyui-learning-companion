---
key: 图片生成/图生图/OmniConsistency强一致性Rick Morty风格转绘V1_1928658501009096706.json
name: OmniConsistency强一致性Rick Morty风格转绘V1_1928658501009096706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/OmniConsistency强一致性Rick Morty风格转绘V1_1928658501009096706.json
hash: 01dec013b5ef58d1
coverage: 1
learned_at: 2026-10-23 11:10:18
nodes: [ImageConcanate, SaveImage, RunningHub OmniConsistency Sampler, easy promptConcat, SaveImage, JWInteger, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, RunningHub OmniConsistency LoraLoader, CR Prompt Text, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/OmniConsistency强一致性Rick Morty风格转绘V1_1928658501009096706.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/OmniConsistency强一致性Rick Morty风格转绘V1_1928658501009096706.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（11 个）：
- `ImageConcanate`
- `SaveImage`
- `RunningHub OmniConsistency Sampler` ★核心
- `easy promptConcat`
- `SaveImage`
- `JWInteger`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RunningHub OmniConsistency LoraLoader` ★核心
- `CR Prompt Text`
- `LoadImage`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`ImageConcanate`、`SaveImage`、`RunningHub OmniConsistency Sampler`、`easy promptConcat`、`JWInteger`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`RunningHub OmniConsistency LoraLoader`、`LoadImage`

**用到的条目**：LoadImage、RunningHub OmniConsistency Sampler、RunningHub OmniConsistency LoraLoader、CR Prompt Text、easy promptConcat、SaveImage、ImageConcanate、JWInteger
