---
name: text_to_image_lora_sampler_clip_276
type: Text To Image
frequency: 2
level: weak
coverage: 0.9
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, LoraLoader, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text, Text Concatenate]
members: [图片生成/文生图/1922031385077547010.json, 图片生成/文生图/1981699548944965633.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_276

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1922031385077547010.json、图片生成/文生图/1981699548944965633.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ArgosTranslateTextNode` —— 1/2 个有
- `Bjornulf_ShowStringText` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Int` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 2 | 75% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 1.5 | - | 2 | 67% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1.5，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Text Concatenate
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
