---
name: text_to_image_upscale_lora_sampler_50
type: Text To Image
frequency: 2
level: weak
coverage: 0.7475
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, DualCLIPLoader, EmptyLatentImage, FluxGuidance, Image Comparer (rgthree), ImageListToImageBatch, ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerSelect, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: [LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, easy imageBatchToImageList]
members: [图片生成/文生图/1959285997471215617.json, 图片生成/文生图/1960606308279943169.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_50

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1959285997471215617.json、图片生成/文生图/1960606308279943169.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
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
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `LatentUpscaleBy` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.9 | - | 2 | 89% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1280 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.75 | - | 2 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.75，样本不足，未给区间，2 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: JoyCaptionBeta1、LayerUtility: JoyCaptionBeta1ExtraOptions、LayerUtility: LoadJoyCaptionBeta1Model、easy imageBatchToImageList
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
