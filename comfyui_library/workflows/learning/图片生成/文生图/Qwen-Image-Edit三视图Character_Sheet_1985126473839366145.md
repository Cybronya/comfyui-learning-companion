---
key: 图片生成/文生图/Qwen-Image-Edit三视图Character_Sheet_1985126473839366145.json
name: Qwen-Image-Edit三视图Character_Sheet_1985126473839366145
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-Edit三视图Character_Sheet_1985126473839366145.json
hash: aeb41f0231dc8cf9
coverage: 0.66129
learned_at: 2026-10-10 20:59:00
nodes: [VAEEncode, MarkdownNote, ImageScaleToTotalPixels, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSampler, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSampler, KSampler, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, MarkdownNote, MarkdownNote, CFGNorm, ModelSamplingAuraFlow, KSampler, CLIPLoader, PreviewImage, LayerUtility: CropByMask V2, LayerUtility: CropByMask V2, ImageUpscaleWithModel, ImageUpscaleWithModel, VAEDecode, VAEDecode, PreviewImage, PreviewImage, VAEDecode, VAEDecode, PreviewImage, PreviewImage, PreviewImage, SaveImage, PreviewImage, SaveImage, PreviewImage, INTConstant, UpscaleModelLoader, ImageConcanate, ImageUpscaleWithModel, ImageConcanate, LayerUtility: CropByMask V2, ImageUpscaleWithModel, LayerUtility: CropByMask V2, ImageConcanate, ImageConcanate, MarkdownNote, MarkdownNote, LoraLoaderModelOnly, UNETLoader, LoadImage, LayerMask: RemBgUltra, MaskPreview, MaskPreview, LayerMask: RemBgUltra, MaskPreview, MaskPreview, LayerMask: RemBgUltra, LayerMask: RemBgUltra, VAELoader, TextEncodeQwenImageEditPlus]
patterns: [image_to_image]
missing: [LayerMask: RemBgUltra, LayerMask: RemBgUltra, LayerMask: RemBgUltra, LayerMask: RemBgUltra, LayerUtility: CropByMask V2, LayerUtility: CropByMask V2, LayerUtility: CropByMask V2, LayerUtility: CropByMask V2]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 348546921967979, "steps": 4}
discoveries: [次要节点 `LayerMask: RemBgUltra` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: RemBgUltra` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: RemBgUltra` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: RemBgUltra` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: CropByMask V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: CropByMask V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: CropByMask V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: CropByMask V2` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image-Edit三视图Character_Sheet_1985126473839366145.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-Edit三视图Character_Sheet_1985126473839366145.json`

## 结构

**节点**（62 个）：
- `VAEEncode`
- `MarkdownNote`
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `KSampler`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `KSampler`
- `KSampler`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `MarkdownNote`
- `MarkdownNote`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `KSampler`
- `CLIPLoader`
- `PreviewImage`
- `LayerUtility: CropByMask V2`
- `LayerUtility: CropByMask V2`
- `ImageUpscaleWithModel`
- `ImageUpscaleWithModel`
- `VAEDecode`
- `VAEDecode`
- `PreviewImage`
- `PreviewImage`
- `VAEDecode`
- `VAEDecode`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `INTConstant`
- `UpscaleModelLoader`
- `ImageConcanate`
- `ImageUpscaleWithModel`
- `ImageConcanate`
- `LayerUtility: CropByMask V2`
- `ImageUpscaleWithModel`
- `LayerUtility: CropByMask V2`
- `ImageConcanate`
- `ImageConcanate`
- `MarkdownNote`
- `MarkdownNote`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `LoadImage`
- `LayerMask: RemBgUltra`
- `MaskPreview`
- `MaskPreview`
- `LayerMask: RemBgUltra`
- `MaskPreview`
- `MaskPreview`
- `LayerMask: RemBgUltra`
- `LayerMask: RemBgUltra`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`

**识别到的模式**：image_to_image

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `348546921967979`
- `steps` = `4`

## 知识

覆盖率 **66%**（41/62）

**有卡**：`VAEEncode`、`MarkdownNote`、`ImageScaleToTotalPixels`、`TextEncodeQwenImageEditPlus`、`KSampler`、`CFGNorm`、`ModelSamplingAuraFlow`、`CLIPLoader`、`PreviewImage`、`LayerUtility: CropByMask V2`、`ImageUpscaleWithModel`、`VAEDecode`、`SaveImage`、`INTConstant`、`UpscaleModelLoader`、`ImageConcanate`

**缺卡**（8）：`LayerMask: RemBgUltra`、`LayerMask: RemBgUltra`、`LayerMask: RemBgUltra`、`LayerMask: RemBgUltra`、`LayerUtility: CropByMask V2`、`LayerUtility: CropByMask V2`、`LayerUtility: CropByMask V2`、`LayerUtility: CropByMask V2`

## 参数体检

发现 4 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerMask: RemBgUltra` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: RemBgUltra` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: RemBgUltra` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: RemBgUltra` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: CropByMask V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: CropByMask V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: CropByMask V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: CropByMask V2` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
