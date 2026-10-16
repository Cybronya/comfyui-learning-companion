---
key: 视频生成/图生视频/LTX2.3-图生视频升级版（自动提示词）_2030630367857741826.json
name: LTX2.3-图生视频升级版（自动提示词）_2030630367857741826.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2030630367857741826.json
hash: 6e7eacba5dfa9923
coverage: 0.96
learned_at: 2026-10-15 22:35:27
nodes: [LTXVEmptyLatentAudio, LTXVAudioVAELoader, LTXAVTextEncoderLoader, CFGGuider, KSamplerSelect, LTXVAudioVAEDecode, CheckpointLoaderSimple, RandomNoise, GetImageSize, EmptyImage, SimpleMath+, PrimitiveFloat, LTXVPreprocess, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, SamplerCustomAdvanced, CLIPTextEncode, LTXVConditioning, LTXVConcatAVLatent, LTXVScheduler, LoraLoaderModelOnly, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, ResizeImagesByLongerEdge, CFGGuider, KSamplerSelect, ImageScaleBy, llama_cpp_model_loader, CreateVideo, RandomNoise, LTXVSeparateAVLatent, LTXVScheduler, LTXVImgToVideoInplace, LTXVConcatAVLatent, LatentUpscaleModelLoader, LTXVCropGuides, LTXVLatentUpsampler, llama_cpp_unload_model, easy cleanGpuUsed, ShowText|pysssss, LoadImage, llama_cpp_instruct_adv, SaveVideo, Int, ImageResizeKJv2, INTConstant, INTConstant, CLIPTextEncode, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-图生视频升级版（自动提示词）_2030630367857741826.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030630367857741826.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `LTXVEmptyLatentAudio` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `RandomNoise`
- `GetImageSize`
- `EmptyImage`
- `SimpleMath+`
- `PrimitiveFloat`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `LTXVScheduler`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `ResizeImagesByLongerEdge`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ImageScaleBy`
- `llama_cpp_model_loader`
- `CreateVideo`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVScheduler`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `llama_cpp_unload_model`
- `easy cleanGpuUsed`
- `ShowText|pysssss`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `SaveVideo`
- `Int`
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **96%**（48/50）

**有卡**：`LTXVEmptyLatentAudio`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CFGGuider`、`KSamplerSelect`、`LTXVAudioVAEDecode`、`CheckpointLoaderSimple`、`RandomNoise`、`GetImageSize`、`EmptyImage`、`SimpleMath+`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVConcatAVLatent`、`LTXVScheduler`、`LoraLoaderModelOnly`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`ResizeImagesByLongerEdge`、`ImageScaleBy`、`llama_cpp_model_loader`、`CreateVideo`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`llama_cpp_unload_model`、`easy cleanGpuUsed`、`LoadImage`、`llama_cpp_instruct_adv`、`SaveVideo`、`Int`、`ImageResizeKJv2`、`INTConstant`、`Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
