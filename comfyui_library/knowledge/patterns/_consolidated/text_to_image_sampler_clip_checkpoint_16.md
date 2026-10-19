---
name: text_to_image_sampler_clip_checkpoint_16
type: Text To Image
frequency: 2
level: weak
coverage: 0.793
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, DeepTranslatorTextNode, EmptyLatentImage, KSampler, SaveImage, ShowText|pysssss, VAEDecode]
problems: []
missing: [Text Multiline]
members: [图片生成/文生图/1935617160456622081.json, 图片生成/文生图/1946045185828548610.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1935617160456622081.json、图片生成/文生图/1946045185828548610.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DeepTranslatorTextNode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConcatStringSingle` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `Text Multiline` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 496 | - | 2 | 97% |
| 高度 | 672 | - | 2 | 76% |
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 7.5 | - | 2 | 93% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | karras | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.6 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 496，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 高度 中位数 672，样本不足，未给区间，2 个样本
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 7.5，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
