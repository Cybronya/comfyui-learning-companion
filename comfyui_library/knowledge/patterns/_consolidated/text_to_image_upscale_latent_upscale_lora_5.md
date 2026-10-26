---
name: text_to_image_upscale_latent_upscale_lora_5
type: Text To Image
frequency: 6
level: moderate
coverage: 0.927333
common_nodes: [CLIPLoader, CLIPTextEncode, CustomAddLabel, EmptyLatentImage, GetImageSize, GetNode, ImageConcatMulti, ImageScale, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LatentUpscaleBy, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, easy clearCacheAll, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/美学社Zimage+Wan2.2图生视频_2068862940631101442.json, 图片生成/文生图/T002.Zimage文生图（反推+超清放大）_2069595515695755265.json, 视频生成/图生视频/Zimage图生图 发推提示词 + Wan2.2图生视频 二合一工作流_2082452451457847298.json, 视频生成/图生视频/Zimage生图+Wan2.2图生视频_2068224869619294210.json, 视频生成/图生视频/东方美学，Zimage生图+Wan2.2图生视频 (1)_2070632429588668417.json, 视频生成/图生视频/东方美学，Zimage生图+Wan2.2图生视频_2067416151377924097.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_5

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/美学社Zimage+Wan2.2图生视频_2068862940631101442.json、图片生成/文生图/T002.Zimage文生图（反推+超清放大）_2069595515695755265.json、视频生成/图生视频/Zimage图生图 发推提示词 + Wan2.2图生视频 二合一工作流_2082452451457847298.json、视频生成/图生视频/Zimage生图+Wan2.2图生视频_2068224869619294210.json、视频生成/图生视频/东方美学，Zimage生图+Wan2.2图生视频 (1)_2070632429588668417.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CustomAddLabel`
- `EmptyLatentImage`
- `GetImageSize`
- `GetNode`
- `ImageConcatMulti`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LatentUpscaleBy`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
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
- `easy clearCacheAll`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `FlashVSRInitPipe` —— 5/6 个有
- `FlashVSRNodeAdv` —— 5/6 个有
- `ImageResizeKJv2` —— 5/6 个有
- `KSamplerAdvanced` —— 5/6 个有
- `ModelPatchTorchSettings` —— 5/6 个有
- `ModelSamplingSD3` —— 5/6 个有
- `PathchSageAttentionKJ` —— 5/6 个有
- `RIFE VFI` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `WanImageToVideo` —— 5/6 个有
- `easy int` —— 5/6 个有
- `Power Prompt (rgthree)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 83% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 6 | 68% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 6 | 83% |
| 重绘幅度 | simple | - | 6 | 83% |
| 宽度 | 1536 | 1080 - 1536 | 6 | 88% |
| 高度 | 864 | 864 - 1920 | 6 | 62% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 83%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，6 个样本
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 83%
- 重绘幅度 最常用 simple，6 个样本，一致性 83%
- 宽度 中位数 1536，观测区间 1080 - 1536，6 个样本，取值集中（一致性 88%）
- 高度 中位数 864，观测区间 864 - 1920，6 个样本
- 高发问题（12/6 个样本）：Steps较低可能导致细节不足
