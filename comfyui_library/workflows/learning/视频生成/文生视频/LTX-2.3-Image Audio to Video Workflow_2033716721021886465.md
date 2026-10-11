---
key: 视频生成/文生视频/LTX-2.3-Image Audio to Video Workflow_2033716721021886465.json
name: LTX-2.3-Image Audio to Video Workflow_2033716721021886465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3-Image Audio to Video Workflow_2033716721021886465.json
hash: 4a622aba928b0d38
coverage: 0.888889
learned_at: 2026-10-11 03:48:34
nodes: [RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVConcatAVLatent, ManualSigmas, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, Reroute, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVCropGuides, LTXVImgToVideoInplace, LTXVSeparateAVLatent, CreateVideo, SolidMask, LTXAVTextEncoderLoader, ComfyMathExpression, EmptyLTXVLatentVideo, SamplerCustomAdvanced, LTXVConditioning, CLIPTextEncode, RandomNoise, LTXVAudioVAEEncode, LTXVAudioVAELoader, ComfyMathExpression, LatentUpscaleModelLoader, SaveVideo, ComfyMathExpression, TrimAudioDuration, LoadAudio, ComfyMathExpression, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, LoadImage, SetLatentNoiseMask, GetImageSize, LoraLoader, TextGenerateLTX2Prompt, PreviewAny, CLIPTextEncode, LoraLoaderModelOnly, PrimitiveFloat, CheckpointLoaderSimple, PrimitiveStringMultiline, LTXVImgToVideoInplace, PrimitiveBoolean, PrimitiveInt, Note]
patterns: [lora]
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 视频生成/文生视频/LTX-2.3-Image Audio to Video Workflow_2033716721021886465.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3-Image Audio to Video Workflow_2033716721021886465.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `SolidMask`
- `LTXAVTextEncoderLoader`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `SamplerCustomAdvanced` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `LTXVAudioVAEEncode` ★核心
- `LTXVAudioVAELoader`
- `ComfyMathExpression`
- `LatentUpscaleModelLoader`
- `SaveVideo`
- `ComfyMathExpression`
- `TrimAudioDuration`
- `LoadAudio`
- `ComfyMathExpression`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LoadImage`
- `SetLatentNoiseMask`
- `GetImageSize`
- `LoraLoader` ★核心
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveStringMultiline`
- `LTXVImgToVideoInplace`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `Note`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **89%**（48/54）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`CreateVideo`、`SolidMask`、`LTXAVTextEncoderLoader`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVAudioVAEEncode`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`SaveVideo`、`TrimAudioDuration`、`LoadAudio`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LoadImage`、`SetLatentNoiseMask`、`GetImageSize`、`LoraLoader`、`TextGenerateLTX2Prompt`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`PrimitiveBoolean`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
