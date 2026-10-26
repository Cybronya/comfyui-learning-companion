---
name: text_to_image_sampler_clip_checkpoint_9
type: Text To Image
frequency: 7
level: moderate
coverage: 0.976571
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [sd1.5/lora.png, sd1.5/text-to-image-workflow.png, 图片生成/图生图/45.tonnie-Qwen Edit-Rapid AIO改背景，改风格（效果不好）_2005325056215576577.json, 图片生成/文生图/2025_2000816337700126721.json, 图片生成/文生图/Goth_qipao哥特旗袍女孩 v2_1931901282749972482.json, 图片生成/文生图/Goth_qipao哥特旗袍女孩_1931899467023495169.json, 图片生成/文生图/Lora_1894234987661557762.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_9

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（sd1.5/lora.png、sd1.5/text-to-image-workflow.png、图片生成/图生图/45.tonnie-Qwen Edit-Rapid AIO改背景，改风格（效果不好）_2005325056215576577.json、图片生成/文生图/2025_2000816337700126721.json、图片生成/文生图/Goth_qipao哥特旗袍女孩 v2_1931901282749972482.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 5/7 个有
- `LatentUpscale` —— 3/7 个有
- `LoadImage` —— 3/7 个有
- `VAEEncode` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1280 | 7 | 69% |
| 高度 | 1024 | 512 - 2048 | 7 | 51% |
| LoRA 模型强度 | 0.8 | 0.75 - 1 | 5 | 89% |
| LoRA 文本强度 | 0.9 | 0.8 - 1 | 5 | 90% |
| 采样步数 | 20 | 6 - 40 | 7 | 50% |
| Prompt 约束强度(CFG) | 6.5 | 1 - 8 | 7 | 61% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | normal | - | 7 | 57% |
| 重绘幅度 | 1 | 0.5 - 1 | 7 | 74% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1280，7 个样本
- 高度 中位数 1024，观测区间 512 - 2048，7 个样本
- LoRA 模型强度 中位数 0.8，观测区间 0.75 - 1，5 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 0.9，观测区间 0.8 - 1，5 个样本，取值集中（一致性 90%）
- 采样步数 中位数 20，观测区间 6 - 40，7 个样本
- Prompt 约束强度(CFG) 中位数 6.5，观测区间 1 - 8，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 normal，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，7 个样本
