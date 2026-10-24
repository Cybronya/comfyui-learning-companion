---
name: text_to_image_upscale_lora_sampler_66
type: Text To Image
frequency: 4
level: strong
coverage: 0.89725
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetImageSize+, ImageResize+, ImageScaleBy, JjkText, KSampler, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图片放大图生图工作流｜低清小图秒变高清大图，细节无损放大_2107335691196788737.json, 图片生成/图生图/床品放大seed_2107644126702424066.json, 图片生成/图生图/放大工作流，图生图图像高清放大多场景覆盖处理方案_2107610394822008834.json, 图片生成/文生图/Aiden MOSS-Image 文生图｜魔改优化版更好用_2112445192572854274.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_66

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/图片放大图生图工作流｜低清小图秒变高清大图，细节无损放大_2107335691196788737.json、图片生成/图生图/床品放大seed_2107644126702424066.json、图片生成/图生图/放大工作流，图生图图像高清放大多场景覆盖处理方案_2107610394822008834.json、图片生成/文生图/Aiden MOSS-Image 文生图｜魔改优化版更好用_2112445192572854274.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `JjkText`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `SaveImageJPG_GH` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `easy clearCacheAll` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ComfyMathExpression` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `EmptyFlux2LatentImage` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `ResolutionSelector` —— 1/4 个有
- `VOSR2ModelLoader` —— 1/4 个有
- `VOSR2Upscale` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
