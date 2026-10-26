---
name: text_to_image_lora_sampler_clip_539
type: Text To Image
frequency: 3
level: moderate
coverage: 0.825
common_nodes: [AddLabel, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima base v1 动漫生图_2059172782583410690.json, 图片生成/文生图/Anima base v1 动漫生图_2093989338236407810.json, 图片生成/文生图/Anima vs Anima Preview3 vs Illustrious 对比测试_2100439731292168193.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_539

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Anima base v1 动漫生图_2059172782583410690.json、图片生成/文生图/Anima base v1 动漫生图_2093989338236407810.json、图片生成/文生图/Anima vs Anima Preview3 vs Illustrious 对比测试_2100439731292168193.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
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
- `PrimitiveInt` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `Text` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 6 - 30 | 3 | 49% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 3 | 53% |
| 采样算法 | euler_ancestral_cfg_pp | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 896 | 896 - 1024 | 3 | 94% |
| 高度 | 1152 | 1024 - 1152 | 3 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 6 - 30，3 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，3 个样本
- 采样算法 最常用 euler_ancestral_cfg_pp，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 896 - 1024，3 个样本，取值集中（一致性 94%）
- 高度 中位数 1152，观测区间 1024 - 1152，3 个样本，取值集中（一致性 95%）
