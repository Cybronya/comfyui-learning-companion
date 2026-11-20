---
name: unknown_workflow_controlnet_inpaint_upscale_4
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.461
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetInpaintingAliMamaApply, ControlNetLoader, Fast Groups Bypasser (rgthree), GetNode, GrowMaskWithBlur, Image Comparer (rgthree), ImageAndMaskPreview, ImagePadForOutpaint, ImageScaleToTotalPixels, InpaintModelConditioning, InpaintPreprocessor, KSampler, LanPaint_MaskBlend, LayerColor: Brightness & Contrast, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, MaskBlur+, ModelSamplingAuraFlow, PlaySound|pysssss, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, SetUnionControlNetType, ShowText|pysssss, UNETLoader, UnetLoaderGGUF, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/墨幽QWEN2512lora版反推_2038459146705571841.json, 图片生成/文生图/Qwen-image-2512_反推图，文生图、洗图、扩图、局部重绘_2008791898793713666.json, 图片生成/文生图/YZ金鱼-Qwen-image-2512超强多合一_2006629546631630850.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_upscale_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/墨幽QWEN2512lora版反推_2038459146705571841.json、图片生成/文生图/Qwen-image-2512_反推图，文生图、洗图、扩图、局部重绘_2008791898793713666.json、图片生成/文生图/YZ金鱼-Qwen-image-2512超强多合一_2006629546631630850.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImagePadForOutpaint`
- `ImageScaleToTotalPixels`
- `InpaintModelConditioning`
- `InpaintPreprocessor`
- `KSampler`
- `LanPaint_MaskBlend`
- `LayerColor: Brightness & Contrast`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskBlur+`
- `ModelSamplingAuraFlow`
- `PlaySound|pysssss`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `JoinStringMulti` —— 1/3 个有
- `JoinStrings` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | 1 - 1 | 3 | 100% |
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（12/3 个样本）：Steps较低可能导致细节不足
