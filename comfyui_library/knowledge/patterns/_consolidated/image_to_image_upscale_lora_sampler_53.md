---
name: image_to_image_upscale_lora_sampler_53
type: Image To Image
frequency: 4
level: moderate
coverage: 0.753
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetNode, ImageScaleBy, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【动漫转真人】Qwen+Z-image_支持文本修改&去水印&加密_真实洗图_2030319073132814338.json, 图片生成/图生图/二次元转真人，真实感照片_2006712889599594497.json, 图片生成/图生图/二次元转真人，真实感照片aa_2050942539259232257.json, 图片生成/图生图/动漫变成了真实的人_漫画变真人_2010983846753341442.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_53

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【动漫转真人】Qwen+Z-image_支持文本修改&去水印&加密_真实洗图_2030319073132814338.json、图片生成/图生图/二次元转真人，真实感照片_2006712889599594497.json、图片生成/图生图/二次元转真人，真实感照片aa_2050942539259232257.json、图片生成/图生图/动漫变成了真实的人_漫画变真人_2010983846753341442.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetNode`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `JoinStrings` —— 3/4 个有
- `WD14Tagger|pysssss` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `AILab_ImageStitch` —— 1/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `CompressImages` —— 1/4 个有
- `DF_Text_Box` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `Int` —— 1/4 个有
- `ResizeImageNode` —— 1/4 个有
- `TT_img_enc` —— 1/4 个有
- `TextInput_` —— 1/4 个有
- `easy boolean` —— 1/4 个有
- `easy imageSwitch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 5 - 10 | 4 | 75% |
| Prompt 约束强度(CFG) | 1.3 | 1 - 1.6 | 4 | 77% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 0.475 | 0.35 - 1 | 4 | 54% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 5 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1.3，观测区间 1 - 1.6，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 0.475，观测区间 0.35 - 1，4 个样本
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
