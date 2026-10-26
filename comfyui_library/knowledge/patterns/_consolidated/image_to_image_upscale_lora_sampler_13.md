---
name: image_to_image_upscale_lora_sampler_13
type: Image To Image
frequency: 13
level: strong
coverage: 0.774923
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), GetImageSize, Image Comparer (rgthree), ImageScaleBy, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F2K 动漫转真人 AnimeToReal_2061100818362888194.json, 图片生成/图生图/Flux2 Klein 超强真实感细节增强_2020739592365809666.json, 图片生成/图生图/Klein去AI感-人像精修-去油腻-皮肤质感修复-4K-8K_2086087184993579010.json, 图片生成/图生图/去AI感-人像精修-去油腻修复皮肤质感 Flux-2-Klein-9B_2062714845002293250.json, 图片生成/图生图/去AI感-人像精修-去油腻修复皮肤质感_Flux-2-Klein-9B_2083568666586738689.json, 图片生成/图生图/去AI感-人像精修-去油腻修复皮肤质感_Flux-2-Klein-9B_2093143447527059458.json, 图片生成/图生图/去AI感-人像精修-去油腻修复皮肤质感_Flux-2-Klein-9B_2093503227454115842.json, 图片生成/图生图/去AI感-人像精修保留服装原图-去油腻修复皮肤质感 Flux-2-Klein-9B_2071600255497498625.json, 图片生成/图生图/去油腻（2K）_2112003873199185922.json, 图片生成/图生图/工业产品-五金工具-精修洗图-高清修复_2056619564888313857.json, 图片生成/图生图/高清放大-8K画质高清修复-Klein-9B_2060549676453154818.json, 图片生成/文生图/Klein去AI感-人像精修-去油腻-皮肤质感修复-4K-8K_2088947646840004610.json, 图片生成/文生图/高清放大-8K画质高清修复-Klein-9B_2080544604771934209.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/F2K 动漫转真人 AnimeToReal_2061100818362888194.json、图片生成/图生图/Flux2 Klein 超强真实感细节增强_2020739592365809666.json、图片生成/图生图/Klein去AI感-人像精修-去油腻-皮肤质感修复-4K-8K_2086087184993579010.json、图片生成/图生图/去AI感-人像精修-去油腻修复皮肤质感 Flux-2-Klein-9B_2062714845002293250.json、图片生成/图生图/去AI感-人像精修-去油腻修复皮肤质感_Flux-2-Klein-9B_2083568666586738689.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 12/13 个有
- `ConstrainImage|pysssss` —— 12/13 个有
- `Get Image Size` —— 12/13 个有
- `ImageResize+` —— 12/13 个有
- `TTP_Image_Assy` —— 12/13 个有
- `TTP_Image_Tile_Batch` —— 12/13 个有
- `TTP_Tile_image_size` —— 12/13 个有
- `easy imageSize` —— 12/13 个有
- `SeedVR2` —— 10/13 个有
- `SeedVR2BlockSwap` —— 10/13 个有
- `HYPIRAdvancedRestoration` —— 2/13 个有
- `InspyrenetRembg` —— 1/13 个有
- `KOOK_ImageCompression` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `MaskToImage` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有
- `easy clearCacheAll` —— 1/13 个有
- `easy int` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 8 | 13 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 8，13 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
