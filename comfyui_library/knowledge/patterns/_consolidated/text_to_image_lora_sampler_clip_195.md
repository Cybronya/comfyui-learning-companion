---
name: text_to_image_lora_sampler_clip_195
type: Text To Image
frequency: 4
level: moderate
coverage: 0.85475
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, LoraLoader, PreviewImage, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1928363238206128129.json, 图片生成/文生图/1931623761387433985.json, 图片生成/文生图/Text-to-Image + LoRA_1878782083018514433.json, 图片生成/文生图/艺术品高清图-鼻烟壶_1778063085018353666.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_195

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1928363238206128129.json、图片生成/文生图/1931623761387433985.json、图片生成/文生图/Text-to-Image + LoRA_1878782083018514433.json、图片生成/文生图/艺术品高清图-鼻烟壶_1778063085018353666.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoader`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LatentUpscaleBy` —— 2/4 个有
- `JjkText` —— 1/4 个有
- `LatentUpscale` —— 1/4 个有
- `TextCombinerTwo` —— 1/4 个有
- `VAEEncode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.65 | 0.4 - 1.15 | 4 | 59% |
| LoRA 文本强度 | 0.9 | 0.3 - 1 | 4 | 63% |
| 宽度 | 1024 | 512 - 1024 | 4 | 75% |
| 高度 | 1024 | 512 - 1280 | 4 | 71% |
| 采样步数 | 20 | 5 - 35 | 4 | 47% |
| Prompt 约束强度(CFG) | 5.75 | 2 - 8 | 4 | 50% |
| 采样算法 | dpmpp_2m | - | 4 | 50% |
| 调度器 | karras | - | 4 | 75% |
| 重绘幅度 | 0.775 | 0.5 - 1 | 4 | 69% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.65，观测区间 0.4 - 1.15，4 个样本
- LoRA 文本强度 中位数 0.9，观测区间 0.3 - 1，4 个样本
- 宽度 中位数 1024，观测区间 512 - 1024，4 个样本
- 高度 中位数 1024，观测区间 512 - 1280，4 个样本
- 采样步数 中位数 20，观测区间 5 - 35，4 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 5.75，观测区间 2 - 8，4 个样本
- 采样算法 最常用 dpmpp_2m，4 个样本，一致性 50%
- 调度器 最常用 karras，4 个样本，一致性 75%
- 重绘幅度 中位数 0.775，观测区间 0.5 - 1，4 个样本
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
