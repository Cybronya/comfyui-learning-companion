---
name: unknown_workflow_upscale_sampler_clip_42
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9432
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, Joy_caption_two, Joy_caption_two_load, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/保持图像一致+4倍放大_1901578539039367169.json, 平台全量/图像超清放大 物景人 通用F1_1904732440391299074.json, 平台全量/室内外洗图加高清工作流_1970462783244562433.json, 平台全量/极致高清放大_1892487300033777666.json, 平台全量/超级高清放大，任意图像变无比高清图_1923635105280290817.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_42

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/保持图像一致+4倍放大_1901578539039367169.json、平台全量/图像超清放大 物景人 通用F1_1904732440391299074.json、平台全量/室内外洗图加高清工作流_1970462783244562433.json、平台全量/极致高清放大_1892487300033777666.json、平台全量/超级高清放大，任意图像变无比高清图_1923635105280290817.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageListToImageBatch` —— 4/5 个有
- `ImageResizeKJ` —— 4/5 个有
- `VAEDecodeTiled` —— 4/5 个有
- `easy imageBatchToImageList` —— 4/5 个有
- `LoraLoader` —— 3/5 个有
- `VAEDecode` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `ConstrainImage|pysssss` —— 1/5 个有
- `Float` —— 1/5 个有
- `Florence2ModelLoader` —— 1/5 个有
- `Florence2Run` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `PMRF` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
