---
name: text_to_image_lora_sampler_clip_554
type: Text To Image
frequency: 3
level: strong
coverage: 0.965
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy isMaskEmpty]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/QwenImag文生图_1989221367381889026.json, 图片生成/文生图/QwenImag线上文生图（提供本地API调用）_1986272605315485698.json, 图片生成/文生图/Qwen趣味剪纸生成_1962073493561085953.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_554

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/QwenImag文生图_1989221367381889026.json、图片生成/文生图/QwenImag线上文生图（提供本地API调用）_1986272605315485698.json、图片生成/文生图/Qwen趣味剪纸生成_1962073493561085953.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy isMaskEmpty`

**可变部分**（部分 workflow 才有）：
- `SaveLatent` —— 2/3 个有
- `easy seed` —— 2/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1536 | 1536 - 1536 | 3 | 100% |
| 高度 | 928 | 928 - 928 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
- 高度 中位数 928，观测区间 928 - 928，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
