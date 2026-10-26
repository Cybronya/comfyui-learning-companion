---
key: 数字人/数字人/ltx2.5 工作流全集 -1_2114542977581408258.json
name: ltx2.5 工作流全集 -1_2114542977581408258
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/ltx2.5 工作流全集 -1_2114542977581408258.json
hash: 06708f749cd71497
coverage: 0.982143
learned_at: 2026-10-26 22:10:37
nodes: [SamplerCustomAdvanced, UNETLoader, RandomNoise, LTXVDualCFGGuider, KSamplerSelect, KSamplerSelect, RandomNoise, LTXVSeparateAVLatent, LTXVLatentUpsampler, ManualSigmas, ManualSigmas, LTXVConcatAVLatent, ResizeImageMaskNode, LTXVPreprocess, CLIPTextEncode, LTXVConcatAVLatent, LoadImage, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, VHS_VideoCombine, CLIPLoader, LatentUpscaleModelLoader, VAELoader, VAELoader, LTXVAudioVAEDecode, VAEDecode, SimpleMath+, SimpleMath+, LTXVSeparateAVLatent, CLIPTextEncode, Int, Float, ComfyMathExpression, ResizeImageMaskNode, ResizeImageMaskNode, LTXVPreprocess, LTXVPreprocess, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, LTXVConditioning, LTXVAddGuide, LTXVDualCFGGuider, LTXVCropGuides, SamplerCustomAdvanced, LTXVAddGuide, LTXVCropGuides, ResolutionSelector, LoadAudio, TrimAudio, SolidMask, LTXVAudioVAEEncode, 1hew_AudioDuration, SetLatentNoiseMask, LoadImage, LoadImage, easy showAnything]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 数字人/数字人/ltx2.5 工作流全集 -1_2114542977581408258.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/ltx2.5 工作流全集 -1_2114542977581408258.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Other

**节点**（56 个）：
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `RandomNoise`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `ManualSigmas`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `LoadImage`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `VHS_VideoCombine`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `VAELoader`
- `VAELoader`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `SimpleMath+`
- `SimpleMath+`
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `Int`
- `Float`
- `ComfyMathExpression`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `LTXVAddGuide`
- `LTXVDualCFGGuider`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `LTXVAddGuide`
- `LTXVCropGuides`
- `ResolutionSelector`
- `LoadAudio`
- `TrimAudio`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `1hew_AudioDuration`
- `SetLatentNoiseMask`
- `LoadImage`
- `LoadImage`
- `easy showAnything`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **98%**（55/56）

**有卡**：`SamplerCustomAdvanced`、`UNETLoader`、`RandomNoise`、`LTXVDualCFGGuider`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`ManualSigmas`、`LTXVConcatAVLatent`、`ResizeImageMaskNode`、`LTXVPreprocess`、`CLIPTextEncode`、`LoadImage`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`VHS_VideoCombine`、`CLIPLoader`、`LatentUpscaleModelLoader`、`VAELoader`、`LTXVAudioVAEDecode`、`VAEDecode`、`SimpleMath+`、`Int`、`Float`、`ComfyMathExpression`、`LTXVImgToVideoInplace`、`LTXVConditioning`、`LTXVAddGuide`、`LTXVCropGuides`、`ResolutionSelector`、`LoadAudio`、`TrimAudio`、`SolidMask`、`LTXVAudioVAEEncode`、`1hew_AudioDuration`、`SetLatentNoiseMask`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
