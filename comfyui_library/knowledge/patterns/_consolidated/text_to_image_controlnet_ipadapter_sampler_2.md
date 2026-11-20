---
name: text_to_image_controlnet_ipadapter_sampler_2
type: Text To Image
frequency: 2
level: weak
coverage: 0.8665
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ControlNetApplyAdvanced, DualCLIPLoader, EmptyLatentImage, FluxGuidance, IPAdapterUnifiedLoader, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingFlux, PrepImageForClipVision, PreviewImage, ReduxAdvanced, SaveImage, StyleModelLoader, Text, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/20.tonnie-室内设计_1995104009671335938.json, 图片生成/图生图/室内设计毛坯转效果图_2018218247539138561.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_sampler_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/20.tonnie-室内设计_1995104009671335938.json、图片生成/图生图/室内设计毛坯转效果图_2018218247539138561.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `DiffControlNetLoader` —— 1/2 个有
- `Display Any (rgthree)` —— 1/2 个有
- `DownloadAndLoadFlorence2Model` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `IPAdapter` —— 1/2 个有
- `IPAdapterAdvanced` —— 1/2 个有
- `IPAdapterNoise` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1` —— 1/2 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 1/2 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 67% |
| 高度 | 768 | - | 2 | 67% |
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 50% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.75 | - | 2 | 67% |
| ControlNet 权重 | 0.7 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本
- 高度 中位数 768，样本不足，未给区间，2 个样本
- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.75，样本不足，未给区间，2 个样本
- ControlNet 权重 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
