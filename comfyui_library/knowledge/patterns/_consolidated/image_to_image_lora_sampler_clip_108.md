---
name: image_to_image_lora_sampler_clip_108
type: Image To Image
frequency: 3
level: moderate
coverage: 0.918333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, LoadImage, LoraLoader, SaveImage, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图生图（含Lora小模型）工作流_1970297101831860225.json, 图片生成/图生图/图生图：Qwen-image-Edite-Remix-AIO-v2.0_2046034572529373185.json, 图片生成/图生图/超级易懂基础图生图工作流_1967046500456992769.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_108

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图生图（含Lora小模型）工作流_1970297101831860225.json、图片生成/图生图/图生图：Qwen-image-Edite-Remix-AIO-v2.0_2046034572529373185.json、图片生成/图生图/超级易懂基础图生图工作流_1967046500456992769.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `CR Text Concatenate` —— 2/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LatentUpscaleBy` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 25 | 3 | 45% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 5 | 3 | 49% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 0.5 | 0.3 - 0.65 | 3 | 70% |
| LoRA 模型强度 | 1 | 1 - 1.01 | 3 | 100% |
| LoRA 文本强度 | 1 | 0.8 - 1 | 3 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 25，3 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 5，3 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 0.5，观测区间 0.3 - 0.65，3 个样本
- LoRA 模型强度 中位数 1，观测区间 1 - 1.01，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
