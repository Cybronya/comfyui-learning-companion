---
name: text_to_image_controlnet_lora_sampler_2
type: Text To Image
frequency: 7
level: weak
coverage: 0.629286
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, Image Comparer (rgthree), ImageScaleBy, ImageScaleToTotalPixels, JoinStrings, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, SetUnionControlNetType, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image动漫转真人神器｜二次元一键走进现实，图生图还原度高_2099413611251855362.json, 图片生成/图生图/动漫转真人洗图梦幻版｜风格迁移写实图生图_2101238250378715137.json, 图片生成/图生图/超强动漫转真人洗图梦幻版｜二次元秒变写实风，风格迁移效果惊艳_2107292415693516801.json, 图片生成/图生图/👾怪獸-Qwen漫画转真人👾_1988720095994195969.json, 图片生成/图生图/👾怪獸-Qwen真人转漫画👾_1988541458280046593.json, 图片生成/文生图/⭐️Qwen-image真实洗图------图像反推、完美去除AI感_1987077741474459650.json, 数字人/数字人/Qwen Image洗图去AI感高清处理工具_2100675378984611841.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen-image动漫转真人神器｜二次元一键走进现实，图生图还原度高_2099413611251855362.json、图片生成/图生图/动漫转真人洗图梦幻版｜风格迁移写实图生图_2101238250378715137.json、图片生成/图生图/超强动漫转真人洗图梦幻版｜二次元秒变写实风，风格迁移效果惊艳_2107292415693516801.json、图片生成/图生图/👾怪獸-Qwen漫画转真人👾_1988720095994195969.json、图片生成/图生图/👾怪獸-Qwen真人转漫画👾_1988541458280046593.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 7 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `JoinStrings`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ControlNetInpaintingAliMamaApply` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有
- `InpaintModelConditioning` —— 5/7 个有
- `Int` —— 5/7 个有
- `LanPaint_MaskBlend` —— 5/7 个有
- `LayerUtility: ImageReel` —— 5/7 个有
- `LayerUtility: ImageReelComposit` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `MaskBlur+` —— 5/7 个有
- `MaskPreview+` —— 5/7 个有
- `ModelSamplingAuraFlow` —— 5/7 个有
- `PreviewBridge` —— 5/7 个有
- `CR SDXL Aspect Ratio` —— 4/7 个有
- `JjkText` —— 4/7 个有
- `solarL_SaveImagesToZip` —— 4/7 个有
- `孤海注释` —— 4/7 个有
- `GetNode` —— 2/7 个有
- `ImpactSwitch` —— 2/7 个有
- `PlaySound|pysssss` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `CannyEdgePreprocessor` —— 1/7 个有
- `DWPreprocessor` —— 1/7 个有
- `FastGroupsBypassSwitch` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 7 | 60% |
| Prompt 约束强度(CFG) | 4.5 | 1.01 - 4.5 | 7 | 50% |
| 采样算法 | er_sde | - | 7 | 57% |
| 调度器 | beta | - | 7 | 57% |
| 重绘幅度 | 1 | 0.35 - 1 | 7 | 64% |
| ControlNet 权重 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 1024 | 7 | 0% |
| 高度 | 80 | 80 - 1536 | 7 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，7 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1.01 - 4.5，7 个样本
- 采样算法 最常用 er_sde，7 个样本，一致性 57%
- 调度器 最常用 beta，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，7 个样本
- ControlNet 权重 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，7 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，7 个样本，取值分散，一致性仅 0%
- 高发问题（19/7 个样本）：Steps较低可能导致细节不足
