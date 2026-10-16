---
key: 视频生成/图生视频/LTX2.3 I2V test v5(prompt relay版)_2031616581142319106.json
name: LTX2.3 I2V test v5(prompt relay版)_2031616581142319106.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2031616581142319106.json
hash: 9f4c18172f55e7ae
coverage: 0.924528
learned_at: 2026-10-15 22:35:32
nodes: [Note, LTXVSeparateAVLatent, LTXVCropGuides, SolidMask, RandomNoise, GetImageRangeFromBatch, KSamplerSelect, LTXVScheduler, SaveImage, EmptyLTXVLatentVideo, PathchSageAttentionKJ, LoadImage, CFGGuider, ttN float, LTXVAudioVAEDecode, ImageScale, LTXVPreprocess, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, RTXVideoSuperResolution, ImageScale, LTXVPreprocess, LTXVAudioVAEEncode, ImageScale, LTXVConditioning, SamplerCustomAdvanced, SaveAudio, LTXVPreprocess, CLIPTextEncode, LTX2_NAG, ttN text, easy showAnything, LoraLoaderModelOnly, CLIPTextEncode, PrimitiveInt, VHS_LoadAudioUpload, SetLatentNoiseMask, LoadImage, easy int, easy int, LTXVEmptyLatentAudio, LTXVConcatAVLatent, PromptRelayEncodeTimeline, DualCLIPLoader, UNETLoader, VAELoaderKJ, VAELoaderKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, VHS_VideoCombine, LTXVAddGuideMulti]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 20, "width": 93}
---

# 视频生成/图生视频/LTX2.3 I2V test v5(prompt relay版)_2031616581142319106.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031616581142319106.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `Note`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `SolidMask`
- `RandomNoise`
- `GetImageRangeFromBatch`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `SaveImage`
- `EmptyLTXVLatentVideo`
- `PathchSageAttentionKJ`
- `LoadImage`
- `CFGGuider`
- `ttN float`
- `LTXVAudioVAEDecode` ★核心
- `ImageScale`
- `LTXVPreprocess`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `RTXVideoSuperResolution`
- `ImageScale`
- `LTXVPreprocess`
- `LTXVAudioVAEEncode` ★核心
- `ImageScale`
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `SaveAudio`
- `LTXVPreprocess`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `ttN text`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `VHS_LoadAudioUpload`
- `SetLatentNoiseMask`
- `LoadImage`
- `easy int`
- `easy int`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `PromptRelayEncodeTimeline`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `VHS_VideoCombine`
- `LTXVAddGuideMulti`

## 关键参数

- `width` = `93`
- `height` = `20`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（49/53）

**有卡**：`LTXVSeparateAVLatent`、`LTXVCropGuides`、`SolidMask`、`RandomNoise`、`GetImageRangeFromBatch`、`KSamplerSelect`、`LTXVScheduler`、`SaveImage`、`EmptyLTXVLatentVideo`、`PathchSageAttentionKJ`、`LoadImage`、`CFGGuider`、`ttN float`、`LTXVAudioVAEDecode`、`ImageScale`、`LTXVPreprocess`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`RTXVideoSuperResolution`、`LTXVAudioVAEEncode`、`LTXVConditioning`、`SamplerCustomAdvanced`、`SaveAudio`、`CLIPTextEncode`、`LTX2_NAG`、`ttN text`、`LoraLoaderModelOnly`、`VHS_LoadAudioUpload`、`SetLatentNoiseMask`、`easy int`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`PromptRelayEncodeTimeline`、`DualCLIPLoader`、`UNETLoader`、`VAELoaderKJ`、`VHS_VideoCombine`、`LTXVAddGuideMulti`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
