---
name: image_to_image_upscale_lora_sampler_10
type: Image To Image
frequency: 2
level: weak
coverage: 0.6745
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, ETN_Translate, FluxGuidance, GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerSelect, LoadImage, LoraLoader, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: [easy imageBatchToImageList, easy imageListToImageBatch]
members: [图片生成/文生图/1902541158919122945.json, 图片生成/文生图/1909860762637271042.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1902541158919122945.json、图片生成/文生图/1909860762637271042.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `ETN_Translate`
- `FluxGuidance`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
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
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `CLIPVisionEncode` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `Joy_caption_two` —— 1/2 个有
- `Joy_caption_two_load` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `StyleModelApply` —— 1/2 个有
- `StyleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | - | 1 | 100% |
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 0.6 | - | 2 | 83% |
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy imageBatchToImageList、easy imageListToImageBatch
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
