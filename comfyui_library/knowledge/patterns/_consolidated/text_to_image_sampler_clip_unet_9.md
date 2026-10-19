---
name: text_to_image_sampler_clip_unet_9
type: Text To Image
frequency: 7
level: moderate
coverage: 0.924
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-Turbo_CG半写实_2102648900237746178.json, 图片生成/文生图/Z-image生图_2102776816992866305.json, 图片生成/文生图/ki_krea2人物四视图_2104971759140294657.json, 图片生成/文生图/ki_krea2人物四视图_2107463809878282242.json, 图片生成/文生图/千问qwen-image-2.1文生图工作流_2104553799485583362.json, 图片生成/文生图/千问qwen-image-2.1文生图工作流（不可商用）_2101941085793771521.json, 图片生成/文生图/文生图ZImage_2064901103308861442.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_9

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Krea2-Turbo_CG半写实_2102648900237746178.json、图片生成/文生图/Z-image生图_2102776816992866305.json、图片生成/文生图/ki_krea2人物四视图_2104971759140294657.json、图片生成/文生图/ki_krea2人物四视图_2107463809878282242.json、图片生成/文生图/千问qwen-image-2.1文生图工作流_2104553799485583362.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `PreviewImage` —— 4/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `CompressImages` —— 1/7 个有
- `EmptyImage` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `ModelSamplingAuraFlow` —— 1/7 个有
- `PromptBatchQueue` —— 1/7 个有
- `ResolutionSelector` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 30 | 7 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1440 | 864 - 1536 | 7 | 78% |
| 高度 | 1920 | 1024 - 2048 | 7 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 30，7 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1440，观测区间 864 - 1536，7 个样本
- 高度 中位数 1920，观测区间 1024 - 2048，7 个样本
