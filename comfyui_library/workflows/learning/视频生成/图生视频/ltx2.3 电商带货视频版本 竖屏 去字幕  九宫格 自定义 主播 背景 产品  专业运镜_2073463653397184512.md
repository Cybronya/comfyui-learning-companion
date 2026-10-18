---
key: 视频生成/图生视频/ltx2.3 电商带货视频版本 竖屏 去字幕  九宫格 自定义 主播 背景 产品  专业运镜_2073463653397184512.json
name: ltx2.3 电商带货视频版本 竖屏 去字幕  九宫格 自定义 主播 背景 产品  专业运镜_2073463653397184512.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/ltx2.3 电商带货视频版本 竖屏 去字幕  九宫格 自定义 主播 背景 产品  专业运镜_2073463653397184512.json
hash: ac79b40d8d27ddef
coverage: 0.772727
learned_at: 2026-10-15 22:41:07
nodes: [Reroute, Reroute, Reroute, easy showAnything, VAELoaderKJ, MelBandRoFormerModelLoader, PrimitiveBoolean, Reroute, ComfySwitchNode, MelBandRoFormerSampler, SolidMask, LTXVAudioVAEEncode, SetLatentNoiseMask, Reroute, BasicScheduler, VAEDecodeTiled, KSamplerSelect, LTXVSeparateAVLatent, PreviewAudio, LoadImage, LoadImage, PreviewImage, VAELoaderKJ, LTXVCropGuides, SamplerCustom, LTX2SamplingPreviewOverride, LTX2_NAG, DualCLIPLoader, YusuLTXDirectorGuide, LTXVConcatAVLatent, VisualizeSigmasKJ, LoadImage, ShowAnything|Mie, UNETLoader, LoraLoaderModelOnly, ttN concat, RH_Utils, 孤海注释, Int, LTXVAudioVAEDecode, LTXVConditioning, VHS_VideoCombine, ttN concat, ImageRGBChannel, Reroute, Reroute, Reroute, Reroute, CR Text Concatenate, RHHiddenNodes, easy showAnything, JjkText, SaveImage, RH_LLMAPI_Pro_Node, TextInput_, CS-LTXGridDirector, TextInput_, LayerColor: Levels, RH_Nano_Banana2_Image2Image, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 视频生成/图生视频/ltx2.3 电商带货视频版本 竖屏 去字幕  九宫格 自定义 主播 背景 产品  专业运镜_2073463653397184512.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073463653397184512.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `easy showAnything`
- `VAELoaderKJ`
- `MelBandRoFormerModelLoader`
- `PrimitiveBoolean`
- `Reroute`
- `ComfySwitchNode`
- `MelBandRoFormerSampler` ★核心
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `Reroute`
- `BasicScheduler`
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `PreviewAudio`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `VAELoaderKJ`
- `LTXVCropGuides`
- `SamplerCustom` ★核心
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `DualCLIPLoader`
- `YusuLTXDirectorGuide`
- `LTXVConcatAVLatent`
- `VisualizeSigmasKJ`
- `LoadImage`
- `ShowAnything|Mie`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ttN concat`
- `RH_Utils`
- `孤海注释`
- `Int`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `VHS_VideoCombine`
- `ttN concat`
- `ImageRGBChannel`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CR Text Concatenate`
- `RHHiddenNodes`
- `easy showAnything`
- `JjkText`
- `SaveImage`
- `RH_LLMAPI_Pro_Node`
- `TextInput_`
- `CS-LTXGridDirector`
- `TextInput_`
- `LayerColor: Levels`
- `RH_Nano_Banana2_Image2Image`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **77%**（51/66）

**有卡**：`VAELoaderKJ`、`MelBandRoFormerModelLoader`、`PrimitiveBoolean`、`MelBandRoFormerSampler`、`SolidMask`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`BasicScheduler`、`VAEDecodeTiled`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`PreviewAudio`、`LoadImage`、`LTXVCropGuides`、`SamplerCustom`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`DualCLIPLoader`、`YusuLTXDirectorGuide`、`LTXVConcatAVLatent`、`VisualizeSigmasKJ`、`ShowAnything|Mie`、`UNETLoader`、`LoraLoaderModelOnly`、`ttN concat`、`RH_Utils`、`Int`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`VHS_VideoCombine`、`ImageRGBChannel`、`CR Text Concatenate`、`RHHiddenNodes`、`SaveImage`、`RH_LLMAPI_Pro_Node`、`TextInput_`、`CS-LTXGridDirector`、`LayerColor: Levels`、`RH_Nano_Banana2_Image2Image`、`CLIPTextEncode`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler、LTXVConcatAVLatent
