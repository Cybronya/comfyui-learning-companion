---
key: 视频生成/文生视频/LTX2.5 图生视频_2087377269655425025.json
name: LTX2.5 图生视频_2087377269655425025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5 图生视频_2087377269655425025.json
hash: 60aeb776a602b986
coverage: 0.803571
learned_at: 2026-10-15 22:45:16
nodes: [MarkdownNote, MarkdownNote, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVSeparateAVLatent, LTXVDualCFGGuider, KSamplerSelect, ManualSigmas, LTXVConditioning, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, CreateVideo, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, LTXVConcatAVLatent, MarkdownNote, RandomNoise, ResizeImageMaskNode, LTXVPreprocess, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVImgToVideoInplace, ComfyMathExpression, ComfyMathExpression, MarkdownNote, SamplerCustomAdvanced, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CLIPTextEncode, CLIPTextEncode, VAELoader, VAELoader, LatentUpscaleModelLoader, UNETLoader, llama_cpp_model_loader, PrimitiveBoolean, llama_cpp_parameters, LoadImage, PreviewAny, PrimitiveStringMultiline, PrimitiveInt, SaveVideo, PrimitiveBoolean, RandomNoise, CLIPLoader, llama_cpp_instruct_adv, ComfySwitchNode, DisTorchPurgeVRAMV2, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5 图生视频_2087377269655425025.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5 图生视频_2087377269655425025.json`

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
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `llama_cpp_model_loader`
- `PrimitiveBoolean`
- `llama_cpp_parameters`
- `LoadImage`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `SaveVideo`
- `PrimitiveBoolean`
- `RandomNoise`
- `CLIPLoader`
- `llama_cpp_instruct_adv`
- `ComfySwitchNode`
- `DisTorchPurgeVRAMV2`
- `ResolutionSelector`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（45/56）

**有卡**：`LTXVSeparateAVLatent`、`LTXVDualCFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`CreateVideo`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`VAELoader`、`LatentUpscaleModelLoader`、`UNETLoader`、`llama_cpp_model_loader`、`PrimitiveBoolean`、`llama_cpp_parameters`、`LoadImage`、`SaveVideo`、`CLIPLoader`、`llama_cpp_instruct_adv`、`DisTorchPurgeVRAMV2`、`ResolutionSelector`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
