---
key: 视频生成/图生视频/ltx2.5图文生视频_2111289590802903041.json
name: ltx2.5图文生视频_2111289590802903041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/ltx2.5图文生视频_2111289590802903041.json
hash: b4a581d0fa9fa7df
coverage: 0.84
learned_at: 2026-10-18 00:43:57
nodes: [TextGenerateLTX2Prompt, ComfySwitchNode, PreviewAny, LTXVConditioning, PrimitiveInt, PrimitiveInt, KSamplerSelect, RandomNoise, ManualSigmas, PrimitiveInt, LTXVDualCFGGuider, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LTXVConcatAVLatent, ResizeImageMaskNode, ComfyMathExpression, ComfyMathExpression, LTXVPreprocess, EmptyLTXVLatentVideo, LTXVLatentUpsampler, LTXVImgToVideoInplace, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, ManualSigmas, LTXVDualCFGGuider, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, CLIPTextEncode, UNETLoader, LatentUpscaleModelLoader, VAELoader, VAELoader, LoadImage, CLIPLoader, ComfyMathExpression, PrimitiveBoolean, MarkdownNote, PrimitiveStringMultiline, CLIPTextEncode, SaveVideo, ResolutionSelector, PrimitiveInt, PrimitiveBoolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/ltx2.5图文生视频_2111289590802903041.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/ltx2.5图文生视频_2111289590802903041.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（50 个）：
- `TextGenerateLTX2Prompt`
- `ComfySwitchNode`
- `PreviewAny`
- `LTXVConditioning`
- `PrimitiveInt`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ManualSigmas`
- `PrimitiveInt`
- `LTXVDualCFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `ComfyMathExpression`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LatentUpscaleModelLoader`
- `VAELoader`
- `VAELoader`
- `LoadImage`
- `CLIPLoader`
- `ComfyMathExpression`
- `PrimitiveBoolean`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `ResolutionSelector`
- `PrimitiveInt`
- `PrimitiveBoolean`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（42/50）

**有卡**：`TextGenerateLTX2Prompt`、`LTXVConditioning`、`KSamplerSelect`、`RandomNoise`、`ManualSigmas`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`ResizeImageMaskNode`、`ComfyMathExpression`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`CLIPTextEncode`、`UNETLoader`、`LatentUpscaleModelLoader`、`VAELoader`、`LoadImage`、`CLIPLoader`、`PrimitiveBoolean`、`SaveVideo`、`ResolutionSelector`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
