---
name: image_to_image_controlnet_sampler_clip_12
type: Image To Image
frequency: 4
level: strong
coverage: 0.8575
common_nodes: [CLIPTextEncode, ControlNetApplySD3, ControlNetLoader, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, ImageConcatMulti, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Kontext+Union Pro2.0姿势控制及修复V1_1961122601273901058.json, 图片生成/图生图/Flux Kontext+Union Pro2.0深度控制及修复V1_1961134410970107905.json, 图片生成/图生图/Kontext Controlnet姿态控制生图_1962696721929224194.json, 平台全量/✅Flux Kontext+Union Pro2.0深度迁移_2003351711626428418.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux Kontext+Union Pro2.0姿势控制及修复V1_1961122601273901058.json、图片生成/图生图/Flux Kontext+Union Pro2.0深度控制及修复V1_1961134410970107905.json、图片生成/图生图/Kontext Controlnet姿态控制生图_1962696721929224194.json、平台全量/✅Flux Kontext+Union Pro2.0深度迁移_2003351711626428418.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
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
- `CR Prompt Text` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `DF_Get_image_size` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `SeedVR2GGUF` —— 3/4 个有
- `AIO_Preprocessor` —— 2/4 个有
- `DepthAnything_V2` —— 2/4 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 2/4 个有
- `PDIMAGE_LongerSize` —— 2/4 个有
- `SaveLatent` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `PDImageResizeV2` —— 1/4 个有
- `PurgeVRAM_UTK` —— 1/4 个有
- `SetUnionControlNetType` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 1.25 | 1 - 1.8 | 4 | 74% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1.25，观测区间 1 - 1.8，4 个样本
