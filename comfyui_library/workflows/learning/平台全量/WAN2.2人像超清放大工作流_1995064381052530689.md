---
key: 平台全量/WAN2.2人像超清放大工作流_1995064381052530689.json
name: WAN2.2人像超清放大工作流_1995064381052530689
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/WAN2.2人像超清放大工作流_1995064381052530689.json
hash: c45f977bfe96a7d5
coverage: 0.8125
learned_at: 2026-11-14 01:03:43
nodes: [Reroute, SUPIR_model_loader_v2, UpscaleModelLoader, ModelSamplingSD3, VAEEncode, ImageFromBatch, TTP_Image_Tile_Batch, VAEDecode, CLIPTextEncode, FluxGuidance, PreviewImage, easy imageBatchToImageList, ImageListToImageBatch, CLIPLoader, VAELoader, CLIPTextEncode, PathchSageAttentionKJ, easy cleanGpuUsed, KSampler, CheckpointLoaderSimple, SUPIR_first_stage, SUPIR_encode, SetNode, SUPIR_conditioner, SUPIR_sample, SUPIR_decode, ImageBlend, GetNode, GetNode, ImageScaleToTotalPixels, TTP_Tile_image_size, ImageUpscaleWithModel, PrimitiveFloat, LoadImage, SaveImage, Image Comparer (rgthree), SetNode, ImageScaleToTotalPixels, TTP_Image_Assy, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, ColorMatch, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "XLL dreamshaperXL_lightningDPMSDE.safetensors", "denoise": 0.02, "sampler_name": "euler", "scheduler": "simple", "seed": 208361218264987, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/WAN2.2人像超清放大工作流_1995064381052530689.json

> 来源文件 `comfyui_library/workflows/平台全量/WAN2.2人像超清放大工作流_1995064381052530689.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `Reroute`
- `SUPIR_model_loader_v2`
- `UpscaleModelLoader`
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `ImageFromBatch`
- `TTP_Image_Tile_Batch`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `PreviewImage`
- `easy imageBatchToImageList`
- `ImageListToImageBatch`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `SUPIR_first_stage`
- `SUPIR_encode`
- `SetNode`
- `SUPIR_conditioner`
- `SUPIR_sample`
- `SUPIR_decode`
- `ImageBlend`
- `GetNode`
- `GetNode`
- `ImageScaleToTotalPixels`
- `TTP_Tile_image_size`
- `ImageUpscaleWithModel`
- `PrimitiveFloat`
- `LoadImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SetNode`
- `ImageScaleToTotalPixels`
- `TTP_Image_Assy`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ColorMatch`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `208361218264987`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.02`
- `checkpoint` = `XLL dreamshaperXL_lightningDPMSDE.safetensors`

## 知识

覆盖率 **81%**（39/48）

**有卡**：`SUPIR_model_loader_v2`、`UpscaleModelLoader`、`ModelSamplingSD3`、`VAEEncode`、`ImageFromBatch`、`TTP_Image_Tile_Batch`、`VAEDecode`、`CLIPTextEncode`、`FluxGuidance`、`easy imageBatchToImageList`、`ImageListToImageBatch`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`easy cleanGpuUsed`、`KSampler`、`CheckpointLoaderSimple`、`SUPIR_first_stage`、`SUPIR_encode`、`SUPIR_conditioner`、`SUPIR_sample`、`SUPIR_decode`、`ImageBlend`、`ImageScaleToTotalPixels`、`TTP_Tile_image_size`、`ImageUpscaleWithModel`、`LoadImage`、`SaveImage`、`TTP_Image_Assy`、`LoraLoaderModelOnly`、`UNETLoader`、`ColorMatch`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
