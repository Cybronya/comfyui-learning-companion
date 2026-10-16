---
key: 视频生成/图生视频/首尾帧 极速 LTX2.5 音画同出_2087530951474765826.json
name: 首尾帧 极速 LTX2.5 音画同出_2087530951474765826
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧 极速 LTX2.5 音画同出_2087530951474765826.json
hash: fac808d0592ecd06
coverage: 0.857143
learned_at: 2026-10-16 21:28:18
nodes: [LTXVConcatAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVAddGuide, ManualSigmas, LTXVAddGuide, LTXVEmptyLatentAudio, LTXVCropGuides, EmptyLTXVLatentVideo, LTXVConditioning, SamplerEulerAncestral, LTXVDualCFGGuider, RandomNoise, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, TextGenerateLTX2Prompt, ResizeImageMaskNode, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPLoader, UNETLoader, VAELoader, VAELoader, ResizeImageMaskNode, LTXVPreprocess, GetImageSize, CLIPLoader, ComfySwitchNode, PreviewAny, LoadImage, PrimitiveBoolean, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/首尾帧 极速 LTX2.5 音画同出_2087530951474765826.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/首尾帧 极速 LTX2.5 音画同出_2087530951474765826.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（42 个）：
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVAddGuide`
- `ManualSigmas`
- `LTXVAddGuide`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVCropGuides`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `SamplerEulerAncestral` ★核心
- `LTXVDualCFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `TextGenerateLTX2Prompt`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `GetImageSize`
- `CLIPLoader`
- `ComfySwitchNode`
- `PreviewAny`
- `LoadImage`
- `PrimitiveBoolean`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（36/42）

**有卡**：`LTXVConcatAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVAddGuide`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`SamplerEulerAncestral`、`LTXVDualCFGGuider`、`RandomNoise`、`CLIPTextEncode`、`LTXVPreprocess`、`TextGenerateLTX2Prompt`、`ResizeImageMaskNode`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`GetImageSize`、`LoadImage`、`PrimitiveBoolean`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、SamplerCustomAdvanced、SamplerEulerAncestral
