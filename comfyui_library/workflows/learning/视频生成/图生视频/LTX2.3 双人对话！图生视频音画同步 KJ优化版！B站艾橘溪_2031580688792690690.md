---
key: 视频生成/图生视频/LTX2.3 双人对话！图生视频音画同步 KJ优化版！B站艾橘溪_2031580688792690690.json
name: LTX2.3 双人对话！图生视频音画同步 KJ优化版！B站艾橘溪_2031580688792690690.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 双人对话！图生视频音画同步 KJ优化版！B站艾橘溪_2031580688792690690.json
hash: 66661ea599dd1755
coverage: 0.666667
learned_at: 2026-10-15 22:35:31
nodes: [GetNode, VAELoader, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, SetNode, VAELoaderKJ, BasicScheduler, SetNode, SetNode, StringFunction|pysssss, VAELoaderKJ, DualCLIPLoader, GetNode, GetNode, AILab_QwenVL_Advanced, ImageResizeKJv2, LayerUtility: If , LayerUtility: BooleanOperatorV2, PathchSageAttentionKJ, KSamplerSelect, LayerUtility: NumberCalculatorV2, SimpleMath+, PrimitiveStringMultiline, JoinStrings, EmptyLTXVLatentVideo, ModelSamplingSD3, UNETLoader, ShowText|pysssss, PrimitiveInt, PrimitiveInt, LoadImage, LTX2_NAG, LTXVPreprocess, SamplerCustom, SetNode, VAEDecode, LTXVConcatAVLatent, LTXVAudioVAEDecode, SetNode, GetNode, DF_Int_to_Float, GetNode, GetNode, Note, CLIPTextEncode, CLIPTextEncode, JjkText, VHS_VideoCombine, Int, PrimitiveInt, easy positive, LTXVImgToVideoInplaceKJ, GetNode, LTXVSeparateAVLatent, LTX2SamplingPreviewOverride, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 305}
---

# 视频生成/图生视频/LTX2.3 双人对话！图生视频音画同步 KJ优化版！B站艾橘溪_2031580688792690690.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031580688792690690.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（57 个）：
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
- `LoadImage`
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
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `JjkText`
- `VHS_VideoCombine`
- `Int`
- `PrimitiveInt`
- `easy positive`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **67%**（38/57）

**有卡**：`VAELoader`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`VAELoaderKJ`、`BasicScheduler`、`StringFunction|pysssss`、`DualCLIPLoader`、`AILab_QwenVL_Advanced`、`ImageResizeKJv2`、`LayerUtility: If `、`LayerUtility: BooleanOperatorV2`、`PathchSageAttentionKJ`、`KSamplerSelect`、`LayerUtility: NumberCalculatorV2`、`SimpleMath+`、`JoinStrings`、`EmptyLTXVLatentVideo`、`ModelSamplingSD3`、`UNETLoader`、`LoadImage`、`LTX2_NAG`、`LTXVPreprocess`、`SamplerCustom`、`VAEDecode`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`DF_Int_to_Float`、`CLIPTextEncode`、`VHS_VideoCombine`、`Int`、`easy positive`、`LTXVImgToVideoInplaceKJ`、`LTXVSeparateAVLatent`、`LTX2SamplingPreviewOverride`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
