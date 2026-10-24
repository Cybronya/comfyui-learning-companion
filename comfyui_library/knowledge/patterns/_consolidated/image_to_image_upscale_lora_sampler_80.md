---
name: image_to_image_upscale_lora_sampler_80
type: Image To Image
frequency: 2
level: weak
coverage: 0.83
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSize+, ImageResize+, ImageScaleBy, KOOK_ImageCompression, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image极致真实感图生图洗图8K版_2003079606582280193.json, 图片生成/图生图/一键写真套图V15版Qwen-Edit-2511+Zimage写实洗图+FFlora版_2007094262273417218.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_80

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Z-image极致真实感图生图洗图8K版_2003079606582280193.json、图片生成/图生图/一键写真套图V15版Qwen-Edit-2511+Zimage写实洗图+FFlora版_2007094262273417218.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KOOK_ImageCompression`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `DuckHideNode` —— 1/2 个有
- `HFEPostProcessor (lrzjason)` —— 1/2 个有
- `Int` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `MemoryCleaner` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有
- `easy float` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 0.55 | - | 2 | 64% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 0.55，样本不足，未给区间，2 个样本
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
