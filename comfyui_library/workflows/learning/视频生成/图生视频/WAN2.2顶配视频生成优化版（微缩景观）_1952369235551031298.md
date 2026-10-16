---
key: 视频生成/图生视频/WAN2.2顶配视频生成优化版（微缩景观）_1952369235551031298.json
name: WAN2.2顶配视频生成优化版（微缩景观）_1952369235551031298.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952369235551031298.json
hash: 189593e878de4c20
coverage: 0.949367
learned_at: 2026-10-15 22:31:01
nodes: [CreateCFGScheduleFloatList, WanVideoSampler, WanVideoEasyCache, WanVideoEasyCache, LayerUtility: ImageScaleByAspectRatio V2, WanVideoImageToVideoEncode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, PrimitiveNode, WanVideoVAELoader, GetImageSizeAndCount, JWInteger, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoModelLoader, WanVideoDecode, CR Text Concatenate, LoadWanVideoT5TextEncoder, BasicScheduler, EmptyLatentImage, KSamplerSelect, RandomNoise, LoraLoaderModelOnly, SamplerCustomAdvanced, BasicGuider, DualCLIPLoader, VAELoader, ImageFromBatch+, WanVideoBlockSwap, VHS_VideoCombine, WanVideoSampler, INTConstant, INTConstant, UNETLoader, CR Prompt Text, Note, BasicScheduler, easy imageBatchToImageList, CLIPTextEncode, ImageListToImageBatch, KSamplerSelect, RandomNoise, ImageUpscaleWithModel, ImageScaleToTotalPixels, Reroute, TTP_Image_Assy, UNETLoader, UpscaleModelLoader, ImageResizeKJ, SamplerCustomAdvanced, VAEDecodeTiled, VAEEncode, VAELoader, FluxGuidance, BasicGuider, VAEDecode, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy cleanGpuUsed, Joy_caption_two_load, Joy_caption_two, JjkShowText, LoraLoaderModelOnly, DualCLIPLoader, LoraLoader, Note, CLIPTextEncode, SaveImage, RH_Translator, SaveImage, LoadImage, WanVideoTextEncode, CR Prompt Text, JWInteger]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 1024, "lora_name": "Flux Dev模型4步出图lora_Flux Dev模型4步出图lora_Flux Dev 4-step.safetensors", "strength_clip": 1, "strength_model": 1, "width": 768}
---

# 视频生成/图生视频/WAN2.2顶配视频生成优化版（微缩景观）_1952369235551031298.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952369235551031298.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoEasyCache`
- `WanVideoEasyCache`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoImageToVideoEncode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `GetImageSizeAndCount`
- `JWInteger`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `CR Text Concatenate`
- `LoadWanVideoT5TextEncoder`
- `BasicScheduler`
- `EmptyLatentImage` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `DualCLIPLoader`
- `VAELoader`
- `ImageFromBatch+`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `UNETLoader` ★核心
- `CR Prompt Text`
- `Note`
- `BasicScheduler`
- `easy imageBatchToImageList`
- `CLIPTextEncode` ★核心
- `ImageListToImageBatch`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ImageUpscaleWithModel`
- `ImageScaleToTotalPixels`
- `Reroute`
- `TTP_Image_Assy`
- `UNETLoader` ★核心
- `UpscaleModelLoader`
- `ImageResizeKJ`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `VAEEncode` ★核心
- `VAELoader`
- `FluxGuidance`
- `BasicGuider`
- `VAEDecode` ★核心
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy cleanGpuUsed`
- `Joy_caption_two_load`
- `Joy_caption_two`
- `JjkShowText`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `RH_Translator`
- `SaveImage`
- `LoadImage`
- `WanVideoTextEncode`
- `CR Prompt Text`
- `JWInteger`

**识别到的模式**：lora

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `lora_name` = `Flux Dev模型4步出图lora_Flux Dev模型4步出图lora_Flux Dev 4-step.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **95%**（75/79）

**有卡**：`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoEasyCache`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoImageToVideoEncode`、`LayerUtility: PurgeVRAM`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`JWInteger`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoDecode`、`CR Text Concatenate`、`LoadWanVideoT5TextEncoder`、`BasicScheduler`、`EmptyLatentImage`、`KSamplerSelect`、`RandomNoise`、`LoraLoaderModelOnly`、`SamplerCustomAdvanced`、`BasicGuider`、`DualCLIPLoader`、`VAELoader`、`ImageFromBatch+`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`INTConstant`、`UNETLoader`、`CR Prompt Text`、`easy imageBatchToImageList`、`CLIPTextEncode`、`ImageListToImageBatch`、`ImageUpscaleWithModel`、`ImageScaleToTotalPixels`、`TTP_Image_Assy`、`UpscaleModelLoader`、`ImageResizeKJ`、`VAEDecodeTiled`、`VAEEncode`、`FluxGuidance`、`VAEDecode`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`easy cleanGpuUsed`、`Joy_caption_two_load`、`Joy_caption_two`、`JjkShowText`、`LoraLoader`、`SaveImage`、`RH_Translator`、`LoadImage`、`WanVideoTextEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、LayerUtility: ImageScaleByAspectRatio V2
