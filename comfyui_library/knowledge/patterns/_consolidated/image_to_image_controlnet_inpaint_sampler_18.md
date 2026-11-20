---
name: image_to_image_controlnet_inpaint_sampler_18
type: Image To Image
frequency: 2
level: weak
coverage: 0.6765
common_nodes: [Anything Everywhere, Anything Everywhere3, CLIPTextEncode, CR Prompt Text, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, FluxGuidance, GetNode, GrowMaskWithBlur, Image Blank, Image Comparer (rgthree), InvertMask, KSampler, LayerUtility: ImageBlendAdvance V2, LoadImage, PreviewImage, SaveImage, SetLatentNoiseMask, SetNode, SetUnionControlNetType, VAEDecode, VAEEncode, VAEEncodeForInpaint]
problems: []
missing: []
members: [平台全量/Expand and Enhance Perfect Outpainting with Flux_1869951872134975490.json, 平台全量/扩图：Perfect Outpainting with Flux_1839710049769062401.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_sampler_18

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Expand and Enhance Perfect Outpainting with Flux_1869951872134975490.json、平台全量/扩图：Perfect Outpainting with Flux_1839710049769062401.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `FluxGuidance`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Blank`
- `Image Comparer (rgthree)`
- `InvertMask`
- `KSampler`
- `LayerUtility: ImageBlendAdvance V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SetLatentNoiseMask`
- `SetNode`
- `SetUnionControlNetType`
- `VAEDecode`
- `VAEEncode`
- `VAEEncodeForInpaint`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 50% |
| 采样算法 | dpmpp_3m_sde | - | 2 | 50% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.975 | - | 2 | 97% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本
- 采样算法 最常用 dpmpp_3m_sde，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.975，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
