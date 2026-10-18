---
key: 视频生成/图生视频/LTX-2.5 音频驱动数字人口播视频｜自然口型｜微表情｜动作同步_2095839296384229377.json
name: LTX-2.5 音频驱动数字人口播视频｜自然口型｜微表情｜动作同步_2095839296384229377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.5 音频驱动数字人口播视频｜自然口型｜微表情｜动作同步_2095839296384229377.json
hash: 7449c8f3d450f870
coverage: 0.882353
learned_at: 2026-10-17 01:09:23
nodes: [KSamplerSelect, ResizeImageMaskNode, ComfyMathExpression, ComfyMathExpression, LTXVImgToVideoInplace, PrimitiveInt, PrimitiveInt, VAELoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, LTXVDualCFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, LTXVLatentUpsampler, LTXVConcatAVLatent, ManualSigmas, LTXVDualCFGGuider, RandomNoise, LTXVSeparateAVLatent, CLIPTextEncode, CLIPTextEncode, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVPreprocess, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEEncode, LTXVConditioning, PrimitiveBoolean, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, EmptyLTXVLatentVideo, MarkdownNote, UNETLoader, VHS_VideoCombine, PrimitiveInt, ResolutionSelector, PrimitiveInt, LoadAudio, TrimAudioDuration, CR Text, LoadImage, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX-2.5 音频驱动数字人口播视频｜自然口型｜微表情｜动作同步_2095839296384229377.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX-2.5 音频驱动数字人口播视频｜自然口型｜微表情｜动作同步_2095839296384229377.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Other

**节点**（51 个）：
- `KSamplerSelect` ★核心
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVImgToVideoInplace`
- `PrimitiveInt`
- `PrimitiveInt`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `LTXVDualCFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVDualCFGGuider`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `LTXVConditioning`
- `PrimitiveBoolean`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `MarkdownNote`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `PrimitiveInt`
- `ResolutionSelector`
- `PrimitiveInt`
- `LoadAudio`
- `TrimAudioDuration`
- `CR Text`
- `LoadImage`
- `MarkdownNote`

## 知识

覆盖率 **88%**（45/51）

**有卡**：`KSamplerSelect`、`ResizeImageMaskNode`、`ComfyMathExpression`、`LTXVImgToVideoInplace`、`VAELoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`LTXVDualCFGGuider`、`RandomNoise`、`ManualSigmas`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LTXVPreprocess`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEEncode`、`LTXVConditioning`、`PrimitiveBoolean`、`EmptyLTXVLatentVideo`、`UNETLoader`、`VHS_VideoCombine`、`ResolutionSelector`、`LoadAudio`、`TrimAudioDuration`、`CR Text`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
