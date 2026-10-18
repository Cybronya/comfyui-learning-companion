---
key: 视频生成/图生视频/极速图生视频音画同出   LTX2.5_2095738668177780738.json
name: 极速图生视频音画同出   LTX2.5_2095738668177780738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/极速图生视频音画同出   LTX2.5_2095738668177780738.json
hash: f04f8da032c72037
coverage: 0.843137
learned_at: 2026-10-17 01:10:38
nodes: [PrimitiveBoolean, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVSeparateAVLatent, LTXVDualCFGGuider, KSamplerSelect, ComfySwitchNode, ManualSigmas, LTXVConditioning, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, RandomNoise, ResizeImageMaskNode, LTXVPreprocess, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVImgToVideoInplace, ComfyMathExpression, ComfyMathExpression, PreviewAny, SamplerCustomAdvanced, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CLIPTextEncode, CLIPTextEncode, CLIPLoader, UNETLoader, VAELoader, VAELoader, LatentUpscaleModelLoader, CLIPLoader, MarkdownNote, VHS_VideoCombine, TextGenerateLTX2Prompt, PrimitiveBoolean, VHS_VideoCombine, ResolutionSelector, LoadImage, PrimitiveStringMultiline, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/极速图生视频音画同出   LTX2.5_2095738668177780738.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/极速图生视频音画同出   LTX2.5_2095738668177780738.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（51 个）：
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `ComfySwitchNode`
- `ManualSigmas`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PreviewAny`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `CLIPLoader`
- `MarkdownNote`
- `VHS_VideoCombine`
- `TextGenerateLTX2Prompt`
- `PrimitiveBoolean`
- `VHS_VideoCombine`
- `ResolutionSelector`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（43/51）

**有卡**：`PrimitiveBoolean`、`LTXVSeparateAVLatent`、`LTXVDualCFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`LatentUpscaleModelLoader`、`VHS_VideoCombine`、`TextGenerateLTX2Prompt`、`ResolutionSelector`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
