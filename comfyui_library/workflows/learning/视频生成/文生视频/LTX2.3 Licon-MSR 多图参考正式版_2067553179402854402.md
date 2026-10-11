---
key: 视频生成/文生视频/LTX2.3 Licon-MSR 多图参考正式版_2067553179402854402.json
name: LTX2.3 Licon-MSR 多图参考正式版_2067553179402854402
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 Licon-MSR 多图参考正式版_2067553179402854402.json
hash: b6719849261e4cf4
coverage: 0.95
learned_at: 2026-10-11 20:21:25
nodes: [LTXVSetAudioRefTokens, LTXVSetAudioRefTokens, LTXVCropGuides, SamplerCustomAdvanced, LTXVAudioVAEDecode, VAEDecode, CreateVideo, LTXVConcatAVLatent, ManualSigmas, RandomNoise, LTXVConditioning, LTX2_NAG, CFGGuider, KSamplerSelect, LTXVSeparateAVLatent, CM_IntToFloat, SimpleCalculatorKJ, CLIPTextEncode, EmptyLTXVLatentVideo, SaveVideo, LowVRAMCheckpointLoader, LTXICLoRALoaderModelOnly, LTXAVTextEncoderLoader, LTXVAudioVAELoader, INTConstant, INTConstant, INTConstant, INTConstant, LiconMSR, LTXVEmptyLatentAudio, LTXAddVideoICLoRAGuide, LoadImage, LoadImage, LoadImage, PromptRelayEncode, LoadImage, LoadImage, PrimitiveStringMultiline, PrimitiveStringMultiline, PromptRelayEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 24, "width": 241}
---

# 视频生成/文生视频/LTX2.3 Licon-MSR 多图参考正式版_2067553179402854402.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 Licon-MSR 多图参考正式版_2067553179402854402.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（40 个）：
- `LTXVSetAudioRefTokens`
- `LTXVSetAudioRefTokens`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `RandomNoise`
- `LTXVConditioning`
- `LTX2_NAG`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `CM_IntToFloat`
- `SimpleCalculatorKJ`
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `SaveVideo`
- `LowVRAMCheckpointLoader` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `LiconMSR`
- `LTXVEmptyLatentAudio` ★核心
- `LTXAddVideoICLoRAGuide`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PromptRelayEncode`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PromptRelayEncode`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`
- `width` = `241`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`LTXVSetAudioRefTokens`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`VAEDecode`、`CreateVideo`、`LTXVConcatAVLatent`、`ManualSigmas`、`RandomNoise`、`LTXVConditioning`、`LTX2_NAG`、`CFGGuider`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`CM_IntToFloat`、`SimpleCalculatorKJ`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`SaveVideo`、`LowVRAMCheckpointLoader`、`LTXICLoRALoaderModelOnly`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`INTConstant`、`LiconMSR`、`LTXVEmptyLatentAudio`、`LTXAddVideoICLoRAGuide`、`LoadImage`、`PromptRelayEncode`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
