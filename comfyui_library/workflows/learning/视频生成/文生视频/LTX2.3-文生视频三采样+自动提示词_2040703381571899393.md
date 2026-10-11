---
key: 视频生成/文生视频/LTX2.3-文生视频三采样+自动提示词_2040703381571899393.json
name: LTX2.3-文生视频三采样+自动提示词_2040703381571899393
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-文生视频三采样+自动提示词_2040703381571899393.json
hash: 83d2391b0fef216d
coverage: 0.875
learned_at: 2026-10-11 19:49:38
nodes: [DualCLIPLoader, ManualSigmas, KSamplerSelect, KSamplerSelect, PrimitiveInt, ManualSigmas, CFGGuider, UNETLoader, easy cleanGpuUsed, llama_cpp_instruct_adv, SamplerCustomAdvanced, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, CFGGuider, VAELoaderKJ, SamplerCustomAdvanced, RandomNoise, SamplerCustomAdvanced, LoraLoaderModelOnly, RandomNoise, LTXVSeparateAVLatent, VAELoaderKJ, LatentUpscaleModelLoader, ShowText|pysssss, LTXVConditioning, SimpleMath+, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, EmptyImage, GetImageSize, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, CLIPTextEncode, CLIPTextEncode, LTXVCropGuides, LTXVLatentUpsampler, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, llama_cpp_model_loader, PrimitiveInt, PrimitiveInt, PrimitiveInt, VAEDecodeTiled, CreateVideo, LTXVAudioVAEDecode, Text, Text, LTXVConcatAVLatent, SaveVideo]
patterns: []
missing: [SimpleMath+, easy cleanGpuUsed]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3-文生视频三采样+自动提示词_2040703381571899393.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-文生视频三采样+自动提示词_2040703381571899393.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `DualCLIPLoader`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `ManualSigmas`
- `CFGGuider`
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `VAELoaderKJ`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `ShowText|pysssss`
- `LTXVConditioning`
- `SimpleMath+`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyImage`
- `GetImageSize`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `llama_cpp_model_loader`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `Text`
- `Text`
- `LTXVConcatAVLatent`
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（49/56）

**有卡**：`DualCLIPLoader`、`ManualSigmas`、`KSamplerSelect`、`CFGGuider`、`UNETLoader`、`llama_cpp_instruct_adv`、`SamplerCustomAdvanced`、`RandomNoise`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`LTXVConditioning`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`EmptyImage`、`GetImageSize`、`ComfyMathExpression`、`CLIPTextEncode`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`llama_cpp_model_loader`、`VAEDecodeTiled`、`CreateVideo`、`LTXVAudioVAEDecode`、`Text`、`SaveVideo`

**缺卡**（2）：`SimpleMath+`、`easy cleanGpuUsed`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
