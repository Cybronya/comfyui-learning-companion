---
key: 视频生成/图生视频/LTX-2.3 MSR V2参考生视频（AI短剧漫剧一键生成）_2079038691699412993.json
name: LTX-2.3 MSR V2参考生视频（AI短剧漫剧一键生成）_2079038691699412993.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3 MSR V2参考生视频（AI短剧漫剧一键生成）_2079038691699412993.json
hash: 921bf4d0c8637bf2
coverage: 1
learned_at: 2026-10-15 22:41:58
nodes: [RandomNoise, LTXVSetAudioRefTokens, LTXVSetAudioRefTokens, LTXVEmptyLatentAudio, LTXVAudioVAEDecode, KSamplerSelect, LTXVSeparateAVLatent, ManualSigmas, CFGGuider, LTXAddVideoICLoRAGuide, LTXVConditioning, LTXVConcatAVLatent, LTXVAudioVAELoader, CR Float To Integer, LowVRAMCheckpointLoader, LTXAVTextEncoderLoader, INTConstant, CLIPTextEncode, LTXICLoRALoaderModelOnly, SamplerCustomAdvanced, LTXVCropGuides, VAEDecode, CreateVideo, EmptyLTXVLatentVideo, LiconMSR, PromptRelayEncode, LoadImage, LTX2_NAG, LoadImage, CR Prompt Text, CR Prompt Text, SaveVideo, LoadImage, SimpleMath+, FloatConstant, LoadImage, INTConstant, INTConstant, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 50, "width": 241}
---

# 视频生成/图生视频/LTX-2.3 MSR V2参考生视频（AI短剧漫剧一键生成）_2079038691699412993.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2079038691699412993.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（39 个）：
- `RandomNoise`
- `LTXVSetAudioRefTokens`
- `LTXVSetAudioRefTokens`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVAudioVAEDecode` ★核心
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `CFGGuider`
- `LTXAddVideoICLoRAGuide`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `LTXVAudioVAELoader`
- `CR Float To Integer`
- `LowVRAMCheckpointLoader` ★核心
- `LTXAVTextEncoderLoader`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `LiconMSR`
- `PromptRelayEncode`
- `LoadImage`
- `LTX2_NAG`
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `SaveVideo`
- `LoadImage`
- `SimpleMath+`
- `FloatConstant`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `INTConstant`

## 关键参数

- `width` = `241`
- `height` = `50`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **100%**（39/39）

**有卡**：`RandomNoise`、`LTXVSetAudioRefTokens`、`LTXVEmptyLatentAudio`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`ManualSigmas`、`CFGGuider`、`LTXAddVideoICLoRAGuide`、`LTXVConditioning`、`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`CR Float To Integer`、`LowVRAMCheckpointLoader`、`LTXAVTextEncoderLoader`、`INTConstant`、`CLIPTextEncode`、`LTXICLoRALoaderModelOnly`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`VAEDecode`、`CreateVideo`、`EmptyLTXVLatentVideo`、`LiconMSR`、`PromptRelayEncode`、`LoadImage`、`LTX2_NAG`、`CR Prompt Text`、`SaveVideo`、`SimpleMath+`、`FloatConstant`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
