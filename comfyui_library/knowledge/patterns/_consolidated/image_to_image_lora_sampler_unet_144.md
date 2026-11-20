---
name: image_to_image_lora_sampler_unet_144
type: Image To Image
frequency: 4
level: strong
coverage: 0.89575
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/25yijianqianyiimage_2049410337732038657.json, 图片生成/图生图/Qwen-Edit_Plus-新版双图编辑姿势迁移工作流_1971490029245775873.json, 图片生成/图生图/终极姿态迁移优化高清一致性image Plus_1973224400117960705.json, 图片生成/图生图/首发Image Edit Plus遮罩编辑_1973260134178795522.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_144

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/25yijianqianyiimage_2049410337732038657.json、图片生成/图生图/Qwen-Edit_Plus-新版双图编辑姿势迁移工作流_1971490029245775873.json、图片生成/图生图/终极姿态迁移优化高清一致性image Plus_1973224400117960705.json、图片生成/图生图/首发Image Edit Plus遮罩编辑_1973260134178795522.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 3/4 个有
- `ImageUpscaleWithModel` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `VAEDecodeTiled` —— 3/4 个有
- `VAEEncodeTiled` —— 3/4 个有
- `easy imageScaleDownBy` —— 3/4 个有
- `LayerUtility: ImageReel` —— 2/4 个有
- `LayerUtility: ImageReelComposit` —— 2/4 个有
- `LayerUtility: SaveImagePlusV2` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `ImageStitch` —— 1/4 个有
- `LayerUtility: ColorImage V2` —— 1/4 个有
- `LayerUtility: ImageCombineAlpha` —— 1/4 个有
- `PorterDuffImageComposite` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `RTXVideoSuperResolution` —— 1/4 个有
- `SplitImageWithAlpha` —— 1/4 个有
- `YCMaskComposite` —— 1/4 个有
- `easy float` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 4 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（7/4 个样本）：Steps较低可能导致细节不足
