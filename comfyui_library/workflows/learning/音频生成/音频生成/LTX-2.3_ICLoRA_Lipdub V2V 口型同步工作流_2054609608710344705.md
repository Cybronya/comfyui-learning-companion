---
key: 音频生成/音频生成/LTX-2.3_ICLoRA_Lipdub V2V 口型同步工作流_2054609608710344705.json
name: LTX-2.3_ICLoRA_Lipdub V2V 口型同步工作流_2054609608710344705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/LTX-2.3_ICLoRA_Lipdub V2V 口型同步工作流_2054609608710344705.json
hash: a5827e729902215d
coverage: 0.851852
learned_at: 2026-10-18 03:04:50
nodes: [CLIPTextEncode, RandomNoise, LTXVConditioning, CFGGuider, CreateVideo, KSamplerSelect, ManualSigmas, PrimitiveString, GemmaAPITextEncode, GemmaAPITextEncode, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVSeparateAVLatent, LTXAddVideoICLoRAGuide, KSamplerSelect, SamplerCustomAdvanced, LTXVCropGuides, ManualSigmas, CFGGuider, LTXVConcatAVLatent, RandomNoise, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVCropGuides, LTXVAudioVAEEncode, LTXVTiledVAEDecode, MarkdownNote, LTXAddVideoICLoRAGuide, LTXVSetAudioRefTokens, LTXVSetAudioRefTokens, MarkdownNote, Note, LTXVAudioVAELoader, CheckpointLoaderSimple, LatentUpscaleModelLoader, LoraLoaderModelOnly, Note, LTXAVTextEncoderLoader, Note, LTXICLoRALoaderModelOnly, CLIPTextEncode, LoadVideo, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXFloatToInt, GetVideoComponents, SaveVideo, ComfyMathExpression, GetImageSizeAndCount, Note, Note, ResizeImageMaskNode, ResizeImageMaskNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 音频生成/音频生成/LTX-2.3_ICLoRA_Lipdub V2V 口型同步工作流_2054609608710344705.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/LTX-2.3_ICLoRA_Lipdub V2V 口型同步工作流_2054609608710344705.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `LTXVConditioning`
- `CFGGuider`
- `CreateVideo`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `PrimitiveString`
- `GemmaAPITextEncode`
- `GemmaAPITextEncode`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXAddVideoICLoRAGuide`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `ManualSigmas`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVAudioVAEEncode` ★核心
- `LTXVTiledVAEDecode` ★核心
- `MarkdownNote`
- `LTXAddVideoICLoRAGuide`
- `LTXVSetAudioRefTokens`
- `LTXVSetAudioRefTokens`
- `MarkdownNote`
- `Note`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LTXAVTextEncoderLoader`
- `Note`
- `LTXICLoRALoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoadVideo`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXFloatToInt`
- `GetVideoComponents`
- `SaveVideo`
- `ComfyMathExpression`
- `GetImageSizeAndCount`
- `Note`
- `Note`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（46/54）

**有卡**：`CLIPTextEncode`、`RandomNoise`、`LTXVConditioning`、`CFGGuider`、`CreateVideo`、`KSamplerSelect`、`ManualSigmas`、`GemmaAPITextEncode`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`LTXAddVideoICLoRAGuide`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`LTXVAudioVAEEncode`、`LTXVTiledVAEDecode`、`LTXVSetAudioRefTokens`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`LTXICLoRALoaderModelOnly`、`LoadVideo`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXFloatToInt`、`GetVideoComponents`、`SaveVideo`、`ComfyMathExpression`、`GetImageSizeAndCount`、`ResizeImageMaskNode`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
