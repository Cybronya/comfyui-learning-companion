---
key: 视频生成/图生视频/video_ltx2_3_i2v_kijai_three_stage_2041087454286979073.json
name: video_ltx2_3_i2v_kijai_three_stage_2041087454286979073.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2041087454286979073.json
hash: 26518d4262526f83
coverage: 0.519231
learned_at: 2026-10-15 22:36:17
nodes: [RandomNoise, KSamplerSelect, ManualSigmas, PrimitiveInt, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, LTXVPreprocess, SetNode, SetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, SetNode, SetNode, SetNode, PreviewImage, GetNode, GetNode, GetNode, LTXVImgToVideoInplace, GetNode, GetNode, GetNode, CFGGuider, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ResizeImagesByLongerEdge, GetNode, LTXVEmptyLatentAudio, LTXVConcatAVLatent, SetNode, GetNode, LoraLoader, SetNode, GetNode, LTXVCropGuides, LTXVSeparateAVLatent, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, CFGGuider, GetNode, GetNode, GetNode, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, GetNode, GetNode, LTXVAudioVAEDecode, VAEDecodeTiled, ComfyMathExpression, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, ImageResizeKJv2, LTXVImgToVideoInplace, SamplerCustomAdvanced, RandomNoise, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVLatentUpsampler, PrimitiveInt, PrimitiveInt, SDVN Load Image Url, UNETLoader, LTXVConditioning, SetNode, SetNode, GetNode, PathchSageAttentionKJ, CFGGuider, LTX2_NAG, GetNode, String, PrimitiveStringMultiline, PrimitiveInt, CLIPTextEncode]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 25, "lora_name": "gemma-3-12b-it-abliterated_heretic_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1, "width": 97}
---

# 视频生成/图生视频/video_ltx2_3_i2v_kijai_three_stage_2041087454286979073.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041087454286979073.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（104 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVPreprocess`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
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
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `ImageResizeKJv2`
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVLatentUpsampler` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `SDVN Load Image Url`
- `UNETLoader` ★核心
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `CFGGuider`
- `LTX2_NAG`
- `GetNode`
- `String`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心

**识别到的模式**：lora

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `lora_name` = `gemma-3-12b-it-abliterated_heretic_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **52%**（54/104）

**有卡**：`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`LTXVPreprocess`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`CFGGuider`、`CLIPTextEncode`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`ResizeImagesByLongerEdge`、`LTXVEmptyLatentAudio`、`LoraLoader`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`VHS_VideoCombine`、`VAELoaderKJ`、`DualCLIPLoader`、`ImageResizeKJv2`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`SDVN Load Image Url`、`UNETLoader`、`LTXVConditioning`、`PathchSageAttentionKJ`、`LTX2_NAG`、`String`

**用到的条目**：CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent、LTXVSeparateAVLatent
