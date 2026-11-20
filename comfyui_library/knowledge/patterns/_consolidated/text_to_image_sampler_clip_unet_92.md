---
name: text_to_image_sampler_clip_unet_92
type: Text To Image
frequency: 8
level: weak
coverage: 0.967125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-IMAGE-4_8STEPN工作流_2022208584058146817.json, 图片生成/文生图/Z-IMAGE-TURBO：文生图 （api 专用）_2034271324402622466.json, 图片生成/文生图/Z-Image Base 8步&4步加速_2022636633476046849.json, 图片生成/文生图/Z-Image Turbo _ 文生图_1916516546913435650.json, 图片生成/文生图/Z‑Image‑Turbo 极速出图・身材优化 + 丰满 LoRA 一体化_2048945759399186433.json, 图片生成/文生图/Z‑Image‑Turbo 极速出图・身材优化 + 丰满 LoRA 一体化_2096423431855230977.json, 图片生成/文生图/Z‑Image‑Turbo+蜂腰身材_2101265974426161154.json, 图片生成/文生图/🦄Z-IMAGE-4&8STEPN🎯天下无腰_2022940063344103425.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_92

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Z-IMAGE-4_8STEPN工作流_2022208584058146817.json、图片生成/文生图/Z-IMAGE-TURBO：文生图 （api 专用）_2034271324402622466.json、图片生成/文生图/Z-Image Base 8步&4步加速_2022636633476046849.json、图片生成/文生图/Z-Image Turbo _ 文生图_1916516546913435650.json、图片生成/文生图/Z‑Image‑Turbo 极速出图・身材优化 + 丰满 LoRA 一体化_2048945759399186433.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `ModelSamplingAuraFlow` —— 7/8 个有
- `Int` —— 5/8 个有
- `easy globalSeed` —— 2/8 个有
- `Anything Everywhere` —— 1/8 个有
- `Anything Everywhere3` —— 1/8 个有
- `ImpactInt` —— 1/8 个有
- `String Literal` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 4 - 20 | 8 | 48% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 8 | 47% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 512 | 56 - 1920 | 8 | 6% |
| 高度 | 1308 | 512 - 1920 | 8 | 53% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 4 - 20，8 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，8 个样本，取值分散，一致性仅 47%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 56 - 1920，8 个样本，取值分散，一致性仅 6%
- 高度 中位数 1308，观测区间 512 - 1920，8 个样本
- 高发问题（23/8 个样本）：Steps较低可能导致细节不足
