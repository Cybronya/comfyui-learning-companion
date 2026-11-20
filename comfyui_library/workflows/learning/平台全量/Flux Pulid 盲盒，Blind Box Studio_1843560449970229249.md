---
key: 平台全量/Flux Pulid 盲盒，Blind Box Studio_1843560449970229249.json
name: Flux Pulid 盲盒，Blind Box Studio_1843560449970229249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux Pulid 盲盒，Blind Box Studio_1843560449970229249.json
hash: 9eead60626540762
coverage: 0.833333
learned_at: 2026-11-14 00:28:02
nodes: [EmptyLatentImage, CLIPTextEncode, KSamplerSelect, PreviewImage, Latent Upscale by Factor (WAS), CLIPTextEncodeFlux, SamplerCustomAdvanced, BasicGuider, ModelSamplingFlux, SamplerCustomAdvanced, VAEDecode, FluxGuidance, Image Comparer (rgthree), PulidFluxModelLoader, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, LoraLoader, SDXLAspectRatioSelector, BasicScheduler, RandomNoise, Note, Image Size to Number, Image Size to Number, VAEDecode, ImageScaleToTotalPixels, JWIntegerSub, JWIntegerSub, easy int, Reroute, Note, Note, MaskToSEGS, SEGSPreview, PreviewImage, ApplyPulidFlux, PreviewImage, Image Overlay, SaveImage, AegisFlow/aflogo, Florence2Run, CheckpointLoaderSimple, LoraLoader, LoraLoader, Note, String Literal, DownloadAndLoadFlorence2Model, SaveImage, BasicScheduler, LatentInterpolate, BNK_Unsampler, LatentInterpolate, BasicScheduler, SamplerCustomAdvanced, LoadImage]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "checkpoint": "flux1-dev-fp8.safetensors", "height": 1216, "lora_name": "flux\\Hyper-FLUX.1-dev-8steps-lora_rank1.safetensors", "strength_clip": 1, "strength_model": 0.8, "width": 832}
---

# 平台全量/Flux Pulid 盲盒，Blind Box Studio_1843560449970229249.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux Pulid 盲盒，Blind Box Studio_1843560449970229249.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `PreviewImage`
- `Latent Upscale by Factor (WAS)`
- `CLIPTextEncodeFlux` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `ModelSamplingFlux`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `PulidFluxModelLoader`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `LoraLoader` ★核心
- `SDXLAspectRatioSelector`
- `BasicScheduler`
- `RandomNoise`
- `Note`
- `Image Size to Number`
- `Image Size to Number`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `JWIntegerSub`
- `JWIntegerSub`
- `easy int`
- `Reroute`
- `Note`
- `Note`
- `MaskToSEGS`
- `SEGSPreview`
- `PreviewImage`
- `ApplyPulidFlux`
- `PreviewImage`
- `Image Overlay`
- `SaveImage`
- `AegisFlow/aflogo`
- `Florence2Run`
- `CheckpointLoaderSimple` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `Note`
- `String Literal`
- `DownloadAndLoadFlorence2Model`
- `SaveImage`
- `BasicScheduler`
- `LatentInterpolate`
- `BNK_Unsampler` ★核心
- `LatentInterpolate`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `width` = `832`
- `height` = `1216`
- `batch_size` = `1`
- `lora_name` = `flux\Hyper-FLUX.1-dev-8steps-lora_rank1.safetensors`
- `strength_model` = `0.8`
- `strength_clip` = `1`
- `checkpoint` = `flux1-dev-fp8.safetensors`

## 知识

覆盖率 **83%**（45/54）

**有卡**：`EmptyLatentImage`、`CLIPTextEncode`、`KSamplerSelect`、`Latent Upscale by Factor (WAS)`、`CLIPTextEncodeFlux`、`SamplerCustomAdvanced`、`BasicGuider`、`ModelSamplingFlux`、`VAEDecode`、`FluxGuidance`、`PulidFluxModelLoader`、`PulidFluxEvaClipLoader`、`PulidFluxInsightFaceLoader`、`LoraLoader`、`SDXLAspectRatioSelector`、`BasicScheduler`、`RandomNoise`、`Image Size to Number`、`ImageScaleToTotalPixels`、`JWIntegerSub`、`easy int`、`MaskToSEGS`、`SEGSPreview`、`ApplyPulidFlux`、`Image Overlay`、`SaveImage`、`AegisFlow/aflogo`、`Florence2Run`、`CheckpointLoaderSimple`、`String Literal`、`DownloadAndLoadFlorence2Model`、`LatentInterpolate`、`BNK_Unsampler`、`LoadImage`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、BNK_Unsampler、FluxGuidance、KSamplerSelect
