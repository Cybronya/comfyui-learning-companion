---
name: text_to_image_sampler_clip_unet_157
type: Text To Image
frequency: 2
level: weak
coverage: 0.8585
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/For 循环 - ZIT 批量提示词文生图_2026533897093259265.json, 图片生成/文生图/z-image随机Prompt.一键生成一组写真_2004923441016958978.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_157

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/For 循环 - ZIT 批量提示词文生图_2026533897093259265.json、图片生成/文生图/z-image随机Prompt.一键生成一组写真_2004923441016958978.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `CR Prompt List` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `DPRandomGenerator` —— 1/2 个有
- `GODMT_SplitString` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | - | 2 | 97% |
| 高度 | 1920 | - | 2 | 100% |
| 采样步数 | 9.5 | - | 2 | 95% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1052，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 9.5，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
