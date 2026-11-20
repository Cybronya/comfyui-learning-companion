---
key: 视频生成/图生视频/qwen_image_2.1_换脸_2115954917260226561.json
name: qwen_image_2.1_换脸_2115954917260226561
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/qwen_image_2.1_换脸_2115954917260226561.json
hash: 3bd6cc884b3587ab
coverage: 0.810345
learned_at: 2026-10-30 23:29:12
nodes: [LoadImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, CLIPLoader, PrimitiveStringMultiline, PreviewAny, ComfySwitchNode, BatchImagesNode, TextGenerate, easy positive, CLIPLoader, LoraLoaderModelOnly, UNETLoader, VAEEncode, CLIPTextEncode, VAELoader, ReferenceLatent, ConditioningZeroOut, Flux2Scheduler, RandomNoise, KSamplerSelect, CFGGuider, EmptyFlux2LatentImage, VAEDecode, SamplerCustomAdvanced, ImageColorMatch+, ImageRemoveAlpha+, ACE_ImageFaceCrop, ResizeImagesByShorterEdge, DrawMaskOnImage, InpaintCropImproved, InpaintStitchImproved, Reroute, InpaintCropImproved, ACE_ImageFaceCrop, easy imageRemBg, PreviewImage, Reroute, Reroute, ComfyMathExpression, GetImageSize+, ComfyMathExpression, ImageScale, ImageCropByMaskAndResize, PreviewImage, PreviewImage, AnySwitch, PreviewImage, OpenposePreprocessor, SaveImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 33343569827773, "steps": 40, "width": 1024}
---

# 视频生成/图生视频/qwen_image_2.1_换脸_2115954917260226561.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/qwen_image_2.1_换脸_2115954917260226561.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `ComfySwitchNode`
- `BatchImagesNode`
- `TextGenerate`
- `easy positive`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `ImageColorMatch+`
- `ImageRemoveAlpha+`
- `ACE_ImageFaceCrop`
- `ResizeImagesByShorterEdge`
- `DrawMaskOnImage`
- `InpaintCropImproved`
- `InpaintStitchImproved`
- `Reroute`
- `InpaintCropImproved`
- `ACE_ImageFaceCrop`
- `easy imageRemBg`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `ComfyMathExpression`
- `GetImageSize+`
- `ComfyMathExpression`
- `ImageScale`
- `ImageCropByMaskAndResize`
- `PreviewImage`
- `PreviewImage`
- `AnySwitch`
- `PreviewImage`
- `OpenposePreprocessor`
- `SaveImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `33343569827773`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（47/58）

**有卡**：`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`BatchImagesNode`、`TextGenerate`、`easy positive`、`LoraLoaderModelOnly`、`VAEEncode`、`CLIPTextEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`Flux2Scheduler`、`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`ImageColorMatch+`、`ImageRemoveAlpha+`、`ACE_ImageFaceCrop`、`ResizeImagesByShorterEdge`、`DrawMaskOnImage`、`InpaintCropImproved`、`InpaintStitchImproved`、`easy imageRemBg`、`ComfyMathExpression`、`GetImageSize+`、`ImageScale`、`ImageCropByMaskAndResize`、`AnySwitch`、`OpenposePreprocessor`、`SaveImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode
