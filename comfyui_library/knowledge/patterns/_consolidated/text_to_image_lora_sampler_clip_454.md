---
name: text_to_image_lora_sampler_clip_454
type: Text To Image
frequency: 4
level: strong
coverage: 0.896
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, LoraLoader, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/厚涂cg风格-文生图-krea2_2077167625519583233.json, 图片生成/文生图/国漫cg风格-文生图-krea2_2077165275518160898.json, 图片生成/文生图/沙雕场景-四视图-klein_2084085233376382977.json, 图片生成/文生图/鬼刀画风-文生图-krea2_2076834870831181825.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_454

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/厚涂cg风格-文生图-krea2_2077167625519583233.json、图片生成/文生图/国漫cg风格-文生图-krea2_2077165275518160898.json、图片生成/文生图/沙雕场景-四视图-klein_2084085233376382977.json、图片生成/文生图/鬼刀画风-文生图-krea2_2076834870831181825.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LatentUpscaleBy` —— 3/4 个有
- `MultiTextConcatenate` —— 3/4 个有
- `OneButtonPrompt` —— 3/4 个有
- `PreviewAny` —— 3/4 个有
- `CR Prompt List` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 采样步数 | 5 | 4 - 6 | 4 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 0.6 | 0.6 - 1 | 4 | 75% |
| 宽度 | 1664 | 1024 - 1920 | 4 | 79% |
| 高度 | 1004 | 928 - 1536 | 4 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 5，观测区间 4 - 6，4 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 1，4 个样本
- 宽度 中位数 1664，观测区间 1024 - 1920，4 个样本
- 高度 中位数 1004，观测区间 928 - 1536，4 个样本
- 高发问题（7/4 个样本）：Steps较低可能导致细节不足
