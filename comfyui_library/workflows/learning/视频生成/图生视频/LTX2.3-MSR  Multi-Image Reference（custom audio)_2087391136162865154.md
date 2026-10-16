---
key: 视频生成/图生视频/LTX2.3-MSR  Multi-Image Reference（custom audio)_2087391136162865154.json
name: LTX2.3-MSR  Multi-Image Reference（custom audio)_2087391136162865154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-MSR  Multi-Image Reference（custom audio)_2087391136162865154.json
hash: b51a237c94067085
coverage: 0.931818
learned_at: 2026-10-16 21:27:34
nodes: [KSamplerSelect, LTXVCropGuides, LTXVSeparateAVLatent, LTX2SamplingPreviewOverride, VisualizeSigmasKJ, CLIPTextEncode, DualCLIPLoader, VAELoaderKJ, VAEDecodeTiled, LTXAddVideoICLoRAGuide, VHS_VideoCombine, LTX2_NAG, LTXVConditioning, UNETLoader, LTXICLoRALoaderModelOnly, VAELoaderKJ, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SamplerCustom, LTXVEmptyLatentAudio, SimpleMath+, BasicScheduler, ComfySwitchNode, LTXVAudioVAEDecode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEEncode, VHS_VideoCombine, ComfySwitchNode, Reroute, LoadAudio, LoadAudioUI, PrimitiveBoolean, Label (rgthree), Label (rgthree), LoadImage, LiconMSR, Float, INTConstant, LoadImage, INTConstant, INTConstant, CLIPTextEncode, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 50, "width": 241}
---

# 视频生成/图生视频/LTX2.3-MSR  Multi-Image Reference（custom audio)_2087391136162865154.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3-MSR  Multi-Image Reference（custom audio)_2087391136162865154.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Other

**节点**（44 个）：
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTX2SamplingPreviewOverride`
- `VisualizeSigmasKJ`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAEDecodeTiled` ★核心
- `LTXAddVideoICLoRAGuide`
- `VHS_VideoCombine`
- `LTX2_NAG`
- `LTXVConditioning`
- `UNETLoader` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `VAELoaderKJ`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `SamplerCustom` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `SimpleMath+`
- `BasicScheduler`
- `ComfySwitchNode`
- `LTXVAudioVAEDecode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `VHS_VideoCombine`
- `ComfySwitchNode`
- `Reroute`
- `LoadAudio`
- `LoadAudioUI`
- `PrimitiveBoolean`
- `Label (rgthree)`
- `Label (rgthree)`
- `LoadImage`
- `LiconMSR`
- `Float`
- `INTConstant`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `LoadImage`

## 关键参数

- `width` = `241`
- `height` = `50`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（41/44）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTX2SamplingPreviewOverride`、`VisualizeSigmasKJ`、`CLIPTextEncode`、`DualCLIPLoader`、`VAELoaderKJ`、`VAEDecodeTiled`、`LTXAddVideoICLoRAGuide`、`VHS_VideoCombine`、`LTX2_NAG`、`LTXVConditioning`、`UNETLoader`、`LTXICLoRALoaderModelOnly`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`SamplerCustom`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`BasicScheduler`、`LTXVAudioVAEDecode`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEEncode`、`LoadAudio`、`LoadAudioUI`、`PrimitiveBoolean`、`Label (rgthree)`、`LoadImage`、`LiconMSR`、`Float`、`INTConstant`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent、SetLatentNoiseMask
