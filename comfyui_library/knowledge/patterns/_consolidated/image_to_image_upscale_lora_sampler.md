---
name: image_to_image_upscale_lora_sampler
type: Image To Image
frequency: 5
level: strong
coverage: 0.8264
common_nodes: [BetterFilmGrain, CLIPLoader, CLIPTextEncode, CR Simple Image Compare, DualCLIPLoader, EsesImageEffectBloom, ImageListToImageBatch, ImageScaleBy, ImageScaleDownToSize, ImageSharpen, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSampler, LayerFilter: FilmV2, LoadImage, LoraLoader, PathchSageAttentionKJ, PreviewImage, RH_Captioner, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text Concatenate, Text Multiline, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: [CR Simple Image Compare, LayerFilter: FilmV2, Text Concatenate, Text Multiline]
members: [图片生成/文生图/1944310191020232705.json, 图片生成/文生图/1947217865588035585.json, 图片生成/文生图/1947618979507548162.json, 视频生成/文生视频/1944310191020232705.json, 视频生成/文生视频/WAN2.1图生图单帧细节增强洗图(TTP)_2034438567707021314.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1944310191020232705.json、图片生成/文生图/1947217865588035585.json、图片生成/文生图/1947618979507548162.json、视频生成/文生视频/1944310191020232705.json、视频生成/文生视频/WAN2.1图生图单帧细节增强洗图(TTP)_2034438567707021314.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `BetterFilmGrain`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Simple Image Compare`
- `DualCLIPLoader`
- `EsesImageEffectBloom`
- `ImageListToImageBatch`
- `ImageScaleBy`
- `ImageScaleDownToSize`
- `ImageSharpen`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `KSampler`
- `LayerFilter: FilmV2`
- `LoadImage`
- `LoraLoader`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RH_Captioner`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |
| 采样步数 | 10 | 10 - 10 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | res_2s | - | 5 | 60% |
| 调度器 | bong_tangent | - | 5 | 60% |
| 重绘幅度 | 0.2 | 0.2 - 0.2 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，5 个样本，一致性 60%
- 调度器 最常用 bong_tangent，5 个样本，一致性 60%
- 重绘幅度 中位数 0.2，观测区间 0.2 - 0.2，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Simple Image Compare、LayerFilter: FilmV2、Text Concatenate、Text Multiline
