---
name: unknown_workflow_lora_sampler_clip_123
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.945
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX图生图+Lora_洗图v2.0_1943525612562620418.json, 图片生成/图生图/FLUX图生图_1968865610891501570.json, 图片生成/图生图/Flux-图生图（Lora）_1947629935571722241.json, 图片生成/图生图/Flux图生图反推加速高清放大_1900124364195491841.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_123

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX图生图+Lora_洗图v2.0_1943525612562620418.json、图片生成/图生图/FLUX图生图_1968865610891501570.json、图片生成/图生图/Flux-图生图（Lora）_1947629935571722241.json、图片生成/图生图/Flux图生图反推加速高清放大_1900124364195491841.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `CR Upscale Image` —— 2/4 个有
- `Florence2ModelLoader` —— 2/4 个有
- `Florence2Run` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `ConstrainImage|pysssss` —— 1/4 个有
- `EmptyLatentImage` —— 1/4 个有
- `Float` —— 1/4 个有
- `LoadImagesFromURL` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `TeaCache` —— 1/4 个有
- `easy imageSize` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.9 | 0.7 - 1 | 4 | 85% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1536 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.9，观测区间 0.7 - 1，4 个样本，取值集中（一致性 85%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
