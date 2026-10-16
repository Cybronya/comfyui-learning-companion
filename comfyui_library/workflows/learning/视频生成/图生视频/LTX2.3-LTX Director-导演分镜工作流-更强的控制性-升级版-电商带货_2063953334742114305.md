---
key: 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-升级版-电商带货_2063953334742114305.json
name: LTX2.3-LTX Director-导演分镜工作流-更强的控制性-升级版-电商带货_2063953334742114305.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2063953334742114305.json
hash: 6e234f96cb06fd2e
coverage: 0.875
learned_at: 2026-10-15 22:39:18
nodes: [ImageScaleToTotalPixels, SeedVR2BlockSwap, SeedVR2ExtraArgs, SaveImage, SeedVR2, Fast Groups Bypasser (rgthree), CLIPTextEncode, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, LTX2SamplingPreviewOverride, BasicScheduler, LTXVConcatAVLatent, LTX2_NAG, SamplerCustom, LTXVSeparateAVLatent, LTXVCropGuides, VAEDecodeTiled, CreateVideo, GetVideoComponents, LTXVAudioVAEDecode, VHS_VideoCombine, LoadImage, GuHaiAutoImageSplit, PreviewImage, Fast Groups Bypasser (rgthree), 孤海注释, VHS_VideoCombine, MarkdownNote, VisualizeSigmasKJ, KSamplerSelect, YusuLTXDirector, LTXDirectorGuide, LTXVConditioning]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-升级版-电商带货_2063953334742114305.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063953334742114305.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `ImageScaleToTotalPixels`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SaveImage`
- `SeedVR2`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTX2SamplingPreviewOverride`
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `LTX2_NAG`
- `SamplerCustom` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `GetVideoComponents`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `GuHaiAutoImageSplit`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `孤海注释`
- `VHS_VideoCombine`
- `MarkdownNote`
- `VisualizeSigmasKJ`
- `KSamplerSelect` ★核心
- `YusuLTXDirector`
- `LTXDirectorGuide`
- `LTXVConditioning`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`ImageScaleToTotalPixels`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SaveImage`、`SeedVR2`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoaderKJ`、`LTX2SamplingPreviewOverride`、`BasicScheduler`、`LTXVConcatAVLatent`、`LTX2_NAG`、`SamplerCustom`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecodeTiled`、`CreateVideo`、`GetVideoComponents`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`LoadImage`、`GuHaiAutoImageSplit`、`VisualizeSigmasKJ`、`KSamplerSelect`、`YusuLTXDirector`、`LTXDirectorGuide`、`LTXVConditioning`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、KSamplerSelect、SeedVR2、SeedVR2BlockSwap、SeedVR2ExtraArgs
