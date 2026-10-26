---
name: text_to_image_upscale_sampler_clip_14
type: Text To Image
frequency: 7
level: moderate
coverage: 0.858286
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImpactInt, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MemoryCleaner, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/qwen3反推提示词并生图+Z-tmage高清文生图_2063940919455473666.json, 图片生成/反推提示词/qwen3反推提示词并生图+Z-tmage高清文生图_2063940961151045633.json, 图片生成/图生图/Qwen3反推提示词_2050402437873315841.json, 图片生成/文生图/Z-tmage高清文生图+反推提示词并生图_2056899865396989954.json, 图片生成/文生图/Z-tmage高清文生图_2031773633609211906.json, 图片生成/文生图/qwen3反推提示词并生图+Z-tmage高清文生图_2031245492893519874.json, 图片生成/文生图/qwen3反推提示词并生图｜数字人人像写真一键复刻出图_2112910540124278785.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_14

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/qwen3反推提示词并生图+Z-tmage高清文生图_2063940919455473666.json、图片生成/反推提示词/qwen3反推提示词并生图+Z-tmage高清文生图_2063940961151045633.json、图片生成/图生图/Qwen3反推提示词_2050402437873315841.json、图片生成/文生图/Z-tmage高清文生图+反推提示词并生图_2056899865396989954.json、图片生成/文生图/Z-tmage高清文生图_2031773633609211906.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
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
- `Float` —— 6/7 个有
- `CR Prompt List` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `Primitive integer [Crystools]` —— 5/7 个有
- `Text Multiline` —— 5/7 个有
- `easy saveText` —— 5/7 个有
- `PreviewImage` —— 4/7 个有
- `ModelSamplingAuraFlow` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `LoraLoader` —— 2/7 个有
- `JjkText` —— 1/7 个有
- `MuyeTextEditOutput` —— 1/7 个有
- `easy textSwitch` —— 1/7 个有
- `solarL_SaveImagesToZip` —— 1/7 个有
- `孤海注释` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 80 - 1080 | 7 | 63% |
| 高度 | 1920 | 80 - 1920 | 7 | 61% |
| 采样步数 | 10 | 4 - 10 | 7 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 7 | 18% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 0.9 | 0.7 - 1 | 7 | 89% |
| LoRA 模型强度 | 0.85 | - | 2 | 94% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 80 - 1080，7 个样本
- 高度 中位数 1920，观测区间 80 - 1920，7 个样本
- 采样步数 中位数 10，观测区间 4 - 10，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，7 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 0.9，观测区间 0.7 - 1，7 个样本，取值集中（一致性 89%）
- LoRA 模型强度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
