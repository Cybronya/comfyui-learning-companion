---
key: 数字人/数字人/竖屏短剧 多宫格工作流，六宫格 九宫格  全自动 LTX2.3 无字幕_2078050041528406017.json
name: 竖屏短剧 多宫格工作流，六宫格 九宫格  全自动 LTX2.3 无字幕_2078050041528406017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/竖屏短剧 多宫格工作流，六宫格 九宫格  全自动 LTX2.3 无字幕_2078050041528406017.json
hash: 4e62ed86c985bea3
coverage: 0.772727
learned_at: 2026-10-26 02:04:14
nodes: [Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ttN concat, RH_Utils, VAELoaderKJ, PrimitiveBoolean, SetLatentNoiseMask, BasicScheduler, VAEDecodeTiled, 孤海注释, KSamplerSelect, LayerColor: Levels, LTXVSeparateAVLatent, UNETLoader, Reroute, RH_RhartImageG2ImageToImage, RHHiddenNodes, VAELoaderKJ, LTXVCropGuides, LTX2SamplingPreviewOverride, DualCLIPLoader, LTXVConcatAVLatent, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, easy showAnything, Reroute, SolidMask, LTXVAudioVAEDecode, ComfySwitchNode, Reroute, LTXVAudioVAEEncode, MelBandRoFormerModelLoader, VisualizeSigmasKJ, ShowAnything|Mie, ttN concat, JjkText, CR Text Concatenate, SaveImage, RH_LLMAPI_Pro_Node, PreviewImage, ImageRGBChannel, LTXVConditioning, LTX2_NAG, YusuLTXDirectorGuide, easy showAnything, PreviewAudio, MelBandRoFormerSampler, TextInput_, CS-LTXGridDirector, SamplerCustom, VHS_VideoCombine, Int, LoadImage, LoadImage, LoadImage, LoadImage, TextInput_, CLIPTextEncode]
patterns: []
missing: []
---

# 数字人/数字人/竖屏短剧 多宫格工作流，六宫格 九宫格  全自动 LTX2.3 无字幕_2078050041528406017.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/竖屏短剧 多宫格工作流，六宫格 九宫格  全自动 LTX2.3 无字幕_2078050041528406017.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ttN concat`
- `RH_Utils`
- `VAELoaderKJ`
- `PrimitiveBoolean`
- `SetLatentNoiseMask`
- `BasicScheduler`
- `VAEDecodeTiled` ★核心
- `孤海注释`
- `KSamplerSelect` ★核心
- `LayerColor: Levels`
- `LTXVSeparateAVLatent`
- `UNETLoader` ★核心
- `Reroute`
- `RH_RhartImageG2ImageToImage`
- `RHHiddenNodes`
- `VAELoaderKJ`
- `LTXVCropGuides`
- `LTX2SamplingPreviewOverride`
- `DualCLIPLoader`
- `LTXVConcatAVLatent`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `Reroute`
- `SolidMask`
- `LTXVAudioVAEDecode` ★核心
- `ComfySwitchNode`
- `Reroute`
- `LTXVAudioVAEEncode` ★核心
- `MelBandRoFormerModelLoader`
- `VisualizeSigmasKJ`
- `ShowAnything|Mie`
- `ttN concat`
- `JjkText`
- `CR Text Concatenate`
- `SaveImage`
- `RH_LLMAPI_Pro_Node`
- `PreviewImage`
- `ImageRGBChannel`
- `LTXVConditioning`
- `LTX2_NAG`
- `YusuLTXDirectorGuide`
- `easy showAnything`
- `PreviewAudio`
- `MelBandRoFormerSampler` ★核心
- `TextInput_`
- `CS-LTXGridDirector`
- `SamplerCustom` ★核心
- `VHS_VideoCombine`
- `Int`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextInput_`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **77%**（51/66）

**有卡**：`ttN concat`、`RH_Utils`、`VAELoaderKJ`、`PrimitiveBoolean`、`SetLatentNoiseMask`、`BasicScheduler`、`VAEDecodeTiled`、`KSamplerSelect`、`LayerColor: Levels`、`LTXVSeparateAVLatent`、`UNETLoader`、`RH_RhartImageG2ImageToImage`、`RHHiddenNodes`、`LTXVCropGuides`、`LTX2SamplingPreviewOverride`、`DualCLIPLoader`、`LTXVConcatAVLatent`、`LoraLoaderModelOnly`、`SolidMask`、`LTXVAudioVAEDecode`、`LTXVAudioVAEEncode`、`MelBandRoFormerModelLoader`、`VisualizeSigmasKJ`、`ShowAnything|Mie`、`CR Text Concatenate`、`SaveImage`、`RH_LLMAPI_Pro_Node`、`ImageRGBChannel`、`LTXVConditioning`、`LTX2_NAG`、`YusuLTXDirectorGuide`、`PreviewAudio`、`MelBandRoFormerSampler`、`TextInput_`、`CS-LTXGridDirector`、`SamplerCustom`、`VHS_VideoCombine`、`Int`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler、LTXVConcatAVLatent
