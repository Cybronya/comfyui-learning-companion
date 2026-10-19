---
name: text_to_image_video_upscale_latent_upscale_19
type: Text To Image
frequency: 4
level: strong
coverage: 0.934
common_nodes: [CLIPLoader, CLIPTextEncode, CustomAddLabel, EmptyLatentImage, FlashVSRInitPipe, FlashVSRNodeAdv, GetImageSize, GetNode, ImageConcatMulti, ImageResizeKJv2, ImageScale, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerAdvanced, LatentUpscaleBy, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RIFE VFI, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy clearCacheAll, easy int, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2082452451457847298.json, 视频生成/图生视频/2068224869619294210.json, 视频生成/图生视频/2070632429588668417.json, 视频生成/图生视频/2067416151377924097.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_19

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2082452451457847298.json、视频生成/图生视频/2068224869619294210.json、视频生成/图生视频/2070632429588668417.json、视频生成/图生视频/2067416151377924097.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CustomAddLabel`
- `EmptyLatentImage`
- `FlashVSRInitPipe`
- `FlashVSRNodeAdv`
- `GetImageSize`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerAdvanced`
- `LatentUpscaleBy`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy clearCacheAll`
- `easy int`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |
| 宽度 | 1536 | 1536 - 1536 | 4 | 100% |
| 高度 | 864 | 864 - 864 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 宽度 中位数 1536，观测区间 1536 - 1536，4 个样本，取值集中（一致性 100%）
- 高度 中位数 864，观测区间 864 - 864，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
