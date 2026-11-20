---
name: text_to_image_upscale_lora_sampler_145
type: Text To Image
frequency: 2
level: weak
coverage: 0.804
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerSelect, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/文生图/麦橘千问美人(Qwen-Image)_1954828357163638786.json, 平台全量/kontext双主体万物迁移换背景+FLUX高清放大_1943231782114246657.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_145

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/麦橘千问美人(Qwen-Image)_1954828357163638786.json、平台全量/kontext双主体万物迁移换背景+FLUX高清放大_1943231782114246657.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
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
- `CLIPLoader` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `ImageStitch` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `Seed Everywhere` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.75 | - | 2 | 67% |
| LoRA 文本强度 | 0.75 | - | 2 | 67% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1.75 | - | 2 | 57% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 956 | - | 2 | 80% |
| 高度 | 1248 | - | 2 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.75，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 0.75，样本不足，未给区间，2 个样本
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.75，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 956，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 高度 中位数 1248，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
