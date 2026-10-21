---
key: 图片生成/文生图/【阿良绘】大透视角度出图流程（XL模型+不同CN）V2.0_2060222636877238273.json
name: 【阿良绘】大透视角度出图流程（XL模型+不同CN）V2.0_2060222636877238273
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【阿良绘】大透视角度出图流程（XL模型+不同CN）V2.0_2060222636877238273.json
hash: bd83d1882c27e46b
coverage: 0.788732
learned_at: 2026-10-19 23:03:39
nodes: [IPAdapterAdvanced, CLIPVisionLoader, IPAdapterUnifiedLoader, IPAdapterAdvanced, CLIPVisionLoader, IPAdapterUnifiedLoader, CLIPVisionLoader, PreviewImage, PreviewImage, AIO_Preprocessor, AIO_Preprocessor, ControlNetLoader, ControlNetLoader, PreviewImage, AIO_Preprocessor, PreviewImage, InvertMask, SetLatentNoiseMask, LayerMask: MaskPreview, SaveImage, Note, AIO_Preprocessor, ControlNetLoader, LayerMask: SegmentAnythingUltra V2, VAEEncode, Anything Everywhere, Anything Everywhere, CLIPTextEncode, LoadImage, LoadImage, LoadImage, IPAdapterAdvanced, IPAdapterUnifiedLoader, PreviewImage, PreviewImage, easy promptConcat, JjkText, KSampler, VAEDecode, Reroute, Reroute, EmptyLatentImage, Get Image Size, ControlNetApplyAdvanced, ControlNetApplyAdvanced, ControlNetApplyAdvanced, ControlNetLoader, Joy_caption_two_load, Joy_extra_options, LoadImage, CLIPTextEncode, easy showAnything, Joy_caption_two_advanced, ControlNetApplyAdvanced, UltralyticsDetectorProvider, SAMLoader, FaceDetailer, SaveImage, UltimateSDUpscale, UpscaleModelLoader, CheckpointLoaderSimple, LoraLoader, LoraLoader, LoadImage, JjkText, Anything Everywhere, ControlNetApplyAdvanced, VAELoader, AIO_Preprocessor, ControlNetLoader, SaveImage]
patterns: [text_to_image, image_to_image, lora]
missing: []
parameters: {"batch_size": 2, "cfg": 5, "checkpoint": "动漫光影-AniShadow [无需lora，自带画风和热门角色]_V5.safetensors", "controlnet_strength": 0.6, "denoise": 1, "height": 1024, "lora_name": "线稿大师加强版_Franklin Booth.safetensors", "sampler_name": "dpmpp_2m_sde_gpu", "scheduler": "karras", "seed": 213365547818119, "steps": 25, "strength_clip": 0.4, "strength_model": 0.4, "width": 768}
---

# 图片生成/文生图/【阿良绘】大透视角度出图流程（XL模型+不同CN）V2.0_2060222636877238273.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【阿良绘】大透视角度出图流程（XL模型+不同CN）V2.0_2060222636877238273.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `IPAdapterAdvanced`
- `CLIPVisionLoader`
- `IPAdapterUnifiedLoader`
- `IPAdapterAdvanced`
- `CLIPVisionLoader`
- `IPAdapterUnifiedLoader`
- `CLIPVisionLoader`
- `PreviewImage`
- `PreviewImage`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `ControlNetLoader`
- `ControlNetLoader`
- `PreviewImage`
- `AIO_Preprocessor`
- `PreviewImage`
- `InvertMask`
- `SetLatentNoiseMask`
- `LayerMask: MaskPreview`
- `SaveImage`
- `Note`
- `AIO_Preprocessor`
- `ControlNetLoader`
- `LayerMask: SegmentAnythingUltra V2`
- `VAEEncode` ★核心
- `Anything Everywhere`
- `Anything Everywhere`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `PreviewImage`
- `PreviewImage`
- `easy promptConcat`
- `JjkText`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `EmptyLatentImage` ★核心
- `Get Image Size`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `Joy_caption_two_load`
- `Joy_extra_options`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `Joy_caption_two_advanced`
- `ControlNetApplyAdvanced` ★核心
- `UltralyticsDetectorProvider`
- `SAMLoader`
- `FaceDetailer`
- `SaveImage`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoadImage`
- `JjkText`
- `Anything Everywhere`
- `ControlNetApplyAdvanced` ★核心
- `VAELoader`
- `AIO_Preprocessor`
- `ControlNetLoader`
- `SaveImage`

**识别到的模式**：text_to_image、image_to_image、lora

## 关键参数

- `seed` = `213365547818119`
- `steps` = `25`
- `cfg` = `5`
- `sampler_name` = `dpmpp_2m_sde_gpu`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `768`
- `height` = `1024`
- `batch_size` = `2`
- `controlnet_strength` = `0.6`
- `checkpoint` = `动漫光影-AniShadow [无需lora，自带画风和热门角色]_V5.safetensors`
- `lora_name` = `线稿大师加强版_Franklin Booth.safetensors`
- `strength_model` = `0.4`
- `strength_clip` = `0.4`

## 知识

覆盖率 **79%**（56/71）

**有卡**：`IPAdapterAdvanced`、`CLIPVisionLoader`、`IPAdapterUnifiedLoader`、`AIO_Preprocessor`、`ControlNetLoader`、`InvertMask`、`SetLatentNoiseMask`、`LayerMask: MaskPreview`、`SaveImage`、`LayerMask: SegmentAnythingUltra V2`、`VAEEncode`、`CLIPTextEncode`、`LoadImage`、`easy promptConcat`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`Get Image Size`、`ControlNetApplyAdvanced`、`Joy_caption_two_load`、`Joy_extra_options`、`Joy_caption_two_advanced`、`UltralyticsDetectorProvider`、`SAMLoader`、`FaceDetailer`、`UltimateSDUpscale`、`UpscaleModelLoader`、`CheckpointLoaderSimple`、`LoraLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced
