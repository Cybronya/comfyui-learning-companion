---
key: 平台全量/ltx2.3 精简 电商带货视频生成_2059373645289574401.json
name: ltx2.3 精简 电商带货视频生成_2059373645289574401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ltx2.3 精简 电商带货视频生成_2059373645289574401.json
hash: 28a139bc6221adc9
coverage: 0.909091
learned_at: 2026-11-14 01:14:37
nodes: [BasicScheduler, VAEDecodeTiled, LTXVAudioVAEEncode, MelBandRoFormerSampler, MelBandRoFormerModelLoader, VAELoaderKJ, VAELoaderKJ, SolidMask, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVCropGuides, Reroute, PreviewAudio, Reroute, DualCLIPLoader, SetLatentNoiseMask, VHS_VideoCombine, UNETLoader, LoraLoaderModelOnly, ComfySwitchNode, CLIPTextEncode, PrimitiveBoolean, LTX2SamplingPreviewOverride, LTXVConditioning, LTXDirectorGuide, VisualizeSigmasKJ, KSamplerSelect, SamplerCustom, LTX2_NAG, LTXVSeparateAVLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXDirector]
patterns: []
missing: []
---

# 平台全量/ltx2.3 精简 电商带货视频生成_2059373645289574401.json

> 来源文件 `comfyui_library/workflows/平台全量/ltx2.3 精简 电商带货视频生成_2059373645289574401.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Other

**节点**（33 个）：
- `BasicScheduler`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEEncode` ★核心
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SolidMask`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `Reroute`
- `PreviewAudio`
- `Reroute`
- `DualCLIPLoader`
- `SetLatentNoiseMask`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ComfySwitchNode`
- `CLIPTextEncode` ★核心
- `PrimitiveBoolean`
- `LTX2SamplingPreviewOverride`
- `LTXVConditioning`
- `LTXDirectorGuide`
- `VisualizeSigmasKJ`
- `KSamplerSelect` ★核心
- `SamplerCustom` ★核心
- `LTX2_NAG`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXDirector`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`BasicScheduler`、`VAEDecodeTiled`、`LTXVAudioVAEEncode`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`VAELoaderKJ`、`SolidMask`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`PreviewAudio`、`DualCLIPLoader`、`SetLatentNoiseMask`、`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`PrimitiveBoolean`、`LTX2SamplingPreviewOverride`、`LTXVConditioning`、`LTXDirectorGuide`、`VisualizeSigmasKJ`、`KSamplerSelect`、`SamplerCustom`、`LTX2_NAG`、`LTXVSeparateAVLatent`、`LTXDirector`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、KSamplerSelect、MelBandRoFormerSampler、SamplerCustom、LTXVAudioVAEDecode、LTXVAudioVAEEncode
