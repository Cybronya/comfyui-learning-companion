---
name: image_to_image_lora_sampler_clip_35
type: Image To Image
frequency: 8
level: strong
coverage: 0.823875
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/灰度信息图_2105841689272344577.json, 图片生成/图生图/电商 图片高清放大4K_1963862609970941954.json, 图片生成/图生图/葫芦娃Kontext高清放大_1963559904337547265.json, 图片生成/图生图/葫芦娃Kontext高清放大_1982989364558999553.json, 图片生成/图生图/葫芦娃_kontext_hires+PMRF_1967343441250279425.json, 图片生成/图生图/葫芦娃大佬Kontext无损高清放大_1971766740843753474.json, 图片生成/图生图/葫芦娃版Highres Kontext图像超分V1_1963909701552656385.json, 图片生成/图生图/轻微模糊图像高清放大【6K】_1965274033971449858.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_35

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/灰度信息图_2105841689272344577.json、图片生成/图生图/电商 图片高清放大4K_1963862609970941954.json、图片生成/图生图/葫芦娃Kontext高清放大_1963559904337547265.json、图片生成/图生图/葫芦娃Kontext高清放大_1982989364558999553.json、图片生成/图生图/葫芦娃_kontext_hires+PMRF_1967343441250279425.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerColor: ColorAdapter` —— 7/8 个有
- `LayerUtility: NumberCalculatorV2` —— 7/8 个有
- `PrimitiveInt` —— 7/8 个有
- `Image Comparer (rgthree)` —— 6/8 个有
- `ImageListToBatch+` —— 6/8 个有
- `LayerUtility: Seed` —— 6/8 个有
- `TeaCache` —— 6/8 个有
- `LayerUtility: ImageMaskScaleAs` —— 5/8 个有
- `ImpactImageBatchToImageList` —— 3/8 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 3/8 个有
- `ImageBatchToList+` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `UpscaleModelLoader` —— 2/8 个有
- `easy imageListToImageBatch` —— 2/8 个有
- `CLIPLoader` —— 1/8 个有
- `ImageBatchToList` —— 1/8 个有
- `ImageUpscaleWithModel` —— 1/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `ModelSamplingAuraFlow` —— 1/8 个有
- `NunchakuQwenImageDiTLoader` —— 1/8 个有
- `PMRF` —— 1/8 个有
- `UltimateSDUpscale` —— 1/8 个有
- `easy imageBatchToImageList` —— 1/8 个有
- `easy positive` —— 1/8 个有
- `easy sleep` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 25 | 8 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 25，8 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
