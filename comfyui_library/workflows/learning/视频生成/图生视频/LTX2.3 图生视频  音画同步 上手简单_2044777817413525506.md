---
key: 视频生成/图生视频/LTX2.3 图生视频  音画同步 上手简单_2044777817413525506.json
name: LTX2.3 图生视频  音画同步 上手简单_2044777817413525506.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2044777817413525506.json
hash: ff597be91a52eec0
coverage: 0.660714
learned_at: 2026-10-15 22:36:41
nodes: [GetNode, LTXVSeparateAVLatent, VAELoader, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, SetNode, VAELoaderKJ, BasicScheduler, SetNode, SetNode, StringFunction|pysssss, VAELoaderKJ, DualCLIPLoader, GetNode, GetNode, AILab_QwenVL_Advanced, ImageResizeKJv2, LayerUtility: If , LayerUtility: BooleanOperatorV2, Int, JjkText, PathchSageAttentionKJ, KSamplerSelect, LayerUtility: NumberCalculatorV2, SimpleMath+, PrimitiveStringMultiline, JoinStrings, EmptyLTXVLatentVideo, ModelSamplingSD3, UNETLoader, LTX2SamplingPreviewOverride, ShowText|pysssss, PrimitiveInt, PrimitiveInt, LoadImage, easy positive, CLIPTextEncode, CLIPTextEncode, LTX2_NAG, LTXVPreprocess, SamplerCustom, SetNode, VAEDecode, LTXVConcatAVLatent, LTXVImgToVideoInplaceKJ, LTXVAudioVAEDecode, GetNode, SetNode, GetNode, DF_Int_to_Float, GetNode, GetNode, Note, VHS_VideoCombine, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 305}
---

# 视频生成/图生视频/LTX2.3 图生视频  音画同步 上手简单_2044777817413525506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044777817413525506.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（56 个）：
- `GetNode`
- `LTXVSeparateAVLatent`
- `VAELoader`
- `LTXVConditioning`
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `VAELoaderKJ`
- `BasicScheduler`
- `SetNode`
- `SetNode`
- `StringFunction|pysssss`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `GetNode`
- `GetNode`
- `AILab_QwenVL_Advanced`
- `ImageResizeKJv2`
- `LayerUtility: If `
- `LayerUtility: BooleanOperatorV2`
- `Int`
- `JjkText`
- `PathchSageAttentionKJ`
- `KSamplerSelect` ★核心
- `LayerUtility: NumberCalculatorV2`
- `SimpleMath+`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `EmptyLTXVLatentVideo`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LTX2SamplingPreviewOverride`
- `ShowText|pysssss`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `easy positive`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `LTXVPreprocess`
- `SamplerCustom` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplaceKJ`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `DF_Int_to_Float`
- `GetNode`
- `GetNode`
- `Note`
- `VHS_VideoCombine`
- `PrimitiveInt`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **66%**（37/56）

**有卡**：`LTXVSeparateAVLatent`、`VAELoader`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`VAELoaderKJ`、`BasicScheduler`、`StringFunction|pysssss`、`DualCLIPLoader`、`AILab_QwenVL_Advanced`、`ImageResizeKJv2`、`LayerUtility: If `、`LayerUtility: BooleanOperatorV2`、`Int`、`PathchSageAttentionKJ`、`KSamplerSelect`、`LayerUtility: NumberCalculatorV2`、`SimpleMath+`、`JoinStrings`、`EmptyLTXVLatentVideo`、`ModelSamplingSD3`、`UNETLoader`、`LTX2SamplingPreviewOverride`、`LoadImage`、`easy positive`、`CLIPTextEncode`、`LTX2_NAG`、`LTXVPreprocess`、`SamplerCustom`、`VAEDecode`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplaceKJ`、`LTXVAudioVAEDecode`、`DF_Int_to_Float`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
