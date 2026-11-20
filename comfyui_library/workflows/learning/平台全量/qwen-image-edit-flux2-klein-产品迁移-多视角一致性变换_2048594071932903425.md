---
key: 平台全量/qwen-image-edit-flux2-klein-产品迁移-多视角一致性变换_2048594071932903425.json
name: qwen-image-edit-flux2-klein-产品迁移-多视角一致性变换_2048594071932903425
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen-image-edit-flux2-klein-产品迁移-多视角一致性变换_2048594071932903425.json
hash: 16c31fd225c11ec0
coverage: 0.813953
learned_at: 2026-11-14 01:16:19
nodes: [FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, ModelSamplingAuraFlow, CFGNorm, TextEncodeQwenImageEditPlus, CLIPLoader, VAELoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LayerMask: MaskGrow, VAEEncode, TextEncodeQwenImageEditPlus, VAEDecode, ImageScaleToTotalPixelsX, KSampler, VAEDecode, KSampler, LayerUtility: ImageRemoveAlpha, ImageScaleToTotalPixelsX, VAEDecode, ImageScaleToTotalPixelsX, SAM3Segment, ImageScaleToTotalPixelsX, KSampler, ImageColorMatch+, Image Comparer (rgthree), Image Comparer (rgthree), LoadImage, SaveImage, LoadImage, Note, PreviewImage, Note, easy ifElse, PreviewImage, UNETLoader, LoraLoaderModelOnly, UNETLoader, PainterFluxImageEdit, PainterFluxImageEdit, easy ifElse, QwenMultiangleCameraNode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 379949745321491, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/qwen-image-edit-flux2-klein-产品迁移-多视角一致性变换_2048594071932903425.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen-image-edit-flux2-klein-产品迁移-多视角一致性变换_2048594071932903425.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LayerMask: MaskGrow`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixelsX`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageRemoveAlpha`
- `ImageScaleToTotalPixelsX`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixelsX`
- `SAM3Segment`
- `ImageScaleToTotalPixelsX`
- `KSampler` ★核心
- `ImageColorMatch+`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `Note`
- `PreviewImage`
- `Note`
- `easy ifElse`
- `PreviewImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PainterFluxImageEdit`
- `PainterFluxImageEdit`
- `easy ifElse`
- `QwenMultiangleCameraNode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `379949745321491`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（35/43）

**有卡**：`FluxKontextMultiReferenceLatentMethod`、`ModelSamplingAuraFlow`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LayerMask: MaskGrow`、`VAEEncode`、`VAEDecode`、`ImageScaleToTotalPixelsX`、`KSampler`、`LayerUtility: ImageRemoveAlpha`、`SAM3Segment`、`ImageColorMatch+`、`LoadImage`、`SaveImage`、`UNETLoader`、`PainterFluxImageEdit`、`QwenMultiangleCameraNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
