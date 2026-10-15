---
key: 图片生成/文生图/DreamO-Story Diffusion IN4超级加速单人一致性加强版V1_1925982816373264386.json
name: DreamO-Story Diffusion IN4超级加速单人一致性加强版V1_1925982816373264386
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/DreamO-Story Diffusion IN4超级加速单人一致性加强版V1_1925982816373264386.json
hash: 363967299bbafa3a
coverage: 0.884058
learned_at: 2026-10-15 22:26:15
nodes: [VAELoader, StoryDiffusion_KSampler, EmptyLatentImage, StoryDiffusion_Apply, EasyFunction_Lite, SaveImage, CM_NumberUnaryOperation, CM_NumberToInt, ImageScale, KSampler, CM_NumberToInt, LayerMask: MaskGrow, ApplyInstantID, InstantIDModelLoader, ControlNetLoader, SetLatentNoiseMask, VAEEncode, InstantIDFaceAnalysis, ControlNetApplyAdvanced, VAEDecode, ImageScaleBy, LayerMask: MaskGrow, CM_IntToFloat, LayerMask: PersonMaskUltra V2, ImageScaleBy, CR Upscale Image, CM_IntToNumber, PreviewImage, MaskPreview+, GetImageSize+, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, PreviewImage, LayerUtility: LayerImageTransform, PreviewImage, easy imageColorMatch, PreviewImage, PreviewImage, PreviewImage, Image Comparer (rgthree), ImageScale, LayerUtility: CropBoxResolve, CM_IntToFloat, JWImageResizeByLongerSide, LayerUtility: CropByMask, LayerMask: PersonMaskUltra V2, CLIPTextEncode, FaceBoundingBox, PreviewImage, FaceAnalysisModels, JWImageResizeByLongerSide, LayerUtility: LayerImageTransform, SaveImage, PMRF, LayerUtility: PurgeVRAM V2, ImageComposite+, ImageConcanate, ImageConcanate, SaveImage, LoadImage, PDIMAGE_LongerSize, VAEDecode, SaveImage, StoryDiffusion_CLIPTextEncode, CR Prompt Text, CR Prompt Text, JWInteger, JWInteger]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "controlnet_strength": 0.1, "denoise": 0.5, "height": 512, "sampler_name": "euler_ancestral", "scheduler": "sgm_uniform", "seed": 288003003594540, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/DreamO-Story Diffusion IN4超级加速单人一致性加强版V1_1925982816373264386.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/DreamO-Story Diffusion IN4超级加速单人一致性加强版V1_1925982816373264386.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `VAELoader`
- `StoryDiffusion_KSampler` ★核心
- `EmptyLatentImage` ★核心
- `StoryDiffusion_Apply`
- `EasyFunction_Lite`
- `SaveImage`
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
- `InstantIDFaceAnalysis`
- `ControlNetApplyAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `LayerMask: MaskGrow`
- `CM_IntToFloat`
- `LayerMask: PersonMaskUltra V2`
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
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `ImageScale`
- `LayerUtility: CropBoxResolve`
- `CM_IntToFloat`
- `JWImageResizeByLongerSide`
- `LayerUtility: CropByMask`
- `LayerMask: PersonMaskUltra V2`
- `CLIPTextEncode` ★核心
- `FaceBoundingBox`
- `PreviewImage`
- `FaceAnalysisModels`
- `JWImageResizeByLongerSide`
- `LayerUtility: LayerImageTransform`
- `SaveImage`
- `PMRF`
- `LayerUtility: PurgeVRAM V2`
- `ImageComposite+`
- `ImageConcanate`
- `ImageConcanate`
- `SaveImage`
- `LoadImage`
- `PDIMAGE_LongerSize`
- `VAEDecode` ★核心
- `SaveImage`
- `StoryDiffusion_CLIPTextEncode` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
- `JWInteger`
- `JWInteger`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `288003003594540`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.5`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `controlnet_strength` = `0.1`
- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`

## 知识

覆盖率 **88%**（61/69）

**有卡**：`VAELoader`、`StoryDiffusion_KSampler`、`EmptyLatentImage`、`StoryDiffusion_Apply`、`EasyFunction_Lite`、`SaveImage`、`CM_NumberUnaryOperation`、`CM_NumberToInt`、`ImageScale`、`KSampler`、`LayerMask: MaskGrow`、`ApplyInstantID`、`InstantIDModelLoader`、`ControlNetLoader`、`SetLatentNoiseMask`、`VAEEncode`、`InstantIDFaceAnalysis`、`ControlNetApplyAdvanced`、`VAEDecode`、`ImageScaleBy`、`CM_IntToFloat`、`LayerMask: PersonMaskUltra V2`、`CR Upscale Image`、`CM_IntToNumber`、`MaskPreview+`、`GetImageSize+`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LayerUtility: LayerImageTransform`、`easy imageColorMatch`、`LayerUtility: CropBoxResolve`、`JWImageResizeByLongerSide`、`LayerUtility: CropByMask`、`FaceBoundingBox`、`FaceAnalysisModels`、`PMRF`、`LayerUtility: PurgeVRAM V2`、`ImageComposite+`、`ImageConcanate`、`LoadImage`、`PDIMAGE_LongerSize`、`StoryDiffusion_CLIPTextEncode`、`CR Prompt Text`、`JWInteger`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
