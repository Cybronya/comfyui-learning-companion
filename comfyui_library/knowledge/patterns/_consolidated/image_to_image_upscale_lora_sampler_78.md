---
name: image_to_image_upscale_lora_sampler_78
type: Image To Image
frequency: 3
level: strong
coverage: 0.848667
common_nodes: [CLIPTextEncode, ColorMatch, ConditioningZeroOut, DownloadAndLoadFlorence2Model, DualCLIPLoader, Florence2Run, FluxGuidance, Image Comparer (rgthree), Image Lucy Sharpen, ImageScaleBy, ImageUpscaleWithModel, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/高清放大-材质类（质感还原）_1981237637421891585.json, 图片生成/图生图/高清放大_1984096056239685634.json, 平台全量/高清放大-材质类（质感还原）_1998204112917422081.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_78

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/高清放大-材质类（质感还原）_1981237637421891585.json、图片生成/图生图/高清放大_1984096056239685634.json、平台全量/高清放大-材质类（质感还原）_1998204112917422081.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `Florence2Run`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `Image Lucy Sharpen`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `UltimateSDUpscale` —— 2/3 个有
- `UltimateSDUpscaleNoUpscale` —— 2/3 个有
- `Float` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `easy imageSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | kl_optimal | - | 3 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 0.3 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 kl_optimal，3 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.3，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
