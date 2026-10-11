---
key: 视频生成/文生视频/ltx2.3文生视频+局部重绘_2053834955712671746.json
name: ltx2.3文生视频+局部重绘_2053834955712671746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3文生视频+局部重绘_2053834955712671746.json
hash: f453576eafa1c4f8
coverage: 0.517544
learned_at: 2026-10-11 19:49:44
nodes: [PrimitiveInt, PrimitiveInt, SetNode, SetNode, SetNode, VHS_VideoCombine, GetNode, ComfyMathExpression, SetNode, GetNode, GetNode, CLIPTextEncode, GetNode, ComfyMathExpression, GetNode, GetNode, ComfyMathExpression, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, SetNode, LTXVConditioning, GetNode, GetNode, LTXVEmptyLatentAudio, GetNode, GetNode, ComfyMathExpression, GetNode, GetNode, LTXVConcatAVLatent, ComfyMathExpression, ComfyMathExpression, GetNode, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, BlockifyMask, EmptyLTXVLatentVideo, LTXVAddGuideMulti, GetNode, SetNode, SetNode, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, CFGGuider, RandomNoise, SamplerCustomAdvanced, GetNode, LTXVSeparateAVLatent, VAEDecodeTiled, GetNode, GetNode, GetNode, LTXVLatentUpsampler, LTXVAddGuideMulti, LTXVSeparateAVLatent, GetNode, KSamplerSelect, ManualSigmas, BasicScheduler, RandomNoise, SamplerCustomAdvanced, GetNode, GetNode, CFGGuider, GetNode, LTXVCropGuides, SAM3_TrackToMask, GrowMaskWithBlur, MaskToImage, LTXVPreprocess, SetNode, GetNode, GetImageRangeFromBatch, MarkdownNote, MarkdownNote, VHS_LoadVideo, SetNode, SetNode, SAM3_VideoTrack, SAM3_Detect, SAM3_TrackPreview, PreviewImage, DrawMaskOnImage, VHS_VideoCombine, VHS_VideoCombine, PrimitiveInt, PrimitiveInt, SetNode, SetNode, SetNode, ComfyMathExpression, GetNode, GetNode, DrawMaskOnImage, CLIPTextEncode, VHS_VideoInfo, SetNode, ImageResizeKJv2, CheckpointLoaderSimple, GetNode, UNETLoader, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveStringMultiline, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/ltx2.3文生视频+局部重绘_2053834955712671746.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.3文生视频+局部重绘_2053834955712671746.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（114 个）：
- `PrimitiveInt`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `BlockifyMask`
- `EmptyLTXVLatentVideo`
- `LTXVAddGuideMulti`
- `GetNode`
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVAddGuideMulti`
- `LTXVSeparateAVLatent`
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `BasicScheduler`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `LTXVCropGuides`
- `SAM3_TrackToMask`
- `GrowMaskWithBlur`
- `MaskToImage`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `MarkdownNote`
- `MarkdownNote`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `SAM3_VideoTrack`
- `SAM3_Detect`
- `SAM3_TrackPreview`
- `PreviewImage`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `DrawMaskOnImage`
- `CLIPTextEncode` ★核心
- `VHS_VideoInfo`
- `SetNode`
- `ImageResizeKJv2`
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `UNETLoader` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **52%**（59/114）

**有卡**：`VHS_VideoCombine`、`ComfyMathExpression`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`BlockifyMask`、`EmptyLTXVLatentVideo`、`LTXVAddGuideMulti`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVLatentUpsampler`、`BasicScheduler`、`LTXVCropGuides`、`SAM3_TrackToMask`、`GrowMaskWithBlur`、`MaskToImage`、`LTXVPreprocess`、`GetImageRangeFromBatch`、`VHS_LoadVideo`、`SAM3_VideoTrack`、`SAM3_Detect`、`SAM3_TrackPreview`、`DrawMaskOnImage`、`VHS_VideoInfo`、`ImageResizeKJv2`、`CheckpointLoaderSimple`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
