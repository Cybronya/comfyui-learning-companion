---
name: unknown_workflow_sampler_clip_unet_59
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.806667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [StringFunction|pysssss, LayerUtility: PurgeVRAM V2]
members: [图片生成/文生图/1913052188661481473.json, 图片生成/文生图/1914936305506287617.json, 图片生成/文生图/1915225224143372289.json, 图片生成/文生图/1915236159570509826.json, 图片生成/文生图/1929847965068988417.json, 图片生成/文生图/1943610986538692609.json, 图片生成/文生图/1966782963511930881.json, 图片生成/文生图/1967418961937698817.json, 图片生成/文生图/1971799414320852993.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_59

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1913052188661481473.json、图片生成/文生图/1914936305506287617.json、图片生成/文生图/1915225224143372289.json、图片生成/文生图/1915236159570509826.json、图片生成/文生图/1929847965068988417.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingFlux` —— 8/9 个有
- `LoraLoader` —— 5/9 个有
- `LayerUtility: PurgeVRAM V2` —— 2/9 个有
- `SeedVR2` —— 2/9 个有
- `TeaCache` —— 2/9 个有
- `BlurFusionForegroundEstimation` —— 1/9 个有
- `GetMaskByBiRefNet` —— 1/9 个有
- `LoadRembgByBiRefNetModel` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `RH_Translator` —— 1/9 个有
- `RembgByBiRefNet` —— 1/9 个有
- `StringFunction|pysssss` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：StringFunction|pysssss、LayerUtility: PurgeVRAM V2
