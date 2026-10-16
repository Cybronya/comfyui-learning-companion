---
key: 视频生成/图生视频/LTX2.3-图生视频（KJ版）_2031018191203340289.json
name: LTX2.3-图生视频（KJ版）_2031018191203340289.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2031018191203340289.json
hash: 4f367d4850b65222
coverage: 0.88
learned_at: 2026-10-15 22:35:29
nodes: [SamplerCustomAdvanced, LatentUpscaleModelLoader, LTXVSeparateAVLatent, llama_cpp_unload_model, easy cleanGpuUsed, llama_cpp_model_loader, llama_cpp_instruct_adv, UNETLoader, VAELoaderKJ, VAELoaderKJ, ComfyMathExpression, ComfyMathExpression, LTXVSeparateAVLatent, LoadImage, LTXVLatentUpsampler, ResizeImagesByLongerEdge, ComfyMathExpression, ImageResizeKJv2, CLIPTextEncode, CreateVideo, RandomNoise, CFGGuider, SamplerCustomAdvanced, VAEDecodeTiled, SaveVideo, LTXVPreprocess, SimpleMath+, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, LTXVAudioVAEDecode, LTXVCropGuides, LTXVConcatAVLatent, LTXVConditioning, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, LTXVImgToVideoInplace, PrimitiveInt, DualCLIPLoader, ShowText|pysssss, PrimitiveStringMultiline, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-图生视频（KJ版）_2031018191203340289.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031018191203340289.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `SamplerCustomAdvanced` ★核心
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `llama_cpp_unload_model`
- `easy cleanGpuUsed`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LTXVLatentUpsampler` ★核心
- `ResizeImagesByLongerEdge`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `RandomNoise`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `SaveVideo`
- `LTXVPreprocess`
- `SimpleMath+`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `LTXVCropGuides`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `PrimitiveInt`
- `DualCLIPLoader`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（44/50）

**有卡**：`SamplerCustomAdvanced`、`LatentUpscaleModelLoader`、`LTXVSeparateAVLatent`、`llama_cpp_unload_model`、`easy cleanGpuUsed`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`UNETLoader`、`VAELoaderKJ`、`ComfyMathExpression`、`LoadImage`、`LTXVLatentUpsampler`、`ResizeImagesByLongerEdge`、`ImageResizeKJv2`、`CLIPTextEncode`、`CreateVideo`、`RandomNoise`、`CFGGuider`、`VAEDecodeTiled`、`SaveVideo`、`LTXVPreprocess`、`SimpleMath+`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`KSamplerSelect`、`ManualSigmas`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`LTXVConditioning`、`DualCLIPLoader`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
