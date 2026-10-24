---
name: unknown_workflow_controlnet_lora_sampler_28
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8235
common_nodes: [ACN_AdvancedControlNetApplySingle_v2, AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, CR Latent Batch Size, ControlNetLoader, DifferentialDiffusion, FluxGuidance, GetImageSize, Image Comparer (rgthree), KSamplerSelect, LoadImage, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【超级加速】Nunchaku+Controlnet控制快速生图_1910561153553235970.json, 图片生成/文生图/Nunchaku加速+FluxControlnet合集_1910000993843773442.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_28

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【超级加速】Nunchaku+Controlnet控制快速生图_1910561153553235970.json、图片生成/文生图/Nunchaku加速+FluxControlnet合集_1910000993843773442.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `ACN_AdvancedControlNetApplySingle_v2`
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Latent Batch Size`
- `ControlNetLoader`
- `DifferentialDiffusion`
- `FluxGuidance`
- `GetImageSize`
- `Image Comparer (rgthree)`
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
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `ConstrainImage|pysssss` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `Get resolution [Crystools]` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.65 | - | 2 | 92% |
| 宽度 | 952 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.65，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
