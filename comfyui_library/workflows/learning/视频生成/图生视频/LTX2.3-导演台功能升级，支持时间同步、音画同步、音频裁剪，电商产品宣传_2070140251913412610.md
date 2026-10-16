---
key: 视频生成/图生视频/LTX2.3-导演台功能升级，支持时间同步、音画同步、音频裁剪，电商产品宣传_2070140251913412610.json
name: LTX2.3-导演台功能升级，支持时间同步、音画同步、音频裁剪，电商产品宣传_2070140251913412610.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2070140251913412610.json
hash: fbaedb7168031dc4
coverage: 0.885714
learned_at: 2026-10-15 22:40:36
nodes: [CLIPTextEncode, BasicScheduler, LTX2SamplingPreviewOverride, VAEDecodeTiled, VAELoaderKJ, VAELoaderKJ, LTXVAudioVAEDecode, VisualizeSigmasKJ, KSamplerSelect, LTXVConditioning, Note, LTXVCropGuides, SamplerCustom, LoraLoaderModelOnly, DualCLIPLoader, LoraLoaderModelOnly, LTX2_NAG, VHS_VideoCombine, LoadImage, ImageScaleToTotalPixels, SeedVR2BlockSwap, SeedVR2ExtraArgs, SaveImage, LTXVConcatAVLatent, LTXVSeparateAVLatent, SeedVR2, GuHaiAutoImageSplit, PreviewImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), UNETLoader, YusuLTXDirectorGuide, Label (rgthree), Label (rgthree), YusuLTXDirector]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3-导演台功能升级，支持时间同步、音画同步、音频裁剪，电商产品宣传_2070140251913412610.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070140251913412610.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `LTX2SamplingPreviewOverride`
- `VAEDecodeTiled` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTXVAudioVAEDecode` ★核心
- `VisualizeSigmasKJ`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `Note`
- `LTXVCropGuides`
- `SamplerCustom` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `VHS_VideoCombine`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SaveImage`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `SeedVR2`
- `GuHaiAutoImageSplit`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `YusuLTXDirectorGuide`
- `Label (rgthree)`
- `Label (rgthree)`
- `YusuLTXDirector`

## 知识

覆盖率 **89%**（31/35）

**有卡**：`CLIPTextEncode`、`BasicScheduler`、`LTX2SamplingPreviewOverride`、`VAEDecodeTiled`、`VAELoaderKJ`、`LTXVAudioVAEDecode`、`VisualizeSigmasKJ`、`KSamplerSelect`、`LTXVConditioning`、`LTXVCropGuides`、`SamplerCustom`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`LTX2_NAG`、`VHS_VideoCombine`、`LoadImage`、`ImageScaleToTotalPixels`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SaveImage`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`SeedVR2`、`GuHaiAutoImageSplit`、`UNETLoader`、`YusuLTXDirectorGuide`、`Label (rgthree)`、`YusuLTXDirector`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SeedVR2、SeedVR2BlockSwap、SeedVR2ExtraArgs
