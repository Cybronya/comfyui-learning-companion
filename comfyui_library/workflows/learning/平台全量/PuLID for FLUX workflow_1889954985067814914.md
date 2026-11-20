---
key: 平台全量/PuLID for FLUX workflow_1889954985067814914.json
name: PuLID for FLUX workflow_1889954985067814914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/PuLID for FLUX workflow_1889954985067814914.json
hash: ae1e295700c4fa56
coverage: 0.971429
learned_at: 2026-11-14 00:48:39
nodes: [PulidFluxModelLoader, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, BasicGuider, BasicScheduler, ReroutePrimitive|pysssss, KSamplerSelect, RandomNoise, VAEEncode, Joy_caption_two, UNETLoader, Switch any [Crystools], UnetLoaderGGUF, ApplyPulidFlux, SDXL Empty Latent Image (rgthree), Sampler Selector (Image Saver), Scheduler Selector (Image Saver), Primitive float [Crystools], FluxGuidance, SamplerCustomAdvanced, Switch any [Crystools], Seed (rgthree), Primitive integer [Crystools], VAELoader, Switch any [Crystools], DualCLIPLoader, CLIPTextEncode, LoraLoader, Joy_caption_two_load, VAEDecode, CR Prompt Text, ShowText|pysssss, LoadImage, LoadImage, SaveImage]
patterns: [lora]
missing: []
parameters: {"lora_name": "FLUX超真实人像_1.0.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 平台全量/PuLID for FLUX workflow_1889954985067814914.json

> 来源文件 `comfyui_library/workflows/平台全量/PuLID for FLUX workflow_1889954985067814914.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `PulidFluxModelLoader`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `BasicGuider`
- `BasicScheduler`
- `ReroutePrimitive|pysssss`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `VAEEncode` ★核心
- `Joy_caption_two`
- `UNETLoader` ★核心
- `Switch any [Crystools]`
- `UnetLoaderGGUF` ★核心
- `ApplyPulidFlux`
- `SDXL Empty Latent Image (rgthree)`
- `Sampler Selector (Image Saver)` ★核心
- `Scheduler Selector (Image Saver)`
- `Primitive float [Crystools]`
- `FluxGuidance`
- `SamplerCustomAdvanced` ★核心
- `Switch any [Crystools]`
- `Seed (rgthree)`
- `Primitive integer [Crystools]`
- `VAELoader`
- `Switch any [Crystools]`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `Joy_caption_two_load`
- `VAEDecode` ★核心
- `CR Prompt Text`
- `ShowText|pysssss`
- `LoadImage`
- `LoadImage`
- `SaveImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `FLUX超真实人像_1.0.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **97%**（34/35）

**有卡**：`PulidFluxModelLoader`、`PulidFluxEvaClipLoader`、`PulidFluxInsightFaceLoader`、`BasicGuider`、`BasicScheduler`、`ReroutePrimitive|pysssss`、`KSamplerSelect`、`RandomNoise`、`VAEEncode`、`Joy_caption_two`、`UNETLoader`、`Switch any [Crystools]`、`UnetLoaderGGUF`、`ApplyPulidFlux`、`SDXL Empty Latent Image (rgthree)`、`Sampler Selector (Image Saver)`、`Scheduler Selector (Image Saver)`、`Primitive float [Crystools]`、`FluxGuidance`、`SamplerCustomAdvanced`、`Seed (rgthree)`、`Primitive integer [Crystools]`、`VAELoader`、`DualCLIPLoader`、`CLIPTextEncode`、`LoraLoader`、`Joy_caption_two_load`、`VAEDecode`、`CR Prompt Text`、`LoadImage`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、Sampler Selector (Image Saver)
