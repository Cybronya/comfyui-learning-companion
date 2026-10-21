---
name: unknown_workflow_lora_sampler_clip_106
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.743667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Text, DualCLIPLoader, EmptyLatentImage, Int, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text, ImageSmartSharpen+, Note Plus (mtb)]
members: [图片生成/文生图/1941002485245100033.json, 图片生成/文生图/1951074575276814337.json, 图片生成/文生图/1951091883130953729.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_106

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1941002485245100033.json、图片生成/文生图/1951074575276814337.json、图片生成/文生图/1951091883130953729.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Int`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `ModelSamplingFlux` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `ImageSmartSharpen+` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1440 | 3 | 47% |
| 高度 | 512 | 512 - 1024 | 3 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1440，3 个样本，取值分散，一致性仅 47%
- 高度 中位数 512，观测区间 512 - 1024，3 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、ImageSmartSharpen+、Note Plus (mtb)
