---
name: text_to_image_controlnet_upscale_lora_8
type: Text To Image
frequency: 3
level: moderate
coverage: 0.751667
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, GoogleTranslateTextNode, Image Comparer (rgthree), ImageConcanate, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PMRF, QwenImageDiffsynthControlnet, RH_Captioner, SaveImage, SetNode, ShowText|pysssss, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Zimage文生图动作迁移  ZImage_Merged_Optimized_2006238737826582529.json, 图片生成/文生图/多合一，放大，动作参考，提示词反推，集成Qwen_2512_2511_ZImage_十秒出图_2006666537956020226.json, 图片生成/文生图/多合一，放大，动作参考，提示词反推，集成Qwen_2512_2511_ZImage_十秒出图_2032349637339783169.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora_8

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Zimage文生图动作迁移  ZImage_Merged_Optimized_2006238737826582529.json、图片生成/文生图/多合一，放大，动作参考，提示词反推，集成Qwen_2512_2511_ZImage_十秒出图_2006666537956020226.json、图片生成/文生图/多合一，放大，动作参考，提示词反推，集成Qwen_2512_2511_ZImage_十秒出图_2032349637339783169.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `GoogleTranslateTextNode`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PMRF`
- `QwenImageDiffsynthControlnet`
- `RH_Captioner`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 2/3 个有
- `CFGNorm` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `KSamplerAdvanced` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `easy int` —— 2/3 个有
- `PreviewBridge` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `easy imageSplitGrid` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 3 | 42% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 67% |
| 宽度 | 720 | 720 - 1024 | 3 | 83% |
| 高度 | 1280 | 1280 - 1536 | 3 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，3 个样本，取值分散，一致性仅 42%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 67%
- 宽度 中位数 720，观测区间 720 - 1024，3 个样本，取值集中（一致性 83%）
- 高度 中位数 1280，观测区间 1280 - 1536，3 个样本，取值集中（一致性 91%）
