---
key: 视频生成/图生视频/Ltx2.5图生视频-极速版-高质量-自动扩写提示词_2089690744842969089.json
name: Ltx2.5图生视频-极速版-高质量-自动扩写提示词_2089690744842969089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.5图生视频-极速版-高质量-自动扩写提示词_2089690744842969089.json
hash: 1d4c6a99d27e1360
coverage: 0.870968
learned_at: 2026-10-16 22:02:01
nodes: [CLIPTextEncode, CLIPTextEncode, EmptyLTXVLatentVideo, LTXVConcatAVLatent, LTXVImgToVideoInplace, PreviewAny, ResizeImageMaskNode, LTXVDualCFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, SaveVideo, ComfyMathExpression, LTXVEmptyLatentAudio, LTXVConditioning, CreateVideo, ResolutionSelector, LTXVAudioVAEDecode, MarkdownNote, UNETLoader, VAELoader, VAELoader, CLIPLoader, LoadImage, TextGenerateLTX2Prompt, CLIPLoader, PrimitiveStringMultiline, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 97}
---

# 视频生成/图生视频/Ltx2.5图生视频-极速版-高质量-自动扩写提示词_2089690744842969089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Ltx2.5图生视频-极速版-高质量-自动扩写提示词_2089690744842969089.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（31 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `PreviewAny`
- `ResizeImageMaskNode`
- `LTXVDualCFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `SaveVideo`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `CreateVideo`
- `ResolutionSelector`
- `LTXVAudioVAEDecode` ★核心
- `MarkdownNote`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LoadImage`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`ResizeImageMaskNode`、`LTXVDualCFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`SaveVideo`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`CreateVideo`、`ResolutionSelector`、`LTXVAudioVAEDecode`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LoadImage`、`TextGenerateLTX2Prompt`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
