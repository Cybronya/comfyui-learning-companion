---
name: text_to_image_lora_sampler_clip_557
type: Text To Image
frequency: 2
level: weak
coverage: 0.8665
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DepthAnythingPreprocessor, DualCLIPLoader, EmptyLatentImage, Flex2Conditioner, Florence2ModelLoader, Florence2Run, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flex.2+Redux512_模仿生图_提示词重绘_1913045125293928450.json, 图片生成/图生图/万象首尾帧图片的快速获取-Flex2实现controlnet和Reduc能力_1931597836973223938.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_557

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flex.2+Redux512_模仿生图_提示词重绘_1913045125293928450.json、图片生成/图生图/万象首尾帧图片的快速获取-Flex2实现controlnet和Reduc能力_1931597836973223938.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DepthAnythingPreprocessor`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Flex2Conditioner`
- `Florence2ModelLoader`
- `Florence2Run`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStar` —— 1/2 个有
- `CFGZeroStarAndInit` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `InpaintModelConditioning` —— 1/2 个有
- `LayerMask: MaskStroke` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 676 | - | 2 | 76% |
| 高度 | 816 | - | 2 | 63% |
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 0.65 | - | 2 | 46% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 676，样本不足，未给区间，2 个样本
- 高度 中位数 816，样本不足，未给区间，2 个样本
- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 0.65，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
