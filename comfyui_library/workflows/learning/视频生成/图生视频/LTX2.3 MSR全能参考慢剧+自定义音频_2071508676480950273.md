---
key: 视频生成/图生视频/LTX2.3 MSR全能参考慢剧+自定义音频_2071508676480950273.json
name: LTX2.3 MSR全能参考慢剧+自定义音频_2071508676480950273.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2071508676480950273.json
hash: 8f5eb153a4dfde5a
coverage: 0.892857
learned_at: 2026-10-15 22:40:46
nodes: [UNETLoader, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, LoadAudioUI, EmptyLTXVLatentVideo, LTX2_NAG, LTXAddVideoICLoRAGuide, ComfySwitchNode, LTXVConcatAVLatent, SolidMask, SetLatentNoiseMask, LTXVAudioVAEEncode, LTXVEmptyLatentAudio, LTXVConditioning, CLIPTextEncode, LTX2SamplingPreviewOverride, VisualizeSigmasKJ, BasicScheduler, KSamplerSelect, LTXVAudioVAEDecode, LTXVSeparateAVLatent, SamplerCustom, ComfySwitchNode, LTXVCropGuides, VAEDecodeTiled, VHS_VideoCombine, VHS_VideoCombine, Int, Int, LTXICLoRALoaderModelOnly, LiconMSR, VHS_VideoCombine, Dapao_LlamaCaptionOptions, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMathBoolean+, ComfySwitchNode, easy cleanGpuUsed, RegexReplace, Note, LoadImage, LoadImage, LoadImage, Float, Float, ttN concat, ttN concat, RH_Utils, CR Prompt Text, Dapao_LlamaCaption, PrimitiveBoolean, CLIPTextEncode, PrimitiveStringMultiline, easy showAnything]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 241}
---

# 视频生成/图生视频/LTX2.3 MSR全能参考慢剧+自定义音频_2071508676480950273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2071508676480950273.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Other

**节点**（56 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LoadAudioUI`
- `EmptyLTXVLatentVideo`
- `LTX2_NAG`
- `LTXAddVideoICLoRAGuide`
- `ComfySwitchNode`
- `LTXVConcatAVLatent`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTX2SamplingPreviewOverride`
- `VisualizeSigmasKJ`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustom` ★核心
- `ComfySwitchNode`
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `LTXICLoRALoaderModelOnly` ★核心
- `LiconMSR`
- `VHS_VideoCombine`
- `Dapao_LlamaCaptionOptions`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMathBoolean+`
- `ComfySwitchNode`
- `easy cleanGpuUsed`
- `RegexReplace`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Float`
- `Float`
- `ttN concat`
- `ttN concat`
- `RH_Utils`
- `CR Prompt Text`
- `Dapao_LlamaCaption`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `easy showAnything`

## 关键参数

- `width` = `241`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（50/56）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`LoadAudioUI`、`EmptyLTXVLatentVideo`、`LTX2_NAG`、`LTXAddVideoICLoRAGuide`、`LTXVConcatAVLatent`、`SolidMask`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`CLIPTextEncode`、`LTX2SamplingPreviewOverride`、`VisualizeSigmasKJ`、`BasicScheduler`、`KSamplerSelect`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`SamplerCustom`、`LTXVCropGuides`、`VAEDecodeTiled`、`VHS_VideoCombine`、`Int`、`LTXICLoRALoaderModelOnly`、`LiconMSR`、`Dapao_LlamaCaptionOptions`、`SimpleMath+`、`SimpleMathBoolean+`、`easy cleanGpuUsed`、`RegexReplace`、`LoadImage`、`Float`、`ttN concat`、`RH_Utils`、`CR Prompt Text`、`Dapao_LlamaCaption`、`PrimitiveBoolean`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent、SetLatentNoiseMask
