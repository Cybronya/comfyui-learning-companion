---
key: 视频生成/图生视频/LTX2.3图生视频KJ版｜音画同步提示词润色直出_2091641388155887618.json
name: LTX2.3图生视频KJ版｜音画同步提示词润色直出_2091641388155887618
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3图生视频KJ版｜音画同步提示词润色直出_2091641388155887618.json
hash: 2884ccb002d3b2a5
coverage: 0.78481
learned_at: 2026-10-16 22:30:32
nodes: [LTX2_NAG, LTX2SamplingPreviewOverride, GetNode, GetNode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAELoader, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, LTXVConcatAVLatent, PathchSageAttentionKJ, SetNode, VAELoaderKJ, EmptyLTXVLatentVideo, BasicScheduler, LTXVPreprocess, SetNode, ConditioningZeroOut, SamplerCustom, VAEDecode, KSamplerSelect, CLIPTextEncode, CLIPTextEncode, LTXVImgToVideoInplaceKJ, SetNode, DF_Int_to_Float, GetNode, StringFunction|pysssss, UNETLoader, VAELoaderKJ, DualCLIPLoader, GetNode, GetNode, ModelSamplingSD3, AILab_QwenVL_Advanced, ImageResizeKJv2, LayerUtility: If , LayerUtility: BooleanOperatorV2, LayerUtility: NumberCalculatorV2, SimpleMath+, JjkText, VHS_VideoCombine, ShowText|pysssss, LoadImage, PrimitiveInt, Int, PrimitiveInt, PrimitiveInt, easy positive, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3图生视频KJ版｜音画同步提示词润色直出_2091641388155887618.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3图生视频KJ版｜音画同步提示词润色直出_2091641388155887618.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAELoader`
- `LTXVConditioning`
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `PathchSageAttentionKJ`
- `SetNode`
- `VAELoaderKJ`
- `EmptyLTXVLatentVideo`
- `BasicScheduler`
- `LTXVPreprocess`
- `SetNode`
- `ConditioningZeroOut`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVImgToVideoInplaceKJ`
- `SetNode`
- `DF_Int_to_Float`
- `GetNode`
- `StringFunction|pysssss`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `AILab_QwenVL_Advanced`
- `ImageResizeKJv2`
- `LayerUtility: If `
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: NumberCalculatorV2`
- `SimpleMath+`
- `JjkText`
- `VHS_VideoCombine`
- `ShowText|pysssss`
- `LoadImage`
- `PrimitiveInt`
- `Int`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy positive`
- `孤海注释`
- `孤海注释`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **78%**（62/79）

**有卡**：`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAELoader`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`PathchSageAttentionKJ`、`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`BasicScheduler`、`LTXVPreprocess`、`ConditioningZeroOut`、`SamplerCustom`、`VAEDecode`、`KSamplerSelect`、`CLIPTextEncode`、`LTXVImgToVideoInplaceKJ`、`DF_Int_to_Float`、`StringFunction|pysssss`、`UNETLoader`、`DualCLIPLoader`、`ModelSamplingSD3`、`AILab_QwenVL_Advanced`、`ImageResizeKJv2`、`LayerUtility: If `、`LayerUtility: BooleanOperatorV2`、`LayerUtility: NumberCalculatorV2`、`SimpleMath+`、`VHS_VideoCombine`、`LoadImage`、`Int`、`easy positive`、`LoraLoaderModelOnly`、`KSampler`、`solarL_SaveImagesToZip`、`CLIPLoader`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
