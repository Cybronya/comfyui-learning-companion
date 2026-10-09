---
key: 图片生成/文生图/HyperLora人物一致性CN控制+InstantID强化换脸（姿势版）V2-修复脸部识别问题_1915996781723713538.json
name: HyperLora人物一致性CN控制+InstantID强化换脸（姿势版）V2-修复脸部识别问题_1915996781723713538.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/HyperLora人物一致性CN控制+InstantID强化换脸（姿势版）V2-修复脸部识别问题_1915996781723713538.json
hash: 6fb9766f3da7be66
coverage: 0.642857
learned_at: 2026-10-07 22:07:41
nodes: [HyperLoRAConfig, HyperLoRAIDCond, HyperLoRAFaceAttr, HyperLoRAGenerateIDLoRA, ImpactMakeImageBatch, BNK_CLIPTextEncodeAdvanced, ControlNetApplyAdvanced, HyperLoRAApplyLoRA, HyperLoRALoader, BNK_CLIPTextEncodeAdvanced, CheckpointLoaderSimple, OpenposePreprocessor, PreviewImage, ControlNetLoader, KSampler, ApplyFBCacheOnModel, CLIPSetLastLayer, LoadImage, SaveImage, EmptyLatentImage, JWInteger, JWInteger, LayerUtility: PurgeVRAM V2, ImageConcanate, CM_NumberUnaryOperation, CM_NumberToInt, ImageScale, KSampler, CM_NumberToInt, LayerMask: MaskGrow, ApplyInstantID, InstantIDModelLoader, ControlNetLoader, SetLatentNoiseMask, VAEEncode, FaceBoundingBox, ImageComposite+, InstantIDFaceAnalysis, ControlNetApplyAdvanced, VAEDecode, ImageScaleBy, LayerMask: MaskGrow, CM_IntToFloat, LayerMask: PersonMaskUltra V2, LayerUtility: LayerImageTransform, ImageScaleBy, CR Upscale Image, CM_IntToNumber, PreviewImage, MaskPreview+, GetImageSize+, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, PreviewImage, LayerUtility: LayerImageTransform, PreviewImage, easy imageColorMatch, PreviewImage, SaveImage, PreviewImage, PreviewImage, Image Comparer (rgthree), FaceAnalysisModels, ImageScale, LayerUtility: CropBoxResolve, PreviewImage, LoadImage, LoadImage, Note, Note, CM_IntToFloat, Note Plus (mtb), SaveImage, VAEDecode, JWImageResizeByLongerSide, LayerUtility: CropByMask, LayerMask: PersonMaskUltra V2, JWInteger, Note, CLIPTextEncode, CR Prompt Text, Note, Note]
patterns: [text_to_image, image_to_image]
missing: [ImageComposite+, LayerMask: MaskGrow, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: LayerImageTransform, LayerUtility: LayerImageTransform, LayerUtility: PurgeVRAM V2, Note Plus (mtb), easy imageColorMatch, CR Prompt Text, CR Upscale Image, GetImageSize+, MaskPreview+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "controlnet_strength": 0.1, "denoise": 0.5, "height": 1024, "sampler_name": "euler_ancestral", "scheduler": "sgm_uniform", "seed": 597058677907752, "steps": 8, "width": 1024}
discoveries: [次要节点 `ImageComposite+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: PersonMaskUltra V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: PersonMaskUltra V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: CropBoxResolve` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: CropByMask` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LayerImageTransform` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LayerImageTransform` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Upscale Image` 仅有 Upscale 的通用知识，没有该节点自己的说明, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/HyperLora人物一致性CN控制+InstantID强化换脸（姿势版）V2-修复脸部识别问题_1915996781723713538.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1915996781723713538.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（84 个）：
- `HyperLoRAConfig`
- `HyperLoRAIDCond`
- `HyperLoRAFaceAttr`
- `HyperLoRAGenerateIDLoRA`
- `ImpactMakeImageBatch`
- `BNK_CLIPTextEncodeAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `HyperLoRAApplyLoRA`
- `HyperLoRALoader` ★核心
- `BNK_CLIPTextEncodeAdvanced` ★核心
- `CheckpointLoaderSimple` ★核心
- `OpenposePreprocessor`
- `PreviewImage`
- `ControlNetLoader`
- `KSampler` ★核心
- `ApplyFBCacheOnModel`
- `CLIPSetLastLayer`
- `LoadImage`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `JWInteger`
- `JWInteger`
- `LayerUtility: PurgeVRAM V2`
- `ImageConcanate`
- `CM_NumberUnaryOperation`
- `CM_NumberToInt`
- `ImageScale`
- `KSampler` ★核心
- `CM_NumberToInt`
- `LayerMask: MaskGrow`
- `ApplyInstantID`
- `InstantIDModelLoader`
- `ControlNetLoader`
- `SetLatentNoiseMask`
- `VAEEncode` ★核心
- `FaceBoundingBox`
- `ImageComposite+`
- `InstantIDFaceAnalysis`
- `ControlNetApplyAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `LayerMask: MaskGrow`
- `CM_IntToFloat`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: LayerImageTransform`
- `ImageScaleBy`
- `CR Upscale Image`
- `CM_IntToNumber`
- `PreviewImage`
- `MaskPreview+`
- `GetImageSize+`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `PreviewImage`
- `LayerUtility: LayerImageTransform`
- `PreviewImage`
- `easy imageColorMatch`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `FaceAnalysisModels`
- `ImageScale`
- `LayerUtility: CropBoxResolve`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `Note`
- `Note`
- `CM_IntToFloat`
- `Note Plus (mtb)`
- `SaveImage`
- `VAEDecode` ★核心
- `JWImageResizeByLongerSide`
- `LayerUtility: CropByMask`
- `LayerMask: PersonMaskUltra V2`
- `JWInteger`
- `Note`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `Note`
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `controlnet_strength` = `0.1`
- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`
- `seed` = `597058677907752`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.5`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **64%**（54/84）

**有卡**：`HyperLoRAConfig`、`HyperLoRAIDCond`、`HyperLoRAFaceAttr`、`HyperLoRAGenerateIDLoRA`、`ImpactMakeImageBatch`、`BNK_CLIPTextEncodeAdvanced`、`ControlNetApplyAdvanced`、`HyperLoRAApplyLoRA`、`HyperLoRALoader`、`CheckpointLoaderSimple`、`OpenposePreprocessor`、`ControlNetLoader`、`KSampler`、`ApplyFBCacheOnModel`、`CLIPSetLastLayer`、`LoadImage`、`SaveImage`、`EmptyLatentImage`、`JWInteger`、`ImageConcanate`、`CM_NumberUnaryOperation`、`CM_NumberToInt`、`ImageScale`、`ApplyInstantID`、`InstantIDModelLoader`、`SetLatentNoiseMask`、`VAEEncode`、`FaceBoundingBox`、`InstantIDFaceAnalysis`、`VAEDecode`、`ImageScaleBy`、`CM_IntToFloat`、`CM_IntToNumber`、`CLIPTextEncode`、`FaceAnalysisModels`、`JWImageResizeByLongerSide`

**缺卡**（16）：`ImageComposite+`、`LayerMask: MaskGrow`、`LayerMask: MaskGrow`、`LayerMask: PersonMaskUltra V2`、`LayerMask: PersonMaskUltra V2`、`LayerUtility: CropBoxResolve`、`LayerUtility: CropByMask`、`LayerUtility: LayerImageTransform`、`LayerUtility: LayerImageTransform`、`LayerUtility: PurgeVRAM V2`、`Note Plus (mtb)`、`easy imageColorMatch`、`CR Prompt Text`、`CR Upscale Image`、`GetImageSize+`、`MaskPreview+`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `ImageComposite+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: PersonMaskUltra V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: PersonMaskUltra V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: CropBoxResolve` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: CropByMask` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LayerImageTransform` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LayerImageTransform` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Upscale Image` 仅有 Upscale 的通用知识，没有该节点自己的说明
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
