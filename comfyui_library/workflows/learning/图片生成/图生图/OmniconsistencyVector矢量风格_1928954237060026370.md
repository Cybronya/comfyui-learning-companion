---
key: 图片生成/图生图/OmniconsistencyVector矢量风格_1928954237060026370.json
name: OmniconsistencyVector矢量风格_1928954237060026370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/OmniconsistencyVector矢量风格_1928954237060026370.json
hash: 35c7a1b588571dc8
coverage: 1
learned_at: 2026-10-23 11:10:23
nodes: [LayerUtility: ImageScaleByAspectRatio V2, ImageConcanate, easy promptConcat, SaveImage, SaveImage, Florence2, LoadFlorence2Model, CR Prompt Text, JWInteger, RunningHub OmniConsistency Sampler, RunningHub OmniConsistency LoraLoader, CR Prompt Text, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/OmniconsistencyVector矢量风格_1928954237060026370.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/OmniconsistencyVector矢量风格_1928954237060026370.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（13 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcanate`
- `easy promptConcat`
- `SaveImage`
- `SaveImage`
- `Florence2`
- `LoadFlorence2Model`
- `CR Prompt Text`
- `JWInteger`
- `RunningHub OmniConsistency Sampler` ★核心
- `RunningHub OmniConsistency LoraLoader` ★核心
- `CR Prompt Text`
- `LoadImage`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`easy promptConcat`、`SaveImage`、`Florence2`、`LoadFlorence2Model`、`CR Prompt Text`、`JWInteger`、`RunningHub OmniConsistency Sampler`、`RunningHub OmniConsistency LoraLoader`、`LoadImage`

**用到的条目**：LoadImage、RunningHub OmniConsistency Sampler、RunningHub OmniConsistency LoraLoader、CR Prompt Text、easy promptConcat、SaveImage、ImageConcanate、JWInteger
