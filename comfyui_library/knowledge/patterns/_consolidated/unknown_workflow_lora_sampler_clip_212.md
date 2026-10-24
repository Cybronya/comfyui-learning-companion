---
name: unknown_workflow_lora_sampler_clip_212
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.848
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptyLatentImage, FluxGuidance, ImageScaleBy, ImpactSwitch, Int, JjkText, KSamplerSelect, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, PreviewImage, RH_Prompter, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImagePlus, TextCombinerTwo, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/极速文生图_1983350145905532929.json, 图片生成/文生图/极速文生图_1983456421763325954.json, 图片生成/文生图/极速文生图（测试）_1957340539244965890.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_212

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/极速文生图_1983350145905532929.json、图片生成/文生图/极速文生图_1983456421763325954.json、图片生成/文生图/极速文生图（测试）_1957340539244965890.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `FluxGuidance`
- `ImageScaleBy`
- `ImpactSwitch`
- `Int`
- `JjkText`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `PreviewImage`
- `RH_Prompter`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImagePlus`
- `TextCombinerTwo`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
