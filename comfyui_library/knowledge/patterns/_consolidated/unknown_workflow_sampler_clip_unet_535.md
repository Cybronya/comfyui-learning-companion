---
name: unknown_workflow_sampler_clip_unet_535
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7505
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, GetNode, KSamplerSelect, ModelSamplingFlux, PlaySound|pysssss, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/时尚杂志封面Fashion Cover_Flux_Workflow——SoilSihgStudio_1895373448997175297.json, 平台全量/中文_文生图_Soil Sigh Studio_1895726457270435841.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_535

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/时尚杂志封面Fashion Cover_Flux_Workflow——SoilSihgStudio_1895373448997175297.json、平台全量/中文_文生图_Soil Sigh Studio_1895726457270435841.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `GetNode`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `PlaySound|pysssss`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyTeaCachePatch` —— 1/2 个有
- `ConditioningCombine` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `FluxForwardOverrider` —— 1/2 个有
- `Int Literal` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `String Literal` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.35 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
