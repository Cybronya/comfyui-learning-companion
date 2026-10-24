---
name: text_to_image_upscale_lora_sampler_100
type: Text To Image
frequency: 3
level: strong
coverage: 0.700333
common_nodes: [CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, INTConstant, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PreviewImage, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RegexExtract, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, ShowText|pysssss, Text Concatenate, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy indexAnything, easy positive, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image短剧拍档支持场景和角色V3_2064306047208218626.json, 图片生成/文生图/Z-Image短剧拍档支持场景和角色V4_2065565112349577217.json, 图片生成/文生图/Z-Image短剧拍档支持场景和角色V5_2069262873309831169.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_100

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-Image短剧拍档支持场景和角色V3_2064306047208218626.json、图片生成/文生图/Z-Image短剧拍档支持场景和角色V4_2065565112349577217.json、图片生成/文生图/Z-Image短剧拍档支持场景和角色V5_2069262873309831169.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RegexExtract`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `ShowText|pysssss`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy indexAnything`
- `easy positive`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `ClipLoaderGGUF` —— 2/3 个有
- `QwenImageDiffsynthControlnet` —— 2/3 个有
- `ZImageFunControlnet` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2s_ode | - | 3 | 100% |
| 调度器 | kl_optimal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 1080 - 1920 | 3 | 71% |
| 高度 | 1920 | 1080 - 1920 | 3 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s_ode，3 个样本，一致性 100%
- 调度器 最常用 kl_optimal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1920，3 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，3 个样本
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
