---
key: 平台全量/Flux 创意贴纸 Creative Sticker(Flux Turbo)_1845100064808300545.json
name: Flux 创意贴纸 Creative Sticker(Flux Turbo)_1845100064808300545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux 创意贴纸 Creative Sticker(Flux Turbo)_1845100064808300545.json
hash: f084e4c86306eee4
coverage: 0.87234
learned_at: 2026-11-14 00:28:14
nodes: [EmptyLatentImage, CLIPTextEncode, KSamplerSelect, PreviewImage, Latent Upscale by Factor (WAS), LatentInterpolate, LatentInterpolate, CLIPTextEncodeFlux, SamplerCustomAdvanced, BasicGuider, ModelSamplingFlux, VAEDecode, FluxGuidance, BasicScheduler, Image Comparer (rgthree), PulidFluxModelLoader, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, LoraLoader, SDXLAspectRatioSelector, RandomNoise, VAEDecode, MaskToSEGS, SEGSPreview, PreviewImage, ApplyPulidFlux, Florence2Run, Florence2ModelLoader, PreviewImage, String Literal, LayerUtility: TextJoin, Note, SaveImage, CheckpointLoaderSimple, Note, LoraLoader, DisplayText_Zho, SamplerCustomAdvanced, SamplerCustomAdvanced, LayerUtility: JoyCaption2ExtraOptions, LoadImage, LayerUtility: JoyCaption2, LoraLoader, BasicScheduler, BNK_Unsampler, BasicScheduler, Text Prompt (JPS)]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "checkpoint": "flux1-dev-fp8.safetensors", "height": 1216, "lora_name": "FLUX.1-Turbo-Alpha.safetensors", "strength_clip": 1, "strength_model": 0.8, "width": 832}
---

# 平台全量/Flux 创意贴纸 Creative Sticker(Flux Turbo)_1845100064808300545.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux 创意贴纸 Creative Sticker(Flux Turbo)_1845100064808300545.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `PreviewImage`
- `Latent Upscale by Factor (WAS)`
- `LatentInterpolate`
- `LatentInterpolate`
- `CLIPTextEncodeFlux` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `ModelSamplingFlux`
- `VAEDecode` ★核心
- `FluxGuidance`
- `BasicScheduler`
- `Image Comparer (rgthree)`
- `PulidFluxModelLoader`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `LoraLoader` ★核心
- `SDXLAspectRatioSelector`
- `RandomNoise`
- `VAEDecode` ★核心
- `MaskToSEGS`
- `SEGSPreview`
- `PreviewImage`
- `ApplyPulidFlux`
- `Florence2Run`
- `Florence2ModelLoader`
- `PreviewImage`
- `String Literal`
- `LayerUtility: TextJoin`
- `Note`
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `LoraLoader` ★核心
- `DisplayText_Zho`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: JoyCaption2ExtraOptions`
- `LoadImage`
- `LayerUtility: JoyCaption2`
- `LoraLoader` ★核心
- `BasicScheduler`
- `BNK_Unsampler` ★核心
- `BasicScheduler`
- `Text Prompt (JPS)`

**识别到的模式**：lora

## 关键参数

- `width` = `832`
- `height` = `1216`
- `batch_size` = `1`
- `lora_name` = `FLUX.1-Turbo-Alpha.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`
- `checkpoint` = `flux1-dev-fp8.safetensors`

## 知识

覆盖率 **87%**（41/47）

**有卡**：`EmptyLatentImage`、`CLIPTextEncode`、`KSamplerSelect`、`Latent Upscale by Factor (WAS)`、`LatentInterpolate`、`CLIPTextEncodeFlux`、`SamplerCustomAdvanced`、`BasicGuider`、`ModelSamplingFlux`、`VAEDecode`、`FluxGuidance`、`BasicScheduler`、`PulidFluxModelLoader`、`PulidFluxEvaClipLoader`、`PulidFluxInsightFaceLoader`、`LoraLoader`、`SDXLAspectRatioSelector`、`RandomNoise`、`MaskToSEGS`、`SEGSPreview`、`ApplyPulidFlux`、`Florence2Run`、`Florence2ModelLoader`、`String Literal`、`LayerUtility: TextJoin`、`SaveImage`、`CheckpointLoaderSimple`、`DisplayText_Zho`、`LayerUtility: JoyCaption2ExtraOptions`、`LoadImage`、`LayerUtility: JoyCaption2`、`BNK_Unsampler`、`Text Prompt (JPS)`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、BNK_Unsampler、FluxGuidance、KSamplerSelect
