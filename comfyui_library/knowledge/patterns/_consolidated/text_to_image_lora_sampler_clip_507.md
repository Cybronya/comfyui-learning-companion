---
name: text_to_image_lora_sampler_clip_507
type: Text To Image
frequency: 3
level: strong
coverage: 0.814
common_nodes: [Bjornulf_ShowInt, CLIPLoader, CLIPTextEncode, CM_BoolBinaryOperation, CR Load LoRA, ConditioningZeroOut, EmptyLatentImage, FluxResolutionNode, ImageConcatMulti, ImpactConditionalBranch, Int, IntConditions, InversionDemoLazyIndexSwitch, JWIntegerSub, KSampler, LoadImage, PreviewImage, PrimitiveInt, PrimitiveString, PrimitiveStringMultiline, RH_Translator, SaveImage, StringListToCombo, Switch any [Crystools], TextInputBasic, UNETLoader, VAEDecode, VAELoader, easy mathString]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea 2 文生图【9个不同风格可选】_2069710272683663361.json, 图片生成/文生图/Krea 2 文生图【9个不同风格可选】_2070305854175399938.json, 图片生成/文生图/Krea 2 文生图【9个不同风格可选】_2080475070568419330.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_507

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea 2 文生图【9个不同风格可选】_2069710272683663361.json、图片生成/文生图/Krea 2 文生图【9个不同风格可选】_2070305854175399938.json、图片生成/文生图/Krea 2 文生图【9个不同风格可选】_2080475070568419330.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_BoolBinaryOperation`
- `CR Load LoRA`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FluxResolutionNode`
- `ImageConcatMulti`
- `ImpactConditionalBranch`
- `Int`
- `IntConditions`
- `InversionDemoLazyIndexSwitch`
- `JWIntegerSub`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `PrimitiveInt`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `RH_Translator`
- `SaveImage`
- `StringListToCombo`
- `Switch any [Crystools]`
- `TextInputBasic`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy mathString`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 1280 - 1280 | 3 | 100% |
| 高度 | 720 | 720 - 720 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
- 高度 中位数 720，观测区间 720 - 720，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
