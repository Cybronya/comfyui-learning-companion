---
name: text_to_image_sampler_clip_checkpoint_10
type: Text To Image
frequency: 6
level: moderate
coverage: 0.892667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: [Label (rgthree)]
members: [图片生成/文生图/1953425536221675521.json, 图片生成/文生图/1954083787858690050.json, 图片生成/文生图/1954187211258392578.json, 图片生成/文生图/Lora_1894234987661557762.json, 图片生成/文生图/文生图折纸_1788776494500212738.json, 图片生成/文生图/艺术品高清图-青花龙_1778063653963108354.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_10

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1953425536221675521.json、图片生成/文生图/1954083787858690050.json、图片生成/文生图/1954187211258392578.json、图片生成/文生图/Lora_1894234987661557762.json、图片生成/文生图/文生图折纸_1788776494500212738.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 4/6 个有
- `VAEEncode` —— 4/6 个有
- `ImageUpscaleWithModel` —— 2/6 个有
- `Label (rgthree)` —— 2/6 个有
- `UpscaleModelLoader` —— 2/6 个有
- `ImageScaleBy` —— 1/6 个有
- `LoadImage` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 5 - 30 | 6 | 62% |
| Prompt 约束强度(CFG) | 8 | 2 - 8 | 6 | 68% |
| 采样算法 | dpmpp_2m | - | 6 | 33% |
| 调度器 | karras | - | 6 | 50% |
| 重绘幅度 | 0.625 | 0.3 - 1 | 6 | 59% |
| 宽度 | 640 | 512 - 1920 | 6 | 42% |
| 高度 | 768 | 512 - 1080 | 6 | 75% |
| LoRA 模型强度 | 0.5 | 0.5 - 1 | 4 | 65% |
| LoRA 文本强度 | 1 | 0.3 - 1 | 4 | 63% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 5 - 30，6 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 2 - 8，6 个样本
- 采样算法 最常用 dpmpp_2m，6 个样本，一致性 33%
- 调度器 最常用 karras，6 个样本，一致性 50%
- 重绘幅度 中位数 0.625，观测区间 0.3 - 1，6 个样本
- 宽度 中位数 640，观测区间 512 - 1920，6 个样本，取值分散，一致性仅 42%
- 高度 中位数 768，观测区间 512 - 1080，6 个样本
- LoRA 模型强度 中位数 0.5，观测区间 0.5 - 1，4 个样本
- LoRA 文本强度 中位数 1，观测区间 0.3 - 1，4 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)
