---
name: text_to_image_upscale_lora_sampler_74
type: Text To Image
frequency: 3
level: moderate
coverage: 0.796667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningKrea2Rebalance, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, Krea2StyleReference, Krea2StyleTransfer, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/78.Krea2最新合集（动漫转绘+洗图+风格参考）_2096538809881157634.json, 图片生成/图生图/Krea2动漫转绘+洗图+风格参考合集 By 像素幻想Lab_2077261605552873474.json, 图片生成/文生图/Krea2+zimage双采极致风格参考_2074326036057255937.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_74

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/78.Krea2最新合集（动漫转绘+洗图+风格参考）_2096538809881157634.json、图片生成/图生图/Krea2动漫转绘+洗图+风格参考合集 By 像素幻想Lab_2077261605552873474.json、图片生成/文生图/Krea2+zimage双采极致风格参考_2074326036057255937.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningKrea2Rebalance`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `Krea2StyleReference`
- `Krea2StyleTransfer`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `Any Switch (rgthree)` —— 2/3 个有
- `Anything Everywhere3` —— 2/3 个有
- `Krea2ControlApply` —— 2/3 个有
- `Krea2ControlImageEncode` —— 2/3 个有
- `Krea2ControlLoRALoader` —— 2/3 个有
- `Krea2EditGroundedEncode` —— 2/3 个有
- `Krea2EditModelPatch` —— 2/3 个有
- `LayerUtility: ImageReel` —— 2/3 个有
- `LayerUtility: ImageReelComposit` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `llama_cpp_instruct_adv` —— 2/3 个有
- `llama_cpp_model_loader` —— 2/3 个有
- `CLIPLoaderGGUF` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `TTResolutionSelector` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1024 | 3 | 65% |
| 高度 | 512 | 512 - 1024 | 3 | 65% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.25 - 1 | 3 | 53% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1024，3 个样本
- 高度 中位数 512，观测区间 512 - 1024，3 个样本
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，3 个样本
- 高发问题（8/3 个样本）：Steps较低可能导致细节不足
