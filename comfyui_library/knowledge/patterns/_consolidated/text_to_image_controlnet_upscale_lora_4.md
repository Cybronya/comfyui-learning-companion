---
name: text_to_image_controlnet_upscale_lora_4
type: Text To Image
frequency: 2
level: weak
coverage: 0.734
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, GoogleTranslateTextNode, Image Comparer (rgthree), ImageConcanate, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PMRF, QwenImageDiffsynthControlnet, RH_Captioner, SaveImage, SetNode, ShowText|pysssss, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Zimage文生图动作迁移  ZImage_Merged_Optimized_2006238737826582529.json, 图片生成/文生图/多合一，放大，动作参考，提示词反推，集成Qwen_2512_2511_ZImage_十秒出图_2006666537956020226.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Zimage文生图动作迁移  ZImage_Merged_Optimized_2006238737826582529.json、图片生成/文生图/多合一，放大，动作参考，提示词反推，集成Qwen_2512_2511_ZImage_十秒出图_2006666537956020226.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
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
- `AddLabel` —— 1/2 个有
- `CFGNorm` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PreviewBridge` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `easy imageSplitGrid` —— 1/2 个有
- `easy int` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 22% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.75 | - | 1 | 100% |
| 宽度 | 872 | - | 2 | 83% |
| 高度 | 1408 | - | 2 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 22%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 宽度 中位数 872，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 高度 中位数 1408，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
