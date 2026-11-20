---
key: 平台全量/角色一致性 & CONSISTENT CHARACTERS from an INPUT IMAGE_1856746778539544578.json
name: 角色一致性 & CONSISTENT CHARACTERS from an INPUT IMAGE_1856746778539544578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/角色一致性 & CONSISTENT CHARACTERS from an INPUT IMAGE_1856746778539544578.json
hash: f167240367428c6b
coverage: 0.727273
learned_at: 2026-11-14 02:43:25
nodes: [PreviewImage, ImageCrop, Reroute, PreviewImage, ImageCrop, PreviewImage, PreviewImage, ImageCrop, ImageCrop, Reroute, String Literal, GetNode, JoinStrings, SaveImage, SaveImage, SaveImage, SaveImage, String Literal, GetNode, JoinStrings, JoinStrings, GetNode, String Literal, SetNode, ImageScale, SaveImage, String Literal, JoinStrings, GetNode, JoinStrings, String Literal, Anything Everywhere, SaveImage, Anything Everywhere, Anything Everywhere, JoinStrings, VAEDecode, SaveImage, SaveImage, JoinStrings, JoinStrings, SetNode, CLIPTextEncode, CLIPTextEncode, Anything Everywhere, PulidFluxEvaClipLoader, JoinStrings, JoinStrings, SetNode, GetNode, SamplerCustomAdvanced, SamplerCustomAdvanced, GetNode, Fast Bypasser (rgthree), EmptyLatentImage, SetUnionControlNetType, SetUnionControlNetType, SetUnionControlNetType, SetUnionControlNetType, GetNode, SamplerCustomAdvanced, CFGGuider, CFGGuider, CFGGuider, PrimitiveNode, PrimitiveNode, FluxGuidance, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, JoinStrings, ImageCrop, Anything Everywhere, PrimitiveNode, ImageCrop, ImageCrop, ImageResize+, ImageCrop, GetNode, GetNode, PulidFluxInsightFaceLoader, CFGGuider, VAEDecode, VAEDecode, VAEDecode, VAEDecode, ImageCrop, GetNode, ImageResize+, String Literal, RandomNoise, CLIPTextEncode, PreviewImage, SamplerCustomAdvanced, ImageScale, String Literal, SetNode, SetNode, SetNode, SetNode, String Literal, ImageResize+, ImageResize+, AnyLineArtPreprocessor_aux, AnyLineArtPreprocessor_aux, AnyLineArtPreprocessor_aux, AnyLineArtPreprocessor_aux, String Literal, String Literal, String Literal, GetNode, String Literal, GetNode, ModelPassThrough, Anything Everywhere, ApplyPulidFlux, ControlNetApplySD3, ControlNetApplySD3, ControlNetApplySD3, ControlNetApplySD3, LoadImage, PrimitiveNode, SetNode, Anything Everywhere, BasicScheduler, SetNode, SetNode, Anything Everywhere, Anything Everywhere, String Literal, Note, Note, BasicGuider, KSamplerSelect, ToBasicPipe, FromBasicPipe_v2, JoinStrings, SetNode, SaveImage, GetNode, String Literal, SaveImage, SaveImage, SaveImage, JoinStrings, SaveImage, SaveImage, Fast Bypasser (rgthree), CFGGuider, ExpressionEditor, ExpressionEditor, ExpressionEditor, ExpressionEditor, Load Lora, FaceDetailerPipe, Fast Groups Muter (rgthree), LoraLoader, Int Literal, DualCLIPLoader, VAELoader, PulidFluxModelLoader, GetNode, SaveImage, PreviewImage, SaveImage, UNETLoader, GetNode, RandomNoise, ModelSamplingFlux, easy cleanGpuUsed, UltralyticsDetectorProvider, ToDetailerPipe, Anything Everywhere, ControlNetApplySD3, SamplerCustomAdvanced, EmptySD3LatentImage, easy cleanGpuUsed, SetUnionControlNetType, ControlNetLoader, easy cleanGpuUsed, ApplyPulidFlux, ModelSamplingFlux, easy cleanGpuUsed, UpscaleModelLoader, UltimateSDUpscale, easy cleanGpuUsed, LoadImage]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "controlnet_strength": 0.63, "height": 720, "lora_name": "flux\\diffusion_pytorch_model.safetensors", "strength_clip": 1, "strength_model": 1, "width": 1280}
---

# 平台全量/角色一致性 & CONSISTENT CHARACTERS from an INPUT IMAGE_1856746778539544578.json

> 来源文件 `comfyui_library/workflows/平台全量/角色一致性 & CONSISTENT CHARACTERS from an INPUT IMAGE_1856746778539544578.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（187 个）：
- `PreviewImage`
- `ImageCrop`
- `Reroute`
- `PreviewImage`
- `ImageCrop`
- `PreviewImage`
- `PreviewImage`
- `ImageCrop`
- `ImageCrop`
- `Reroute`
- `String Literal`
- `GetNode`
- `JoinStrings`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `String Literal`
- `GetNode`
- `JoinStrings`
- `JoinStrings`
- `GetNode`
- `String Literal`
- `SetNode`
- `ImageScale`
- `SaveImage`
- `String Literal`
- `JoinStrings`
- `GetNode`
- `JoinStrings`
- `String Literal`
- `Anything Everywhere`
- `SaveImage`
- `Anything Everywhere`
- `Anything Everywhere`
- `JoinStrings`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `JoinStrings`
- `JoinStrings`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Anything Everywhere`
- `PulidFluxEvaClipLoader`
- `JoinStrings`
- `JoinStrings`
- `SetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `Fast Bypasser (rgthree)`
- `EmptyLatentImage` ★核心
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `PrimitiveNode`
- `PrimitiveNode`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `JoinStrings`
- `ImageCrop`
- `Anything Everywhere`
- `PrimitiveNode`
- `ImageCrop`
- `ImageCrop`
- `ImageResize+`
- `ImageCrop`
- `GetNode`
- `GetNode`
- `PulidFluxInsightFaceLoader`
- `CFGGuider`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageCrop`
- `GetNode`
- `ImageResize+`
- `String Literal`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `SamplerCustomAdvanced` ★核心
- `ImageScale`
- `String Literal`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `String Literal`
- `ImageResize+`
- `ImageResize+`
- `AnyLineArtPreprocessor_aux`
- `AnyLineArtPreprocessor_aux`
- `AnyLineArtPreprocessor_aux`
- `AnyLineArtPreprocessor_aux`
- `String Literal`
- `String Literal`
- `String Literal`
- `GetNode`
- `String Literal`
- `GetNode`
- `ModelPassThrough`
- `Anything Everywhere`
- `ApplyPulidFlux`
- `ControlNetApplySD3` ★核心
- `ControlNetApplySD3` ★核心
- `ControlNetApplySD3` ★核心
- `ControlNetApplySD3` ★核心
- `LoadImage`
- `PrimitiveNode`
- `SetNode`
- `Anything Everywhere`
- `BasicScheduler`
- `SetNode`
- `SetNode`
- `Anything Everywhere`
- `Anything Everywhere`
- `String Literal`
- `Note`
- `Note`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ToBasicPipe`
- `FromBasicPipe_v2`
- `JoinStrings`
- `SetNode`
- `SaveImage`
- `GetNode`
- `String Literal`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `JoinStrings`
- `SaveImage`
- `SaveImage`
- `Fast Bypasser (rgthree)`
- `CFGGuider`
- `ExpressionEditor`
- `ExpressionEditor`
- `ExpressionEditor`
- `ExpressionEditor`
- `Load Lora`
- `FaceDetailerPipe`
- `Fast Groups Muter (rgthree)`
- `LoraLoader` ★核心
- `Int Literal`
- `DualCLIPLoader`
- `VAELoader`
- `PulidFluxModelLoader`
- `GetNode`
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader` ★核心
- `GetNode`
- `RandomNoise`
- `ModelSamplingFlux`
- `easy cleanGpuUsed`
- `UltralyticsDetectorProvider`
- `ToDetailerPipe`
- `Anything Everywhere`
- `ControlNetApplySD3` ★核心
- `SamplerCustomAdvanced` ★核心
- `EmptySD3LatentImage`
- `easy cleanGpuUsed`
- `SetUnionControlNetType`
- `ControlNetLoader`
- `easy cleanGpuUsed`
- `ApplyPulidFlux`
- `ModelSamplingFlux`
- `easy cleanGpuUsed`
- `UpscaleModelLoader`
- `UltimateSDUpscale`
- `easy cleanGpuUsed`
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`
- `controlnet_strength` = `0.63`
- `lora_name` = `flux\diffusion_pytorch_model.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **73%**（136/187）

**有卡**：`ImageCrop`、`String Literal`、`JoinStrings`、`SaveImage`、`ImageScale`、`VAEDecode`、`CLIPTextEncode`、`PulidFluxEvaClipLoader`、`SamplerCustomAdvanced`、`Fast Bypasser (rgthree)`、`EmptyLatentImage`、`SetUnionControlNetType`、`CFGGuider`、`FluxGuidance`、`ImageResize+`、`PulidFluxInsightFaceLoader`、`RandomNoise`、`AnyLineArtPreprocessor_aux`、`ModelPassThrough`、`ApplyPulidFlux`、`ControlNetApplySD3`、`LoadImage`、`BasicScheduler`、`BasicGuider`、`KSamplerSelect`、`ToBasicPipe`、`FromBasicPipe_v2`、`ExpressionEditor`、`Load Lora`、`FaceDetailerPipe`、`LoraLoader`、`Int Literal`、`DualCLIPLoader`、`VAELoader`、`PulidFluxModelLoader`、`UNETLoader`、`ModelSamplingFlux`、`easy cleanGpuUsed`、`UltralyticsDetectorProvider`、`ToDetailerPipe`、`EmptySD3LatentImage`、`ControlNetLoader`、`UpscaleModelLoader`、`UltimateSDUpscale`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplySD3、ControlNetLoader
