---
key: 平台全量/NNW_Character-Multiangle-Face-Pose-Refer_20250618_1935111311548456962.json
name: NNW_Character-Multiangle-Face-Pose-Refer_20250618_1935111311548456962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/NNW_Character-Multiangle-Face-Pose-Refer_20250618_1935111311548456962.json
hash: a8239ee9e64ccd4a
coverage: 0.866667
learned_at: 2026-11-14 00:47:00
nodes: [UpscaleModelLoader, PreviewImage, FromBasicPipe_v2, ToBasicPipe, KSamplerSelect, Reroute, Reroute, Reroute, UltimateSDUpscale, CoreMLDetailerHookProvider, SaveImage, SetUnionControlNetType, ControlNetLoader, UNETLoader, VAEDecode, ControlNetApplySD3, BasicScheduler, ModelSamplingFlux, SamplerCustomAdvanced, ApplyPulidFlux, BasicGuider, PulidFluxInsightFaceLoader, PulidFluxEvaClipLoader, PulidFluxModelLoader, UnetLoaderGGUF, LoadImage, CLIPTextEncode, FaceDetailerPipe, DualCLIPLoader, VAELoader, UNETLoader, EmptySD3LatentImage, RandomNoise, ImageScale, GetImage_(Width&Height) _O, CLIPTextEncode, OpenposePreprocessor, SaveImage, FluxGuidance, ToDetailerPipe, UltralyticsDetectorProvider, Simple String, Fast Groups Muter (rgthree), PreviewImage, LoadImage]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.63}
---

# 平台全量/NNW_Character-Multiangle-Face-Pose-Refer_20250618_1935111311548456962.json

> 来源文件 `comfyui_library/workflows/平台全量/NNW_Character-Multiangle-Face-Pose-Refer_20250618_1935111311548456962.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `UpscaleModelLoader`
- `PreviewImage`
- `FromBasicPipe_v2`
- `ToBasicPipe`
- `KSamplerSelect` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `UltimateSDUpscale`
- `CoreMLDetailerHookProvider`
- `SaveImage`
- `SetUnionControlNetType`
- `ControlNetLoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `ControlNetApplySD3` ★核心
- `BasicScheduler`
- `ModelSamplingFlux`
- `SamplerCustomAdvanced` ★核心
- `ApplyPulidFlux`
- `BasicGuider`
- `PulidFluxInsightFaceLoader`
- `PulidFluxEvaClipLoader`
- `PulidFluxModelLoader`
- `UnetLoaderGGUF` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `FaceDetailerPipe`
- `DualCLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `EmptySD3LatentImage`
- `RandomNoise`
- `ImageScale`
- `GetImage_(Width&Height) _O`
- `CLIPTextEncode` ★核心
- `OpenposePreprocessor`
- `SaveImage`
- `FluxGuidance`
- `ToDetailerPipe`
- `UltralyticsDetectorProvider`
- `Simple String`
- `Fast Groups Muter (rgthree)`
- `PreviewImage`
- `LoadImage`

## 关键参数

- `controlnet_strength` = `0.63`

## 知识

覆盖率 **87%**（39/45）

**有卡**：`UpscaleModelLoader`、`FromBasicPipe_v2`、`ToBasicPipe`、`KSamplerSelect`、`UltimateSDUpscale`、`CoreMLDetailerHookProvider`、`SaveImage`、`SetUnionControlNetType`、`ControlNetLoader`、`UNETLoader`、`VAEDecode`、`ControlNetApplySD3`、`BasicScheduler`、`ModelSamplingFlux`、`SamplerCustomAdvanced`、`ApplyPulidFlux`、`BasicGuider`、`PulidFluxInsightFaceLoader`、`PulidFluxEvaClipLoader`、`PulidFluxModelLoader`、`UnetLoaderGGUF`、`LoadImage`、`CLIPTextEncode`、`FaceDetailerPipe`、`DualCLIPLoader`、`VAELoader`、`EmptySD3LatentImage`、`RandomNoise`、`ImageScale`、`GetImage_(Width&Height) _O`、`OpenposePreprocessor`、`FluxGuidance`、`ToDetailerPipe`、`UltralyticsDetectorProvider`、`Simple String`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplySD3、ControlNetLoader、OpenposePreprocessor
