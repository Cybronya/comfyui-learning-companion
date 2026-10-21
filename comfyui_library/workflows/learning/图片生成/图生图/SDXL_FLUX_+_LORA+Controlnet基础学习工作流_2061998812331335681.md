---
key: 图片生成/图生图/SDXL_FLUX_+_LORA+Controlnet基础学习工作流_2061998812331335681.json
name: SDXL_FLUX_+_LORA+Controlnet基础学习工作流_2061998812331335681
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SDXL_FLUX_+_LORA+Controlnet基础学习工作流_2061998812331335681.json
hash: a5e05ff4e88569fa
coverage: 0.839286
learned_at: 2026-10-21 00:44:17
nodes: [Reroute, EmptyFlux2LatentImage, EmptySD3LatentImage, Reroute, EmptyLatentImage, SDXLEmptyLatentSizePicker+, CR Prompt Text, KSampler, DualCLIPLoader, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Text Concatenate, CLIPTextEncode, CLIPTextEncode, FluxGuidance, CR Prompt Text, CLIPTextEncode, Reroute, DualCLIPLoader, Reroute, JanusImageUnderstanding, ControlNetApplyAdvanced, Reroute, ControlNetApplyAdvanced, PreviewImage, ControlNetApplyAdvanced, PreviewImage, GetImageSize, AnyLineArtPreprocessor_aux, AIO_Preprocessor, MarkdownNote, Canny, SDXLEmptyLatentSizePicker+, ShowText|pysssss, JanusModelLoader, CR Text Concatenate, EmptyLatentImage, VAEEncode, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, FluxGuidance, KSampler, CLIPTextEncode, Reroute, Reroute, KSampler, Canny, AIO_Preprocessor, DepthAnythingV2Preprocessor, LineArtPreprocessor, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, CR Prompt Text, VAELoader, Reroute, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoraLoader, LoraLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, Reroute, KSampler, UNETLoader, MarkdownNote, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CheckpointLoaderSimple, UNETLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoader, LoraLoader, ControlNetLoader, ControlNetLoader, ControlNetLoader, Metric3D-NormalMapPreprocessor, EmptySD3LatentImage, EmptyFlux2LatentImage, VAEDecode, SaveImage, VAEDecode, SaveImage, VAEDecode, SaveImage, SaveImage, VAEDecode, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoader, LoraLoader, CR Prompt Text, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), MarkdownNote]
patterns: [text_to_image, image_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 1.5, "checkpoint": "waiNsfwIllustrious16.bhnI.safetensors", "controlnet_strength": 0.5, "denoise": 0.3, "height": 512, "lora_name": "SDXL 色彩平涂-焦茶-Illustriou_NoobAI_1.0 LORA.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 119652317977329, "steps": 24, "strength_clip": 1, "strength_model": 1, "width": 512}
---

# 图片生成/图生图/SDXL_FLUX_+_LORA+Controlnet基础学习工作流_2061998812331335681.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SDXL_FLUX_+_LORA+Controlnet基础学习工作流_2061998812331335681.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（112 个）：
- `Reroute`
- `EmptyFlux2LatentImage`
- `EmptySD3LatentImage`
- `Reroute`
- `EmptyLatentImage` ★核心
- `SDXLEmptyLatentSizePicker+` ★核心
- `CR Prompt Text`
- `KSampler` ★核心
- `DualCLIPLoader`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Text Concatenate`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `Reroute`
- `DualCLIPLoader`
- `Reroute`
- `JanusImageUnderstanding`
- `ControlNetApplyAdvanced` ★核心
- `Reroute`
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `GetImageSize`
- `AnyLineArtPreprocessor_aux`
- `AIO_Preprocessor`
- `MarkdownNote`
- `Canny`
- `SDXLEmptyLatentSizePicker+` ★核心
- `ShowText|pysssss`
- `JanusModelLoader`
- `CR Text Concatenate`
- `EmptyLatentImage` ★核心
- `VAEEncode` ★核心
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `FluxGuidance`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `KSampler` ★核心
- `Canny`
- `AIO_Preprocessor`
- `DepthAnythingV2Preprocessor`
- `LineArtPreprocessor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `CR Prompt Text`
- `VAELoader`
- `Reroute`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `ControlNetLoader`
- `ControlNetLoader`
- `ControlNetLoader`
- `Metric3D-NormalMapPreprocessor`
- `EmptySD3LatentImage`
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`

**识别到的模式**：text_to_image、image_to_image、lora

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `119652317977329`
- `steps` = `24`
- `cfg` = `1.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.3`
- `controlnet_strength` = `0.5`
- `lora_name` = `SDXL 色彩平涂-焦茶-Illustriou_NoobAI_1.0 LORA.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `checkpoint` = `waiNsfwIllustrious16.bhnI.safetensors`

## 知识

覆盖率 **84%**（94/112）

**有卡**：`EmptyFlux2LatentImage`、`EmptySD3LatentImage`、`EmptyLatentImage`、`SDXLEmptyLatentSizePicker+`、`CR Prompt Text`、`KSampler`、`DualCLIPLoader`、`CR Text Concatenate`、`CLIPTextEncode`、`FluxGuidance`、`JanusImageUnderstanding`、`ControlNetApplyAdvanced`、`GetImageSize`、`AnyLineArtPreprocessor_aux`、`AIO_Preprocessor`、`Canny`、`JanusModelLoader`、`VAEEncode`、`DepthAnythingV2Preprocessor`、`LineArtPreprocessor`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`LoadImage`、`LoraLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`CheckpointLoaderSimple`、`ControlNetLoader`、`Metric3D-NormalMapPreprocessor`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、EmptyLatentImage
