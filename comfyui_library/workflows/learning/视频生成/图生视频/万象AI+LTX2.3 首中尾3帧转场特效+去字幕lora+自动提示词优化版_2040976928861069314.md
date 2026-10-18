---
key: 视频生成/图生视频/万象AI+LTX2.3 首中尾3帧转场特效+去字幕lora+自动提示词优化版_2040976928861069314.json
name: 万象AI+LTX2.3 首中尾3帧转场特效+去字幕lora+自动提示词优化版_2040976928861069314.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/万象AI+LTX2.3 首中尾3帧转场特效+去字幕lora+自动提示词优化版_2040976928861069314.json
hash: 52d8a6ab5ce42b2e
coverage: 0.931034
learned_at: 2026-10-15 22:36:16
nodes: [VAELoaderKJ, Note, ImageResizeKJv2, ComfyMathExpression, LTXVConditioning, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, RandomNoise, LTXVSeparateAVLatent, LTXVCropGuides, RandomNoise, LTXVImgToVideoInplace, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVLatentUpsampler, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, CreateVideo, LTXVAudioVAEDecode, PrimitiveInt, ComfyMathExpression, ImageResizeKJv2, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVPreprocess, LTXVPreprocess, SimpleMath+, ComfyMathExpression, EmptyLTXVLatentVideo, ImageResizeKJv2, DualCLIPLoader, LatentUpscaleModelLoader, VAELoaderKJ, LTXVAddGuideMulti, AspectRatio, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, CR Prompt Text, RH_LLMAPI_Pro_Node, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, SaveVideo, easy showAnything, LoadImage, LoadImage, LoadImage, PrimitiveInt, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/万象AI+LTX2.3 首中尾3帧转场特效+去字幕lora+自动提示词优化版_2040976928861069314.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2040976928861069314.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `VAELoaderKJ`
- `Note`
- `ImageResizeKJv2`
- `ComfyMathExpression`
- `LTXVConditioning`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `RandomNoise`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveInt`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `SimpleMath+`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `LTXVAddGuideMulti`
- `AspectRatio`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `RH_LLMAPI_Pro_Node`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `SaveVideo`
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `CR Prompt Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（54/58）

**有卡**：`VAELoaderKJ`、`ImageResizeKJv2`、`ComfyMathExpression`、`LTXVConditioning`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`CreateVideo`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`SimpleMath+`、`EmptyLTXVLatentVideo`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LTXVAddGuideMulti`、`AspectRatio`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`CR Prompt Text`、`RH_LLMAPI_Pro_Node`、`ResizeImagesByLongerEdge`、`SaveVideo`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
