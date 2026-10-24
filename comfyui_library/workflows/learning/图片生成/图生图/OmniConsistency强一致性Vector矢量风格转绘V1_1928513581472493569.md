---
key: 图片生成/图生图/OmniConsistency强一致性Vector矢量风格转绘V1_1928513581472493569.json
name: OmniConsistency强一致性Vector矢量风格转绘V1_1928513581472493569
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/OmniConsistency强一致性Vector矢量风格转绘V1_1928513581472493569.json
hash: 31766fa1fb8e1cac
coverage: 1
learned_at: 2026-10-23 11:10:19
nodes: [LoadImage, LayerUtility: ImageScaleByAspectRatio V2, RunningHub OmniConsistency LoraLoader, ImageConcanate, SaveImage, RunningHub OmniConsistency Sampler, CR Prompt Text, easy promptConcat, CR Prompt Text, SaveImage, JWInteger]
patterns: []
missing: []
---

# 图片生成/图生图/OmniConsistency强一致性Vector矢量风格转绘V1_1928513581472493569.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/OmniConsistency强一致性Vector矢量风格转绘V1_1928513581472493569.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（11 个）：
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RunningHub OmniConsistency LoraLoader` ★核心
- `ImageConcanate`
- `SaveImage`
- `RunningHub OmniConsistency Sampler` ★核心
- `CR Prompt Text`
- `easy promptConcat`
- `CR Prompt Text`
- `SaveImage`
- `JWInteger`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`RunningHub OmniConsistency LoraLoader`、`ImageConcanate`、`SaveImage`、`RunningHub OmniConsistency Sampler`、`CR Prompt Text`、`easy promptConcat`、`JWInteger`

**用到的条目**：LoadImage、RunningHub OmniConsistency Sampler、RunningHub OmniConsistency LoraLoader、CR Prompt Text、easy promptConcat、SaveImage、ImageConcanate、JWInteger
