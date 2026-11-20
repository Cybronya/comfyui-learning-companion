---
name: image_to_image_upscale_lora_sampler_51
type: Image To Image
frequency: 4
level: strong
coverage: 0.78
common_nodes: [Anything Everywhere3, BiRefNetRMBG, CFGNorm, CLIPLoader, CR Text, ConditioningZeroOut, Fast Groups Muter (rgthree), GetImageSize, GetNode, Image Comparer (rgthree), ImageCropByMask, ImagePadForOutpaintTargetSize, ImageResize+, ImageScaleBy, ImageUpscaleWithModel, ImpactSwitch, Int, InvertMask, KSampler, LayerUtility: HLFrequencyDetailRestore, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskPreview, ModelSamplingAuraFlow, Prompts Everywhere, ResizeMask, SaveImage, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageDetailTransfer, easy imageSizeByLongerSide, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/融图_2033389303937638402.json, 图片生成/图生图/重打光融图(无偏移Qwen_2511_edit_2097149976257318913.json, 图片生成/图生图/重打光融图(无偏移Qwen_2511_edit_2097244806606053378.json, 图片生成/图生图/重打光融图(无偏移）Qwen 2511 edit_2009433454328422401.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_51

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/融图_2033389303937638402.json、图片生成/图生图/重打光融图(无偏移Qwen_2511_edit_2097149976257318913.json、图片生成/图生图/重打光融图(无偏移Qwen_2511_edit_2097244806606053378.json、图片生成/图生图/重打光融图(无偏移）Qwen 2511 edit_2009433454328422401.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere3`
- `BiRefNetRMBG`
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `Fast Groups Muter (rgthree)`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageCropByMask`
- `ImagePadForOutpaintTargetSize`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImpactSwitch`
- `Int`
- `InvertMask`
- `KSampler`
- `LayerUtility: HLFrequencyDetailRestore`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview`
- `ModelSamplingAuraFlow`
- `Prompts Everywhere`
- `ResizeMask`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageDetailTransfer`
- `easy imageSizeByLongerSide`
- `easy seed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
