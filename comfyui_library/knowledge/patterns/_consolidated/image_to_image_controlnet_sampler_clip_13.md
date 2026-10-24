---
name: image_to_image_controlnet_sampler_clip_13
type: Image To Image
frequency: 3
level: strong
coverage: 0.830667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, ImageConcatMulti, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Kontext+Union Pro2.0姿势控制及修复V1_1961122601273901058.json, 图片生成/图生图/Flux Kontext+Union Pro2.0深度控制及修复V1_1961134410970107905.json, 图片生成/图生图/Kontext Controlnet姿态控制生图_1962696721929224194.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux Kontext+Union Pro2.0姿势控制及修复V1_1961122601273901058.json、图片生成/图生图/Flux Kontext+Union Pro2.0深度控制及修复V1_1961134410970107905.json、图片生成/图生图/Kontext Controlnet姿态控制生图_1962696721929224194.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageConcatMulti`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `CR Prompt Text` —— 2/3 个有
- `DF_Get_image_size` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PDIMAGE_LongerSize` —— 2/3 个有
- `SaveLatent` —— 2/3 个有
- `SeedVR2GGUF` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `DepthAnything_V2` —— 1/3 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 1.5 | 1 - 1.8 | 3 | 77% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1.5，观测区间 1 - 1.8，3 个样本
