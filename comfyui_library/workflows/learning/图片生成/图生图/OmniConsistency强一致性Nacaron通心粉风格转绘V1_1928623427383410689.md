---
key: 图片生成/图生图/OmniConsistency强一致性Nacaron通心粉风格转绘V1_1928623427383410689.json
name: OmniConsistency强一致性Nacaron通心粉风格转绘V1_1928623427383410689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/OmniConsistency强一致性Nacaron通心粉风格转绘V1_1928623427383410689.json
hash: a59904ce990f1116
coverage: 1
learned_at: 2026-10-23 11:10:16
nodes: [ImageConcanate, SaveImage, RunningHub OmniConsistency Sampler, easy promptConcat, SaveImage, JWInteger, CR Prompt Text, CR Prompt Text, LoadImage, RunningHub OmniConsistency LoraLoader, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
---

# 图片生成/图生图/OmniConsistency强一致性Nacaron通心粉风格转绘V1_1928623427383410689.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/OmniConsistency强一致性Nacaron通心粉风格转绘V1_1928623427383410689.json`

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
- `CR Prompt Text`
- `LoadImage`
- `RunningHub OmniConsistency LoraLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`ImageConcanate`、`SaveImage`、`RunningHub OmniConsistency Sampler`、`easy promptConcat`、`JWInteger`、`CR Prompt Text`、`LoadImage`、`RunningHub OmniConsistency LoraLoader`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoadImage、RunningHub OmniConsistency Sampler、RunningHub OmniConsistency LoraLoader、CR Prompt Text、easy promptConcat、SaveImage、ImageConcanate、JWInteger
