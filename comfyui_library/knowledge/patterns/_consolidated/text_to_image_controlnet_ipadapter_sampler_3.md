---
name: text_to_image_controlnet_ipadapter_sampler_3
type: Text To Image
frequency: 3
level: moderate
coverage: 0.902333
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ControlNetApplyAdvanced, DualCLIPLoader, EmptyLatentImage, FluxGuidance, IPAdapterUnifiedLoader, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingFlux, PrepImageForClipVision, PreviewImage, ReduxAdvanced, SaveImage, StyleModelLoader, Text, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/20.tonnie-室内设计_1995104009671335938.json, 图片生成/图生图/室内设计毛坯转效果图_2018218247539138561.json, 平台全量/室内设计毛坯转效果图_1944371459416576001.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_sampler_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/20.tonnie-室内设计_1995104009671335938.json、图片生成/图生图/室内设计毛坯转效果图_2018218247539138561.json、平台全量/室内设计毛坯转效果图_1944371459416576001.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `IPAdapterUnifiedLoader`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingFlux`
- `PrepImageForClipVision`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `ControlNetLoader` —— 2/3 个有
- `DownloadAndLoadFlorence2Model` —— 2/3 个有
- `Florence2Run` —— 2/3 个有
- `IPAdapterAdvanced` —— 2/3 个有
- `IPAdapterNoise` —— 2/3 个有
- `DiffControlNetLoader` —— 1/3 个有
- `Display Any (rgthree)` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `IPAdapter` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/3 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1024 | 3 | 65% |
| 高度 | 512 | 512 - 1024 | 3 | 65% |
| 采样步数 | 25 | 20 - 25 | 3 | 90% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 3 | 60% |
| 采样算法 | dpmpp_2m | - | 3 | 67% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 1 | 0.5 - 1 | 3 | 72% |
| ControlNet 权重 | 0.7 | 0.7 - 0.7 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1024，3 个样本
- 高度 中位数 512，观测区间 512 - 1024，3 个样本
- 采样步数 中位数 25，观测区间 20 - 25，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，3 个样本
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，3 个样本
- ControlNet 权重 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）
