---
name: image_to_image_upscale_lora_sampler_15
type: Image To Image
frequency: 2
level: weak
coverage: 0.76
common_nodes: [CLIPTextEncode, ConditioningZeroOut, Florence2ModelLoader, Florence2Run, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: [easy imageBatchToImageList, easy imageListToImageBatch, Latent Noise Injection]
members: [图片生成/文生图/1987808205147451394.json, 图片生成/文生图/1988253883254358017.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_15

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1987808205147451394.json、图片生成/文生图/1988253883254358017.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Florence2ModelLoader`
- `Florence2Run`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
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
- `CFGNorm` —— 1/2 个有
- `CLIPLoader` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `DyPE_FLUX` —— 1/2 个有
- `Latent Noise Injection` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1.05 | - | 2 | 95% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 0.325 | - | 2 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.05，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 0.325，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 这些节点还没有知识卡，系统对它们的理解有限：easy imageBatchToImageList、easy imageListToImageBatch、Latent Noise Injection
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
