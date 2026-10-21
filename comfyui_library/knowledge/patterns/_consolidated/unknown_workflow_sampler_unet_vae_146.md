---
name: unknown_workflow_sampler_unet_vae_146
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.789
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, EmptySD3LatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [easy int]
members: [图片生成/文生图/1923305531946299393.json, 图片生成/文生图/1932014239752323074.json, 图片生成/文生图/1965956635371941889.json, 图片生成/文生图/1977989588658651138.json, 图片生成/文生图/国漫美女生成器_2059552047061626882.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_146

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1923305531946299393.json、图片生成/文生图/1932014239752323074.json、图片生成/文生图/1965956635371941889.json、图片生成/文生图/1977989588658651138.json、图片生成/文生图/国漫美女生成器_2059552047061626882.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 4/5 个有
- `ModelSamplingFlux` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `LoraLoader` —— 3/5 个有
- `PrimitiveInt` —— 2/5 个有
- `easy int` —— 2/5 个有
- `CLIPTextEncode` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `TextCombinerTwo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.8 - 0.9 | 3 | 94% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.9，3 个样本，取值集中（一致性 94%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy int
