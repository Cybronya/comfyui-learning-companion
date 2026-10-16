---
key: 视频生成/图生视频/牛叉 爆款视频反推+产品带货视频 LTX2.3导演台 生成，竖版全自动 去字幕 四宫格六宫格九宫格_2069522054554148865.json
name: 牛叉 爆款视频反推+产品带货视频 LTX2.3导演台 生成，竖版全自动 去字幕 四宫格六宫格九宫格_2069522054554148865.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2069522054554148865.json
hash: 4140c0bc0e98a386
coverage: 0.87931
learned_at: 2026-10-15 22:40:30
nodes: [VAELoaderKJ, SetLatentNoiseMask, SamplerCustom, LTXVSeparateAVLatent, LTXVCropGuides, Reroute, VAELoaderKJ, Reroute, LTX2SamplingPreviewOverride, VAEDecodeTiled, DualCLIPLoader, LoraLoaderModelOnly, BasicScheduler, VisualizeSigmasKJ, LTXVAudioVAEDecode, LoraLoaderModelOnly, PrimitiveBoolean, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ComfySwitchNode, LTXVAudioVAEEncode, SolidMask, PreviewAudio, UNETLoader, ShellAgentPluginOutputText, easy imageSave, Preview from image [Crystools], LayerColor: Levels, CR Text, VHS_VideoCombine, YusuLTXDirectorGuide, LTXVConditioning, LTX2_NAG, KSamplerSelect, LTXVConcatAVLatent, easy showAnything, PreviewAny, LoraLoaderModelOnly, 孤海注释, RHHiddenNodes, LoadImage, LoadImage, LoadImage, LoadImage, LoadVideo, 孤海注释, CS-LTXGridDirector, RH_LLMAPI_Pro_Node, ImageRGBChannel, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, RH_Nano_Banana2_Image2Image, MuyeTextEditOutput, RH_LLMAPI_Pro_Node, MuyeTextEditOutput]
patterns: []
missing: []
---

# 视频生成/图生视频/牛叉 爆款视频反推+产品带货视频 LTX2.3导演台 生成，竖版全自动 去字幕 四宫格六宫格九宫格_2069522054554148865.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2069522054554148865.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `VAELoaderKJ`
- `SetLatentNoiseMask`
- `SamplerCustom` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `Reroute`
- `VAELoaderKJ`
- `Reroute`
- `LTX2SamplingPreviewOverride`
- `VAEDecodeTiled` ★核心
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `VisualizeSigmasKJ`
- `LTXVAudioVAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveBoolean`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `ComfySwitchNode`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `PreviewAudio`
- `UNETLoader` ★核心
- `ShellAgentPluginOutputText`
- `easy imageSave`
- `Preview from image [Crystools]`
- `LayerColor: Levels`
- `CR Text`
- `VHS_VideoCombine`
- `YusuLTXDirectorGuide`
- `LTXVConditioning`
- `LTX2_NAG`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `easy showAnything`
- `PreviewAny`
- `LoraLoaderModelOnly` ★核心
- `孤海注释`
- `RHHiddenNodes`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadVideo`
- `孤海注释`
- `CS-LTXGridDirector`
- `RH_LLMAPI_Pro_Node`
- `ImageRGBChannel`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `RH_Nano_Banana2_Image2Image`
- `MuyeTextEditOutput`
- `RH_LLMAPI_Pro_Node`
- `MuyeTextEditOutput`

## 知识

覆盖率 **88%**（51/58）

**有卡**：`VAELoaderKJ`、`SetLatentNoiseMask`、`SamplerCustom`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTX2SamplingPreviewOverride`、`VAEDecodeTiled`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`BasicScheduler`、`VisualizeSigmasKJ`、`LTXVAudioVAEDecode`、`PrimitiveBoolean`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SolidMask`、`PreviewAudio`、`UNETLoader`、`ShellAgentPluginOutputText`、`easy imageSave`、`Preview from image [Crystools]`、`LayerColor: Levels`、`CR Text`、`VHS_VideoCombine`、`YusuLTXDirectorGuide`、`LTXVConditioning`、`LTX2_NAG`、`KSamplerSelect`、`LTXVConcatAVLatent`、`RHHiddenNodes`、`LoadImage`、`LoadVideo`、`CS-LTXGridDirector`、`RH_LLMAPI_Pro_Node`、`ImageRGBChannel`、`CLIPTextEncode`、`RH_Nano_Banana2_Image2Image`、`MuyeTextEditOutput`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler、LTXVConcatAVLatent
