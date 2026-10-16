---
key: 视频生成/图生视频/LTX2.3-MSR多图像参考数字人(自定义音频)_2086423602479591426.json
name: LTX2.3-MSR多图像参考数字人(自定义音频)_2086423602479591426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-MSR多图像参考数字人(自定义音频)_2086423602479591426.json
hash: 6b721ea2d9165963
coverage: 0.931818
learned_at: 2026-10-16 21:07:14
nodes: [KSamplerSelect, LTXVCropGuides, LTXVSeparateAVLatent, LTX2SamplingPreviewOverride, VisualizeSigmasKJ, CLIPTextEncode, DualCLIPLoader, VAELoaderKJ, VAEDecodeTiled, LTXAddVideoICLoRAGuide, VHS_VideoCombine, LTX2_NAG, LTXVConditioning, UNETLoader, LTXICLoRALoaderModelOnly, Float, VAELoaderKJ, EmptyLTXVLatentVideo, LTXVConcatAVLatent, INTConstant, SamplerCustom, LTXVEmptyLatentAudio, SimpleMath+, BasicScheduler, ComfySwitchNode, LTXVAudioVAEDecode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEEncode, VHS_VideoCombine, ComfySwitchNode, Reroute, LoadAudioUI, PrimitiveBoolean, Label (rgthree), Label (rgthree), LoadImage, INTConstant, INTConstant, LiconMSR, LoadImage, LoadImage, CLIPTextEncode, LoadAudio]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 50, "width": 241}
---

# 视频生成/图生视频/LTX2.3-MSR多图像参考数字人(自定义音频)_2086423602479591426.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3-MSR多图像参考数字人(自定义音频)_2086423602479591426.json`

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
- `Float`
- `VAELoaderKJ`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `INTConstant`
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
- `LoadAudioUI`
- `PrimitiveBoolean`
- `Label (rgthree)`
- `Label (rgthree)`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `LiconMSR`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadAudio`

## 关键参数

- `width` = `241`
- `height` = `50`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（41/44）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTX2SamplingPreviewOverride`、`VisualizeSigmasKJ`、`CLIPTextEncode`、`DualCLIPLoader`、`VAELoaderKJ`、`VAEDecodeTiled`、`LTXAddVideoICLoRAGuide`、`VHS_VideoCombine`、`LTX2_NAG`、`LTXVConditioning`、`UNETLoader`、`LTXICLoRALoaderModelOnly`、`Float`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`INTConstant`、`SamplerCustom`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`BasicScheduler`、`LTXVAudioVAEDecode`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEEncode`、`LoadAudioUI`、`PrimitiveBoolean`、`Label (rgthree)`、`LoadImage`、`LiconMSR`、`LoadAudio`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent、SetLatentNoiseMask
