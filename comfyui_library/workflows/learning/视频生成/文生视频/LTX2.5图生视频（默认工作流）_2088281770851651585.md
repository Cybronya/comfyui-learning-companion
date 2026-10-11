---
key: 视频生成/文生视频/LTX2.5图生视频（默认工作流）_2088281770851651585.json
name: LTX2.5图生视频（默认工作流）_2088281770851651585
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5图生视频（默认工作流）_2088281770851651585.json
hash: 804417eb08a42b42
coverage: 0.784314
learned_at: 2026-10-11 20:53:38
nodes: [KSamplerSelect, ComfyMathExpression, ComfyMathExpression, MarkdownNote, ResizeImageMaskNode, ComfyMathExpression, ComfyMathExpression, LTXVImgToVideoInplace, MarkdownNote, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, PrimitiveInt, UNETLoader, VAELoader, VAELoader, CLIPLoader, LatentUpscaleModelLoader, LTXVDualCFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, LTXVLatentUpsampler, LTXVConcatAVLatent, ManualSigmas, LTXVDualCFGGuider, RandomNoise, LTXVSeparateAVLatent, MarkdownNote, PrimitiveInt, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConcatAVLatent, CR Text, MarkdownNote, LTXVPreprocess, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, VHS_VideoCombine, CR Text, RH_LLMAPI_Pro_Node, PreviewAny, ResolutionSelector, LoadImage]
patterns: []
missing: [CR Text, CR Text]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.5图生视频（默认工作流）_2088281770851651585.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5图生视频（默认工作流）_2088281770851651585.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（51 个）：
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `ResizeImageMaskNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVImgToVideoInplace`
- `MarkdownNote`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `LTXVDualCFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVDualCFGGuider`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `MarkdownNote`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `CR Text`
- `MarkdownNote`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `CR Text`
- `RH_LLMAPI_Pro_Node`
- `PreviewAny`
- `ResolutionSelector`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（40/51）

**有卡**：`KSamplerSelect`、`ComfyMathExpression`、`ResizeImageMaskNode`、`LTXVImgToVideoInplace`、`PrimitiveBoolean`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LatentUpscaleModelLoader`、`LTXVDualCFGGuider`、`RandomNoise`、`ManualSigmas`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`CLIPTextEncode`、`LTXVConditioning`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`RH_LLMAPI_Pro_Node`、`ResolutionSelector`、`LoadImage`

**缺卡**（2）：`CR Text`、`CR Text`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
