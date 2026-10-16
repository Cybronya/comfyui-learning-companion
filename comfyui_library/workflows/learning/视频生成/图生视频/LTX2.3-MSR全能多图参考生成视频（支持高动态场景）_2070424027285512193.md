---
key: 视频生成/图生视频/LTX2.3-MSR全能多图参考生成视频（支持高动态场景）_2070424027285512193.json
name: LTX2.3-MSR全能多图参考生成视频（支持高动态场景）_2070424027285512193.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2070424027285512193.json
hash: 3d9d605a3be73a77
coverage: 0.970588
learned_at: 2026-10-15 22:40:39
nodes: [KSamplerSelect, LTXVCropGuides, LTXVSeparateAVLatent, LTX2SamplingPreviewOverride, VisualizeSigmasKJ, LTXVConcatAVLatent, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, SamplerCustom, CLIPTextEncode, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, VAEDecodeTiled, LTXAddVideoICLoRAGuide, BasicScheduler, Reroute, SimpleMath+, VHS_VideoCombine, LTX2_NAG, LTXVConditioning, INTConstant, LoadImage, UNETLoader, LiconMSR, INTConstant, Float, INTConstant, LoadImage, VHS_VideoCombine, LoadImage, CLIPTextEncode, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 50, "width": 241}
---

# 视频生成/图生视频/LTX2.3-MSR全能多图参考生成视频（支持高动态场景）_2070424027285512193.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070424027285512193.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（34 个）：
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTX2SamplingPreviewOverride`
- `VisualizeSigmasKJ`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `SamplerCustom` ★核心
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `VAEDecodeTiled` ★核心
- `LTXAddVideoICLoRAGuide`
- `BasicScheduler`
- `Reroute`
- `SimpleMath+`
- `VHS_VideoCombine`
- `LTX2_NAG`
- `LTXVConditioning`
- `INTConstant`
- `LoadImage`
- `UNETLoader` ★核心
- `LiconMSR`
- `INTConstant`
- `Float`
- `INTConstant`
- `LoadImage`
- `VHS_VideoCombine`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVAudioVAEDecode` ★核心

## 关键参数

- `width` = `241`
- `height` = `50`
- `batch_size` = `1`

## 知识

覆盖率 **97%**（33/34）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTX2SamplingPreviewOverride`、`VisualizeSigmasKJ`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`SamplerCustom`、`CLIPTextEncode`、`DualCLIPLoader`、`VAELoaderKJ`、`VAEDecodeTiled`、`LTXAddVideoICLoRAGuide`、`BasicScheduler`、`SimpleMath+`、`VHS_VideoCombine`、`LTX2_NAG`、`LTXVConditioning`、`INTConstant`、`LoadImage`、`UNETLoader`、`LiconMSR`、`Float`、`LTXICLoRALoaderModelOnly`、`LTXVAudioVAEDecode`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent、VAEDecodeTiled
