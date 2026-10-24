---
name: text_to_image_controlnet_inpaint_lora_7
type: Text To Image
frequency: 2
level: weak
coverage: 0.9495
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ControlNetLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, ImageAndMaskResizeNode, InpaintModelConditioning, KSampler, KSamplerSelect, LoadImage, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, StyleModelApply, StyleModelLoader, VAEDecode, VAEDecodeTiled, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/Nunchaku FLUX加速工作流合集_1911983445990670338.json, 图片生成/文生图/Nunchaku-flux  应用_1911369470202576898.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_lora_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Nunchaku FLUX加速工作流合集_1911983445990670338.json、图片生成/文生图/Nunchaku-flux  应用_1911369470202576898.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ControlNetLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `ImageAndMaskResizeNode`
- `InpaintModelConditioning`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ACN_AdvancedControlNetApplySingle_v2` —— 1/2 个有
- `AIO_Preprocessor` —— 1/2 个有
- `CR Aspect Ratio` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `DepthAnything_V2` —— 1/2 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.7 | - | 2 | 86% |
| 宽度 | 768 | - | 2 | 67% |
| 高度 | 768 | - | 2 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 宽度 中位数 768，样本不足，未给区间，2 个样本
- 高度 中位数 768，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
