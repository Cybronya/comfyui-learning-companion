---
key: 视频生成/图生视频/Cosmic-RaysX-LTX2.3-LTX Director-导演分镜工作流-电商带货_2078887009887809537.json
name: Cosmic-RaysX-LTX2.3-LTX Director-导演分镜工作流-电商带货_2078887009887809537.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Cosmic-RaysX-LTX2.3-LTX Director-导演分镜工作流-电商带货_2078887009887809537.json
hash: c03c96a1d458efa1
coverage: 0.9
learned_at: 2026-10-15 22:41:57
nodes: [ImageScaleToTotalPixels, SeedVR2BlockSwap, SeedVR2ExtraArgs, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, VAELoaderKJ, LTXVAudioVAEDecode, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoaderKJ, DualCLIPLoader, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), MuyeTextEditOutput, PreviewAny, CLIPTextEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVCropGuides, LTXDirectorGuide, SamplerCustom, LTX2SamplingPreviewOverride, VisualizeSigmasKJ, BasicScheduler, SaveImage, SeedVR2, LoadImage, CS-LTXGridDirector, PreviewImage, GuHaiAutoImageSplit, LTX2_NAG, KSamplerSelect, LTXVConditioning, CreateVideo, VAEDecodeTiled, GetVideoComponents, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 视频生成/图生视频/Cosmic-RaysX-LTX2.3-LTX Director-导演分镜工作流-电商带货_2078887009887809537.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2078887009887809537.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `ImageScaleToTotalPixels`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `LTXVAudioVAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `MuyeTextEditOutput`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXDirectorGuide`
- `SamplerCustom` ★核心
- `LTX2SamplingPreviewOverride`
- `VisualizeSigmasKJ`
- `BasicScheduler`
- `SaveImage`
- `SeedVR2`
- `LoadImage`
- `CS-LTXGridDirector`
- `PreviewImage`
- `GuHaiAutoImageSplit`
- `LTX2_NAG`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `GetVideoComponents`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **90%**（36/40）

**有卡**：`ImageScaleToTotalPixels`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`LoraLoaderModelOnly`、`VAELoaderKJ`、`LTXVAudioVAEDecode`、`CheckpointLoaderSimple`、`DualCLIPLoader`、`MuyeTextEditOutput`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXDirectorGuide`、`SamplerCustom`、`LTX2SamplingPreviewOverride`、`VisualizeSigmasKJ`、`BasicScheduler`、`SaveImage`、`SeedVR2`、`LoadImage`、`CS-LTXGridDirector`、`GuHaiAutoImageSplit`、`LTX2_NAG`、`KSamplerSelect`、`LTXVConditioning`、`CreateVideo`、`VAEDecodeTiled`、`GetVideoComponents`、`VHS_VideoCombine`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、SaveImage、LoadImage、KSamplerSelect、SeedVR2、SeedVR2BlockSwap
