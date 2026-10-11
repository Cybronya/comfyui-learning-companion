---
key: 视频生成/文生视频/LTX2.5 首尾帧图生视频+全节点注释_2087729834381373441.json
name: LTX2.5 首尾帧图生视频+全节点注释_2087729834381373441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5 首尾帧图生视频+全节点注释_2087729834381373441.json
hash: 58a1eb7fe598be76
coverage: 0.434211
learned_at: 2026-10-11 20:53:38
nodes: [SamplerEulerAncestral, LTXVCropGuides, VAEDecodeTiled, LTXVAudioVAEDecode, ComfyMathExpression, ComfyMathExpression, CLIPTextEncode, UNETLoader, VAELoader, VAELoader, CLIPLoader, LTXVSeparateAVLatent, ManualSigmas, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConditioning, LTXVAddGuide, LTXVAddGuide, PrimitiveInt, PrimitiveInt, PrimitiveInt, ResizeImageMaskNode, ResizeImageMaskNode, LTXVPreprocess, VHS_VideoCombine, RandomNoise, LTXVDualCFGGuider, SamplerCustomAdvanced, GetImageSize, LTXVPreprocess, PrimitiveInt, CLIPTextEncode, CR Text, LoadImage, LoadImage, CR Text, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, Note]
patterns: []
missing: [CR Text, CR Text]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.5 首尾帧图生视频+全节点注释_2087729834381373441.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5 首尾帧图生视频+全节点注释_2087729834381373441.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（76 个）：
- `SamplerEulerAncestral` ★核心
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `LTXVAddGuide`
- `LTXVAddGuide`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `VHS_VideoCombine`
- `RandomNoise`
- `LTXVDualCFGGuider`
- `SamplerCustomAdvanced` ★核心
- `GetImageSize`
- `LTXVPreprocess`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `CR Text`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `Note`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **43%**（33/76）

**有卡**：`SamplerEulerAncestral`、`LTXVCropGuides`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ComfyMathExpression`、`CLIPTextEncode`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LTXVSeparateAVLatent`、`ManualSigmas`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LTXVAddGuide`、`ResizeImageMaskNode`、`LTXVPreprocess`、`VHS_VideoCombine`、`RandomNoise`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`GetImageSize`、`LoadImage`

**缺卡**（2）：`CR Text`、`CR Text`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SamplerCustomAdvanced、SamplerEulerAncestral、LTXVDualCFGGuider

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
