---
name: image_to_image_upscale_lora_sampler_112
type: Image To Image
frequency: 2
level: weak
coverage: 0.846
common_nodes: [CLIPTextEncode, ColorMatch, ConditioningZeroOut, DownloadAndLoadFlorence2Model, DualCLIPLoader, Florence2Run, FluxGuidance, Image Comparer (rgthree), Image Lucy Sharpen, ImageScaleBy, ImageUpscaleWithModel, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UltimateSDUpscale, UltimateSDUpscaleNoUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/高清放大-材质类（质感还原）_1981237637421891585.json, 图片生成/图生图/高清放大_1984096056239685634.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_112

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/高清放大-材质类（质感还原）_1981237637421891585.json、图片生成/图生图/高清放大_1984096056239685634.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
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
- `UltimateSDUpscale`
- `UltimateSDUpscaleNoUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | kl_optimal | - | 2 | 100% |
| 重绘幅度 | 0.3 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 kl_optimal，2 个样本，一致性 100%
- 重绘幅度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
