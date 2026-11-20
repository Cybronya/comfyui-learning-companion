---
name: text_to_image_lora_sampler_clip_544
type: Text To Image
frequency: 3
level: strong
coverage: 0.42
common_nodes: [Anything Everywhere, CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, ImageStitch, KSampler, LoraLoaderModelOnly, PreviewImage, ResolutionSelector, SaveImage, Seed (rgthree), SetNode, UNETLoader, VAEDecode, VAELoader, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea 2 深度探索：视觉参考，让图片成为 Prompt_2078509637904719874.json, 图片生成/文生图/Krea 2：我们可能误解了 Raw 模型_2075137774411411458.json, 图片生成/文生图/Krea+2+深度探索：视觉参考，让图片成为+Prompt (1)_2082655123242840066.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_544

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea 2 深度探索：视觉参考，让图片成为 Prompt_2078509637904719874.json、图片生成/文生图/Krea 2：我们可能误解了 Raw 模型_2075137774411411458.json、图片生成/文生图/Krea+2+深度探索：视觉参考，让图片成为+Prompt (1)_2082655123242840066.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：42%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `ImageStitch`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `TextEncodeQwenImageEditPlus` —— 2/3 个有
- `easy textIndexSwitch` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 12 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 12，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
