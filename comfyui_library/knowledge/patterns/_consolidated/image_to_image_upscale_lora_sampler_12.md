---
name: image_to_image_upscale_lora_sampler_12
type: Image To Image
frequency: 16
level: strong
coverage: 0.777
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), GetImageSize, Image Comparer (rgthree), ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F2K 动漫转真人 AnimeToReal_2061100818362888194.json, 图片生成/图生图/Flux2 Klein 超强真实感细节增强_2020739592365809666.json, 图片生成/图生图/Klein去AI感-人像精修-去油腻-皮肤质感修复-4K-8K_2086087184993579010.json, 图片生成/图生图/去AI感-人像精修-去油腻修复皮肤质感 Flux-2-Klein-9B_2062714845002293250.json, 图片生成/图生图/去AI感-人像精修-去油腻修复皮肤质感_Flux-2-Klein-9B_2083568666586738689.json, 图片生成/图生图/去AI感-人像精修-去油腻修复皮肤质感_Flux-2-Klein-9B_2093143447527059458.json, 图片生成/图生图/去AI感-人像精修-去油腻修复皮肤质感_Flux-2-Klein-9B_2093503227454115842.json, 图片生成/图生图/去AI感-人像精修保留服装原图-去油腻修复皮肤质感 Flux-2-Klein-9B_2071600255497498625.json, 图片生成/图生图/去油腻（2K）_2112003873199185922.json, 图片生成/图生图/工业产品-五金工具-精修洗图-高清修复_2056619564888313857.json, 图片生成/图生图/高清放大-8K画质高清修复-Klein-9B_2060549676453154818.json, 图片生成/文生图/Klein去AI感-人像精修-去油腻-皮肤质感修复-4K-8K_2088947646840004610.json, 图片生成/文生图/高清放大-8K画质高清修复-Klein-9B_2080544604771934209.json, 平台全量/F2Klein-9B高清放大-画质修复-2K-4K-6K-8K_2038136740057194497.json, 平台全量/修复图像 高清放大-8K 画质高清修复 Ultimate Upscaler  Flux klein_2061970842417975297.json, 平台全量/去AI感-人像精修-去油腻修复皮肤质感 保留细节 还原真实质感 真实材质_2067068182661259265.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_12

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/F2K 动漫转真人 AnimeToReal_2061100818362888194.json、图片生成/图生图/Flux2 Klein 超强真实感细节增强_2020739592365809666.json、图片生成/图生图/Klein去AI感-人像精修-去油腻-皮肤质感修复-4K-8K_2086087184993579010.json、图片生成/图生图/去AI感-人像精修-去油腻修复皮肤质感 Flux-2-Klein-9B_2062714845002293250.json、图片生成/图生图/去AI感-人像精修-去油腻修复皮肤质感_Flux-2-Klein-9B_2083568666586738689.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `KSampler`
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
- `ColorMatch` —— 15/16 个有
- `ConstrainImage|pysssss` —— 15/16 个有
- `Get Image Size` —— 15/16 个有
- `ImageResize+` —— 15/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 15/16 个有
- `TTP_Image_Assy` —— 15/16 个有
- `TTP_Image_Tile_Batch` —— 15/16 个有
- `TTP_Tile_image_size` —— 15/16 个有
- `easy imageSize` —— 15/16 个有
- `SeedVR2` —— 12/16 个有
- `SeedVR2BlockSwap` —— 12/16 个有
- `HYPIRAdvancedRestoration` —— 2/16 个有
- `InspyrenetRembg` —— 1/16 个有
- `KOOK_ImageCompression` —— 1/16 个有
- `LayerUtility: PurgeVRAM V2` —— 1/16 个有
- `MaskToImage` —— 1/16 个有
- `easy cleanGpuUsed` —— 1/16 个有
- `easy clearCacheAll` —— 1/16 个有
- `easy int` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 16 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，16 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
