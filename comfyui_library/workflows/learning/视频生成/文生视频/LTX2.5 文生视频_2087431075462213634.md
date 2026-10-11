---
key: 视频生成/文生视频/LTX2.5 文生视频_2087431075462213634.json
name: LTX2.5 文生视频_2087431075462213634
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5 文生视频_2087431075462213634.json
hash: 9ecec983f48a47e8
coverage: 0.803571
learned_at: 2026-10-11 20:53:37
nodes: [MarkdownNote, MarkdownNote, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVSeparateAVLatent, LTXVDualCFGGuider, KSamplerSelect, ManualSigmas, LTXVConditioning, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, CreateVideo, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, LTXVConcatAVLatent, MarkdownNote, RandomNoise, ResizeImageMaskNode, LTXVPreprocess, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVImgToVideoInplace, ComfyMathExpression, ComfyMathExpression, SamplerCustomAdvanced, VAEDecodeTiled, LTXVSeparateAVLatent, CLIPTextEncode, CLIPTextEncode, VAELoader, VAELoader, LatentUpscaleModelLoader, UNETLoader, llama_cpp_model_loader, PrimitiveBoolean, llama_cpp_parameters, PreviewAny, RandomNoise, CLIPLoader, llama_cpp_instruct_adv, PrimitiveBoolean, LoadImage, MarkdownNote, ComfySwitchNode, ResolutionSelector, PrimitiveStringMultiline, PrimitiveInt, DisTorchPurgeVRAMV2, SaveVideo, LTXVAudioVAEDecode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5 文生视频_2087431075462213634.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5 文生视频_2087431075462213634.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（56 个）：
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `RandomNoise`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `llama_cpp_model_loader`
- `PrimitiveBoolean`
- `llama_cpp_parameters`
- `PreviewAny`
- `RandomNoise`
- `CLIPLoader`
- `llama_cpp_instruct_adv`
- `PrimitiveBoolean`
- `LoadImage`
- `MarkdownNote`
- `ComfySwitchNode`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `DisTorchPurgeVRAMV2`
- `SaveVideo`
- `LTXVAudioVAEDecode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（45/56）

**有卡**：`LTXVSeparateAVLatent`、`LTXVDualCFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`CreateVideo`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`CLIPTextEncode`、`VAELoader`、`LatentUpscaleModelLoader`、`UNETLoader`、`llama_cpp_model_loader`、`PrimitiveBoolean`、`llama_cpp_parameters`、`CLIPLoader`、`llama_cpp_instruct_adv`、`LoadImage`、`ResolutionSelector`、`DisTorchPurgeVRAMV2`、`SaveVideo`、`LTXVAudioVAEDecode`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
