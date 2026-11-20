---
name: text_to_image_lora_sampler_clip_201
type: Text To Image
frequency: 9
level: moderate
coverage: 0.703111
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, PreviewAny, PrimitiveBoolean, PrimitiveStringMultiline, ResolutionSelector, SaveImage, StringConcatenate, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2_turbo_t2i_2070347845965803522.json, 图片生成/图生图/Krea2_turbo_t2i_2071412507268444161.json, 图片生成/图生图/image_krea2_optimizer_workflow_2073588797480198146.json, 图片生成/图生图/image_krea2_tourbo_lora_t2i_edit_2073947059031461889.json, 图片生成/文生图/K2模特级生成_2089374387597307906.json, 图片生成/文生图/Krea2_turbo_t2i_2069610463943553025.json, 图片生成/文生图/opsv-krea2_t2i_2074897972374097921.json, 图片生成/文生图/opsv-krea2_t2i_2086450223353778178.json, 数字人/数字人/krea2_文生图_2074796223978106881.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_201

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Krea2_turbo_t2i_2070347845965803522.json、图片生成/图生图/Krea2_turbo_t2i_2071412507268444161.json、图片生成/图生图/image_krea2_optimizer_workflow_2073588797480198146.json、图片生成/图生图/image_krea2_tourbo_lora_t2i_edit_2073947059031461889.json、图片生成/文生图/K2模特级生成_2089374387597307906.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 9 个 workflow 都包含：
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
- `FaceDetailer` —— 6/9 个有
- `SAMLoader` —— 6/9 个有
- `UltralyticsDetectorProvider` —— 6/9 个有
- `RTXVideoSuperResolution` —— 5/9 个有
- `CustomCombo` —— 3/9 个有
- `PrimitiveInt` —— 3/9 个有
- `RH_Translator` —— 3/9 个有
- `RegexExtract` —— 3/9 个有
- `StringReplace` —— 3/9 个有
- `CR Prompt Text` —— 2/9 个有
- `LoadImage` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `VAEEncode` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 2048 | 1024 - 2048 | 9 | 72% |
| 高度 | 2048 | 1024 - 2048 | 9 | 72% |
| 采样步数 | 2 | 2 - 8 | 9 | 36% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | deis | - | 9 | 56% |
| 调度器 | bong_tangent | - | 9 | 56% |
| 重绘幅度 | 0.2 | 0.2 - 1 | 9 | 29% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 2048，观测区间 1024 - 2048，9 个样本
- 高度 中位数 2048，观测区间 1024 - 2048，9 个样本
- 采样步数 中位数 2，观测区间 2 - 8，9 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，9 个样本，一致性 56%
- 调度器 最常用 bong_tangent，9 个样本，一致性 56%
- 重绘幅度 中位数 0.2，观测区间 0.2 - 1，9 个样本，取值分散，一致性仅 29%
- 高发问题（14/9 个样本）：Steps较低可能导致细节不足
