---
name: text_to_image_upscale_sampler_clip_22
type: Text To Image
frequency: 3
level: strong
coverage: 0.836667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImpactInt, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MemoryCleaner, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-tmage高清文生图+反推提示词并生图_2056899865396989954.json, 图片生成/文生图/Z-tmage高清文生图_2031773633609211906.json, 图片生成/文生图/qwen3反推提示词并生图+Z-tmage高清文生图_2031245492893519874.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-tmage高清文生图+反推提示词并生图_2056899865396989954.json、图片生成/文生图/Z-tmage高清文生图_2031773633609211906.json、图片生成/文生图/qwen3反推提示词并生图+Z-tmage高清文生图_2031245492893519874.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MemoryCleaner`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt List` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `Float` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Primitive integer [Crystools]` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有
- `easy saveText` —— 1/3 个有
- `easy textSwitch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 10 | 3 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.9 - 1 | 3 | 95% |
| 宽度 | 1080 | 1080 - 1080 | 3 | 100% |
| 高度 | 1920 | 1920 - 1920 | 3 | 100% |
| LoRA 模型强度 | 0.85 | - | 2 | 94% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 10，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，3 个样本，取值集中（一致性 95%）
- 宽度 中位数 1080，观测区间 1080 - 1080，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
