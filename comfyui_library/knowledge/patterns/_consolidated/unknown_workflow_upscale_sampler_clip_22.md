---
name: unknown_workflow_upscale_sampler_clip_22
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8535
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Image Comparer (rgthree), ImageLoader, ImageResizeKJv2, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LayerUtility: PurgeVRAM V2, ModelSamplingAuraFlow, MultiplePathsInput, Qwen3_VQA, SaveImage, Seed (rgthree), ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList, easy imageListToImageBatch, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Qwen3vl-洗图-放大_1994350779123240961.json, 图片生成/文生图/Z-Image-base洗图放大_2016774612377407489.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-Image-Qwen3vl-洗图-放大_1994350779123240961.json、图片生成/文生图/Z-Image-base洗图放大_2016774612377407489.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `ImageLoader`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingAuraFlow`
- `MultiplePathsInput`
- `Qwen3_VQA`
- `SaveImage`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Florence2ModelLoader` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `Miaoshouai_Tagger` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.85 | - | 1 | 100% |
| LoRA 文本强度 | 0.85 | - | 1 | 100% |
| 采样步数 | 17 | - | 2 | 53% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 40% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.825 | - | 2 | 91% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 17，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.825，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
