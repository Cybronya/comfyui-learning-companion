---
key: 视频生成/图生视频/Zimage图生图 发推提示词 + Wan2.2图生视频 二合一工作流_2082452451457847298.json
name: Zimage图生图 发推提示词 + Wan2.2图生视频 二合一工作流_2082452451457847298.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Zimage图生图 发推提示词 + Wan2.2图生视频 二合一工作流_2082452451457847298.json
hash: 222edec1ab671e6d
coverage: 0.933962
learned_at: 2026-10-15 22:42:32
nodes: [llama_cpp_model_loader, LayerUtility: PurgeVRAM, llama_cpp_parameters, SetNode, easy showAnything, LayerUtility: PurgeVRAM, SaveImage, VAEDecode, UpscaleModelLoader, ImageUpscaleWithModel, GetNode, TTP_Tile_image_size, TTP_Image_Tile_Batch, ImageScaleToTotalPixels, SeedVR2LoadVAEModel, easy clearCacheAll, SetNode, LatentUpscaleBy, GetImageSize, CLIPTextEncode, SaveImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, KSampler, KSampler, EmptyLatentImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ImageResizeKJv2, llama_cpp_model_loader, LayerUtility: PurgeVRAM, llama_cpp_parameters, Note, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, easy int, easy int, CLIPLoader, VAELoader, ImageResizeKJv2, easy int, ModelSamplingSD3, ModelSamplingSD3, WanImageToVideo, KSamplerAdvanced, KSamplerAdvanced, LayerUtility: PurgeVRAM, VAEDecode, CLIPTextEncode, LoadImage, CLIPTextEncode, easy showAnything, RIFE VFI, FlashVSRNodeAdv, ImageScale, SaveImage, CustomAddLabel, LoadImage, FlashVSRInitPipe, TTP_Image_Assy, CustomAddLabel, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, LoraLoaderModelOnly, VAELoader, SaveImage, LoadImage, SetNode, ImageConcatMulti, VAEDecode, VHS_VideoCombine, SaveImage, SaveImage, VHS_VideoCombine, CLIPTextEncode, LoadImage, llama_cpp_instruct_adv, LoadImage, llama_cpp_instruct_adv]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4, "denoise": "simple", "height": 864, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed", "width": 1536}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Zimage图生图 发推提示词 + Wan2.2图生视频 二合一工作流_2082452451457847298.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2082452451457847298.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（106 个）：
- `llama_cpp_model_loader`
- `LayerUtility: PurgeVRAM`
- `llama_cpp_parameters`
- `SetNode`
- `easy showAnything`
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `GetNode`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadVAEModel`
- `easy clearCacheAll`
- `SetNode`
- `LatentUpscaleBy`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `KSampler` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `llama_cpp_model_loader`
- `LayerUtility: PurgeVRAM`
- `llama_cpp_parameters`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `easy int`
- `easy int`
- `CLIPLoader`
- `VAELoader`
- `ImageResizeKJv2`
- `easy int`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `RIFE VFI`
- `FlashVSRNodeAdv`
- `ImageScale`
- `SaveImage`
- `CustomAddLabel`
- `LoadImage`
- `FlashVSRInitPipe`
- `TTP_Image_Assy`
- `CustomAddLabel`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `SaveImage`
- `LoadImage`
- `SetNode`
- `ImageConcatMulti`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `SaveImage`
- `SaveImage`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `llama_cpp_instruct_adv`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `width` = `1536`
- `height` = `864`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（99/106）

**有卡**：`llama_cpp_model_loader`、`LayerUtility: PurgeVRAM`、`llama_cpp_parameters`、`SaveImage`、`VAEDecode`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`ImageScaleToTotalPixels`、`SeedVR2LoadVAEModel`、`easy clearCacheAll`、`LatentUpscaleBy`、`GetImageSize`、`CLIPTextEncode`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`KSampler`、`EmptyLatentImage`、`LoadImage`、`ImageResizeKJv2`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`easy int`、`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`WanImageToVideo`、`KSamplerAdvanced`、`RIFE VFI`、`FlashVSRNodeAdv`、`ImageScale`、`CustomAddLabel`、`FlashVSRInitPipe`、`TTP_Image_Assy`、`ImageConcatMulti`、`VHS_VideoCombine`、`llama_cpp_instruct_adv`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
