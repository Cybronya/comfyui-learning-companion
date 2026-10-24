---
name: image_to_image_upscale_sampler_clip_19
type: Image To Image
frequency: 6
level: weak
coverage: 0.865833
common_nodes: [CLIPTextEncode, Florence2ModelLoader, Florence2Run, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Wan2.2分块超清放大_1950926254155431937.json, 图片生成/图生图/flux分块放大_1944289057977303042.json, 图片生成/图生图/生图-超清放大4k-Qwen-Image-2512-分块TTP_1988667248485208066.json, 图片生成/图生图/生图-超清放大4k-Z_Image-分块TTP_2008100856264134657.json, 图片生成/图生图/电商人物图片高清放大 保持皮肤纹理真实感 MagicWan TTP_1991451112989544450.json, 图片生成/文生图/DyPE+Flux超清放大_1987808205147451394.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Wan2.2分块超清放大_1950926254155431937.json、图片生成/图生图/flux分块放大_1944289057977303042.json、图片生成/图生图/生图-超清放大4k-Qwen-Image-2512-分块TTP_1988667248485208066.json、图片生成/图生图/生图-超清放大4k-Z_Image-分块TTP_2008100856264134657.json、图片生成/图生图/电商人物图片高清放大 保持皮肤纹理真实感 MagicWan TTP_1991451112989544450.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `Florence2ModelLoader`
- `Florence2Run`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 4/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `Anything Everywhere3` —— 2/6 个有
- `CFGNorm` —— 2/6 个有
- `DualCLIPLoader` —— 2/6 个有
- `Float` —— 2/6 个有
- `GetImageSizeAndCount` —— 2/6 个有
- `ModelSamplingSD3` —— 2/6 个有
- `ShowText|pysssss` —— 2/6 个有
- `Anything Everywhere` —— 1/6 个有
- `DyPE_FLUX` —— 1/6 个有
- `FluxGuidance` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `ModelPatchTorchSettings` —— 1/6 个有
- `ModelSamplingAuraFlow` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.85 | - | 1 | 100% |
| LoRA 文本强度 | 0.85 | - | 1 | 100% |
| 采样步数 | 8 | 4 - 10 | 6 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 6 | 34% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 0.3 | 0.1 - 0.33 | 6 | 62% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 6/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 0.3，观测区间 0.1 - 0.33，6 个样本
- 高发问题（6/6 个样本）：发现KSampler但没有VAEDecode
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
