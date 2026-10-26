---
name: text_to_image_upscale_lora_sampler_80
type: Text To Image
frequency: 3
level: moderate
coverage: 0.651667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ClownsharKSampler_Beta, ConditioningZeroOut, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, GetNode, KSampler, Krea2ControlApply, Krea2ControlImageEncode, Krea2ControlLoRALoader, Krea2OstrisEditModelPatch, Krea2StyleReference, Krea2StyleTransfer, Label (rgthree), LoadImage, LoraLoaderModelOnly, PlaySound|pysssss, PreviewAny, PreviewImage, PrimitiveStringMultiline, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, StringConcatenate, TextGenerate, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader, easy globalSeed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Krea2短剧角色_场景_动漫生成器-单_双采_角色LoRA_库_A2R_提示词增强_图像放大_2113458637443264514.json, 图片生成/图生图/Krea2短剧角色生成器-单采_双采_角色_LoRA_库_提示词增强_图像放大_2114201424493109250.json, 图片生成/文生图/Krea2全面-亚洲审美lora_小丑双采_controlnet_风格迁移_巨物_微观世界_2083741350612258817.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_80

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/Krea2短剧角色_场景_动漫生成器-单_双采_角色LoRA_库_A2R_提示词增强_图像放大_2113458637443264514.json、图片生成/图生图/Krea2短剧角色生成器-单采_双采_角色_LoRA_库_提示词增强_图像放大_2114201424493109250.json、图片生成/文生图/Krea2全面-亚洲审美lora_小丑双采_controlnet_风格迁移_巨物_微观世界_2083741350612258817.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ClownsharKSampler_Beta`
- `ConditioningZeroOut`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `GetNode`
- `KSampler`
- `Krea2ControlApply`
- `Krea2ControlImageEncode`
- `Krea2ControlLoRALoader`
- `Krea2OstrisEditModelPatch`
- `Krea2StyleReference`
- `Krea2StyleTransfer`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PlaySound|pysssss`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `StringConcatenate`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `easy globalSeed`

**可变部分**（部分 workflow 才有）：
- `ColorCorrect` —— 2/3 个有
- `Easy_QwenEdit2509` —— 2/3 个有
- `LayerUtility: ImageReel` —— 2/3 个有
- `LayerUtility: ImageReelComposit` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `EmptyImage` —— 1/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `SeedVR2TorchCompileSettings` —— 1/3 个有
- `TextEncodeKrea2OstrisEdit` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | kl_optimal | - | 3 | 33% |
| Prompt 约束强度(CFG) | 15 | 1 - 15 | 3 | 36% |
| 采样算法 | 7.5 | - | 2 | 40% |
| 调度器 | 0.635 | - | 2 | 43% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 最常用 kl_optimal，3 个样本，一致性 33%
- Prompt 约束强度(CFG) 中位数 15，观测区间 1 - 15，3 个样本，取值分散，一致性仅 36%
- 采样算法 中位数 7.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 调度器 中位数 0.635，样本不足，未给区间，2 个样本，取值分散，一致性仅 43%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
