---
key: 视频生成/图生视频/LTX2.3极速脱口秀爆款工作流｜图文直接生成段子视频_2103699150805233666.json
name: LTX2.3极速脱口秀爆款工作流｜图文直接生成段子视频_2103699150805233666
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3极速脱口秀爆款工作流｜图文直接生成段子视频_2103699150805233666.json
hash: 28f536b27a4fe6dc
coverage: 0.929825
learned_at: 2026-10-17 02:28:52
nodes: [DualCLIPLoader, easy setNode, Int, easy setNode, easy setNode, easy setNode, Int, Int, VAELoaderKJ, VAELoaderKJ, ImageResizeKJv2, PrimitiveBoolean, PrimitiveInt, LTXVPreprocess, VRAMReserver, easy setNode, UNETLoader, PathchSageAttentionKJ, EmptyLTXVLatentVideo, SimpleMath+, ModelSamplingSD3, BasicScheduler, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2_NAG, VisualizeSigmasKJ, LTXVEmptyLatentAudio, easy getNode, LTXVImgToVideoConditionOnly, easy getNode, easy getNode, ConditioningZeroOut, VAELoader, LTXVConcatAVLatent, KSamplerSelect, easy getNode, LTXVSeparateAVLatent, DF_Int_to_Float, easy getNode, VAEDecode, LTXVAudioVAEDecode, LTXVConditioning, LTX2SamplingPreviewOverride, SamplerCustom, easy getNode, easy getNode, LatentUpscaleModelLoader, LTXVCropGuides, LTXVLatentUpsampler, CFGGuider, ManualSigmas, KSamplerSelect, LTXVImgToVideoInplace, LTXVConcatAVLatent, easy getNode, easy getNode, RandomNoise, LTXVSeparateAVLatent, VAEDecode, LTXVAudioVAEDecode, Reroute, SamplerCustomAdvanced, VHS_VideoCombine, Fast Groups Bypasser (rgthree), CLIPTextEncode, easy getNode, easy getNode, VHS_VideoCombine, CLIPTextEncode, PrimitiveInt, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3极速脱口秀爆款工作流｜图文直接生成段子视频_2103699150805233666.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3极速脱口秀爆款工作流｜图文直接生成段子视频_2103699150805233666.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（114 个）：
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
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `easy getNode`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
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

覆盖率 **93%**（106/114）

**有卡**：`DualCLIPLoader`、`easy setNode`、`Int`、`VAELoaderKJ`、`ImageResizeKJv2`、`PrimitiveBoolean`、`LTXVPreprocess`、`VRAMReserver`、`UNETLoader`、`PathchSageAttentionKJ`、`EmptyLTXVLatentVideo`、`SimpleMath+`、`ModelSamplingSD3`、`BasicScheduler`、`LoraLoaderModelOnly`、`LTX2_NAG`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`easy getNode`、`LTXVImgToVideoConditionOnly`、`ConditioningZeroOut`、`VAELoader`、`LTXVConcatAVLatent`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`DF_Int_to_Float`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`LTX2SamplingPreviewOverride`、`SamplerCustom`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`CFGGuider`、`ManualSigmas`、`LTXVImgToVideoInplace`、`RandomNoise`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`CLIPTextEncode`、`LoadImage`、`CLIPLoader`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
