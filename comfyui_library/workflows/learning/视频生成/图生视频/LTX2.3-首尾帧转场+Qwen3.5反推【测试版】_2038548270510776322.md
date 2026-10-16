---
key: 视频生成/图生视频/LTX2.3-首尾帧转场+Qwen3.5反推【测试版】_2038548270510776322.json
name: LTX2.3-首尾帧转场+Qwen3.5反推【测试版】_2038548270510776322.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2038548270510776322.json
hash: 36eb7fd08a7375a2
coverage: 0.910714
learned_at: 2026-10-15 22:36:03
nodes: [SamplerCustomAdvanced, ResizeImagesByLongerEdge, LatentUpscaleModelLoader, VAELoaderKJ, DualCLIPLoader, LTXVPreprocess, LTXVPreprocess, LTXVAudioVAEDecode, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, ResizeImagesByLongerEdge, ImageResizeKJv2, ManualSigmas, LTXVConcatAVLatent, CFGGuider, KSamplerSelect, LTXVEmptyLatentAudio, ComfyMathExpression, VAELoaderKJ, KSamplerSelect, LTXVSeparateAVLatent, VAEDecodeTiled, PrimitiveInt, SimpleMath+, LTXVConditioning, CreateVideo, LTXVConcatAVLatent, ManualSigmas, RandomNoise, CFGGuider, LoraLoaderModelOnly, UNETLoader, CLIPTextEncode, CLIPTextEncode, Text, ImageResizeKJv2, PrimitiveInt, PrimitiveInt, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, RandomNoise, LoadImage, LoadImage, ImageConcanate, Text, SaveVideo, llama_cpp_model_loader, llama_cpp_instruct_adv, easy cleanGpuUsed, ShowText|pysssss, EmptyLTXVLatentVideo, LTXVAddGuideMulti, LTXVLatentUpsampler, LTXVImgToVideoInplace]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-首尾帧转场+Qwen3.5反推【测试版】_2038548270510776322.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038548270510776322.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `SamplerCustomAdvanced` ★核心
- `ResizeImagesByLongerEdge`
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `ComfyMathExpression`
- `VAELoaderKJ`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `PrimitiveInt`
- `SimpleMath+`
- `LTXVConditioning`
- `CreateVideo`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `RandomNoise`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Text`
- `ImageResizeKJv2`
- `PrimitiveInt`
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `RandomNoise`
- `LoadImage`
- `LoadImage`
- `ImageConcanate`
- `Text`
- `SaveVideo`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `easy cleanGpuUsed`
- `ShowText|pysssss`
- `EmptyLTXVLatentVideo`
- `LTXVAddGuideMulti`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（51/56）

**有卡**：`SamplerCustomAdvanced`、`ResizeImagesByLongerEdge`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXVPreprocess`、`LTXVAudioVAEDecode`、`ComfyMathExpression`、`ImageResizeKJv2`、`ManualSigmas`、`LTXVConcatAVLatent`、`CFGGuider`、`KSamplerSelect`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`SimpleMath+`、`LTXVConditioning`、`CreateVideo`、`RandomNoise`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPTextEncode`、`Text`、`LTXVCropGuides`、`LoadImage`、`ImageConcanate`、`SaveVideo`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`easy cleanGpuUsed`、`EmptyLTXVLatentVideo`、`LTXVAddGuideMulti`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
