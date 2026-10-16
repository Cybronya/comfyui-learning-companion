---
key: 视频生成/图生视频/LTX2.3--高动态图生视频_2041388395624140802.json
name: LTX2.3--高动态图生视频_2041388395624140802.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2041388395624140802.json
hash: 2be54138cd129f8d
coverage: 0.52381
learned_at: 2026-10-15 22:36:19
nodes: [RandomNoise, KSamplerSelect, ManualSigmas, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, LTXVPreprocess, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, SetNode, MarkdownNote, MarkdownNote, SetNode, PreviewImage, LTXVConditioning, GetNode, LTXVImgToVideoInplace, GetNode, GetNode, GetNode, GetNode, CFGGuider, CLIPTextEncode, ComfyMathExpression, CLIPTextEncode, ComfyMathExpression, ResizeImagesByLongerEdge, GetNode, LTXVEmptyLatentAudio, LTXVConcatAVLatent, SetNode, GetNode, LoraLoader, SetNode, GetNode, LTXVCropGuides, LTXVSeparateAVLatent, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, CFGGuider, GetNode, GetNode, GetNode, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, GetNode, GetNode, VAEDecodeTiled, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, UNETLoader, LTXVImgToVideoInplace, SamplerCustomAdvanced, RandomNoise, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVLatentUpsampler, ManualSigmas, SetNode, Note, Note, Note, Note, LTXVAudioVAEDecode, VHS_VideoCombine, LoadImage, ImageResizeKJv2, EmptyLTXVLatentVideo, Int, Int, Int, Int, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, ComfyMathExpression, ComfyMathExpression, PrimitiveStringMultiline]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 25, "lora_name": "gemma-3-12b-it-abliterated_heretic_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1, "width": 97}
---

# 视频生成/图生视频/LTX2.3--高动态图生视频_2041388395624140802.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041388395624140802.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（105 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVPreprocess`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `PreviewImage`
- `LTXVConditioning`
- `GetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `LoraLoader` ★核心
- `SetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVLatentUpsampler` ★核心
- `ManualSigmas`
- `SetNode`
- `Note`
- `Note`
- `Note`
- `Note`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `ImageResizeKJv2`
- `EmptyLTXVLatentVideo`
- `Int`
- `Int`
- `Int`
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveStringMultiline`

**识别到的模式**：lora

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `lora_name` = `gemma-3-12b-it-abliterated_heretic_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **52%**（55/105）

**有卡**：`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`LTXVPreprocess`、`LTXVConcatAVLatent`、`LTXVConditioning`、`LTXVImgToVideoInplace`、`CFGGuider`、`CLIPTextEncode`、`ComfyMathExpression`、`ResizeImagesByLongerEdge`、`LTXVEmptyLatentAudio`、`LoraLoader`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`VAELoaderKJ`、`DualCLIPLoader`、`UNETLoader`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`LoadImage`、`ImageResizeKJv2`、`EmptyLTXVLatentVideo`、`Int`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
