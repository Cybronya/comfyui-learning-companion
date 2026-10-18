---
key: 视频生成/图生视频/LTX2.3极速文图生视频 脱口秀数字人人物特效直出_2104354109565526017.json
name: LTX2.3极速文图生视频 脱口秀数字人人物特效直出_2104354109565526017
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3极速文图生视频 脱口秀数字人人物特效直出_2104354109565526017.json
hash: cf83c7184ed2bed5
coverage: 0.930233
learned_at: 2026-10-17 02:43:49
nodes: [DualCLIPLoader, easy setNode, Int, easy setNode, easy setNode, easy setNode, Int, Int, VAELoaderKJ, VAELoaderKJ, ImageResizeKJv2, PrimitiveBoolean, PrimitiveInt, LTXVPreprocess, VRAMReserver, easy setNode, UNETLoader, PathchSageAttentionKJ, EmptyLTXVLatentVideo, SimpleMath+, ModelSamplingSD3, BasicScheduler, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2_NAG, VisualizeSigmasKJ, LTXVEmptyLatentAudio, easy getNode, LTXVImgToVideoConditionOnly, easy getNode, easy getNode, ConditioningZeroOut, VAELoader, LTXVConcatAVLatent, KSamplerSelect, easy getNode, LTXVSeparateAVLatent, DF_Int_to_Float, easy getNode, VAEDecode, LTXVAudioVAEDecode, LTXVConditioning, LTX2SamplingPreviewOverride, SamplerCustom, easy getNode, easy getNode, LatentUpscaleModelLoader, LTXVCropGuides, LTXVLatentUpsampler, CFGGuider, ManualSigmas, KSamplerSelect, LTXVImgToVideoInplace, LTXVConcatAVLatent, easy getNode, easy getNode, RandomNoise, LTXVSeparateAVLatent, VAEDecode, LTXVAudioVAEDecode, Reroute, SamplerCustomAdvanced, VHS_VideoCombine, CLIPTextEncode, Fast Groups Bypasser (rgthree), CLIPTextEncode, CLIPTextEncode, easy getNode, easy getNode, VHS_VideoCombine, CLIPTextEncode, PrimitiveInt, LoadImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3极速文图生视频 脱口秀数字人人物特效直出_2104354109565526017.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3极速文图生视频 脱口秀数字人人物特效直出_2104354109565526017.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（129 个）：
- `DualCLIPLoader`
- `easy setNode`
- `Int`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `Int`
- `Int`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `ImageResizeKJv2`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `LTXVPreprocess`
- `VRAMReserver`
- `easy setNode`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `EmptyLTXVLatentVideo`
- `SimpleMath+`
- `ModelSamplingSD3`
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
- `easy getNode`
- `LTXVImgToVideoConditionOnly`
- `easy getNode`
- `easy getNode`
- `ConditioningZeroOut`
- `VAELoader`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `easy getNode`
- `LTXVSeparateAVLatent`
- `DF_Int_to_Float`
- `easy getNode`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `LTX2SamplingPreviewOverride`
- `SamplerCustom` ★核心
- `easy getNode`
- `easy getNode`
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `easy getNode`
- `easy getNode`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy getNode`
- `easy getNode`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `LoadImage`
- `UNETLoader` ★核心
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **93%**（120/129）

**有卡**：`DualCLIPLoader`、`easy setNode`、`Int`、`VAELoaderKJ`、`ImageResizeKJv2`、`PrimitiveBoolean`、`LTXVPreprocess`、`VRAMReserver`、`UNETLoader`、`PathchSageAttentionKJ`、`EmptyLTXVLatentVideo`、`SimpleMath+`、`ModelSamplingSD3`、`BasicScheduler`、`LoraLoaderModelOnly`、`LTX2_NAG`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`easy getNode`、`LTXVImgToVideoConditionOnly`、`ConditioningZeroOut`、`VAELoader`、`LTXVConcatAVLatent`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`DF_Int_to_Float`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`LTX2SamplingPreviewOverride`、`SamplerCustom`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`CFGGuider`、`ManualSigmas`、`LTXVImgToVideoInplace`、`RandomNoise`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`CLIPTextEncode`、`LoadImage`、`KSampler`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`CLIPLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
