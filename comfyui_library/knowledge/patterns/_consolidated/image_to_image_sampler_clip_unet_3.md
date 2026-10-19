---
name: image_to_image_sampler_clip_unet_3
type: Image To Image
frequency: 4
level: strong
coverage: 0.918
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, GetImageSizeAndCount, ImageStitch, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [Text Multiline]
members: [图片生成/文生图/1944383441200664578.json, 图片生成/文生图/1962350864377823234.json, 图片生成/文生图/1962546980700467202.json, 视频生成/图生视频/1994289242960576513.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1944383441200664578.json、图片生成/文生图/1962350864377823234.json、图片生成/文生图/1962546980700467202.json、视频生成/图生视频/1994289242960576513.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSizeAndCount`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 3/4 个有
- `ImageScaleDownToSize` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `Text Multiline` —— 3/4 个有
- `AIO_Preprocessor` —— 2/4 个有
- `EmptySD3LatentImage` —— 2/4 个有
- `FluxKontextImageScale` —— 2/4 个有
- `ImageCrop` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `LoadKontextPresets` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline
