---
key: 视频生成/图生视频/【优化版】LTX2.3-MSR全能参考升级-支持自定义音频_2072216632251998209.json
name: 【优化版】LTX2.3-MSR全能参考升级-支持自定义音频_2072216632251998209.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2072216632251998209.json
hash: 29b633ec1ef67de8
coverage: 0.933333
learned_at: 2026-10-15 22:40:53
nodes: [KSamplerSelect, LTXVCropGuides, LTXVSeparateAVLatent, LTX2SamplingPreviewOverride, VisualizeSigmasKJ, CLIPTextEncode, VAELoaderKJ, VAEDecodeTiled, LTXAddVideoICLoRAGuide, LTX2_NAG, LTXVConditioning, VAELoaderKJ, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SamplerCustom, LTXVEmptyLatentAudio, SimpleMath+, BasicScheduler, ComfySwitchNode, LTXVAudioVAEDecode, SolidMask, ComfySwitchNode, Reroute, LoadAudioUI, INTConstant, INTConstant, VHS_VideoCombine, LoadAudio, PrimitiveBoolean, DualCLIPLoader, LoadImage, LoadImage, LiconMSR, LoadImage, LoadImage, LTXICLoRALoaderModelOnly, LTXICLoRALoaderModelOnly, UNETLoader, INTConstant, Float, LoadImage, LTXVAudioVAEEncode, SetLatentNoiseMask, VHS_VideoCombine, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 50, "width": 241}
---

# 视频生成/图生视频/【优化版】LTX2.3-MSR全能参考升级-支持自定义音频_2072216632251998209.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2072216632251998209.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Other

**节点**（45 个）：
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTX2SamplingPreviewOverride`
- `VisualizeSigmasKJ`
- `CLIPTextEncode` ★核心
- `VAELoaderKJ`
- `VAEDecodeTiled` ★核心
- `LTXAddVideoICLoRAGuide`
- `LTX2_NAG`
- `LTXVConditioning`
- `VAELoaderKJ`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `SamplerCustom` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `SimpleMath+`
- `BasicScheduler`
- `ComfySwitchNode`
- `LTXVAudioVAEDecode` ★核心
- `SolidMask`
- `ComfySwitchNode`
- `Reroute`
- `LoadAudioUI`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `LoadAudio`
- `PrimitiveBoolean`
- `DualCLIPLoader`
- `LoadImage`
- `LoadImage`
- `LiconMSR`
- `LoadImage`
- `LoadImage`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `INTConstant`
- `Float`
- `LoadImage`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `241`
- `height` = `50`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（42/45）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTX2SamplingPreviewOverride`、`VisualizeSigmasKJ`、`CLIPTextEncode`、`VAELoaderKJ`、`VAEDecodeTiled`、`LTXAddVideoICLoRAGuide`、`LTX2_NAG`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`SamplerCustom`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`BasicScheduler`、`LTXVAudioVAEDecode`、`SolidMask`、`LoadAudioUI`、`INTConstant`、`VHS_VideoCombine`、`LoadAudio`、`PrimitiveBoolean`、`DualCLIPLoader`、`LoadImage`、`LiconMSR`、`LTXICLoRALoaderModelOnly`、`UNETLoader`、`Float`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent、SetLatentNoiseMask
