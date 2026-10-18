---
key: 视频生成/图生视频/LTX-2.3-MSR多图参考视频生成V2_2079024443669696513.json
name: LTX-2.3-MSR多图参考视频生成V2_2079024443669696513.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3-MSR多图参考视频生成V2_2079024443669696513.json
hash: 9703ab5582141dca
coverage: 0.926829
learned_at: 2026-10-15 22:41:58
nodes: [LTXVConditioning, LTXAddVideoICLoRAGuide, LTX2_NAG, LTXVEmptyLatentAudio, INTConstant, SimpleMath+, EmptyLTXVLatentVideo, CR Float To Integer, CreateVideo, ManualSigmas, LTXVConcatAVLatent, KSamplerSelect, RandomNoise, LoadImage, LoadImage, LoadImage, LowVRAMCheckpointLoader, LTXICLoRALoaderModelOnly, CLIPTextEncode, MarkdownNote, VAEDecode, SaveVideo, CFGGuider, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LiconMSR, LoadImage, LoadImage, CR Prompt Text, CR Prompt Text, INTConstant, Note, Note, PromptRelayEncode, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVCropGuides, SamplerCustomAdvanced, INTConstant, INTConstant, FloatConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 50, "width": 241}
---

# 视频生成/图生视频/LTX-2.3-MSR多图参考视频生成V2_2079024443669696513.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2079024443669696513.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（41 个）：
- `LTXVConditioning`
- `LTXAddVideoICLoRAGuide`
- `LTX2_NAG`
- `LTXVEmptyLatentAudio` ★核心
- `INTConstant`
- `SimpleMath+`
- `EmptyLTXVLatentVideo`
- `CR Float To Integer`
- `CreateVideo`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LowVRAMCheckpointLoader` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `SaveVideo`
- `CFGGuider`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LiconMSR`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `INTConstant`
- `Note`
- `Note`
- `PromptRelayEncode`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `INTConstant`
- `INTConstant`
- `FloatConstant`

## 关键参数

- `width` = `241`
- `height` = `50`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **93%**（38/41）

**有卡**：`LTXVConditioning`、`LTXAddVideoICLoRAGuide`、`LTX2_NAG`、`LTXVEmptyLatentAudio`、`INTConstant`、`SimpleMath+`、`EmptyLTXVLatentVideo`、`CR Float To Integer`、`CreateVideo`、`ManualSigmas`、`LTXVConcatAVLatent`、`KSamplerSelect`、`RandomNoise`、`LoadImage`、`LowVRAMCheckpointLoader`、`LTXICLoRALoaderModelOnly`、`CLIPTextEncode`、`VAEDecode`、`SaveVideo`、`CFGGuider`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LiconMSR`、`CR Prompt Text`、`PromptRelayEncode`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`FloatConstant`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
