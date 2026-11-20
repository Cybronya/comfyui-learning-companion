---
name: image_to_image_upscale_lora_sampler_59
type: Image To Image
frequency: 4
level: moderate
coverage: 0.9305
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, FluxGuidance, Image Comparer (rgthree), ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [平台全量/Klein_一致性高清放大_2066759930501230594.json, 平台全量/Klein_多角度视角切换_2069678400310177793.json, 平台全量/Klein_珠宝首饰渲染级精修_2055286499456897025.json, 平台全量/高保真一致性图片高清放大_2081624447206907905.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_59

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Klein_一致性高清放大_2066759930501230594.json、平台全量/Klein_多角度视角切换_2069678400310177793.json、平台全量/Klein_珠宝首饰渲染级精修_2055286499456897025.json、平台全量/高保真一致性图片高清放大_2081624447206907905.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 3/4 个有
- `ReferenceLatent` —— 3/4 个有
- `SZ_KleinTiledKSampler` —— 3/4 个有
- `VAEEncodeTiled` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `GetImageSize+` —— 2/4 个有
- `PainterFluxImageEdit` —— 2/4 个有
- `VAEDecode` —— 2/4 个有
- `DualCLIPLoader` —— 1/4 个有
- `GrowMaskWithBlur` —— 1/4 个有
- `ImageLoader` —— 1/4 个有
- `JoinStrings` —— 1/4 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/4 个有
- `LayerUtility: TextBox` —— 1/4 个有
- `MaskToImage` —— 1/4 个有
- `Mix Images By Mask` —— 1/4 个有
- `PixaromaLabel` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `QwenMultiangleCameraNode` —— 1/4 个有
- `easy imageColorMatch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5.5 | 5 - 6 | 4 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 4 | 96% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | kl_optimal | - | 4 | 50% |
| 重绘幅度 | 0.7 | 0.4 - 1 | 4 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/4 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 5.5，观测区间 5 - 6，4 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，4 个样本，取值集中（一致性 96%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 kl_optimal，4 个样本，一致性 50%
- 重绘幅度 中位数 0.7，观测区间 0.4 - 1，4 个样本
- 高发问题（11/4 个样本）：Steps较低可能导致细节不足
- 高发问题（2/4 个样本）：发现KSampler但没有VAEDecode
