---
name: text_to_image_sampler_clip_unet_222
type: Text To Image
frequency: 2
level: weak
coverage: 0.9525
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Boogu vs Z vs Q2152工作流_2069058937420337153.json, 图片生成/文生图/Z-image轻量级 AI 图像生成_1994293019830665217.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_222

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Boogu vs Z vs Q2152工作流_2069058937420337153.json、图片生成/文生图/Z-image轻量级 AI 图像生成_1994293019830665217.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `StringConstantMultiline` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 29 | - | 2 | 28% |
| Prompt 约束强度(CFG) | 1.75 | - | 2 | 57% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1792 | - | 2 | 93% |
| 高度 | 1004 | - | 2 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 29，样本不足，未给区间，2 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 1.75，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1792，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 高度 中位数 1004，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
