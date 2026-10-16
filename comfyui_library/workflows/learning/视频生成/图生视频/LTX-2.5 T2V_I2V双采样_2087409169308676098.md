---
key: 视频生成/图生视频/LTX-2.5 T2V_I2V双采样_2087409169308676098.json
name: LTX-2.5 T2V_I2V双采样_2087409169308676098
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.5 T2V_I2V双采样_2087409169308676098.json
hash: 03d436c4f6dc67bd
coverage: 0.753425
learned_at: 2026-10-16 21:27:31
nodes: [CLIPTextEncode, PrimitiveStringMultiline, CLIPLoader, CLIPLoader, DualCLIPLoader, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, ComfyNotNode, MarkdownNote, MarkdownNote, MarkdownNote, Note, MarkdownNote, MarkdownNote, LTXVConcatAVLatent, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, UNETLoader, LTXVDualCFGGuider, CreateVideo, LTXVLatentUpsampler, RandomNoise, VAEDecodeTiled, LTXVConditioning, PrimitiveFloat, PrimitiveFloat, LTXVPreprocess, ComfySwitchNode, ComfySwitchNode, CLIPTextEncode, PrimitiveInt, LTXVConcatAVLatent, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXFloatToInt, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, ComfyMathExpression, PrimitiveFloat, PrimitiveFloat, PrimitiveBoolean, VAELoader, VAELoader, LTXVAudioVAEDecode, CLIPLoader, LatentUpscaleModelLoader, ResolutionSelector, PreviewAny, LTXVDualCFGGuider, LTXVImgToVideoInplace, PrimitiveBoolean, SaveVideo, CreateVideo, SaveVideo, PreviewImage, PrimitiveStringMultiline, LoadImage, ComfyMathExpression, ComfyMathExpression, ResizeImageMaskNode, ManualSigmas, ManualSigmas, VAEDecodeTiled, RandomNoise, SeedGenerator, LTXVAudioVAEDecode, CFGGuider, Reroute, UNETLoader, LTXVImgToVideoInplace]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 121}
---

# 视频生成/图生视频/LTX-2.5 T2V_I2V双采样_2087409169308676098.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX-2.5 T2V_I2V双采样_2087409169308676098.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（73 个）：
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `CLIPLoader`
- `DualCLIPLoader`
- `TextGenerateLTX2Prompt`
- `TextGenerateLTX2Prompt`
- `ComfyNotNode`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Note`
- `MarkdownNote`
- `MarkdownNote`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `UNETLoader` ★核心
- `LTXVDualCFGGuider`
- `CreateVideo`
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `VAEDecodeTiled` ★核心
- `LTXVConditioning`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `LTXVPreprocess`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXFloatToInt`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveBoolean`
- `VAELoader`
- `VAELoader`
- `LTXVAudioVAEDecode` ★核心
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `ResolutionSelector`
- `PreviewAny`
- `LTXVDualCFGGuider`
- `LTXVImgToVideoInplace`
- `PrimitiveBoolean`
- `SaveVideo`
- `CreateVideo`
- `SaveVideo`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `LoadImage`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ResizeImageMaskNode`
- `ManualSigmas`
- `ManualSigmas`
- `VAEDecodeTiled` ★核心
- `RandomNoise`
- `SeedGenerator`
- `LTXVAudioVAEDecode` ★核心
- `CFGGuider`
- `Reroute`
- `UNETLoader` ★核心
- `LTXVImgToVideoInplace`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（55/73）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`DualCLIPLoader`、`TextGenerateLTX2Prompt`、`ComfyNotNode`、`LTXVConcatAVLatent`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`UNETLoader`、`LTXVDualCFGGuider`、`CreateVideo`、`LTXVLatentUpsampler`、`RandomNoise`、`VAEDecodeTiled`、`LTXVConditioning`、`LTXVPreprocess`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXFloatToInt`、`ManualSigmas`、`ComfyMathExpression`、`PrimitiveBoolean`、`VAELoader`、`LTXVAudioVAEDecode`、`LatentUpscaleModelLoader`、`ResolutionSelector`、`LTXVImgToVideoInplace`、`SaveVideo`、`LoadImage`、`ResizeImageMaskNode`、`SeedGenerator`、`CFGGuider`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
