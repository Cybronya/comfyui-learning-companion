---
key: 图片生成/图生图/Flux.2 Klein 细节增强_2053519932205355010.json
name: Flux.2 Klein 细节增强_2053519932205355010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2 Klein 细节增强_2053519932205355010.json
hash: 0d39f9df28284d30
coverage: 0.909091
learned_at: 2026-10-10 20:48:02
nodes: [ReferenceLatent, ConditioningZeroOut, ReferenceLatent, SamplerCustomAdvanced, VAEEncode, CFGGuider, EmptyFlux2LatentImage, VAELoader, CLIPTextEncode, CLIPLoader, UNETLoader, VAEDecode, KSamplerSelect, RandomNoise, Flux2Scheduler, LoraLoaderModelOnly, SaveImage, CR Text, ImageScaleToTotalPixels, GetImageSize, LoadImage, PreviewImage]
patterns: []
missing: [CR Text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/Flux.2 Klein 细节增强_2053519932205355010.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2 Klein 细节增强_2053519932205355010.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `CFGGuider`
- `EmptyFlux2LatentImage`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `Flux2Scheduler`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `CR Text`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `LoadImage`
- `PreviewImage`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`ReferenceLatent`、`ConditioningZeroOut`、`SamplerCustomAdvanced`、`VAEEncode`、`CFGGuider`、`EmptyFlux2LatentImage`、`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`VAEDecode`、`KSamplerSelect`、`RandomNoise`、`Flux2Scheduler`、`LoraLoaderModelOnly`、`SaveImage`、`ImageScaleToTotalPixels`、`GetImageSize`、`LoadImage`

**缺卡**（1）：`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
