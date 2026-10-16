---
key: 视频生成/图生视频/MSR_角色道具参考-ltx2.3_2067174173994213378.json
name: MSR_角色道具参考-ltx2.3_2067174173994213378.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067174173994213378.json
hash: da670cf35b29f701
coverage: 0.418605
learned_at: 2026-10-15 22:39:57
nodes: [LTXAVTextEncoderLoader, LowVRAMCheckpointLoader, LTXVAudioVAELoader, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, CFGGuider, ManualSigmas, KSamplerSelect, RandomNoise, LTXVAudioVAEDecode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, ComfyMathExpression, LTXVConditioning, VHS_VideoCombine, GetNode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, SamplerCustomAdvanced, ComfyMathExpression, VAEDecode, INTConstant, SetNode, GetNode, GetNode, GetNode, SetNode, LoadImage, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, INTConstant, GetNode, GetNode, SetNode, SetNode, SetNode, VHS_VideoCombine, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, GetNode, GetNode, LiconMSR, GetNode, GetNode, GetNode, SetNode, LTXVCropGuides, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, GetNode, LTXVAddGuideMulti, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, SetNode, LTXAddVideoICLoRAGuide, GetNode, SetNode, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, GetNode, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 24, "width": 145}
---

# 视频生成/图生视频/MSR_角色道具参考-ltx2.3_2067174173994213378.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067174173994213378.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（86 个）：
- `LTXAVTextEncoderLoader`
- `LowVRAMCheckpointLoader` ★核心
- `LTXVAudioVAELoader`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CFGGuider`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `LTXVConditioning`
- `VHS_VideoCombine`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `VAEDecode` ★核心
- `INTConstant`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `LiconMSR`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAddGuideMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`
- `width` = `145`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **42%**（36/86）

**有卡**：`LTXAVTextEncoderLoader`、`LowVRAMCheckpointLoader`、`LTXVAudioVAELoader`、`CFGGuider`、`ManualSigmas`、`KSamplerSelect`、`RandomNoise`、`LTXVAudioVAEDecode`、`ComfyMathExpression`、`LTXVConditioning`、`VHS_VideoCombine`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`VAEDecode`、`INTConstant`、`LoadImage`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`LiconMSR`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVAddGuideMulti`、`LTXVConcatAVLatent`、`LTXAddVideoICLoRAGuide`、`CLIPTextEncode`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
