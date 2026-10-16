---
key: 视频生成/图生视频/LTX2.5图生视频 -自动扩写提示词-高质量直出1K_2087739505318129665.json
name: LTX2.5图生视频 -自动扩写提示词-高质量直出1K_2087739505318129665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频 -自动扩写提示词-高质量直出1K_2087739505318129665.json
hash: 550b6a6885c406f3
coverage: 0.862745
learned_at: 2026-10-16 21:27:36
nodes: [PrimitiveInt, PrimitiveInt, LTXVSeparateAVLatent, LTXVDualCFGGuider, KSamplerSelect, ManualSigmas, LTXVConditioning, LTXVDualCFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, RandomNoise, LTXVConcatAVLatent, RandomNoise, ResizeImageMaskNode, LTXVPreprocess, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVImgToVideoInplace, ComfyMathExpression, ComfyMathExpression, SamplerCustomAdvanced, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVAudioVAEDecode, UNETLoader, VAELoader, VAELoader, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, SaveVideo, MarkdownNote, CreateVideo, CLIPTextEncode, CLIPTextEncode, LatentUpscaleModelLoader, CLIPLoader, MarkdownNote, LoadImage, CR Prompt Text, ShellAgentPluginOutputText, easy showAnything, RH_LLMAPI_Pro_Node, ResolutionSelector, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5图生视频 -自动扩写提示词-高质量直出1K_2087739505318129665.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5图生视频 -自动扩写提示词-高质量直出1K_2087739505318129665.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（51 个）：
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
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `SaveVideo`
- `MarkdownNote`
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LatentUpscaleModelLoader`
- `CLIPLoader`
- `MarkdownNote`
- `LoadImage`
- `CR Prompt Text`
- `ShellAgentPluginOutputText`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `ResolutionSelector`
- `CR Prompt Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（44/51）

**有卡**：`LTXVSeparateAVLatent`、`LTXVDualCFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`UNETLoader`、`VAELoader`、`PrimitiveBoolean`、`SaveVideo`、`CreateVideo`、`CLIPTextEncode`、`LatentUpscaleModelLoader`、`CLIPLoader`、`LoadImage`、`CR Prompt Text`、`ShellAgentPluginOutputText`、`RH_LLMAPI_Pro_Node`、`ResolutionSelector`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
