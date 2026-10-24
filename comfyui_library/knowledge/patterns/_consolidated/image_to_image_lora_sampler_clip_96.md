---
name: image_to_image_lora_sampler_clip_96
type: Image To Image
frequency: 3
level: strong
coverage: 0.890333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, GetImageSizeAndCount, ImageCrop, ImageResizeKJv2, ImageStitch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext支持ControlNet出图啦_1961122374601084929.json, 图片生成/图生图/最新Kontext姿势参考出图_1960158618492547073.json, 图片生成/图生图/最新Kontext深度参考出图_1960162488035782657.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_96

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Kontext支持ControlNet出图啦_1961122374601084929.json、图片生成/图生图/最新Kontext姿势参考出图_1960158618492547073.json、图片生成/图生图/最新Kontext深度参考出图_1960162488035782657.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSizeAndCount`
- `ImageCrop`
- `ImageResizeKJv2`
- `ImageStitch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `DWPreprocessor` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `RBGImageStitchPlus` —— 2/3 个有
- `ControlNetApplySD3` —— 1/3 个有
- `ControlNetLoader` —— 1/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `PoseNode` —— 1/3 个有
- `SetUnionControlNetType` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 1.5 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
