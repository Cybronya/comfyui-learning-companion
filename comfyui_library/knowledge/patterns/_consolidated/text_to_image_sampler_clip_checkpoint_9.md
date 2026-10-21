---
name: text_to_image_sampler_clip_checkpoint_9
type: Text To Image
frequency: 8
level: moderate
coverage: 0.898625
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: [Label (rgthree)]
members: [图片生成/文生图/1953425536221675521.json, 图片生成/文生图/1954083787858690050.json, 图片生成/文生图/1954187211258392578.json, 图片生成/文生图/XL文生图LoRA翠玉汉服女_1782607885553938434.json, 图片生成/文生图/【遇见AI】基础放大方法之像素空间放大_2011366127523336193.json, 图片生成/文生图/半透明膨胀沙发_1795724323667951617.json, 图片生成/文生图/文生图折纸_1788776494500212738.json, 图片生成/文生图/艺术品高清图-青花龙_1778063653963108354.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_9

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1953425536221675521.json、图片生成/文生图/1954083787858690050.json、图片生成/文生图/1954187211258392578.json、图片生成/文生图/XL文生图LoRA翠玉汉服女_1782607885553938434.json、图片生成/文生图/【遇见AI】基础放大方法之像素空间放大_2011366127523336193.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 5/8 个有
- `LoraLoader` —— 5/8 个有
- `UpscaleModelLoader` —— 5/8 个有
- `VAEEncode` —— 5/8 个有
- `PreviewImage` —— 3/8 个有
- `Label (rgthree)` —— 2/8 个有
- `ImageScaleBy` —— 1/8 个有
- `VAELoader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 5 - 30 | 8 | 67% |
| Prompt 约束强度(CFG) | 8 | 2 - 8 | 8 | 72% |
| 采样算法 | dpmpp_2m | - | 8 | 50% |
| 调度器 | karras | - | 8 | 62% |
| 重绘幅度 | 1 | 0.3 - 1 | 8 | 63% |
| 宽度 | 576 | 512 - 1920 | 8 | 43% |
| 高度 | 704 | 512 - 1280 | 8 | 67% |
| LoRA 模型强度 | 0.5 | 0.5 - 0.6 | 5 | 92% |
| LoRA 文本强度 | 1 | 0.3 - 1 | 5 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 5 - 30，8 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 2 - 8，8 个样本
- 采样算法 最常用 dpmpp_2m，8 个样本，一致性 50%
- 调度器 最常用 karras，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，8 个样本
- 宽度 中位数 576，观测区间 512 - 1920，8 个样本，取值分散，一致性仅 43%
- 高度 中位数 704，观测区间 512 - 1280，8 个样本
- LoRA 模型强度 中位数 0.5，观测区间 0.5 - 0.6，5 个样本，取值集中（一致性 92%）
- LoRA 文本强度 中位数 1，观测区间 0.3 - 1，5 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)
