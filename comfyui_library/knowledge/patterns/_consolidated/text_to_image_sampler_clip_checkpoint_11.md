---
name: text_to_image_sampler_clip_checkpoint_11
type: Text To Image
frequency: 9
level: moderate
coverage: 0.981778
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [sd1.5/lora.png, sd1.5/text-to-image-workflow.png, 图片生成/图生图/45.tonnie-Qwen Edit-Rapid AIO改背景，改风格（效果不好）_2005325056215576577.json, 图片生成/文生图/2025_2000816337700126721.json, 图片生成/文生图/Goth_qipao哥特旗袍女孩 v2_1931901282749972482.json, 图片生成/文生图/Goth_qipao哥特旗袍女孩_1931899467023495169.json, 图片生成/文生图/Lora_1894234987661557762.json, 平台全量/乐高人物制作_1782343976217522177.json, 平台全量/手机壳制作_1782351676301160449.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_11

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（sd1.5/lora.png、sd1.5/text-to-image-workflow.png、图片生成/图生图/45.tonnie-Qwen Edit-Rapid AIO改背景，改风格（效果不好）_2005325056215576577.json、图片生成/文生图/2025_2000816337700126721.json、图片生成/文生图/Goth_qipao哥特旗袍女孩 v2_1931901282749972482.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 7/9 个有
- `VAEEncode` —— 4/9 个有
- `LatentUpscale` —— 3/9 个有
- `LoadImage` —— 3/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1280 | 9 | 72% |
| 高度 | 1024 | 512 - 2048 | 9 | 57% |
| LoRA 模型强度 | 0.8 | 0.6 - 1 | 7 | 83% |
| LoRA 文本强度 | 1 | 0.8 - 1 | 7 | 91% |
| 采样步数 | 20 | 6 - 40 | 9 | 55% |
| Prompt 约束强度(CFG) | 7 | 1 - 8 | 9 | 65% |
| 采样算法 | euler | - | 9 | 44% |
| 调度器 | normal | - | 9 | 67% |
| 重绘幅度 | 0.65 | 0.21 - 1 | 9 | 54% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1280，9 个样本
- 高度 中位数 1024，观测区间 512 - 2048，9 个样本
- LoRA 模型强度 中位数 0.8，观测区间 0.6 - 1，7 个样本，取值集中（一致性 83%）
- LoRA 文本强度 中位数 1，观测区间 0.8 - 1，7 个样本，取值集中（一致性 91%）
- 采样步数 中位数 20，观测区间 6 - 40，9 个样本
- Prompt 约束强度(CFG) 中位数 7，观测区间 1 - 8，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 44%
- 调度器 最常用 normal，9 个样本，一致性 67%
- 重绘幅度 中位数 0.65，观测区间 0.21 - 1，9 个样本
