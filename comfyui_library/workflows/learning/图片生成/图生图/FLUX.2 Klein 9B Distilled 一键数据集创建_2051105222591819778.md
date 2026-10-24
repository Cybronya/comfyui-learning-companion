---
key: 图片生成/图生图/FLUX.2 Klein 9B Distilled 一键数据集创建_2051105222591819778.json
name: FLUX.2 Klein 9B Distilled 一键数据集创建_2051105222591819778
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2 Klein 9B Distilled 一键数据集创建_2051105222591819778.json
hash: afb1dc4df9dea792
coverage: 1
learned_at: 2026-10-23 10:54:05
nodes: [UNETLoader, CLIPLoader, VAELoader, ImageScaleToTotalPixels, Flux2KleinRefLatentController, Flux2KleinTextRefBalance, ReferenceLatent, ReferenceLatent, ConditioningZeroOut, SamplerCustomAdvanced, RandomNoise, CFGGuider, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, VAEEncode, CLIPTextEncode, GetImageSize, CR Prompt List, LoadImage, VAEDecode, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2 Klein 9B Distilled 一键数据集创建_2051105222591819778.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2 Klein 9B Distilled 一键数据集创建_2051105222591819778.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `Flux2KleinRefLatentController`
- `Flux2KleinTextRefBalance`
- `ReferenceLatent`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `CR Prompt List`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`Flux2KleinRefLatentController`、`Flux2KleinTextRefBalance`、`ReferenceLatent`、`ConditioningZeroOut`、`SamplerCustomAdvanced`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`VAEEncode`、`CLIPTextEncode`、`GetImageSize`、`CR Prompt List`、`LoadImage`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
