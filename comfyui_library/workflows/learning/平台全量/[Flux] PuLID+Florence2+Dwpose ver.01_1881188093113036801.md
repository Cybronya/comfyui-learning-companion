---
key: 平台全量/[Flux] PuLID+Florence2+Dwpose ver.01_1881188093113036801.json
name: [Flux] PuLID+Florence2+Dwpose ver.01_1881188093113036801
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/[Flux] PuLID+Florence2+Dwpose ver.01_1881188093113036801.json
hash: 185e0d753c92e29d
coverage: 0.877551
learned_at: 2026-11-14 01:08:47
nodes: [CoreMLDetailerHookProvider, ToDetailerPipe, UpscaleModelLoader, PreviewImage, UltimateSDUpscale, VAEDecode, FromBasicPipe_v2, ApplyPulidFlux, CR Apply LoRA Stack, BasicGuider, ToBasicPipe, SamplerCustomAdvanced, BasicScheduler, KSamplerSelect, UltralyticsDetectorProvider, FaceDetailerPipe, SaveImage, Fast Groups Muter (rgthree), Note, PulidFluxEvaClipLoader, PulidFluxModelLoader, PulidFluxInsightFaceLoader, RandomNoise, ReActorRestoreFace, ImageResize+, Florence2ModelLoader, Florence2Run, ControlNetApplySD3, FluxGuidance, CLIPTextEncode, CLIPTextEncode, CR Text Concatenate, ShowText|pysssss, easy positive, easy positive, AIO_Preprocessor, EmptySD3LatentImage, PreviewImage, ShowText|pysssss, LoadImage, LoadImage, DF_Get_image_size, ImageResizeAdvanced, UNETLoader, DualCLIPLoader, VAELoader, ControlNetLoader, SaveImage, CR LoRA Stack]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.6}
---

# 平台全量/[Flux] PuLID+Florence2+Dwpose ver.01_1881188093113036801.json

> 来源文件 `comfyui_library/workflows/平台全量/[Flux] PuLID+Florence2+Dwpose ver.01_1881188093113036801.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `CoreMLDetailerHookProvider`
- `ToDetailerPipe`
- `UpscaleModelLoader`
- `PreviewImage`
- `UltimateSDUpscale`
- `VAEDecode` ★核心
- `FromBasicPipe_v2`
- `ApplyPulidFlux`
- `CR Apply LoRA Stack`
- `BasicGuider`
- `ToBasicPipe`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `UltralyticsDetectorProvider`
- `FaceDetailerPipe`
- `SaveImage`
- `Fast Groups Muter (rgthree)`
- `Note`
- `PulidFluxEvaClipLoader`
- `PulidFluxModelLoader`
- `PulidFluxInsightFaceLoader`
- `RandomNoise`
- `ReActorRestoreFace`
- `ImageResize+`
- `Florence2ModelLoader`
- `Florence2Run`
- `ControlNetApplySD3` ★核心
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `ShowText|pysssss`
- `easy positive`
- `easy positive`
- `AIO_Preprocessor`
- `EmptySD3LatentImage`
- `PreviewImage`
- `ShowText|pysssss`
- `LoadImage`
- `LoadImage`
- `DF_Get_image_size`
- `ImageResizeAdvanced`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `ControlNetLoader`
- `SaveImage`
- `CR LoRA Stack`

## 关键参数

- `controlnet_strength` = `0.6`

## 知识

覆盖率 **88%**（43/49）

**有卡**：`CoreMLDetailerHookProvider`、`ToDetailerPipe`、`UpscaleModelLoader`、`UltimateSDUpscale`、`VAEDecode`、`FromBasicPipe_v2`、`ApplyPulidFlux`、`CR Apply LoRA Stack`、`BasicGuider`、`ToBasicPipe`、`SamplerCustomAdvanced`、`BasicScheduler`、`KSamplerSelect`、`UltralyticsDetectorProvider`、`FaceDetailerPipe`、`SaveImage`、`PulidFluxEvaClipLoader`、`PulidFluxModelLoader`、`PulidFluxInsightFaceLoader`、`RandomNoise`、`ReActorRestoreFace`、`ImageResize+`、`Florence2ModelLoader`、`Florence2Run`、`ControlNetApplySD3`、`FluxGuidance`、`CLIPTextEncode`、`CR Text Concatenate`、`easy positive`、`AIO_Preprocessor`、`EmptySD3LatentImage`、`LoadImage`、`DF_Get_image_size`、`ImageResizeAdvanced`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`ControlNetLoader`、`CR LoRA Stack`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplySD3、ControlNetLoader、FluxGuidance
