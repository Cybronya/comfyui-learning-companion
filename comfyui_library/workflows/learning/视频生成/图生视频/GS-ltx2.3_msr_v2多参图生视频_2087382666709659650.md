---
key: 视频生成/图生视频/GS-ltx2.3_msr_v2多参图生视频_2087382666709659650.json
name: GS-ltx2.3_msr_v2多参图生视频_2087382666709659650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/GS-ltx2.3_msr_v2多参图生视频_2087382666709659650.json
hash: 5b67b906ab0e3e82
coverage: 1
learned_at: 2026-10-16 21:27:29
nodes: [LTXVSetAudioRefTokens, LTXVSetAudioRefTokens, LoadImage, CreateVideo, VAEDecode, LTXVCropGuides, LTXVAudioVAEDecode, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, SimpleMath+, CR Float To Integer, INTConstant, EmptyLTXVLatentVideo, CLIPTextEncode, LTXVConditioning, LTXAddVideoICLoRAGuide, LTX2_NAG, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, SaveVideo, SamplerCustomAdvanced, LoadVideo, LoadVideo, RandomNoise, LoadVideo, LoadVideo, LoadImage, LiconMSR, LowVRAMCheckpointLoader, LTXVAudioVAELoader, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXAVTextEncoderLoader, LoadImage, LoadImage, LoadImage, PromptRelayEncode, INTConstant, INTConstant, FloatConstant, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 50, "width": 241}
---

# 视频生成/图生视频/GS-ltx2.3_msr_v2多参图生视频_2087382666709659650.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/GS-ltx2.3_msr_v2多参图生视频_2087382666709659650.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（45 个）：
- `LTXVSetAudioRefTokens`
- `LTXVSetAudioRefTokens`
- `LoadImage`
- `CreateVideo`
- `VAEDecode` ★核心
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SimpleMath+`
- `CR Float To Integer`
- `INTConstant`
- `EmptyLTXVLatentVideo`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXAddVideoICLoRAGuide`
- `LTX2_NAG`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `LoadImage`
- `SaveVideo`
- `SamplerCustomAdvanced` ★核心
- `LoadVideo`
- `LoadVideo`
- `RandomNoise`
- `LoadVideo`
- `LoadVideo`
- `LoadImage`
- `LiconMSR`
- `LowVRAMCheckpointLoader` ★核心
- `LTXVAudioVAELoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PromptRelayEncode`
- `INTConstant`
- `INTConstant`
- `FloatConstant`
- `INTConstant`

## 关键参数

- `width` = `241`
- `height` = `50`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **100%**（45/45）

**有卡**：`LTXVSetAudioRefTokens`、`LoadImage`、`CreateVideo`、`VAEDecode`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`SimpleMath+`、`CR Float To Integer`、`INTConstant`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`LTXVConditioning`、`LTXAddVideoICLoRAGuide`、`LTX2_NAG`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`SaveVideo`、`SamplerCustomAdvanced`、`LoadVideo`、`RandomNoise`、`LiconMSR`、`LowVRAMCheckpointLoader`、`LTXVAudioVAELoader`、`LTXICLoRALoaderModelOnly`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`PromptRelayEncode`、`FloatConstant`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
