---
key: 视频生成/图生视频/LTX2.3声音+图片（MV 音乐数字人）_2033338918136975362.json
name: LTX2.3声音+图片（MV 音乐数字人）_2033338918136975362.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3声音+图片（MV 音乐数字人）_2033338918136975362.json
hash: e8c34438512332e4
coverage: 0.890625
learned_at: 2026-10-15 22:35:39
nodes: [LoraLoaderModelOnly, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LoadImage, ManualSigmas, KSamplerSelect, LTXVCropGuides, CFGGuider, RandomNoise, ResizeImageMaskNode, LTXVPreprocess, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, PrimitiveInt, ResizeImagesByLongerEdge, ComfyMathExpression, SolidMask, TrimAudioDuration, LTXVConditioning, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVAudioVAEEncode, SetLatentNoiseMask, easy anythingIndexSwitch, LTXVConcatAVLatent, SamplerCustomAdvanced, ComfyMathExpression, ManualSigmas, KSamplerSelect, CFGGuider, LatentUpscaleModelLoader, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVImgToVideoInplace, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, RIFEInterpolation, VAEDecodeTiled, GetNode, GetNode, PlaySound|pysssss, PlaySound|pysssss, PrimitiveBoolean, INTConstant, SetNode, SetNode, INTConstant, INTConstant, ComfyMathExpression, PlaySound|pysssss, UNETLoader, easy showAnything, VHS_VideoCombine, CLIPTextEncode, Text Multiline, PathchSageAttentionKJ, LoadAudio, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3声音+图片（MV 音乐数字人）_2033338918136975362.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033338918136975362.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（64 个）：
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LoadImage`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `CFGGuider`
- `RandomNoise`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveInt`
- `ResizeImagesByLongerEdge`
- `ComfyMathExpression`
- `SolidMask`
- `TrimAudioDuration`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `easy anythingIndexSwitch`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LatentUpscaleModelLoader`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `RIFEInterpolation`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `PrimitiveBoolean`
- `INTConstant`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `ComfyMathExpression`
- `PlaySound|pysssss`
- `UNETLoader` ★核心
- `easy showAnything`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `Text Multiline`
- `PathchSageAttentionKJ`
- `LoadAudio`
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（57/64）

**有卡**：`LoraLoaderModelOnly`、`VAELoaderKJ`、`DualCLIPLoader`、`LoadImage`、`ManualSigmas`、`KSamplerSelect`、`LTXVCropGuides`、`CFGGuider`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`、`ComfyMathExpression`、`ResizeImagesByLongerEdge`、`SolidMask`、`TrimAudioDuration`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`easy anythingIndexSwitch`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LatentUpscaleModelLoader`、`LTXVAudioVAEDecode`、`RIFEInterpolation`、`VAEDecodeTiled`、`PlaySound|pysssss`、`PrimitiveBoolean`、`INTConstant`、`UNETLoader`、`VHS_VideoCombine`、`CLIPTextEncode`、`Text Multiline`、`PathchSageAttentionKJ`、`LoadAudio`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
