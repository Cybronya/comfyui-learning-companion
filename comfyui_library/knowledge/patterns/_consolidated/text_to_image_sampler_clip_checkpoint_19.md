---
name: text_to_image_sampler_clip_checkpoint_19
type: Text To Image
frequency: 3
level: moderate
coverage: 0.771
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, DeepTranslatorTextNode, EmptyLatentImage, KSampler, SaveImage, ShowText|pysssss, VAEDecode]
problems: []
missing: [Text Multiline]
members: [图片生成/文生图/1935617160456622081.json, 图片生成/文生图/1946045185828548610.json, 图片生成/文生图/工作流基础篇-2-文生图带翻译工作流（翻译Alek节点）_2012411720182013954.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_19

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1935617160456622081.json、图片生成/文生图/1946045185828548610.json、图片生成/文生图/工作流基础篇-2-文生图带翻译工作流（翻译Alek节点）_2012411720182013954.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DeepTranslatorTextNode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConcatStringSingle` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `Text Multiline` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 480 - 1024 | 3 | 63% |
| 高度 | 832 | 512 - 1024 | 3 | 73% |
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 8 | 7 - 8 | 3 | 94% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.6 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 480 - 1024，3 个样本
- 高度 中位数 832，观测区间 512 - 1024，3 个样本
- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 7 - 8，3 个样本，取值集中（一致性 94%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline
