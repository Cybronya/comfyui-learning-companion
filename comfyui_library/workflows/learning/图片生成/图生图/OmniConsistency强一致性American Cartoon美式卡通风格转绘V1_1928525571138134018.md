---
key: 图片生成/图生图/OmniConsistency强一致性American Cartoon美式卡通风格转绘V1_1928525571138134018.json
name: OmniConsistency强一致性American Cartoon美式卡通风格转绘V1_1928525571138134018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/OmniConsistency强一致性American Cartoon美式卡通风格转绘V1_1928525571138134018.json
hash: 4ae844fcb02302ea
coverage: 1
learned_at: 2026-10-23 11:10:13
nodes: [ImageConcanate, SaveImage, RunningHub OmniConsistency Sampler, easy promptConcat, SaveImage, JWInteger, RunningHub OmniConsistency LoraLoader, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, CR Prompt Text]
patterns: []
missing: []
---

# 图片生成/图生图/OmniConsistency强一致性American Cartoon美式卡通风格转绘V1_1928525571138134018.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/OmniConsistency强一致性American Cartoon美式卡通风格转绘V1_1928525571138134018.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（11 个）：
- `ImageConcanate`
- `SaveImage`
- `RunningHub OmniConsistency Sampler` ★核心
- `easy promptConcat`
- `SaveImage`
- `JWInteger`
- `RunningHub OmniConsistency LoraLoader` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Prompt Text`
- `CR Prompt Text`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`ImageConcanate`、`SaveImage`、`RunningHub OmniConsistency Sampler`、`easy promptConcat`、`JWInteger`、`RunningHub OmniConsistency LoraLoader`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`

**用到的条目**：LoadImage、RunningHub OmniConsistency Sampler、RunningHub OmniConsistency LoraLoader、CR Prompt Text、easy promptConcat、SaveImage、ImageConcanate、JWInteger
