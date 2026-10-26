---
name: image_to_image_controlnet_lora_sampler_21
type: Image To Image
frequency: 2
level: weak
coverage: 0.8735
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DepthAnythingPreprocessor, DualCLIPLoader, FluxGuidance, Get Image Size, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图片提取转绘线稿图_1908443440823021569.json, 数字人/数字人/【动漫转真人】FLUX进阶版脸部修复放大+调色+CN控制_1919945381658951681.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_21

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图片提取转绘线稿图_1908443440823021569.json、数字人/数字人/【动漫转真人】FLUX进阶版脸部修复放大+调色+CN控制_1919945381658951681.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DepthAnythingPreprocessor`
- `DualCLIPLoader`
- `FluxGuidance`
- `Get Image Size`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 1/2 个有
- `CannyEdgePreprocessor` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `InvertImageNode` —— 1/2 个有
- `LineArtPreprocessor` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `OpenposePreprocessor` —— 1/2 个有
- `ReduxAdvanced` —— 1/2 个有
- `SeedSelector` —— 1/2 个有
- `StyleModelLoader` —— 1/2 个有
- `TilePreprocessor` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.9 | - | 2 | 89% |
| ControlNet 权重 | 0.35 | - | 2 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- ControlNet 权重 中位数 0.35，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
