---
key: 图片生成/图生图/LTX2.3首尾帧转场特效+Qwen3.5提示词优化_2064269147021864961.json
name: LTX2.3首尾帧转场特效+Qwen3.5提示词优化_2064269147021864961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/LTX2.3首尾帧转场特效+Qwen3.5提示词优化_2064269147021864961.json
hash: 78a581f863d34d3b
coverage: 0.929825
learned_at: 2026-10-23 11:08:55
nodes: [UNETLoader, DualCLIPLoader, VAELoaderKJ, Note, PrimitiveInt, VAELoaderKJ, ImageResizeKJv2, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVAddGuideMulti, LTXVConditioning, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, RandomNoise, LTXVSeparateAVLatent, LTXVCropGuides, RandomNoise, LTXVImgToVideoInplace, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, CreateVideo, llama_cpp_model_loader, easy cleanGpuUsed, SaveVideo, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVPreprocess, EmptyLTXVLatentVideo, ImageResizeKJv2, ImageConcanate, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, CLIPTextEncode, CLIPTextEncode, SimpleMath+, LTXVAudioVAEDecode, PrimitiveInt, AspectRatio, ShowText|pysssss, Text, llama_cpp_instruct_adv, LoadImage, LoadImage, Text, LatentUpscaleModelLoader, LoraLoaderModelOnly, LTXVLatentUpsampler, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 图片生成/图生图/LTX2.3首尾帧转场特效+Qwen3.5提示词优化_2064269147021864961.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/LTX2.3首尾帧转场特效+Qwen3.5提示词优化_2064269147021864961.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `Note`
- `PrimitiveInt`
- `VAELoaderKJ`
- `ImageResizeKJv2`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVAddGuideMulti`
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
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `llama_cpp_model_loader`
- `easy cleanGpuUsed`
- `SaveVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `ImageConcanate`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveInt`
- `AspectRatio`
- `ShowText|pysssss`
- `Text`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `LoadImage`
- `Text`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LTXVLatentUpsampler` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（53/57）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`ImageResizeKJv2`、`ComfyMathExpression`、`LTXVAddGuideMulti`、`LTXVConditioning`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`CreateVideo`、`llama_cpp_model_loader`、`easy cleanGpuUsed`、`SaveVideo`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`ImageConcanate`、`ResizeImagesByLongerEdge`、`CLIPTextEncode`、`SimpleMath+`、`LTXVAudioVAEDecode`、`AspectRatio`、`Text`、`llama_cpp_instruct_adv`、`LoadImage`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LTXVLatentUpsampler`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
