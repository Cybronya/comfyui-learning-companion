---
name: text_to_image_sampler_clip_unet_148
type: Text To Image
frequency: 5
level: moderate
coverage: 0.9448
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/anima_2085025424341561345.json, 图片生成/文生图/千问大模型文生图工作流_1959919853350105089.json, 图片生成/文生图/千问文生图工作流_1992469322945851393.json, 图片生成/文生图/千问文生图工作流_2003750459162673154.json, 图片生成/文生图/国漫cg风格-Z-image_2046874150148509697.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_148

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/anima_2085025424341561345.json、图片生成/文生图/千问大模型文生图工作流_1959919853350105089.json、图片生成/文生图/千问文生图工作流_1992469322945851393.json、图片生成/文生图/千问文生图工作流_2003750459162673154.json、图片生成/文生图/国漫cg风格-Z-image_2046874150148509697.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 4/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `ImageUpscaleWithModel` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `UpscaleModelLoader` —— 2/5 个有
- `CLIPLoaderGGUF` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `KSamplerAdvanced` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `VAEEncode` —— 1/5 个有
- `scale` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1280 | 5 | 90% |
| 高度 | 1024 | 768 - 1536 | 5 | 77% |
| LoRA 模型强度 | 0.9 | - | 2 | 89% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 35 | 8 - 35 | 5 | 63% |
| Prompt 约束强度(CFG) | 4 | 1 - 5 | 5 | 62% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1280，5 个样本，取值集中（一致性 90%）
- 高度 中位数 1024，观测区间 768 - 1536，5 个样本
- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 35，观测区间 8 - 35，5 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
