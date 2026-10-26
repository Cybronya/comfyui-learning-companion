---
name: image_to_image_upscale_sampler_clip_36
type: Image To Image
frequency: 3
level: strong
coverage: 0.907667
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Florence2ModelLoader, Florence2Run, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, Latent Noise Injection, LoadImage, ModelSamplingAuraFlow, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/Qwen-Image洗图放大全自动BF16版本_1988252998306545665.json, 图片生成/文生图/Qwen-Image洗图放大全自动Nunchaku版本_1988205105407246337.json, 图片生成/文生图/Qwen-Image超清放大_1988253883254358017.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_36

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen-Image洗图放大全自动BF16版本_1988252998306545665.json、图片生成/文生图/Qwen-Image洗图放大全自动Nunchaku版本_1988205105407246337.json、图片生成/文生图/Qwen-Image超清放大_1988253883254358017.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Florence2ModelLoader`
- `Florence2Run`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `Latent Noise Injection`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 2/3 个有
- `ControlNetApplyAdvanced` —— 2/3 个有
- `ControlNetLoader` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `ImageInvert` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `LoadLotusModel` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `LotusSampler` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `VAEDecode` —— 2/3 个有
- `NunchakuQwenImageDiTLoader` —— 1/3 个有
- `NunchakuQwenImageLoraStack` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1.1 | 1.1 - 1.1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.35 | 0.35 - 0.35 | 3 | 100% |
| ControlNet 权重 | 0.6 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.1，观测区间 1.1 - 1.1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.35，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
