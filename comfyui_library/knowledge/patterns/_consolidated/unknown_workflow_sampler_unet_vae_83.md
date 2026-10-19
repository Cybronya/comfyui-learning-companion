---
name: unknown_workflow_sampler_unet_vae_83
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.836125
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [StringFunction|pysssss, CR Aspect Ratio SDXL, Text Concatenate (JPS)]
members: [图片生成/文生图/1916014463953076225.json, 图片生成/文生图/1920279185280143362.json, 图片生成/文生图/1929042246597820418.json, 图片生成/文生图/1929441410473431042.json, 图片生成/文生图/1930927750276644866.json, 图片生成/文生图/1937774839442903042.json, 图片生成/文生图/1937778776556376066.json, 图片生成/文生图/1957765376640909314.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_83

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1916014463953076225.json、图片生成/文生图/1920279185280143362.json、图片生成/文生图/1929042246597820418.json、图片生成/文生图/1929441410473431042.json、图片生成/文生图/1930927750276644866.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 6/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `FluxGuidance` —— 5/8 个有
- `JjkText` —— 4/8 个有
- `Text Concatenate (JPS)` —— 3/8 个有
- `CLIPTextEncodeFlux` —— 2/8 个有
- `LoraLoader` —— 2/8 个有
- `CR Aspect Ratio SDXL` —— 1/8 个有
- `JjkConcat` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `StringFunction|pysssss` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 1080 | 512 - 1920 | 8 | 66% |
| 高度 | 1080 | 512 - 1920 | 8 | 68% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 512 - 1920，8 个样本
- 高度 中位数 1080，观测区间 512 - 1920，8 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：StringFunction|pysssss、CR Aspect Ratio SDXL、Text Concatenate (JPS)
