---
key: 视频生成/图生视频/KJ版音画同步｜LTX2.3提示词润色图生视频_2091803663361728514.json
name: KJ版音画同步｜LTX2.3提示词润色图生视频_2091803663361728514
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/KJ版音画同步｜LTX2.3提示词润色图生视频_2091803663361728514.json
hash: 3f6cd306484a8259
coverage: 0.779221
learned_at: 2026-10-16 22:30:28
nodes: [LTX2_NAG, LTX2SamplingPreviewOverride, GetNode, GetNode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAELoader, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, LTXVConcatAVLatent, PathchSageAttentionKJ, SetNode, VAELoaderKJ, EmptyLTXVLatentVideo, BasicScheduler, LTXVPreprocess, SetNode, ConditioningZeroOut, SamplerCustom, VAEDecode, KSamplerSelect, CLIPTextEncode, CLIPTextEncode, LTXVImgToVideoInplaceKJ, SetNode, DF_Int_to_Float, GetNode, StringFunction|pysssss, UNETLoader, VAELoaderKJ, DualCLIPLoader, GetNode, GetNode, ModelSamplingSD3, AILab_QwenVL_Advanced, ImageResizeKJv2, LayerUtility: If , LayerUtility: BooleanOperatorV2, LayerUtility: NumberCalculatorV2, SimpleMath+, JjkText, VHS_VideoCombine, ShowText|pysssss, LoadImage, PrimitiveInt, Int, PrimitiveInt, PrimitiveInt, easy positive, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/KJ版音画同步｜LTX2.3提示词润色图生视频_2091803663361728514.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/KJ版音画同步｜LTX2.3提示词润色图生视频_2091803663361728514.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（77 个）：
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
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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

覆盖率 **78%**（60/77）

**有卡**：`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAELoader`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`PathchSageAttentionKJ`、`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`BasicScheduler`、`LTXVPreprocess`、`ConditioningZeroOut`、`SamplerCustom`、`VAEDecode`、`KSamplerSelect`、`CLIPTextEncode`、`LTXVImgToVideoInplaceKJ`、`DF_Int_to_Float`、`StringFunction|pysssss`、`UNETLoader`、`DualCLIPLoader`、`ModelSamplingSD3`、`AILab_QwenVL_Advanced`、`ImageResizeKJv2`、`LayerUtility: If `、`LayerUtility: BooleanOperatorV2`、`LayerUtility: NumberCalculatorV2`、`SimpleMath+`、`VHS_VideoCombine`、`LoadImage`、`Int`、`easy positive`、`CLIPLoader`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
