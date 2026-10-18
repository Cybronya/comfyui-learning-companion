---
key: 视频生成/图生视频/LTX2.3 双人对话 音画同步KJ优化版 图生视频_2081698407059644417.json
name: LTX2.3 双人对话 音画同步KJ优化版 图生视频_2081698407059644417.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 双人对话 音画同步KJ优化版 图生视频_2081698407059644417.json
hash: 991eabe4661bb053
coverage: 0.678571
learned_at: 2026-10-15 22:42:24
nodes: [GetNode, VAELoader, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, SetNode, VAELoaderKJ, BasicScheduler, SetNode, SetNode, StringFunction|pysssss, VAELoaderKJ, DualCLIPLoader, GetNode, GetNode, AILab_QwenVL_Advanced, ImageResizeKJv2, LayerUtility: If , LayerUtility: BooleanOperatorV2, PathchSageAttentionKJ, KSamplerSelect, LayerUtility: NumberCalculatorV2, SimpleMath+, PrimitiveStringMultiline, JoinStrings, EmptyLTXVLatentVideo, ModelSamplingSD3, UNETLoader, ShowText|pysssss, PrimitiveInt, PrimitiveInt, LTX2_NAG, LTXVPreprocess, SamplerCustom, SetNode, VAEDecode, LTXVConcatAVLatent, LTXVAudioVAEDecode, SetNode, GetNode, DF_Int_to_Float, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, JjkText, VHS_VideoCombine, Int, PrimitiveInt, LTXVImgToVideoInplaceKJ, GetNode, LTXVSeparateAVLatent, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, LoadImage, easy positive]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 305}
---

# 视频生成/图生视频/LTX2.3 双人对话 音画同步KJ优化版 图生视频_2081698407059644417.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2081698407059644417.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（56 个）：
- `GetNode`
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
- `PathchSageAttentionKJ`
- `KSamplerSelect` ★核心
- `LayerUtility: NumberCalculatorV2`
- `SimpleMath+`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `EmptyLTXVLatentVideo`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `ShowText|pysssss`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTX2_NAG`
- `LTXVPreprocess`
- `SamplerCustom` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `GetNode`
- `DF_Int_to_Float`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `JjkText`
- `VHS_VideoCombine`
- `Int`
- `PrimitiveInt`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `easy positive`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **68%**（38/56）

**有卡**：`VAELoader`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`VAELoaderKJ`、`BasicScheduler`、`StringFunction|pysssss`、`DualCLIPLoader`、`AILab_QwenVL_Advanced`、`ImageResizeKJv2`、`LayerUtility: If `、`LayerUtility: BooleanOperatorV2`、`PathchSageAttentionKJ`、`KSamplerSelect`、`LayerUtility: NumberCalculatorV2`、`SimpleMath+`、`JoinStrings`、`EmptyLTXVLatentVideo`、`ModelSamplingSD3`、`UNETLoader`、`LTX2_NAG`、`LTXVPreprocess`、`SamplerCustom`、`VAEDecode`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`DF_Int_to_Float`、`CLIPTextEncode`、`VHS_VideoCombine`、`Int`、`LTXVImgToVideoInplaceKJ`、`LTXVSeparateAVLatent`、`LTX2SamplingPreviewOverride`、`LoraLoaderModelOnly`、`LoadImage`、`easy positive`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
