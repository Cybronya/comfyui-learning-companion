---
name: text_to_image_lora_sampler_clip_207
type: Text To Image
frequency: 9
level: moderate
coverage: 0.993111
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z image lora批量测试工作流_1998391849226264577.json, 图片生成/文生图/Z-IMAGE-4_8STEPN工作流_2022208584058146817.json, 图片生成/文生图/Z‑Image‑Turbo 极速出图・身材优化 + 丰满 LoRA 一体化_2048945759399186433.json, 图片生成/文生图/Z‑Image‑Turbo 极速出图・身材优化 + 丰满 LoRA 一体化_2096423431855230977.json, 图片生成/文生图/Z‑Image‑Turbo+蜂腰身材_2101265974426161154.json, 图片生成/文生图/闽粤纹样-文生图-纹样模型v1-48G_2022317374753476610.json, 图片生成/文生图/闽粤纹样-文生图-纹样模型v2-48G_2022345848922841089.json, 图片生成/文生图/闽粤纹样-文生图-纹样模型v3-48G_2022344333025878018.json, 图片生成/文生图/🦄Z-IMAGE-4&8STEPN🎯天下无腰_2022940063344103425.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_207

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Z image lora批量测试工作流_1998391849226264577.json、图片生成/文生图/Z-IMAGE-4_8STEPN工作流_2022208584058146817.json、图片生成/文生图/Z‑Image‑Turbo 极速出图・身材优化 + 丰满 LoRA 一体化_2048945759399186433.json、图片生成/文生图/Z‑Image‑Turbo 极速出图・身材优化 + 丰满 LoRA 一体化_2096423431855230977.json、图片生成/文生图/Z‑Image‑Turbo+蜂腰身材_2101265974426161154.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 8/9 个有
- `ConditioningZeroOut` —— 6/9 个有
- `ttN text` —— 3/9 个有
- `easy globalSeed` —— 2/9 个有
- `CR Seed` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有
- `ttN advPlot images` —— 1/9 个有
- `ttN advanced xyPlot` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 56 - 1080 | 9 | 27% |
| 高度 | 1920 | 512 - 1920 | 9 | 63% |
| 采样步数 | 8 | 4 - 10 | 9 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 56 - 1080，9 个样本，取值分散，一致性仅 27%
- 高度 中位数 1920，观测区间 512 - 1920，9 个样本
- 采样步数 中位数 8，观测区间 4 - 10，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
