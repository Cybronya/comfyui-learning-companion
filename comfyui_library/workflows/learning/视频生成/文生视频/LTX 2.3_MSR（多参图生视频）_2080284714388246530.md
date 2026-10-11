---
key: 视频生成/文生视频/LTX 2.3_MSR（多参图生视频）_2080284714388246530.json
name: LTX 2.3_MSR（多参图生视频）_2080284714388246530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3_MSR（多参图生视频）_2080284714388246530.json
hash: 35c065a999be552b
coverage: 0.705882
learned_at: 2026-10-11 20:38:33
nodes: [LTXVAudioVAELoader, CLIPTextEncode, LTXVConditioning, LTXAddVideoICLoRAGuide, EmptyLTXVLatentVideo, LTX2_NAG, LTXVConcatAVLatent, CFGGuider, ManualSigmas, KSamplerSelect, SamplerCustomAdvanced, LowVRAMCheckpointLoader, LTXICLoRALoaderModelOnly, RandomNoise, LTXVSeparateAVLatent, LTXVCropGuides, LiconMSR, INTConstant, INTConstant, SetNode, ImageScale, ImageScale, SetNode, SetNode, GetNode, GetNode, GetNode, ImageScale, LoadImage, ImageScale, SetNode, LoadImage, LoadImage, LoadImage, PromptRelayEncode, LTXAVTextEncoderLoader, SetNode, SetNode, CR Prompt Text, FloatConstant, VAEDecode, GetNode, INTConstant, VHS_VideoCombine, LTXVAudioVAEDecode, GetNode, SimpleMath+, GetNode, CM_FloatToInt, LTXVEmptyLatentAudio, CR Prompt Text]
patterns: []
missing: [SimpleMath+, CR Prompt Text, CR Prompt Text]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 50, "width": 241}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX 2.3_MSR（多参图生视频）_2080284714388246530.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3_MSR（多参图生视频）_2080284714388246530.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（51 个）：
- `LTXVAudioVAELoader`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXAddVideoICLoRAGuide`
- `EmptyLTXVLatentVideo`
- `LTX2_NAG`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LowVRAMCheckpointLoader` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LiconMSR`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `ImageScale`
- `ImageScale`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageScale`
- `LoadImage`
- `ImageScale`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PromptRelayEncode`
- `LTXAVTextEncoderLoader`
- `SetNode`
- `SetNode`
- `CR Prompt Text`
- `FloatConstant`
- `VAEDecode` ★核心
- `GetNode`
- `INTConstant`
- `VHS_VideoCombine`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `CM_FloatToInt`
- `LTXVEmptyLatentAudio` ★核心
- `CR Prompt Text`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`
- `width` = `241`
- `height` = `50`
- `batch_size` = `1`

## 知识

覆盖率 **71%**（36/51）

**有卡**：`LTXVAudioVAELoader`、`CLIPTextEncode`、`LTXVConditioning`、`LTXAddVideoICLoRAGuide`、`EmptyLTXVLatentVideo`、`LTX2_NAG`、`LTXVConcatAVLatent`、`CFGGuider`、`ManualSigmas`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LowVRAMCheckpointLoader`、`LTXICLoRALoaderModelOnly`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LiconMSR`、`INTConstant`、`ImageScale`、`LoadImage`、`PromptRelayEncode`、`LTXAVTextEncoderLoader`、`FloatConstant`、`VAEDecode`、`VHS_VideoCombine`、`LTXVAudioVAEDecode`、`CM_FloatToInt`、`LTXVEmptyLatentAudio`

**缺卡**（3）：`SimpleMath+`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
