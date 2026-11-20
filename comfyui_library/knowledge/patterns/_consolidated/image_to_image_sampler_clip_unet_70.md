---
name: image_to_image_sampler_clip_unet_70
type: Image To Image
frequency: 8
level: weak
coverage: 0.848125
common_nodes: [CLIPTextEncode, Florence2ModelLoader, Florence2Run, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Wan2.2分块超清放大_1950926254155431937.json, 图片生成/图生图/flux分块放大_1944289057977303042.json, 图片生成/图生图/生图-超清放大4k-Qwen-Image-2512-分块TTP_1988667248485208066.json, 图片生成/图生图/生图-超清放大4k-Z_Image-分块TTP_2008100856264134657.json, 图片生成/图生图/电商人物图片高清放大 保持皮肤纹理真实感 MagicWan TTP_1991451112989544450.json, 图片生成/文生图/DyPE+Flux超清放大_1987808205147451394.json, 平台全量/【功能】KREA+DyPE+SROP+TTP放大_1987162510912630785.json, 数字人/数字人/DyPE+Flux 高清放大优化版_1989141458110263297.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_70

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Wan2.2分块超清放大_1950926254155431937.json、图片生成/图生图/flux分块放大_1944289057977303042.json、图片生成/图生图/生图-超清放大4k-Qwen-Image-2512-分块TTP_1988667248485208066.json、图片生成/图生图/生图-超清放大4k-Z_Image-分块TTP_2008100856264134657.json、图片生成/图生图/电商人物图片高清放大 保持皮肤纹理真实感 MagicWan TTP_1991451112989544450.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `Florence2ModelLoader`
- `Florence2Run`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 7/8 个有
- `UpscaleModelLoader` —— 7/8 个有
- `ConditioningZeroOut` —— 6/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `CLIPLoader` —— 4/8 个有
- `DualCLIPLoader` —— 4/8 个有
- `DyPE_FLUX` —— 3/8 个有
- `Float` —— 3/8 个有
- `ModelPatchTorchSettings` —— 3/8 个有
- `PathchSageAttentionKJ` —— 3/8 个有
- `ShowText|pysssss` —— 3/8 个有
- `Anything Everywhere3` —— 2/8 个有
- `CFGNorm` —— 2/8 个有
- `GetImageSizeAndCount` —— 2/8 个有
- `ModelSamplingSD3` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `Anything Everywhere` —— 1/8 个有
- `FluxGuidance` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LoraLoader` —— 1/8 个有
- `ModelSamplingAuraFlow` —— 1/8 个有
- `MultiTextConcatenate` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `PrimitiveFloat` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `Text` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.85 | - | 1 | 100% |
| LoRA 文本强度 | 0.85 | - | 1 | 100% |
| 采样步数 | 8 | 4 - 12 | 8 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 8 | 37% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | beta | - | 8 | 62% |
| 重绘幅度 | 0.3 | 0.1 - 0.33 | 8 | 68% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 8/8 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 5/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 12，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，8 个样本，取值分散，一致性仅 37%
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 beta，8 个样本，一致性 62%
- 重绘幅度 中位数 0.3，观测区间 0.1 - 0.33，8 个样本
- 高发问题（8/8 个样本）：发现KSampler但没有VAEDecode
- 高发问题（5/8 个样本）：Steps较低可能导致细节不足
