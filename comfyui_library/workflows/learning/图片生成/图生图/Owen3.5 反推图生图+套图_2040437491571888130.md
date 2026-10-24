---
key: 图片生成/图生图/Owen3.5 反推图生图+套图_2040437491571888130.json
name: Owen3.5 反推图生图+套图_2040437491571888130
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Owen3.5 反推图生图+套图_2040437491571888130.json
hash: 292ac2d1e782aec4
coverage: 0.959016
learned_at: 2026-10-23 11:10:40
nodes: [CLIPLoader, UNETLoader, easy showAnything, CLIPTextEncode, WanVideoClipVisionEncode, WanVideoTextEncodeCached, RepeatImageBatch, CLIPVisionLoader, RepeatImageBatch, PoseAndFaceDetection, PoseAndFaceDetection, DrawMaskOnImage, DrawViTPose, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, easy imageSize, CM_IntToFloat, CM_FloatBinaryOperation, CM_FloatBinaryOperation, CM_FloatToInt, LayerUtility: CropByMask V2, easy mathInt, LayerUtility: ImageScaleByAspectRatio V2, easy imageSize, ImageFromBatch, GrowMask, LazySwitch1way, easy int, LayerUtility: CropByMask V2, LazySwitch1way, LazySwitch1way, LayerUtility: ImageBlend, easy isMaskEmpty, easy int, MaskToImage, ImageToMask, Mask Fill Holes, CM_IntToFloat, MaskToImage, Mask Fill Holes, ImageToMask, SamplerCustomAdvanced, VAELoader, RandomNoise, Reroute, CFGGuider, KSamplerSelect, LoraLoaderModelOnly, CLIPLoader, easy seed, CLIPTextEncode, LoraLoaderModelOnly, ReferenceLatent, UNETLoader, WanVideoSetLoRAs, WanVideoLoraSelectMulti, easy mathInt, easy mathInt, CropByMask, ImageCropMerge, easy boolean, WanVideoVAELoader, MaskToImage, Mask Fill Holes, OnnxDetectionModelLoader, LayerUtility: ColorImage V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, RepeatImageBatch, BlockifyMask, ImageAndMaskPreview, Int, CropByMask, GrowMask, LayerMask: PersonMaskUltra V2, ImageToMask, LazySwitch1way, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, easy mathInt, WanVideoDecode, easy imageSize, easy imageSize, BlendInpaint, easy cleanGpuUsed, PrimitiveStringMultiline, WanVideoModelLoader, easy imageSize, WanVideoAnimateEmbeds, WanVideoSampler, easy imageSize, EmptyLatentImage, CLIPTextEncode, Lora Loader Stack (rgthree), ShowText|pysssss, Lora Loader Stack (rgthree), KSampler, BasicScheduler, GrowMask, PerturbedAttentionGuidance, ModelSamplingAuraFlow, AnySwitch, ImageScaleToTotalPixels, easy cleanGpuUsed, VAEEncodeTiled, VAEDecodeTiled, TextEncodeQwenImageEditPlus, Note, ReferenceLatent, SaveImage, ImageScale, VAELoader, easy cleanGpuUsed, VAEDecode, SaveImage, llama_cpp_parameters, llama_cpp_model_loader, Int, Int, llama_cpp_instruct_adv, LoadImage, LoadImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 2.5, "denoise": 1, "height": 1024, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 1085725084185521, "steps": 30, "width": 768}
---

# 图片生成/图生图/Owen3.5 反推图生图+套图_2040437491571888130.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Owen3.5 反推图生图+套图_2040437491571888130.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（122 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `WanVideoClipVisionEncode`
- `WanVideoTextEncodeCached`
- `RepeatImageBatch`
- `CLIPVisionLoader`
- `RepeatImageBatch`
- `PoseAndFaceDetection`
- `PoseAndFaceDetection`
- `DrawMaskOnImage`
- `DrawViTPose`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `easy imageSize`
- `CM_IntToFloat`
- `CM_FloatBinaryOperation`
- `CM_FloatBinaryOperation`
- `CM_FloatToInt`
- `LayerUtility: CropByMask V2`
- `easy mathInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageSize`
- `ImageFromBatch`
- `GrowMask`
- `LazySwitch1way`
- `easy int`
- `LayerUtility: CropByMask V2`
- `LazySwitch1way`
- `LazySwitch1way`
- `LayerUtility: ImageBlend`
- `easy isMaskEmpty`
- `easy int`
- `MaskToImage`
- `ImageToMask`
- `Mask Fill Holes`
- `CM_IntToFloat`
- `MaskToImage`
- `Mask Fill Holes`
- `ImageToMask`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `RandomNoise`
- `Reroute`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `easy seed`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ReferenceLatent`
- `UNETLoader` ★核心
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `easy mathInt`
- `easy mathInt`
- `CropByMask`
- `ImageCropMerge`
- `easy boolean`
- `WanVideoVAELoader`
- `MaskToImage`
- `Mask Fill Holes`
- `OnnxDetectionModelLoader`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RepeatImageBatch`
- `BlockifyMask`
- `ImageAndMaskPreview`
- `Int`
- `CropByMask`
- `GrowMask`
- `LayerMask: PersonMaskUltra V2`
- `ImageToMask`
- `LazySwitch1way`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `easy mathInt`
- `WanVideoDecode`
- `easy imageSize`
- `easy imageSize`
- `BlendInpaint`
- `easy cleanGpuUsed`
- `PrimitiveStringMultiline`
- `WanVideoModelLoader`
- `easy imageSize`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `easy imageSize`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `Lora Loader Stack (rgthree)`
- `ShowText|pysssss`
- `Lora Loader Stack (rgthree)`
- `KSampler` ★核心
- `BasicScheduler`
- `GrowMask`
- `PerturbedAttentionGuidance`
- `ModelSamplingAuraFlow`
- `AnySwitch`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `VAEEncodeTiled` ★核心
- `VAEDecodeTiled` ★核心
- `TextEncodeQwenImageEditPlus`
- `Note`
- `ReferenceLatent`
- `SaveImage`
- `ImageScale`
- `VAELoader`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `SaveImage`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `Int`
- `Int`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1085725084185521`
- `steps` = `30`
- `cfg` = `2.5`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **96%**（117/122）

**有卡**：`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`RepeatImageBatch`、`CLIPVisionLoader`、`PoseAndFaceDetection`、`DrawMaskOnImage`、`DrawViTPose`、`LayerMask: PersonMaskUltra V2`、`LayerUtility: CropByMask V2`、`easy imageSize`、`CM_IntToFloat`、`CM_FloatBinaryOperation`、`CM_FloatToInt`、`easy mathInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageFromBatch`、`GrowMask`、`LazySwitch1way`、`easy int`、`LayerUtility: ImageBlend`、`easy isMaskEmpty`、`MaskToImage`、`ImageToMask`、`Mask Fill Holes`、`SamplerCustomAdvanced`、`VAELoader`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`LoraLoaderModelOnly`、`easy seed`、`ReferenceLatent`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`CropByMask`、`ImageCropMerge`、`easy boolean`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`LayerUtility: ColorImage V2`、`BlockifyMask`、`ImageAndMaskPreview`、`Int`、`WanVideoDecode`、`BlendInpaint`、`easy cleanGpuUsed`、`WanVideoModelLoader`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`EmptyLatentImage`、`Lora Loader Stack (rgthree)`、`KSampler`、`BasicScheduler`、`PerturbedAttentionGuidance`、`ModelSamplingAuraFlow`、`AnySwitch`、`ImageScaleToTotalPixels`、`VAEEncodeTiled`、`VAEDecodeTiled`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`ImageScale`、`VAEDecode`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage
