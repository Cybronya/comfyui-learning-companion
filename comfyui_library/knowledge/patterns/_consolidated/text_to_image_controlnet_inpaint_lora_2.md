---
name: text_to_image_controlnet_inpaint_lora_2
type: Text To Image
frequency: 3
level: weak
coverage: 0.518667
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetInpaintingAliMamaApply, ControlNetLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleBy, ImageScaleToTotalPixels, InpaintModelConditioning, JoinStrings, KSampler, LanPaint_MaskBlend, LoadImage, LoraLoaderModelOnly, MaskBlur+, MaskPreview+, ModelSamplingAuraFlow, PreviewBridge, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, SetUnionControlNetType, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [MaskBlur+, PlaySound|pysssss, easy cleanGpuUsed, MaskPreview+]
members: [图片生成/图生图/超强动漫转真人洗图梦幻版｜二次元秒变写实风，风格迁移效果惊艳_2107292415693516801.json, 图片生成/文生图/1987077741474459650.json, 数字人/数字人/Qwen Image洗图去AI感高清处理工具_2100675378984611841.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_lora_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/超强动漫转真人洗图梦幻版｜二次元秒变写实风，风格迁移效果惊艳_2107292415693516801.json、图片生成/文生图/1987077741474459650.json、数字人/数字人/Qwen Image洗图去AI感高清处理工具_2100675378984611841.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：52%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `InpaintModelConditioning`
- `JoinStrings`
- `KSampler`
- `LanPaint_MaskBlend`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskBlur+`
- `MaskPreview+`
- `ModelSamplingAuraFlow`
- `PreviewBridge`
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
- `CR SDXL Aspect Ratio` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `PlaySound|pysssss` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `solarL_SaveImagesToZip` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `FastGroupsBypassSwitch` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 3 | 53% |
| Prompt 约束强度(CFG) | 4.5 | 1.53 - 4.5 | 3 | 60% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 0.35 - 1 | 3 | 61% |
| ControlNet 权重 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 1024 | 3 | 0% |
| 高度 | 80 | 80 - 1536 | 3 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1.53 - 4.5，3 个样本
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，3 个样本
- ControlNet 权重 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，3 个样本，取值分散，一致性仅 0%
- 高发问题（7/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：MaskBlur+、PlaySound|pysssss、easy cleanGpuUsed、MaskPreview+
