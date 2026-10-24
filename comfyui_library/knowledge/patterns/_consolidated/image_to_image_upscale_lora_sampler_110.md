---
name: image_to_image_upscale_lora_sampler_110
type: Image To Image
frequency: 2
level: weak
coverage: 0.9155
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: SaveImagePlusV2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader, easy cleanGpuUsed, easy imageScaleDownBy]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/终极姿态迁移优化高清一致性image Plus_1973224400117960705.json, 图片生成/图生图/首发Image Edit Plus遮罩编辑_1973260134178795522.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_110

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/终极姿态迁移优化高清一致性image Plus_1973224400117960705.json、图片生成/图生图/首发Image Edit Plus遮罩编辑_1973260134178795522.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: SaveImagePlusV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageScaleDownBy`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `LayerUtility: ColorImage V2` —— 1/2 个有
- `LayerUtility: ImageCombineAlpha` —— 1/2 个有
- `PorterDuffImageComposite` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `SplitImageWithAlpha` —— 1/2 个有
- `YCMaskComposite` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
