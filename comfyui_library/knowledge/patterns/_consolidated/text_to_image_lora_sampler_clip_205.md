---
name: text_to_image_lora_sampler_clip_205
type: Text To Image
frequency: 6
level: moderate
coverage: 0.989667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z image lora批量测试工作流_1998391849226264577.json, 图片生成/文生图/Z-IMAGE-4_8STEPN工作流_2022208584058146817.json, 图片生成/文生图/Z-Image-Turbo 身材优化+丰满LoRA_2004613231027126274.json, 图片生成/文生图/Z‑Image‑Turbo 极速出图・身材优化 + 丰满 LoRA 一体化_2096423431855230977.json, 图片生成/文生图/Z‑Image‑Turbo+蜂腰身材_2101265974426161154.json, 图片生成/文生图/🦄Z-IMAGE-4&8STEPN🎯天下无腰_2022940063344103425.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_205

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z image lora批量测试工作流_1998391849226264577.json、图片生成/文生图/Z-IMAGE-4_8STEPN工作流_2022208584058146817.json、图片生成/文生图/Z-Image-Turbo 身材优化+丰满LoRA_2004613231027126274.json、图片生成/文生图/Z‑Image‑Turbo 极速出图・身材优化 + 丰满 LoRA 一体化_2096423431855230977.json、图片生成/文生图/Z‑Image‑Turbo+蜂腰身材_2101265974426161154.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 4/6 个有
- `easy globalSeed` —— 2/6 个有
- `CR Seed` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `ttN advPlot images` —— 1/6 个有
- `ttN advanced xyPlot` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 56 - 1080 | 6 | 25% |
| 高度 | 1728 | 512 - 1920 | 6 | 54% |
| 采样步数 | 8.5 | 4 - 10 | 6 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 56 - 1080，6 个样本，取值分散，一致性仅 25%
- 高度 中位数 1728，观测区间 512 - 1920，6 个样本
- 采样步数 中位数 8.5，观测区间 4 - 10，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
