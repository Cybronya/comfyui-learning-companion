---
key: 视频生成/图生视频/MINIMAX-H3 ref2va Qwen3.8 27B｜数字人音频图生视频_2092074378220621826.json
name: MINIMAX-H3 ref2va Qwen3.8 27B｜数字人音频图生视频_2092074378220621826
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MINIMAX-H3 ref2va Qwen3.8 27B｜数字人音频图生视频_2092074378220621826.json
hash: cc7dce9d249847ef
coverage: 0.869565
learned_at: 2026-10-16 22:59:07
nodes: [RandomNoise, easy cleanGpuUsed, CLIPLoader, KSamplerSelect, BasicGuider, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, SetNode, BasicGuider, RandomNoise, easy cleanGpuUsed, VAEDecode, VAEDecodeAudio, easy cleanGpuUsed, KSamplerSelect, SamplerCustomAdvanced, MiniMaxH3ReferenceToVideo, VHS_VideoCombine, VHS_VideoCombine, ImageResize+, LoadImage, SetNode, easy cleanGpuUsed, SomethingToString, ProcessString, JoinStrings, PreviewImage, PreviewAny, ShowText|pysssss, TextInput_, LoadImage, ImageResize+, ImageConcatMulti, SamplerCustomAdvanced, TextInput_, llama_cpp_parameters, llama_cpp_instruct_adv, PrimitiveStringMultiline, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, GetNode, LTXVConcatAVLatent, llama_cpp_model_loader, LTXVSeparateAVLatent, MinimaxH3LatentUpscaler3D, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, LoraLoaderModelOnly, LoraLoaderModelOnly, SLASageAttention, CR Prompt Text, SLASageAttention, ModelAttentionBackend, BasicScheduler, BasicScheduler, PrimitiveFloat, ResolutionSelector, Float, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MINIMAX-H3 ref2va Qwen3.8 27B｜数字人音频图生视频_2092074378220621826.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MINIMAX-H3 ref2va Qwen3.8 27B｜数字人音频图生视频_2092074378220621826.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
- `RandomNoise`
- `easy cleanGpuUsed`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `BasicGuider`
- `RandomNoise`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3ReferenceToVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageResize+`
- `LoadImage`
- `SetNode`
- `easy cleanGpuUsed`
- `SomethingToString`
- `ProcessString`
- `JoinStrings`
- `PreviewImage`
- `PreviewAny`
- `ShowText|pysssss`
- `TextInput_`
- `LoadImage`
- `ImageResize+`
- `ImageConcatMulti`
- `SamplerCustomAdvanced` ★核心
- `TextInput_`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `PrimitiveStringMultiline`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `LTXVConcatAVLatent`
- `llama_cpp_model_loader`
- `LTXVSeparateAVLatent`
- `MinimaxH3LatentUpscaler3D`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader` ★核心
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SLASageAttention`
- `CR Prompt Text`
- `SLASageAttention`
- `ModelAttentionBackend`
- `BasicScheduler`
- `BasicScheduler`
- `PrimitiveFloat`
- `ResolutionSelector`
- `Float`
- `孤海注释`
- `孤海注释`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（80/92）

**有卡**：`RandomNoise`、`easy cleanGpuUsed`、`CLIPLoader`、`KSamplerSelect`、`BasicGuider`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`MiniMaxH3ReferenceToVideo`、`VHS_VideoCombine`、`ImageResize+`、`LoadImage`、`SomethingToString`、`ProcessString`、`JoinStrings`、`TextInput_`、`ImageConcatMulti`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`llama_cpp_model_loader`、`LTXVSeparateAVLatent`、`MinimaxH3LatentUpscaler3D`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`UNETLoader`、`MiniMaxH3SigmaShift`、`LoraLoaderModelOnly`、`SLASageAttention`、`CR Prompt Text`、`ModelAttentionBackend`、`BasicScheduler`、`ResolutionSelector`、`Float`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
