---
key: 视频生成/图生视频/多图参考-4宫格-LTX2.3图生视频音画同步_2059942996799479809.json
name: 多图参考-4宫格-LTX2.3图生视频音画同步_2059942996799479809.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2059942996799479809.json
hash: ec9571f799bb15e1
coverage: 0.883333
learned_at: 2026-10-15 22:38:44
nodes: [LoadImage, LoadImage, CLIPTextEncode, LatentUpscaleModelLoader, LTXVConditioning, CLIPTextEncode, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, PrimitiveInt, KSamplerSelect, RandomNoise, KSamplerSelect, LTXVEmptyLatentAudio, RandomNoise, CFGGuider, PrimitiveInt, CFGGuider, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveFloat, RHHiddenNodes, Int, Int, LoadImage, ImageTile+, LoadImage, ImageFromBatch+, LoadImage, ImageFromBatch+, ImageFromBatch+, Fast Groups Bypasser (rgthree), PrimitiveInt, PrimitiveInt, Int, ImageResizeKJv2, ImageResizeKJv2, LTXVPreprocess, ImageResizeKJv2, ComfyMathExpression, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, LTXVPreprocess, ResizeImagesByLongerEdge, LTXVPreprocess, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVPreprocess, ComfyMathExpression, ImageResizeKJv2, VHS_VideoCombine, PrimitiveStringMultiline, ImageFromBatch+]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "sulphur_distil_bf16.safetensors", "height": 1, "width": 1}
---

# 视频生成/图生视频/多图参考-4宫格-LTX2.3图生视频音画同步_2059942996799479809.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2059942996799479809.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Process → Other

**节点**（60 个）：
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LatentUpscaleModelLoader`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `RandomNoise`
- `CFGGuider`
- `PrimitiveInt`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `RHHiddenNodes`
- `Int`
- `Int`
- `LoadImage`
- `ImageTile+`
- `LoadImage`
- `ImageFromBatch+`
- `LoadImage`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveInt`
- `PrimitiveInt`
- `Int`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `ComfyMathExpression`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `ImageFromBatch+`

## 关键参数

- `checkpoint` = `sulphur_distil_bf16.safetensors`
- `width` = `1`
- `height` = `1`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（53/60）

**有卡**：`LoadImage`、`CLIPTextEncode`、`LatentUpscaleModelLoader`、`LTXVConditioning`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`KSamplerSelect`、`RandomNoise`、`LTXVEmptyLatentAudio`、`CFGGuider`、`LoraLoaderModelOnly`、`RHHiddenNodes`、`Int`、`ImageTile+`、`ImageFromBatch+`、`ImageResizeKJv2`、`LTXVPreprocess`、`ComfyMathExpression`、`ResizeImagesByLongerEdge`、`VHS_VideoCombine`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、LatentUpscaleModelLoader、LTXAVTextEncoderLoader
