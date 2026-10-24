---
key: 图片生成/图生图/OmniConsistency强一致性Fabric风格转绘V1_1928620556487180289.json
name: OmniConsistency强一致性Fabric风格转绘V1_1928620556487180289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/OmniConsistency强一致性Fabric风格转绘V1_1928620556487180289.json
hash: 1fcac077d5fa2bbe
coverage: 1
learned_at: 2026-10-23 11:10:14
nodes: [LayerUtility: ImageScaleByAspectRatio V2, ImageConcanate, SaveImage, RunningHub OmniConsistency Sampler, easy promptConcat, SaveImage, JWInteger, CR Prompt Text, RunningHub OmniConsistency LoraLoader, LoadImage, CR Prompt Text]
patterns: []
missing: []
---

# 图片生成/图生图/OmniConsistency强一致性Fabric风格转绘V1_1928620556487180289.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/OmniConsistency强一致性Fabric风格转绘V1_1928620556487180289.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（11 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcanate`
- `SaveImage`
- `RunningHub OmniConsistency Sampler` ★核心
- `easy promptConcat`
- `SaveImage`
- `JWInteger`
- `CR Prompt Text`
- `RunningHub OmniConsistency LoraLoader` ★核心
- `LoadImage`
- `CR Prompt Text`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`SaveImage`、`RunningHub OmniConsistency Sampler`、`easy promptConcat`、`JWInteger`、`CR Prompt Text`、`RunningHub OmniConsistency LoraLoader`、`LoadImage`

**用到的条目**：LoadImage、RunningHub OmniConsistency Sampler、RunningHub OmniConsistency LoraLoader、CR Prompt Text、easy promptConcat、SaveImage、ImageConcanate、JWInteger
