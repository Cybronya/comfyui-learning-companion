---
name: image_to_image_controlnet_ipadapter_sampler_6
type: Image To Image
frequency: 2
level: weak
coverage: 0.728
common_nodes: [CLIPSetLastLayer, CLIPTextEncodeWithWeight //Inspire, CR Color Panel, CR Latent Batch Size, CannyEdgePreprocessor, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DepthAnythingPreprocessor, IPAdapterAdvanced, IPAdapterNoise, IPAdapterUnifiedLoader, Image Comparer (rgthree), InspyrenetRembgAdvanced, KSampler, LayerColor: Exposure, LayerMask: MaskGrow, LayerUtility: HLFrequencyDetailRestore, LayerUtility: ImageBlendAdvance V2, LayerUtility: ImageScaleByAspectRatio V2, LineArtPreprocessor, LoadImage, MaskToImage, PreviewImage, SaveImage, ShowText|pysssss, StringFunction|pysssss, Text Concatenate, TextInput_, VAEDecode, VAEEncode, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX最强精修工作流，无需controlnet参与，更快更强.ai_1915020344825184258.json, 图片生成/图生图/「精修无需抽卡」——修万物-修手-修脸-修产品-修瑕疵_1886829063665799169.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_sampler_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FLUX最强精修工作流，无需controlnet参与，更快更强.ai_1915020344825184258.json、图片生成/图生图/「精修无需抽卡」——修万物-修手-修脸-修产品-修瑕疵_1886829063665799169.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPSetLastLayer`
- `CLIPTextEncodeWithWeight //Inspire`
- `CR Color Panel`
- `CR Latent Batch Size`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DepthAnythingPreprocessor`
- `IPAdapterAdvanced`
- `IPAdapterNoise`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `InspyrenetRembgAdvanced`
- `KSampler`
- `LayerColor: Exposure`
- `LayerMask: MaskGrow`
- `LayerUtility: HLFrequencyDetailRestore`
- `LayerUtility: ImageBlendAdvance V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LineArtPreprocessor`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `Text Concatenate`
- `TextInput_`
- `VAEDecode`
- `VAEEncode`
- `easy imageSize`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.85 | - | 2 | 82% |
| 采样步数 | 5 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 100% |
| 采样算法 | dpmpp_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- 采样步数 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
