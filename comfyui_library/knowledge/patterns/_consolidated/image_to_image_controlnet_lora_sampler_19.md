---
name: image_to_image_controlnet_lora_sampler_19
type: Image To Image
frequency: 2
level: weak
coverage: 0.9225
common_nodes: [AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Conditioning Mixer, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DisableNoise, DualCLIPLoader, FlipSigmas, FluxDeGuidance, FluxForwardODESampler, FluxGuidance, FluxReverseODESampler, Image Lucy Sharpen, ImageResize+, InFluxModelSamplingPred, InstructPixToPixConditioning, KSampler, LoadImage, LoraLoaderModelOnly, OutFluxModelSamplingPred, PreviewImage, SamplerCustomAdvanced, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/双视觉参考+构图参考V2_1989602709244440578.json, 图片生成/文生图/单视觉参考+构图参考V3_1991072806580494338.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_19

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/双视觉参考+构图参考V2_1989602709244440578.json、图片生成/文生图/单视觉参考+构图参考V3_1991072806580494338.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Conditioning Mixer`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DisableNoise`
- `DualCLIPLoader`
- `FlipSigmas`
- `FluxDeGuidance`
- `FluxForwardODESampler`
- `FluxGuidance`
- `FluxReverseODESampler`
- `Image Lucy Sharpen`
- `ImageResize+`
- `InFluxModelSamplingPred`
- `InstructPixToPixConditioning`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OutFluxModelSamplingPred`
- `PreviewImage`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1.5 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
