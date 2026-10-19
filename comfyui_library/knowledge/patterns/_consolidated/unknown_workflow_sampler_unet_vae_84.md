---
name: unknown_workflow_sampler_unet_vae_84
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.818625
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, KSamplerSelect, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR SDXL Aspect Ratio, easy cleanGpuUsed, Seed (rgthree), easy int]
members: [图片生成/文生图/1923305531946299393.json, 图片生成/文生图/1943610986538692609.json, 图片生成/文生图/1955933159051460609.json, 图片生成/文生图/1957737610612670465.json, 图片生成/文生图/1960223327673593857.json, 图片生成/文生图/1965956635371941889.json, 图片生成/文生图/1977989588658651138.json, 图片生成/文生图/FLUX + LORA 基础工作流_1830939420676771841.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_84

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1923305531946299393.json、图片生成/文生图/1943610986538692609.json、图片生成/文生图/1955933159051460609.json、图片生成/文生图/1957737610612670465.json、图片生成/文生图/1960223327673593857.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 6/8 个有
- `CLIPTextEncode` —— 5/8 个有
- `FluxGuidance` —— 5/8 个有
- `LoraLoader` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `CLIPTextEncodeFlux` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `CR SDXL Aspect Ratio` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `PrimitiveInt` —— 2/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.8 - 1 | 4 | 90% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 1，4 个样本，取值集中（一致性 90%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR SDXL Aspect Ratio、easy cleanGpuUsed、Seed (rgthree)、easy int
