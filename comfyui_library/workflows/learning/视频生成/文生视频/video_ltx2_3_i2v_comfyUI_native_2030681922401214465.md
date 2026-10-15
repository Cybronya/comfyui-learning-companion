---
key: 视频生成/文生视频/video_ltx2_3_i2v_comfyUI_native_2030681922401214465.json
name: video_ltx2_3_i2v_comfyUI_native_2030681922401214465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/video_ltx2_3_i2v_comfyUI_native_2030681922401214465.json
hash: bb2e0ea053434015
coverage: 0.833333
learned_at: 2026-10-15 22:47:32
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, ComfyMathExpression, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVAudioVAEDecode, ComfyMathExpression, PrimitiveInt, PrimitiveBoolean, CLIPTextEncode, LTXVConditioning, LTXVConcatAVLatent, LTXVEmptyLatentAudio, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, CreateVideo, CLIPTextEncode, CFGGuider, VAEDecodeTiled, MarkdownNote, MarkdownNote, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, LoadImage, PrimitiveStringMultiline, PrimitiveInt, PrimitiveInt, PrimitiveInt, KSamplerSelect, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, Reroute, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXVAudioVAELoader, SaveVideo, DualCLIPLoader, CheckpointLoaderSimple]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/video_ltx2_3_i2v_comfyUI_native_2030681922401214465.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/video_ltx2_3_i2v_comfyUI_native_2030681922401214465.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXVAudioVAELoader`
- `SaveVideo`
- `DualCLIPLoader`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **83%**（40/48）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`PrimitiveBoolean`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`CreateVideo`、`VAEDecodeTiled`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LoadImage`、`LTXVLatentUpsampler`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LTXVAudioVAELoader`、`SaveVideo`、`DualCLIPLoader`、`CheckpointLoaderSimple`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
