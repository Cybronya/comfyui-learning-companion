---
key: 视频生成/图生视频/LTX2.3 数字人对话！Digital Avatar Dialo图生视频音画同步 双人_单人视频_2092438399465648130.json
name: LTX2.3 数字人对话！Digital Avatar Dialo图生视频音画同步 双人_单人视频_2092438399465648130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 数字人对话！Digital Avatar Dialo图生视频音画同步 双人_单人视频_2092438399465648130.json
hash: 72ad64514ba4a4c7
coverage: 0.655172
learned_at: 2026-10-16 22:59:01
nodes: [GetNode, VAELoader, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, SetNode, VAELoaderKJ, BasicScheduler, SetNode, SetNode, StringFunction|pysssss, VAELoaderKJ, DualCLIPLoader, GetNode, GetNode, AILab_QwenVL_Advanced, ImageResizeKJv2, LayerUtility: If , LayerUtility: BooleanOperatorV2, KSamplerSelect, LayerUtility: NumberCalculatorV2, SimpleMath+, PrimitiveStringMultiline, JoinStrings, EmptyLTXVLatentVideo, ModelSamplingSD3, UNETLoader, LTX2_NAG, LTXVPreprocess, SamplerCustom, SetNode, VAEDecode, LTXVConcatAVLatent, LTXVAudioVAEDecode, SetNode, GetNode, DF_Int_to_Float, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, JjkText, LTXVImgToVideoInplaceKJ, GetNode, LTXVSeparateAVLatent, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, ShowText|pysssss, LoadImage, Int, PrimitiveInt, Note, PrimitiveInt, VHS_VideoCombine, PrimitiveInt, Note, easy positive, PathchSageAttentionKJ]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 305}
---

# 视频生成/图生视频/LTX2.3 数字人对话！Digital Avatar Dialo图生视频音画同步 双人_单人视频_2092438399465648130.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3 数字人对话！Digital Avatar Dialo图生视频音画同步 双人_单人视频_2092438399465648130.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（58 个）：
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
- `KSamplerSelect` ★核心
- `LayerUtility: NumberCalculatorV2`
- `SimpleMath+`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `EmptyLTXVLatentVideo`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
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
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `ShowText|pysssss`
- `LoadImage`
- `Int`
- `PrimitiveInt`
- `Note`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `Note`
- `easy positive`
- `PathchSageAttentionKJ`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **66%**（38/58）

**有卡**：`VAELoader`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`VAELoaderKJ`、`BasicScheduler`、`StringFunction|pysssss`、`DualCLIPLoader`、`AILab_QwenVL_Advanced`、`ImageResizeKJv2`、`LayerUtility: If `、`LayerUtility: BooleanOperatorV2`、`KSamplerSelect`、`LayerUtility: NumberCalculatorV2`、`SimpleMath+`、`JoinStrings`、`EmptyLTXVLatentVideo`、`ModelSamplingSD3`、`UNETLoader`、`LTX2_NAG`、`LTXVPreprocess`、`SamplerCustom`、`VAEDecode`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`DF_Int_to_Float`、`CLIPTextEncode`、`LTXVImgToVideoInplaceKJ`、`LTXVSeparateAVLatent`、`LTX2SamplingPreviewOverride`、`LoraLoaderModelOnly`、`LoadImage`、`Int`、`VHS_VideoCombine`、`easy positive`、`PathchSageAttentionKJ`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
