---
key: 数字人/数字人/LTX2.5，音频驱动口播数字人_2089890373689757697.json
name: LTX2.5，音频驱动口播数字人_2089890373689757697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.5，音频驱动口播数字人_2089890373689757697.json
hash: 5705fca27edb0228
coverage: 0.884615
learned_at: 2026-10-18 22:17:11
nodes: [KSamplerSelect, ComfyMathExpression, ComfyMathExpression, ResizeImageMaskNode, ComfyMathExpression, ComfyMathExpression, LTXVImgToVideoInplace, PrimitiveInt, PrimitiveInt, PrimitiveInt, UNETLoader, VAELoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, LTXVDualCFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, LTXVLatentUpsampler, LTXVConcatAVLatent, ManualSigmas, LTXVDualCFGGuider, RandomNoise, LTXVSeparateAVLatent, CLIPTextEncode, CLIPTextEncode, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVPreprocess, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, VHS_VideoCombine, EmptyLTXVLatentVideo, SetLatentNoiseMask, SolidMask, LTXVAudioVAEEncode, LTXVConditioning, TrimAudioDuration, MarkdownNote, MarkdownNote, LoadImage, PrimitiveBoolean, ComfyMathExpression, CR Text, ResolutionSelector, LoadAudio, PrimitiveInt, LoadImage]
patterns: []
missing: []
---

# 数字人/数字人/LTX2.5，音频驱动口播数字人_2089890373689757697.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.5，音频驱动口播数字人_2089890373689757697.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Other

**节点**（52 个）：
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVImgToVideoInplace`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `UNETLoader` ★核心
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
- `VHS_VideoCombine`
- `EmptyLTXVLatentVideo`
- `SetLatentNoiseMask`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `LTXVConditioning`
- `TrimAudioDuration`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `PrimitiveBoolean`
- `ComfyMathExpression`
- `CR Text`
- `ResolutionSelector`
- `LoadAudio`
- `PrimitiveInt`
- `LoadImage`

## 知识

覆盖率 **88%**（46/52）

**有卡**：`KSamplerSelect`、`ComfyMathExpression`、`ResizeImageMaskNode`、`LTXVImgToVideoInplace`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`LTXVDualCFGGuider`、`RandomNoise`、`ManualSigmas`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LTXVPreprocess`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`EmptyLTXVLatentVideo`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEEncode`、`LTXVConditioning`、`TrimAudioDuration`、`LoadImage`、`PrimitiveBoolean`、`CR Text`、`ResolutionSelector`、`LoadAudio`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
