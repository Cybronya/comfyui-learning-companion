---
name: text_to_image_sampler_clip_checkpoint_12
type: Text To Image
frequency: 4
level: moderate
coverage: 0.7445
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: [Text Multiline, CR Text Concatenate]
members: [图片生成/文生图/1979416721058598913.json, 图片生成/文生图/1980214445693689857.json, 图片生成/文生图/1982645105960067073.json, 图片生成/文生图/1982665506299756546.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_12

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1979416721058598913.json、图片生成/文生图/1980214445693689857.json、图片生成/文生图/1982645105960067073.json、图片生成/文生图/1982665506299756546.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `CR Text Concatenate` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `LoraLoader` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `VAEEncode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 824 | 784 - 1024 | 4 | 89% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 22 | 15 - 25 | 4 | 80% |
| Prompt 约束强度(CFG) | 7 | 5 - 8 | 4 | 84% |
| 采样算法 | dpmpp_2m_sde | - | 4 | 50% |
| 调度器 | karras | - | 4 | 50% |
| 重绘幅度 | 1 | 0.25 - 1 | 4 | 60% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 824，观测区间 784 - 1024，4 个样本，取值集中（一致性 89%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 22，观测区间 15 - 25，4 个样本
- Prompt 约束强度(CFG) 中位数 7，观测区间 5 - 8，4 个样本，取值集中（一致性 84%）
- 采样算法 最常用 dpmpp_2m_sde，4 个样本，一致性 50%
- 调度器 最常用 karras，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，4 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、CR Text Concatenate
