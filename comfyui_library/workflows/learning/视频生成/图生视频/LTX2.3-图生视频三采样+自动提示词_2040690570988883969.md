---
key: 视频生成/图生视频/LTX2.3-图生视频三采样+自动提示词_2040690570988883969.json
name: LTX2.3-图生视频三采样+自动提示词_2040690570988883969.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2040690570988883969.json
hash: 27381f0d4a264d61
coverage: 0.918033
learned_at: 2026-10-15 22:36:15
nodes: [DualCLIPLoader, ManualSigmas, KSamplerSelect, KSamplerSelect, PrimitiveInt, CreateVideo, LTXVConcatAVLatent, ManualSigmas, CFGGuider, UNETLoader, easy cleanGpuUsed, llama_cpp_instruct_adv, SamplerCustomAdvanced, RandomNoise, ResizeImagesByLongerEdge, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, CFGGuider, VAELoaderKJ, SamplerCustomAdvanced, LTXVLatentUpsampler, RandomNoise, SamplerCustomAdvanced, ImageResizeKJv2, LoadImage, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, LTXVCropGuides, LTXVImgToVideoInplace, LTXVConcatAVLatent, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVSeparateAVLatent, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVSeparateAVLatent, VAELoaderKJ, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, LatentUpscaleModelLoader, Text, llama_cpp_model_loader, ShowText|pysssss, Text, LTXVConditioning, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, LTXVPreprocess, SaveVideo, SimpleMath+, PrimitiveInt, PrimitiveInt, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-图生视频三采样+自动提示词_2040690570988883969.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2040690570988883969.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `DualCLIPLoader`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `CreateVideo`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `CFGGuider`
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `CFGGuider`
- `VAELoaderKJ`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `ImageResizeKJv2`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `VAELoaderKJ`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LatentUpscaleModelLoader`
- `Text`
- `llama_cpp_model_loader`
- `ShowText|pysssss`
- `Text`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `SaveVideo`
- `SimpleMath+`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（56/61）

**有卡**：`DualCLIPLoader`、`ManualSigmas`、`KSamplerSelect`、`CreateVideo`、`LTXVConcatAVLatent`、`CFGGuider`、`UNETLoader`、`easy cleanGpuUsed`、`llama_cpp_instruct_adv`、`SamplerCustomAdvanced`、`RandomNoise`、`ResizeImagesByLongerEdge`、`VAELoaderKJ`、`LTXVLatentUpsampler`、`ImageResizeKJv2`、`LoadImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`ComfyMathExpression`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LatentUpscaleModelLoader`、`Text`、`llama_cpp_model_loader`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`SaveVideo`、`SimpleMath+`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
