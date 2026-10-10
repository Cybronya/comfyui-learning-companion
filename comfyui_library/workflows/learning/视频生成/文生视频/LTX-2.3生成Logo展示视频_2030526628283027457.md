---
key: 视频生成/文生视频/LTX-2.3生成Logo展示视频_2030526628283027457.json
name: LTX-2.3生成Logo展示视频_2030526628283027457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3生成Logo展示视频_2030526628283027457.json
hash: 4ec522fbb81e8f1f
coverage: 0.769231
learned_at: 2026-10-11 03:16:45
nodes: [LTXVConcatAVLatent, LTXVAudioVAELoader, KSamplerSelect, ManualSigmas, CheckpointLoaderSimple, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LoraLoaderModelOnly, ResizeImagesByLongerEdge, LTXVLatentUpsampler, KSamplerSelect, Reroute, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVAudioVAEDecode, CLIPTextEncode, LTXVConditioning, LTXVConcatAVLatent, LTXVEmptyLatentAudio, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LatentUpscaleModelLoader, CLIPTextEncode, CFGGuider, VAEDecodeTiled, MarkdownNote, CreateVideo, SaveVideo, MarkdownNote, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXAVTextEncoderLoader, PrimitiveBoolean, CR Text Replace, CR Text, LoadImage, RandomNoise, RandomNoise, ResizeImageMaskNode, LTXVPreprocess, LTXVImgToVideoInplace, PrimitiveStringMultiline, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, Label (rgthree), Label (rgthree)]
patterns: []
missing: [CR Text, CR Text Replace, Label (rgthree), Label (rgthree)]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX-2.3生成Logo展示视频_2030526628283027457.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3生成Logo展示视频_2030526628283027457.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `LTXVConcatAVLatent`
- `LTXVAudioVAELoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CheckpointLoaderSimple` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LoraLoaderModelOnly` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVLatentUpsampler` ★核心
- `KSamplerSelect` ★核心
- `Reroute`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `MarkdownNote`
- `CreateVideo`
- `SaveVideo`
- `MarkdownNote`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXAVTextEncoderLoader`
- `PrimitiveBoolean`
- `CR Text Replace`
- `CR Text`
- `LoadImage`
- `RandomNoise`
- `RandomNoise`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `Label (rgthree)`
- `Label (rgthree)`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（40/52）

**有卡**：`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`KSamplerSelect`、`ManualSigmas`、`CheckpointLoaderSimple`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`ResizeImagesByLongerEdge`、`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`VAEDecodeTiled`、`CreateVideo`、`SaveVideo`、`ComfyMathExpression`、`LTXAVTextEncoderLoader`、`PrimitiveBoolean`、`LoadImage`、`RandomNoise`、`ResizeImageMaskNode`、`LTXVPreprocess`

**缺卡**（4）：`CR Text`、`CR Text Replace`、`Label (rgthree)`、`Label (rgthree)`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
