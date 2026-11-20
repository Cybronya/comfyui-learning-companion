---
name: text_to_image_upscale_lora_sampler_43
type: Text To Image
frequency: 6
level: moderate
coverage: 0.666167
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ClownsharKSampler_Beta, ConditioningZeroOut, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, GetNode, KSampler, Krea2ControlApply, Krea2ControlImageEncode, Krea2ControlLoRALoader, Krea2OstrisEditModelPatch, Krea2StyleReference, Krea2StyleTransfer, Label (rgthree), LoadImage, LoraLoaderModelOnly, PlaySound|pysssss, PreviewAny, PreviewImage, PrimitiveStringMultiline, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, StringConcatenate, TextGenerate, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader, easy globalSeed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Krea2短剧角色_场景_动漫生成器-单_双采_角色LoRA_库_A2R_提示词增强_图像放大_2113458637443264514.json, 图片生成/图生图/Krea2短剧角色生成器-单采_双采_角色_LoRA_库_提示词增强_图像放大_2114201424493109250.json, 图片生成/图生图/Krea2短剧角色生成器-单采_双采_角色_LoRA_库_提示词增强_图像放大_2115281345021833218.json, 图片生成/文生图/Krea2全面-亚洲审美lora_小丑双采_controlnet_风格迁移_巨物_微观世界_2083741350612258817.json, 平台全量/Krea2短剧角色_场景_动漫生成器-单_ 双采 _角色LoRA 库_A2R_提示词增强_图像放大_2085651982815162369.json, 平台全量/Krea2短剧角色生成器-单采 _ 双采 _角色 LoRA 库_提示词增强_图像放大_2091467322555977729.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_43

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/Krea2短剧角色_场景_动漫生成器-单_双采_角色LoRA_库_A2R_提示词增强_图像放大_2113458637443264514.json、图片生成/图生图/Krea2短剧角色生成器-单采_双采_角色_LoRA_库_提示词增强_图像放大_2114201424493109250.json、图片生成/图生图/Krea2短剧角色生成器-单采_双采_角色_LoRA_库_提示词增强_图像放大_2115281345021833218.json、图片生成/文生图/Krea2全面-亚洲审美lora_小丑双采_controlnet_风格迁移_巨物_微观世界_2083741350612258817.json、平台全量/Krea2短剧角色_场景_动漫生成器-单_ 双采 _角色LoRA 库_A2R_提示词增强_图像放大_2085651982815162369.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ColorCorrect` —— 5/6 个有
- `Easy_QwenEdit2509` —— 5/6 个有
- `LayerUtility: ImageReel` —— 5/6 个有
- `LayerUtility: ImageReelComposit` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `EmptyImage` —— 1/6 个有
- `FluxKontextImageScale` —— 1/6 个有
- `SeedVR2TorchCompileSettings` —— 1/6 个有
- `TextEncodeKrea2OstrisEdit` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |
| 采样步数 | beta | - | 6 | 50% |
| Prompt 约束强度(CFG) | 15 | 1 - 15 | 6 | 59% |
| 采样算法 | 12 | 3 - 12 | 5 | 48% |
| 调度器 | 1 | 0.27 - 1 | 5 | 49% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 采样步数 最常用 beta，6 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 15，观测区间 1 - 15，6 个样本
- 采样算法 中位数 12，观测区间 3 - 12，5 个样本，取值分散，一致性仅 48%
- 调度器 中位数 1，观测区间 0.27 - 1，5 个样本，取值分散，一致性仅 49%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（12/6 个样本）：Steps较低可能导致细节不足
