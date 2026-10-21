---
name: unknown_workflow_sampler_vae_38
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.933333
common_nodes: [BasicGuider, BasicScheduler, EmptyLatentImage, KSamplerSelect, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [SDVN Translate]
members: [图片生成/文生图/1927177609728184322.json, 图片生成/文生图/1937516933006671873.json, 图片生成/文生图/1951252739424727041.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_38

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1927177609728184322.json、图片生成/文生图/1937516933006671873.json、图片生成/文生图/1951252739424727041.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `EmptyLatentImage`
- `KSamplerSelect`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 2/3 个有
- `NunchakuFluxLoraLoader` —— 2/3 个有
- `CLIPTextEncodeFlux` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `ModelSamplingFlux` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RH_OneShot_Prompter` —— 1/3 个有
- `SDVN Translate` —— 1/3 个有
- `ShowText` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 640 - 1024 | 3 | 80% |
| 高度 | 1536 | 480 - 1600 | 3 | 57% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 640 - 1024，3 个样本
- 高度 中位数 1536，观测区间 480 - 1600，3 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：SDVN Translate
