---
name: image_to_image_controlnet_lora_sampler_14
type: Image To Image
frequency: 3
level: strong
coverage: 0.877333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DepthAnythingPreprocessor, DualCLIPLoader, FluxGuidance, Get Image Size, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图片提取转绘线稿图_1908443440823021569.json, 平台全量/flux万物转线稿_1908390550750568449.json, 数字人/数字人/【动漫转真人】FLUX进阶版脸部修复放大+调色+CN控制_1919945381658951681.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_14

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图片提取转绘线稿图_1908443440823021569.json、平台全量/flux万物转线稿_1908390550750568449.json、数字人/数字人/【动漫转真人】FLUX进阶版脸部修复放大+调色+CN控制_1919945381658951681.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
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
- `CannyEdgePreprocessor` —— 2/3 个有
- `InvertImageNode` —— 2/3 个有
- `LineArtPreprocessor` —— 2/3 个有
- `ModelSamplingFlux` —— 2/3 个有
- `SeedSelector` —— 2/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `OpenposePreprocessor` —— 1/3 个有
- `ReduxAdvanced` —— 1/3 个有
- `StyleModelLoader` —— 1/3 个有
- `TilePreprocessor` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 3 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.8 - 1 | 3 | 90% |
| ControlNet 权重 | 0.4 | 0.3 - 0.4 | 3 | 87% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
- ControlNet 权重 中位数 0.4，观测区间 0.3 - 0.4，3 个样本，取值集中（一致性 87%）
