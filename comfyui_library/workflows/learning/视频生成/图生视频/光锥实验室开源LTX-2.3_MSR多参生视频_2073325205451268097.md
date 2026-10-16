---
key: 视频生成/图生视频/光锥实验室开源LTX-2.3_MSR多参生视频_2073325205451268097.json
name: 光锥实验室开源LTX-2.3_MSR多参生视频_2073325205451268097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2073325205451268097.json
hash: 2565a03a987d73e0
coverage: 0.942857
learned_at: 2026-10-15 22:41:06
nodes: [LowVRAMCheckpointLoader, LTXAVTextEncoderLoader, LTXVAudioVAELoader, CLIPTextEncode, LTXVConditioning, LTX2_NAG, LTXVEmptyLatentAudio, LTXVAudioVAEDecode, LTXVCropGuides, LTXVSeparateAVLatent, LTXVConcatAVLatent, CFGGuider, KSamplerSelect, EmptyLTXVLatentVideo, RandomNoise, SamplerCustomAdvanced, PromptRelayEncode, CreateVideo, ComfyMathExpression, VAEDecode, LiconMSR, LTXAddVideoICLoRAGuide, LoadImage, LoadImage, LoadImage, INTConstant, INTConstant, INTConstant, LoadImage, LoadImage, PrimitiveStringMultiline, SaveVideo, PrimitiveStringMultiline, ManualSigmas, LTXICLoRALoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 24, "width": 241}
---

# 视频生成/图生视频/光锥实验室开源LTX-2.3_MSR多参生视频_2073325205451268097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073325205451268097.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（35 个）：
- `LowVRAMCheckpointLoader` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTX2_NAG`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `EmptyLTXVLatentVideo`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `PromptRelayEncode`
- `CreateVideo`
- `ComfyMathExpression`
- `VAEDecode` ★核心
- `LiconMSR`
- `LTXAddVideoICLoRAGuide`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `SaveVideo`
- `PrimitiveStringMultiline`
- `ManualSigmas`
- `LTXICLoRALoaderModelOnly` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`
- `width` = `241`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`LowVRAMCheckpointLoader`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`CLIPTextEncode`、`LTXVConditioning`、`LTX2_NAG`、`LTXVEmptyLatentAudio`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`CFGGuider`、`KSamplerSelect`、`EmptyLTXVLatentVideo`、`RandomNoise`、`SamplerCustomAdvanced`、`PromptRelayEncode`、`CreateVideo`、`ComfyMathExpression`、`VAEDecode`、`LiconMSR`、`LTXAddVideoICLoRAGuide`、`LoadImage`、`INTConstant`、`SaveVideo`、`ManualSigmas`、`LTXICLoRALoaderModelOnly`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
