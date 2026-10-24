---
name: image_to_image_upscale_lora_sampler_70
type: Image To Image
frequency: 2
level: weak
coverage: 0.723
common_nodes: [Anything Everywhere, Anything Everywhere3, CLIPTextEncode, CR Text Concatenate, ConditioningZeroOut, DualCLIPLoader, Florence2ModelLoader, Florence2Run, FluxGuidance, GetNode, Image Comparer (rgthree), ImageAndMaskPreview, ImageCompositeMasked, ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LayerColor: ColorAdapter, LayerMask: MaskGrow, LoadImage, LoraLoader, MaskPreview+, PreviewImage, ResizeImageMixlab, SaveImage, SetNode, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextInput_, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/Flux-无损修复放大_1963946685644816386.json, 图片生成/图生图/高清放大-无损去噪_1949822004884062210.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_70

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux-无损修复放大_1963946685644816386.json、图片生成/图生图/高清放大-无损去噪_1949822004884062210.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageCompositeMasked`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerColor: ColorAdapter`
- `LayerMask: MaskGrow`
- `LoadImage`
- `LoraLoader`
- `MaskPreview+`
- `PreviewImage`
- `ResizeImageMixlab`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextInput_`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSize`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 0.3 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
