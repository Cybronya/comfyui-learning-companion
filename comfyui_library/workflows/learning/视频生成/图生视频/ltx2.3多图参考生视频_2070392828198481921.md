---
key: 视频生成/图生视频/ltx2.3多图参考生视频_2070392828198481921.json
name: ltx2.3多图参考生视频_2070392828198481921.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/ltx2.3多图参考生视频_2070392828198481921.json
hash: 90262a4cad51a3c0
coverage: 0.970588
learned_at: 2026-10-15 22:40:38
nodes: [CLIPTextEncode, CLIPTextEncode, LTXVEmptyLatentAudio, INTConstant, CR Float To Integer, VAELoaderKJ, INTConstant, PrimitiveFloat, LTXAVTextEncoderLoader, VHS_VideoCombine, CFGGuider, VHS_VideoCombine, INTConstant, ManualSigmas, KSamplerSelect, RandomNoise, LTXICLoRALoaderModelOnly, LiconMSR, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXAddVideoICLoRAGuide, LTXVCropGuides, LTXVAudioVAEDecode, VAEDecode, LoadImage, LoadImage, EmptyLTXVLatentVideo, LTXVConditioning, LowVRAMCheckpointLoader, LoadImage, LoadImage, LoadImage, LTXVAddGuideMulti]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-fp8.safetensors", "height": 24, "width": 145}
---

# 视频生成/图生视频/ltx2.3多图参考生视频_2070392828198481921.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070392828198481921.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（34 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `INTConstant`
- `CR Float To Integer`
- `VAELoaderKJ`
- `INTConstant`
- `PrimitiveFloat`
- `LTXAVTextEncoderLoader`
- `VHS_VideoCombine`
- `CFGGuider`
- `VHS_VideoCombine`
- `INTConstant`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXICLoRALoaderModelOnly` ★核心
- `LiconMSR`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXAddVideoICLoRAGuide`
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `LowVRAMCheckpointLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LTXVAddGuideMulti`

## 关键参数

- `width` = `145`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-fp8.safetensors`

## 知识

覆盖率 **97%**（33/34）

**有卡**：`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`INTConstant`、`CR Float To Integer`、`VAELoaderKJ`、`LTXAVTextEncoderLoader`、`VHS_VideoCombine`、`CFGGuider`、`ManualSigmas`、`KSamplerSelect`、`RandomNoise`、`LTXICLoRALoaderModelOnly`、`LiconMSR`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LTXAddVideoICLoRAGuide`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`VAEDecode`、`LoadImage`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`LowVRAMCheckpointLoader`、`LTXVAddGuideMulti`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
