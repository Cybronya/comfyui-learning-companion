---
key: 图片生成/图生图/高清修复放大三合一工作流【Flux+Wan2.2+seedvr2-约7分钟】_2013279668945821697.json
name: 高清修复放大三合一工作流【Flux+Wan2.2+seedvr2-约7分钟】_2013279668945821697
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/高清修复放大三合一工作流【Flux+Wan2.2+seedvr2-约7分钟】_2013279668945821697.json
hash: aab79195af9e5c85
coverage: 0.853333
learned_at: 2026-10-23 13:34:15
nodes: [LayerUtility: NumberCalculatorV2, LayerUtility: ImageScaleByAspectRatio V2, TTP_Image_Assy, LayerUtility: ImageMaskScaleAsV2, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, ConditioningZeroOut, AIO_Preprocessor, ControlNetLoader, LayerUtility: NumberCalculatorV2, ControlNetApplyAdvanced, CLIPTextEncode, ControlNetApplyAdvanced, ImageUpscaleWithModel, LoraLoader, CLIPLoader, VAELoader, LoraLoader, LoraLoader, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, VAEEncode, easy imageBatchToImageList, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, TTP_Tile_image_size, TTP_Image_Tile_Batch, LayerUtility: NumberCalculatorV2, VAEDecodeTiled, ImageListToImageBatch, easy cleanGpuUsed, easy cleanGpuUsed, ImageUpscaleWithModel, LayerColor: ColorAdapter, ImageScaleToTotalPixels, easy cleanGpuUsed, SeedVR2BlockSwap, SaveImage, KSampler, AIO_Preprocessor, TTP_Image_Assy, ImageUpscaleWithModel, UpscaleModelLoader, PrimitiveFloat, PrimitiveFloat, DF_Integer, PrimitiveInt, FluxGuidance, PrimitiveInt, LoadImage, UpscaleModelLoader, UNETLoader, UpscaleModelLoader, SeedVR2, TTP_Image_Tile_Batch, VAEDecode, ImageListToBatch+, DualCLIPLoader, TTP_Tile_image_size, KSampler, Anything Everywhere, VAELoader, ControlNetLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageBatchToList+, PreviewImage, PreviewImage, Image Comparer (rgthree), Note, Fast Groups Bypasser (rgthree), LayerUtility: NumberCalculatorV2, PreviewImage]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2.5, "controlnet_strength": 0.6000000000000001, "denoise": 0.20000000000000004, "lora_name": "Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors", "sampler_name": "res_2s", "scheduler": "beta", "seed": 442645612329359, "steps": 4, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/高清修复放大三合一工作流【Flux+Wan2.2+seedvr2-约7分钟】_2013279668945821697.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/高清修复放大三合一工作流【Flux+Wan2.2+seedvr2-约7分钟】_2013279668945821697.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `LayerUtility: NumberCalculatorV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TTP_Image_Assy`
- `LayerUtility: ImageMaskScaleAsV2`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ConditioningZeroOut`
- `AIO_Preprocessor`
- `ControlNetLoader`
- `LayerUtility: NumberCalculatorV2`
- `ControlNetApplyAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ImageUpscaleWithModel`
- `LoraLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `easy imageBatchToImageList`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `LayerUtility: NumberCalculatorV2`
- `VAEDecodeTiled` ★核心
- `ImageListToImageBatch`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `LayerColor: ColorAdapter`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `SeedVR2BlockSwap`
- `SaveImage`
- `KSampler` ★核心
- `AIO_Preprocessor`
- `TTP_Image_Assy`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `DF_Integer`
- `PrimitiveInt`
- `FluxGuidance`
- `PrimitiveInt`
- `LoadImage`
- `UpscaleModelLoader`
- `UNETLoader` ★核心
- `UpscaleModelLoader`
- `SeedVR2`
- `TTP_Image_Tile_Batch`
- `VAEDecode` ★核心
- `ImageListToBatch+`
- `DualCLIPLoader`
- `TTP_Tile_image_size`
- `KSampler` ★核心
- `Anything Everywhere`
- `VAELoader`
- `ControlNetLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageBatchToList+`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: NumberCalculatorV2`
- `PreviewImage`

**识别到的模式**：image_to_image、lora

## 关键参数

- `controlnet_strength` = `0.6000000000000001`
- `lora_name` = `Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `0.4000000000000001`
- `seed` = `442645612329359`
- `steps` = `4`
- `cfg` = `2.5`
- `sampler_name` = `res_2s`
- `scheduler` = `beta`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **85%**（64/75）

**有卡**：`LayerUtility: NumberCalculatorV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`TTP_Image_Assy`、`LayerUtility: ImageMaskScaleAsV2`、`VAEEncode`、`ConditioningZeroOut`、`AIO_Preprocessor`、`ControlNetLoader`、`ControlNetApplyAdvanced`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`LoraLoader`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`easy imageBatchToImageList`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`VAEDecodeTiled`、`ImageListToImageBatch`、`easy cleanGpuUsed`、`LayerColor: ColorAdapter`、`ImageScaleToTotalPixels`、`SeedVR2BlockSwap`、`SaveImage`、`KSampler`、`UpscaleModelLoader`、`DF_Integer`、`FluxGuidance`、`LoadImage`、`UNETLoader`、`SeedVR2`、`VAEDecode`、`ImageListToBatch+`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`ImageBatchToList+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
