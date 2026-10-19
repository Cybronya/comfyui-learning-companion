---
name: text_to_image_sampler_clip_vae
type: Text To Image
frequency: 8
level: moderate
coverage: 0.89675
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [Text Multiline]
members: [图片生成/文生图/1912954176630943746.json, 图片生成/文生图/1912954209854259202.json, 图片生成/文生图/1914963069880205314.json, 图片生成/文生图/1919938265468567553.json, 图片生成/文生图/1922920426165473282.json, 图片生成/文生图/1946442950954115073.json, 图片生成/文生图/1946446513008730114.json, 图片生成/文生图/1946760909358555137.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1912954176630943746.json、图片生成/文生图/1912954209854259202.json、图片生成/文生图/1914963069880205314.json、图片生成/文生图/1919938265468567553.json、图片生成/文生图/1922920426165473282.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `DualCLIPLoader` —— 6/8 个有
- `UNETLoader` —— 5/8 个有
- `ConditioningZeroOut` —— 3/8 个有
- `DeepTranslatorTextNode` —— 3/8 个有
- `LoraLoader` —— 3/8 个有
- `CheckpointLoaderSimple` —— 2/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `NunchakuFluxDiTLoader` —— 1/8 个有
- `PMRF` —— 1/8 个有
- `Text Multiline` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 800 | 800 - 1280 | 8 | 81% |
| 高度 | 1200 | 1024 - 1920 | 8 | 80% |
| 采样步数 | 28 | 20 - 35 | 8 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 7 | 8 | 0% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| LoRA 模型强度 | 1 | 0.8 - 1 | 3 | 90% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 800，观测区间 800 - 1280，8 个样本，取值集中（一致性 81%）
- 高度 中位数 1200，观测区间 1024 - 1920，8 个样本，取值集中（一致性 80%）
- 采样步数 中位数 28，观测区间 20 - 35，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 7，8 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline
