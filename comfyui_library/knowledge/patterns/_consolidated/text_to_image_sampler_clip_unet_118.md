---
name: text_to_image_sampler_clip_unet_118
type: Text To Image
frequency: 3
level: moderate
coverage: 0.980333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1968880877902155777.json, 图片生成/文生图/沙雕场景-klein_2083534277521793026.json, 图片生成/文生图/铅笔画 klein_2078250350842306561.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_118

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1968880877902155777.json、图片生成/文生图/沙雕场景-klein_2083534277521793026.json、图片生成/文生图/铅笔画 klein_2078250350842306561.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `ReferenceLatent` —— 2/3 个有
- `easy anythingIndexSwitch` —— 2/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `ImageScaleToMaxDimension` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `NunchakuFluxDiTLoader` —— 1/3 个有
- `NunchakuFluxLoraLoader` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `scale` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1920 | 3 | 68% |
| 高度 | 1080 | 1024 - 1536 | 3 | 81% |
| LoRA 模型强度 | 0.9 | - | 2 | 89% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 4 | 4 - 35 | 3 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 3 | 43% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1920，3 个样本
- 高度 中位数 1080，观测区间 1024 - 1536，3 个样本，取值集中（一致性 81%）
- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 35，3 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，3 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
