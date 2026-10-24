---
name: text_to_image_lora_sampler_clip_444
type: Text To Image
frequency: 4
level: strong
coverage: 0.90725
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-2512 电影艺术照_2033723824541274113.json, 图片生成/文生图/Qwen-Image-2.1_文生图+4步加速_2103505307195502594.json, 图片生成/文生图/Qwen-Image-2512 电影艺术照片_2011354812247445505.json, 图片生成/文生图/Qwen-Image-2512 电影艺术照片_2033160131764031490.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_444

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen-2512 电影艺术照_2033723824541274113.json、图片生成/文生图/Qwen-Image-2.1_文生图+4步加速_2103505307195502594.json、图片生成/文生图/Qwen-Image-2512 电影艺术照片_2011354812247445505.json、图片生成/文生图/Qwen-Image-2512 电影艺术照片_2033160131764031490.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 3/4 个有
- `LayerUtility: ImageReelComposit` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `easy seed` —— 3/4 个有
- `CR Text` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `ModelAttentionBackend` —— 1/4 个有
- `SaveImageAdvanced` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 6 - 10 | 4 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | ddim | - | 4 | 75% |
| 调度器 | ddim_uniform | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 1024 - 1920 | 4 | 69% |
| 高度 | 1024 | 1024 - 1080 | 4 | 98% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 6 - 10，4 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ddim，4 个样本，一致性 75%
- 调度器 最常用 ddim_uniform，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1920，4 个样本
- 高度 中位数 1024，观测区间 1024 - 1080，4 个样本，取值集中（一致性 98%）
