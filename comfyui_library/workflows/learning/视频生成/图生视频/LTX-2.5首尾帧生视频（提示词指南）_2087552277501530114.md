---
key: 视频生成/图生视频/LTX-2.5首尾帧生视频（提示词指南）_2087552277501530114.json
name: LTX-2.5首尾帧生视频（提示词指南）_2087552277501530114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.5首尾帧生视频（提示词指南）_2087552277501530114.json
hash: d013017f96b5c545
coverage: 0.785714
learned_at: 2026-10-16 21:27:31
nodes: [PrimitiveFloat, PrimitiveFloat, LTXVAudioVAEDecode, CreateVideo, SaveVideo, ComfyMathExpression, PrimitiveFloat, PrimitiveFloat, CLIPTextEncode, CLIPTextEncode, VAELoader, VAELoader, LTXVPreprocess, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoadImage, LTXFloatToInt, CLIPLoader, MarkdownNote, VAEDecodeTiled, Int, RandomNoise, PreviewImage, PrimitiveStringMultiline, ResizeImageMaskNode, ResizeImageMaskNode, PrimitiveInt, LTXVAddGuide, DF_Get_image_size, LTXVDualCFGGuider, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConditioning, LTXVAddGuide, LTXVPreprocess, KSamplerSelect, SamplerCustomAdvanced, LTXVCropGuides, UNETLoader, PrimitiveStringMultiline, ManualSigmas]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 121}
---

# 视频生成/图生视频/LTX-2.5首尾帧生视频（提示词指南）_2087552277501530114.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX-2.5首尾帧生视频（提示词指南）_2087552277501530114.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `PrimitiveFloat`
- `PrimitiveFloat`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAELoader`
- `LTXVPreprocess`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoadImage`
- `LTXFloatToInt`
- `CLIPLoader`
- `MarkdownNote`
- `VAEDecodeTiled` ★核心
- `Int`
- `RandomNoise`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `LTXVAddGuide`
- `DF_Get_image_size`
- `LTXVDualCFGGuider`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `LTXVAddGuide`
- `LTXVPreprocess`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `ManualSigmas`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（33/42）

**有卡**：`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`ComfyMathExpression`、`CLIPTextEncode`、`VAELoader`、`LTXVPreprocess`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LoadImage`、`LTXFloatToInt`、`CLIPLoader`、`VAEDecodeTiled`、`Int`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVAddGuide`、`DF_Get_image_size`、`LTXVDualCFGGuider`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`UNETLoader`、`ManualSigmas`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider
