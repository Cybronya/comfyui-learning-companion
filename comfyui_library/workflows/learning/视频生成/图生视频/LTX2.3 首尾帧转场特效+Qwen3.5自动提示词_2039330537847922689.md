---
key: 视频生成/图生视频/LTX2.3 首尾帧转场特效+Qwen3.5自动提示词_2039330537847922689.json
name: LTX2.3 首尾帧转场特效+Qwen3.5自动提示词_2039330537847922689.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2039330537847922689.json
hash: 59db29cf0628c496
coverage: 0.928571
learned_at: 2026-10-15 22:36:08
nodes: [UNETLoader, DualCLIPLoader, VAELoaderKJ, Note, PrimitiveInt, LoraLoaderModelOnly, LatentUpscaleModelLoader, VAELoaderKJ, ImageResizeKJv2, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVAddGuideMulti, LTXVConditioning, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, RandomNoise, LTXVSeparateAVLatent, LTXVCropGuides, RandomNoise, LTXVImgToVideoInplace, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVLatentUpsampler, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, CreateVideo, llama_cpp_model_loader, easy cleanGpuUsed, SaveVideo, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVPreprocess, EmptyLTXVLatentVideo, ImageResizeKJv2, ImageConcanate, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, CLIPTextEncode, CLIPTextEncode, SimpleMath+, LTXVAudioVAEDecode, PrimitiveInt, LoadImage, LoadImage, AspectRatio, ShowText|pysssss, Text, llama_cpp_instruct_adv, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 首尾帧转场特效+Qwen3.5自动提示词_2039330537847922689.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2039330537847922689.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `Note`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
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
- `LTXVLatentUpsampler` ★核心
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
- `LoadImage`
- `LoadImage`
- `AspectRatio`
- `ShowText|pysssss`
- `Text`
- `llama_cpp_instruct_adv`
- `Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（52/56）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`ImageResizeKJv2`、`ComfyMathExpression`、`LTXVAddGuideMulti`、`LTXVConditioning`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`CreateVideo`、`llama_cpp_model_loader`、`easy cleanGpuUsed`、`SaveVideo`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`ImageConcanate`、`ResizeImagesByLongerEdge`、`CLIPTextEncode`、`SimpleMath+`、`LTXVAudioVAEDecode`、`LoadImage`、`AspectRatio`、`Text`、`llama_cpp_instruct_adv`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
