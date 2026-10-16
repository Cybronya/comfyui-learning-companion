---
key: 视频生成/图生视频/全局多图参考｜LTX2.3-MSR图生视频大片直出_2090898937610858498.json
name: 全局多图参考｜LTX2.3-MSR图生视频大片直出_2090898937610858498
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/全局多图参考｜LTX2.3-MSR图生视频大片直出_2090898937610858498.json
hash: 49450e14ab5761a0
coverage: 0.652632
learned_at: 2026-10-16 22:30:57
nodes: [CFGGuider, ManualSigmas, LTXVConcatAVLatent, INTConstant, INTConstant, LTXAVTextEncoderLoader, SetNode, SetNode, MathExpression|pysssss, LTXVAudioVAEDecode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, GetNode, EmptyLTXVLatentVideo, GetNode, SetNode, SetNode, easy convertAnything, CR Text Concatenate, SetNode, SetNode, RH_LLMAPI_NODE, CR Text, PreviewAny, SetNode, SetNode, SetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, SetNode, CR Value, CreateVideo, SetNode, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LTXVCropGuides, LTXVAudioVAELoader, LowVRAMCheckpointLoader, SamplerCustomAdvanced, RandomNoise, SaveVideo, GetNode, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, GetNode, GetNode, GetNode, LiconMSR, GetNode, INTConstant, easy boolean, LTXAddVideoICLoRAGuide, LoadImage, KSamplerSelect, LoadImage, LoadImage, CR Text, SetNode, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/全局多图参考｜LTX2.3-MSR图生视频大片直出_2090898937610858498.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/全局多图参考｜LTX2.3-MSR图生视频大片直出_2090898937610858498.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（95 个）：
- `CFGGuider`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `INTConstant`
- `INTConstant`
- `LTXAVTextEncoderLoader`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
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
- `LTXICLoRALoaderModelOnly` ★核心
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
- `SetNode`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **65%**（62/95）

**有卡**：`CFGGuider`、`ManualSigmas`、`LTXVConcatAVLatent`、`INTConstant`、`LTXAVTextEncoderLoader`、`MathExpression|pysssss`、`LTXVAudioVAEDecode`、`VAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`easy convertAnything`、`CR Text Concatenate`、`RH_LLMAPI_NODE`、`CR Text`、`LoadImage`、`CR Value`、`CreateVideo`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVAudioVAELoader`、`LowVRAMCheckpointLoader`、`SamplerCustomAdvanced`、`RandomNoise`、`SaveVideo`、`LTXICLoRALoaderModelOnly`、`LoraLoaderModelOnly`、`LiconMSR`、`easy boolean`、`LTXAddVideoICLoRAGuide`、`KSamplerSelect`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
