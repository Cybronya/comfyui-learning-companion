---
key: 视频生成/文生视频/Ltx2.5 图_文生视频-双采高清-蒸馏加速_2087683911039143937.json
name: Ltx2.5 图_文生视频-双采高清-蒸馏加速_2087683911039143937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Ltx2.5 图_文生视频-双采高清-蒸馏加速_2087683911039143937.json
hash: 0cce9529077dc66e
coverage: 0.785714
learned_at: 2026-10-11 20:53:39
nodes: [LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, LTXVConcatAVLatent, LTXVImgToVideoInplace, LTXVLatentUpsampler, ComfyMathExpression, ComfyMathExpression, CLIPTextEncode, CLIPTextEncode, PrimitiveBoolean, CLIPLoader, TextGenerateLTX2Prompt, ComfySwitchNode, PreviewAny, ResizeImageMaskNode, PrimitiveInt, PrimitiveInt, LTXVPreprocess, LTXVConditioning, SamplerCustomAdvanced, RandomNoise, KSamplerSelect, LTXVSeparateAVLatent, RandomNoise, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVConcatAVLatent, LTXVDualCFGGuider, LTXVSeparateAVLatent, LatentUpscaleModelLoader, UNETLoader, CLIPLoader, VAELoader, VAELoader, LTXVImgToVideoInplace, PurgeVRAM_UTK, PrimitiveStringMultiline, LoadImage, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, MarkdownNote, Note Plus (mtb), MarkdownNote, SaveVideo, CreateVideo, MarkdownNote, MarkdownNote, LTXVDualCFGGuider, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, ManualSigmas, ResolutionSelector]
patterns: []
missing: [Note Plus (mtb)]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Ltx2.5 图_文生视频-双采高清-蒸馏加速_2087683911039143937.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Ltx2.5 图_文生视频-双采高清-蒸馏加速_2087683911039143937.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（56 个）：
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveBoolean`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `ComfySwitchNode`
- `PreviewAny`
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVPreprocess`
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVConcatAVLatent`
- `LTXVDualCFGGuider`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LTXVImgToVideoInplace`
- `PurgeVRAM_UTK`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `MarkdownNote`
- `Note Plus (mtb)`
- `MarkdownNote`
- `SaveVideo`
- `CreateVideo`
- `MarkdownNote`
- `MarkdownNote`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `ManualSigmas`
- `ResolutionSelector`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（44/56）

**有卡**：`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`CLIPTextEncode`、`PrimitiveBoolean`、`CLIPLoader`、`TextGenerateLTX2Prompt`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVConditioning`、`SamplerCustomAdvanced`、`RandomNoise`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVDualCFGGuider`、`LatentUpscaleModelLoader`、`UNETLoader`、`VAELoader`、`PurgeVRAM_UTK`、`LoadImage`、`SaveVideo`、`CreateVideo`、`ManualSigmas`、`ResolutionSelector`

**缺卡**（1）：`Note Plus (mtb)`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
