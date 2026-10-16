---
key: 视频生成/图生视频/LTX2.3 MSR V2 (多主体参考) 图生视频_2083493730379722754.json
name: LTX2.3 MSR V2 (多主体参考) 图生视频_2083493730379722754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 MSR V2 (多主体参考) 图生视频_2083493730379722754.json
hash: 461c5a2ce7e5372b
coverage: 0.4375
learned_at: 2026-10-16 19:17:09
nodes: [GetNode, LTXAVTextEncoderLoader, LTXVAudioVAELoader, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, ManualSigmas, KSamplerSelect, RandomNoise, LTXVAudioVAEDecode, SetNode, SetNode, SetNode, GetNode, GetNode, VHS_VideoCombine, SetNode, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, ComfyMathExpression, INTConstant, LTXVCropGuides, VAEDecode, SamplerCustomAdvanced, CFGGuider, INTConstant, SetNode, GetNode, INTConstant, INTConstant, LTXICLoRALoaderModelOnly, SetNode, SetNode, LTXVConditioning, ComfyMathExpression, GetNode, GetNode, GetNode, SetNode, GetNode, LTXVEmptyLatentAudio, SetNode, SetNode, EmptyLTXVLatentVideo, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXAddVideoICLoRAGuide, GetNode, LTX2_NAG, LowVRAMCheckpointLoader, VHS_VideoCombine, CLIPTextEncode, SetNode, LoadImage, GetNode, GetNode, SetNode, LoadImage, LiconMSR, LoadImage, LoadImage, LoadImage, GetNode, PromptRelayEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 24, "width": 145}
---

# 视频生成/图生视频/LTX2.3 MSR V2 (多主体参考) 图生视频_2083493730379722754.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3 MSR V2 (多主体参考) 图生视频_2083493730379722754.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（80 个）：
- `GetNode`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `INTConstant`
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `INTConstant`
- `SetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `LTXICLoRALoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `LTXVConditioning`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `LTX2_NAG`
- `LowVRAMCheckpointLoader` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `SetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `LiconMSR`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `PromptRelayEncode`

## 关键参数

- `width` = `145`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **44%**（35/80）

**有卡**：`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`ManualSigmas`、`KSamplerSelect`、`RandomNoise`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`LTXVSeparateAVLatent`、`ComfyMathExpression`、`INTConstant`、`LTXVCropGuides`、`VAEDecode`、`SamplerCustomAdvanced`、`CFGGuider`、`LTXICLoRALoaderModelOnly`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`LTXAddVideoICLoRAGuide`、`LTX2_NAG`、`LowVRAMCheckpointLoader`、`CLIPTextEncode`、`LoadImage`、`LiconMSR`、`PromptRelayEncode`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
