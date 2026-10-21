---
name: text_to_image_lora_sampler_clip_230
type: Text To Image
frequency: 5
level: strong
coverage: 0.5832
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, PreviewAny, PrimitiveBoolean, PrimitiveStringMultiline, ResolutionSelector, SaveImage, StringConcatenate, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 Turbo 微调文生图 (内)_2073841889299750914.json, 图片生成/文生图/Krea2 文生图极速版_2075489210370445314.json, 图片生成/文生图/Krea2_turbo_t2i_2069610463943553025.json, 图片生成/文生图/image_krea2_turbo_t2i_2099207878002429953.json, 图片生成/文生图/krea2-t2i_2101830220889288705.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_230

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Krea2 Turbo 微调文生图 (内)_2073841889299750914.json、图片生成/文生图/Krea2 文生图极速版_2075489210370445314.json、图片生成/文生图/Krea2_turbo_t2i_2069610463943553025.json、图片生成/文生图/image_krea2_turbo_t2i_2099207878002429953.json、图片生成/文生图/krea2-t2i_2101830220889288705.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `StringConcatenate`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 3/5 个有
- `CustomCombo` —— 2/5 个有
- `RegexExtract` —— 2/5 个有
- `StringReplace` —— 2/5 个有
- `ConditioningKrea2Rebalance` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `ZML_IntegerFloatConverter` —— 1/5 个有
- `easy prompt` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |
| 采样步数 | 8 | 8 - 9 | 5 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 9，5 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
