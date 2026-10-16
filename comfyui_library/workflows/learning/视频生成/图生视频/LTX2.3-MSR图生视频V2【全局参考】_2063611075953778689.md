---
key: 视频生成/图生视频/LTX2.3-MSR图生视频V2【全局参考】_2063611075953778689.json
name: LTX2.3-MSR图生视频V2【全局参考】_2063611075953778689.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2063611075953778689.json
hash: 6676f67c65366299
coverage: 0.573529
learned_at: 2026-10-15 22:39:16
nodes: [CFGGuider, ManualSigmas, LTXVConcatAVLatent, INTConstant, INTConstant, LTXAVTextEncoderLoader, SetNode, SetNode, MathExpression|pysssss, SetNode, LTXVAudioVAEDecode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, GetNode, EmptyLTXVLatentVideo, GetNode, SetNode, SetNode, easy convertAnything, CR Text Concatenate, SetNode, SetNode, RH_LLMAPI_NODE, CR Text, PreviewAny, SetNode, SetNode, SetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, SetNode, CR Value, CreateVideo, SetNode, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LTXVCropGuides, LTXVAudioVAELoader, LowVRAMCheckpointLoader, SamplerCustomAdvanced, RandomNoise, SaveVideo, GetNode, LoraLoaderModelOnly, GetNode, GetNode, GetNode, LiconMSR, GetNode, INTConstant, easy boolean, LTXAddVideoICLoRAGuide, LoadImage, KSamplerSelect, LoadImage, LoadImage, CR Text, LTXICLoRALoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 24, "width": 241}
---

# 视频生成/图生视频/LTX2.3-MSR图生视频V2【全局参考】_2063611075953778689.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063611075953778689.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（68 个）：
- `CFGGuider`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `INTConstant`
- `INTConstant`
- `LTXAVTextEncoderLoader`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy convertAnything`
- `CR Text Concatenate`
- `SetNode`
- `SetNode`
- `RH_LLMAPI_NODE`
- `CR Text`
- `PreviewAny`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CR Value`
- `CreateVideo`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVAudioVAELoader`
- `LowVRAMCheckpointLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `SaveVideo`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LiconMSR`
- `GetNode`
- `INTConstant`
- `easy boolean`
- `LTXAddVideoICLoRAGuide`
- `LoadImage`
- `KSamplerSelect` ★核心
- `LoadImage`
- `LoadImage`
- `CR Text`
- `LTXICLoRALoaderModelOnly` ★核心

## 关键参数

- `width` = `241`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **57%**（39/68）

**有卡**：`CFGGuider`、`ManualSigmas`、`LTXVConcatAVLatent`、`INTConstant`、`LTXAVTextEncoderLoader`、`MathExpression|pysssss`、`LTXVAudioVAEDecode`、`VAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`easy convertAnything`、`CR Text Concatenate`、`RH_LLMAPI_NODE`、`CR Text`、`LoadImage`、`CR Value`、`CreateVideo`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVAudioVAELoader`、`LowVRAMCheckpointLoader`、`SamplerCustomAdvanced`、`RandomNoise`、`SaveVideo`、`LoraLoaderModelOnly`、`LiconMSR`、`easy boolean`、`LTXAddVideoICLoRAGuide`、`KSamplerSelect`、`LTXICLoRALoaderModelOnly`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
