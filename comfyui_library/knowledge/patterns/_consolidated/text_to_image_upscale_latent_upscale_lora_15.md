---
name: text_to_image_upscale_latent_upscale_lora_15
type: Text To Image
frequency: 3
level: strong
coverage: 0.743
common_nodes: [CLIPTextEncode, CR Apply LoRA Stack, CR LoRA Stack, CheckpointLoaderSimple, EmptyLatentImage, ImageScaleBy, Int, KSampler, LatentUpscale, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [CR Apply LoRA Stack, CR LoRA Stack]
members: [图片生成/文生图/1963212956588814337.json, 图片生成/文生图/fgo风格_2089616207459741697.json, 图片生成/文生图/文生图+LoRA (1) (2) (1) (1)_1998630071667712001.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_15

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1963212956588814337.json、图片生成/文生图/fgo风格_2089616207459741697.json、图片生成/文生图/文生图+LoRA (1) (2) (1) (1)_1998630071667712001.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Apply LoRA Stack`
- `CR LoRA Stack`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `ImageScaleBy`
- `Int`
- `KSampler`
- `LatentUpscale`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningCombine` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `LayerUtility: TextJoinV2` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| 采样步数 | 30 | 25 - 30 | 3 | 92% |
| Prompt 约束强度(CFG) | 6 | 3 - 7 | 3 | 68% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 25 - 30，3 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 3 - 7，3 个样本
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Apply LoRA Stack、CR LoRA Stack
