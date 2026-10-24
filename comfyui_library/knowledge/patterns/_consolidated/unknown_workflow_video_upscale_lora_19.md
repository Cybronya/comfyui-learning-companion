---
name: unknown_workflow_video_upscale_lora_19
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.949
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Prompt Text, CR Text Concatenate, CreateCFGScheduleFloatList, DualCLIPLoader, EmptyLatentImage, FluxGuidance, GetImageSizeAndCount, INTConstant, ImageFromBatch+, ImageListToImageBatch, ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, JWInteger, JjkShowText, Joy_caption_two, Joy_caption_two_load, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoT5TextEncoder, LoraLoader, LoraLoaderModelOnly, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEasyCache, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2顶配视频生成优化版（微缩景观）_1952369235551031298.json, 视频生成/图生视频/（微缩景观）WAN2.2图片到视频_1957832678953381890.json, 视频生成/图生视频/（微缩景观）WAN图片到视频_1957835967409352705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_19

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/WAN2.2顶配视频生成优化版（微缩景观）_1952369235551031298.json、视频生成/图生视频/（微缩景观）WAN2.2图片到视频_1957832678953381890.json、视频生成/图生视频/（微缩景观）WAN图片到视频_1957835967409352705.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text Concatenate`
- `CreateCFGScheduleFloatList`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageFromBatch+`
- `ImageListToImageBatch`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `JWInteger`
- `JjkShowText`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEasyCache`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 768 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
