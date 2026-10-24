---
key: 图片生成/图生图/OmniConsistency强一致性Pixel像素风格转绘V1_1928653281340592129.json
name: OmniConsistency强一致性Pixel像素风格转绘V1_1928653281340592129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/OmniConsistency强一致性Pixel像素风格转绘V1_1928653281340592129.json
hash: cd0e701399f98966
coverage: 1
learned_at: 2026-10-23 11:10:17
nodes: [LayerUtility: ImageScaleByAspectRatio V2, SaveImage, RunningHub OmniConsistency Sampler, easy promptConcat, SaveImage, JWInteger, RunningHub OmniConsistency LoraLoader, LoadImage, CR Prompt Text, CR Prompt Text, ImageConcanate]
patterns: []
missing: []
---

# 图片生成/图生图/OmniConsistency强一致性Pixel像素风格转绘V1_1928653281340592129.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/OmniConsistency强一致性Pixel像素风格转绘V1_1928653281340592129.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（11 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `RunningHub OmniConsistency Sampler` ★核心
- `easy promptConcat`
- `SaveImage`
- `JWInteger`
- `RunningHub OmniConsistency LoraLoader` ★核心
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `ImageConcanate`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`RunningHub OmniConsistency Sampler`、`easy promptConcat`、`JWInteger`、`RunningHub OmniConsistency LoraLoader`、`LoadImage`、`CR Prompt Text`、`ImageConcanate`

**用到的条目**：LoadImage、RunningHub OmniConsistency Sampler、RunningHub OmniConsistency LoraLoader、CR Prompt Text、easy promptConcat、SaveImage、ImageConcanate、JWInteger
