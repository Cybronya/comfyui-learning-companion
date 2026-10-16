---
key: 视频生成/图生视频/LTX2.5首尾帧-自动扩写提示词-高质量直出1K_2087739429011148802.json
name: LTX2.5首尾帧-自动扩写提示词-高质量直出1K_2087739429011148802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧-自动扩写提示词-高质量直出1K_2087739429011148802.json
hash: c10b29a272a81a6d
coverage: 0.878049
learned_at: 2026-10-16 21:27:37
nodes: [VAEDecodeTiled, LTXVAudioVAEDecode, ManualSigmas, LTXVAddGuide, LTXVEmptyLatentAudio, LTXVCropGuides, LTXVConditioning, SamplerEulerAncestral, LTXVDualCFGGuider, RandomNoise, CLIPTextEncode, CLIPTextEncode, SamplerCustomAdvanced, UNETLoader, VAELoader, PrimitiveInt, MarkdownNote, CreateVideo, SaveVideo, CLIPLoader, VAELoader, ComfyMathExpression, ComfyMathExpression, LTXVAddGuide, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVPreprocess, LTXVPreprocess, PrimitiveInt, EmptyLTXVLatentVideo, MarkdownNote, CR Prompt Text, ResolutionSelector, CR Prompt Text, RH_LLMAPI_Pro_Node, ShellAgentPluginOutputText, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5首尾帧-自动扩写提示词-高质量直出1K_2087739429011148802.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧-自动扩写提示词-高质量直出1K_2087739429011148802.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ManualSigmas`
- `LTXVAddGuide`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVCropGuides`
- `LTXVConditioning`
- `SamplerEulerAncestral` ★核心
- `LTXVDualCFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `PrimitiveInt`
- `MarkdownNote`
- `CreateVideo`
- `SaveVideo`
- `CLIPLoader`
- `VAELoader`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVAddGuide`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `PrimitiveInt`
- `EmptyLTXVLatentVideo`
- `MarkdownNote`
- `CR Prompt Text`
- `ResolutionSelector`
- `CR Prompt Text`
- `RH_LLMAPI_Pro_Node`
- `ShellAgentPluginOutputText`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（36/41）

**有卡**：`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ManualSigmas`、`LTXVAddGuide`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`LTXVConditioning`、`SamplerEulerAncestral`、`LTXVDualCFGGuider`、`RandomNoise`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`UNETLoader`、`VAELoader`、`CreateVideo`、`SaveVideo`、`CLIPLoader`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`CR Prompt Text`、`ResolutionSelector`、`RH_LLMAPI_Pro_Node`、`ShellAgentPluginOutputText`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、SamplerEulerAncestral
