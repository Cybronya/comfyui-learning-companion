---
key: 视频生成/图生视频/LTX2.3图音生视频_2032443703675068417.json
name: LTX2.3图音生视频_2032443703675068417.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2032443703675068417.json
hash: ca06cd218904e478
coverage: 0.806452
learned_at: 2026-10-15 22:35:36
nodes: [VAELoaderKJ, LTX2SamplingPreviewOverride, GetNode, GetNode, UNETLoader, VAELoader, DualCLIPLoader, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, PathchSageAttentionKJ, SetNode, VAELoaderKJ, EmptyLTXVLatentVideo, BasicScheduler, LTXVPreprocess, ModelSamplingSD3, SetNode, ConditioningZeroOut, KSamplerSelect, SimpleMath+, ImageResizeKJv2, DF_Int_to_Float, GetNode, GetNode, LTX2_NAG, GetNode, SetNode, SamplerCustom, Setter, LTXVConcatAVLatent, LoadImage, PrimitiveInt, CLIPTextEncode, AILab_QwenVL_Advanced, LTXVImgToVideoInplaceKJ, LTXVAudioVAEDecode, TrimAudioDuration, ComfyMathExpression, LTXVAudioVAEEncode, SolidMask, SetLatentNoiseMask, LTXVEmptyLatentAudio, ComfyMathExpression, LTXVSeparateAVLatent, Switch any [Crystools], PrimitiveInt, VAEDecode, StringFunction|pysssss, easy positive, PrimitiveInt, PrimitiveBoolean, PrimitiveBoolean, easy positive, ShowText|pysssss, LoadAudio, VHS_VideoCombine, CLIPTextEncode, ComfyMathExpression, Int, Switch any [Crystools], Getter]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3图音生视频_2032443703675068417.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2032443703675068417.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（62 个）：
- `VAELoaderKJ`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `LTXVConditioning`
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
- `PathchSageAttentionKJ`
- `SetNode`
- `VAELoaderKJ`
- `EmptyLTXVLatentVideo`
- `BasicScheduler`
- `LTXVPreprocess`
- `ModelSamplingSD3`
- `SetNode`
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `SimpleMath+`
- `ImageResizeKJv2`
- `DF_Int_to_Float`
- `GetNode`
- `GetNode`
- `LTX2_NAG`
- `GetNode`
- `SetNode`
- `SamplerCustom` ★核心
- `Setter`
- `LTXVConcatAVLatent`
- `LoadImage`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `AILab_QwenVL_Advanced`
- `LTXVImgToVideoInplaceKJ`
- `LTXVAudioVAEDecode` ★核心
- `TrimAudioDuration`
- `ComfyMathExpression`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVEmptyLatentAudio` ★核心
- `ComfyMathExpression`
- `LTXVSeparateAVLatent`
- `Switch any [Crystools]`
- `PrimitiveInt`
- `VAEDecode` ★核心
- `StringFunction|pysssss`
- `easy positive`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `easy positive`
- `ShowText|pysssss`
- `LoadAudio`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `Int`
- `Switch any [Crystools]`
- `Getter`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（50/62）

**有卡**：`VAELoaderKJ`、`LTX2SamplingPreviewOverride`、`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`PathchSageAttentionKJ`、`EmptyLTXVLatentVideo`、`BasicScheduler`、`LTXVPreprocess`、`ModelSamplingSD3`、`ConditioningZeroOut`、`KSamplerSelect`、`SimpleMath+`、`ImageResizeKJv2`、`DF_Int_to_Float`、`LTX2_NAG`、`SamplerCustom`、`Setter`、`LTXVConcatAVLatent`、`LoadImage`、`CLIPTextEncode`、`AILab_QwenVL_Advanced`、`LTXVImgToVideoInplaceKJ`、`LTXVAudioVAEDecode`、`TrimAudioDuration`、`ComfyMathExpression`、`LTXVAudioVAEEncode`、`SolidMask`、`SetLatentNoiseMask`、`LTXVSeparateAVLatent`、`Switch any [Crystools]`、`VAEDecode`、`StringFunction|pysssss`、`easy positive`、`PrimitiveBoolean`、`LoadAudio`、`VHS_VideoCombine`、`Int`、`Getter`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
