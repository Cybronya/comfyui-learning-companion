---
key: 视频生成/文生视频/video_ltx2_3_i2v图生视频，音画同步视频生成，qwen3.5文本反推，_2042515888879968257.json
name: video_ltx2_3_i2v图生视频，音画同步视频生成，qwen3.5文本反推，_2042515888879968257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/video_ltx2_3_i2v图生视频，音画同步视频生成，qwen3.5文本反推，_2042515888879968257.json
hash: 2049642b4bf2763a
coverage: 0.877551
learned_at: 2026-10-11 19:49:45
nodes: [RandomNoise, LTXVCropGuides, LTXVLatentUpsampler, Reroute, ComfyMathExpression, LTXVConcatAVLatent, LTXVConditioning, KSamplerSelect, LTXVImgToVideoInplace, KSamplerSelect, CFGGuider, llama_cpp_parameters, ShowText|pysssss, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, SamplerCustomAdvanced, SamplerCustomAdvanced, ManualSigmas, EmptyLTXVLatentVideo, ComfyMathExpression, LTXVPreprocess, PrimitiveInt, LatentUpscaleModelLoader, ManualSigmas, LTXVConcatAVLatent, PrimitiveInt, PrimitiveInt, ResizeImageMaskNode, CLIPTextEncode, ResizeImagesByLongerEdge, CLIPTextEncode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CreateVideo, LTXVSeparateAVLatent, VAEDecode, RandomNoise, CFGGuider, PrimitiveInt, ComfyMathExpression, SaveVideo, LTXAVTextEncoderLoader, LoraLoaderModelOnly, PrimitiveBoolean, CheckpointLoaderSimple, LTXVAudioVAELoader, LoadImage, llama_cpp_model_loader, llama_cpp_instruct_adv]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/video_ltx2_3_i2v图生视频，音画同步视频生成，qwen3.5文本反推，_2042515888879968257.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/video_ltx2_3_i2v图生视频，音画同步视频生成，qwen3.5文本反推，_2042515888879968257.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `RandomNoise`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `llama_cpp_parameters`
- `ShowText|pysssss`
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `LTXVPreprocess`
- `PrimitiveInt`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `PrimitiveInt`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `CLIPTextEncode` ★核心
- `ResizeImagesByLongerEdge`
- `CLIPTextEncode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `RandomNoise`
- `CFGGuider`
- `PrimitiveInt`
- `ComfyMathExpression`
- `SaveVideo`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveBoolean`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LoadImage`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-fp8.safetensors`

## 知识

覆盖率 **88%**（43/49）

**有卡**：`RandomNoise`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`LTXVConditioning`、`KSamplerSelect`、`LTXVImgToVideoInplace`、`CFGGuider`、`llama_cpp_parameters`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`ManualSigmas`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LatentUpscaleModelLoader`、`ResizeImageMaskNode`、`CLIPTextEncode`、`ResizeImagesByLongerEdge`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`CreateVideo`、`VAEDecode`、`SaveVideo`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`PrimitiveBoolean`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LoadImage`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
