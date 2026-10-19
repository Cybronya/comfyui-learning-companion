---
name: text_to_image_lora_sampler_clip_274
type: Text To Image
frequency: 2
level: weak
coverage: 0.785
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, KSampler, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [YANC.ConcatStrings]
members: [图片生成/文生图/1915386250260316161.json, 图片生成/文生图/1943499738438397954.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_274

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1915386250260316161.json、图片生成/文生图/1943499738438397954.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConvertAny2String` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `RandomPrompt` —— 1/2 个有
- `Seed` —— 1/2 个有
- `YANC.ConcatStrings` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1044 | - | 2 | 98% |
| 高度 | 1712 | - | 2 | 90% |
| 采样步数 | 27.5 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1044，样本不足，未给区间，2 个样本，取值集中（一致性 98%）
- 高度 中位数 1712，样本不足，未给区间，2 个样本，取值集中（一致性 90%）
- 采样步数 中位数 27.5，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：YANC.ConcatStrings
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
