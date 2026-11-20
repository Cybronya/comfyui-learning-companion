---
name: unknown_workflow_controlnet_lora_sampler_45
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9145
common_nodes: [AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, EmptySD3LatentImage, FluxGuidance, ImageConcatMulti, KSamplerSelect, LoadImage, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/Nunchaku3.0-Controlnet+lora工作流_1929912735440736257.json, 平台全量/Nunchaku3.0-Pulid+Controlnet工作流_1929865248663310338.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_45

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Nunchaku3.0-Controlnet+lora工作流_1929912735440736257.json、平台全量/Nunchaku3.0-Pulid+Controlnet工作流_1929865248663310338.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `ImageConcatMulti`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `CFGZeroStarAndInit` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `GetImageSize+` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `NunchakuPulidApply` —— 1/2 个有
- `NunchakuPulidLoader` —— 1/2 个有
- `NunchakuTextEncoderLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.625 | - | 2 | 96% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.625，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
