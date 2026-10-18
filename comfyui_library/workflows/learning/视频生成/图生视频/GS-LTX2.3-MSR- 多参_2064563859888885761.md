---
key: 视频生成/图生视频/GS-LTX2.3-MSR- 多参_2064563859888885761.json
name: GS-LTX2.3-MSR- 多参_2064563859888885761.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/GS-LTX2.3-MSR- 多参_2064563859888885761.json
hash: da59670626207e25
coverage: 0.942857
learned_at: 2026-10-15 22:39:26
nodes: [LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXAddVideoICLoRAGuide, CFGGuider, SaveVideo, CreateVideo, LTXVCropGuides, VAEDecode, CLIPTextEncode, LTXVConditioning, EmptyLTXVLatentVideo, RandomNoise, KSamplerSelect, LTXVEmptyLatentAudio, LoadImage, LiconMSR, LowVRAMCheckpointLoader, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LTXICLoRALoaderModelOnly, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, Reroute, Reroute, MathExpression|pysssss, MathExpression|pysssss, LoadImage, LoadImage, CLIPTextEncode, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 50, "width": 241}
---

# 视频生成/图生视频/GS-LTX2.3-MSR- 多参_2064563859888885761.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064563859888885761.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXAddVideoICLoRAGuide`
- `CFGGuider`
- `SaveVideo`
- `CreateVideo`
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LoadImage`
- `LiconMSR`
- `LowVRAMCheckpointLoader` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `Reroute`
- `Reroute`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `INTConstant`

## 关键参数

- `width` = `241`
- `height` = `50`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **94%**（33/35）

**有卡**：`LTXVConcatAVLatent`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXAddVideoICLoRAGuide`、`CFGGuider`、`SaveVideo`、`CreateVideo`、`LTXVCropGuides`、`VAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`RandomNoise`、`KSamplerSelect`、`LTXVEmptyLatentAudio`、`LoadImage`、`LiconMSR`、`LowVRAMCheckpointLoader`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LTXICLoRALoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`MathExpression|pysssss`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
