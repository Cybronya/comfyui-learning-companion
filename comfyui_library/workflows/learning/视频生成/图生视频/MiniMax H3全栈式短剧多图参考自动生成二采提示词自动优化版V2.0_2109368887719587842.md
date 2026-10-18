---
key: 视频生成/图生视频/MiniMax H3全栈式短剧多图参考自动生成二采提示词自动优化版V2.0_2109368887719587842.json
name: MiniMax H3全栈式短剧多图参考自动生成二采提示词自动优化版V2.0_2109368887719587842
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3全栈式短剧多图参考自动生成二采提示词自动优化版V2.0_2109368887719587842.json
hash: b83134b1069f9d84
coverage: 0.49375
learned_at: 2026-10-18 00:23:21
nodes: [GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, CLIPLoader, YUAN_TXTJsonExtractor, GetNode, GetNode, GetImage, GetImage, GetNode, GetImage, ResolutionSelector, GetNode, YuanTool, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, PrimitiveInt, SetNode, TextGenerate, StringConcatenate, SetNode, ResolutionSelector, SetNode, SetNode, SetNode, GetNode, PreviewImage, GetNode, PrimitiveNode, YuanAudioList, PrimitiveStringMultiline, ImageScale, LoadImage, GetNode, Reroute, Reroute, GetNode, GetNode, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, SetNode, BasicGuider, SetNode, SetNode, SetNode, GetNode, LTXVConcatAVLatent, GetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, RandomNoise, KSamplerSelect, UNETLoader, SetNode, GetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, LoraLoaderModelOnly, BasicScheduler, MinimaxH3LatentUpscaler3D, VAEDecode, VAEDecodeAudio, GetNode, GetNode, ComfyMathExpression, easy float, SetNode, MiniMaxH3ReferenceToVideo, PrimitiveFloat, ComfyMathExpression, SetNode, ResolutionSelector, SetNode, SetNode, YuanAudioSplit, PrimitiveFloat, YuanMultiImage, SplitSigmas, SetNode, VAELoader, SetNode, SetNode, SetNode, VAELoader, SetNode, CLIPLoader, SetNode, LoraLoaderModelOnly, SetNode, SetNode, SetNode, VHS_VideoCombine, StringConcatenate, ToString, JoinStringMulti, llama_cpp_model_loader, llama_cpp_parameters, PurgeVRAM_UTK, Any Switch (rgthree), SetNode, PrimitiveStringMultiline, easy showAnything, VHS_VideoCombine, easy showAnything, llama_cpp_instruct_adv, PrimitiveStringMultiline, ShowText|pysssss, SetNode, YUAN_TXTParagraphSplitter, YUAN_TXTShotReplace, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax H3全栈式短剧多图参考自动生成二采提示词自动优化版V2.0_2109368887719587842.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3全栈式短剧多图参考自动生成二采提示词自动优化版V2.0_2109368887719587842.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（160 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPLoader`
- `YUAN_TXTJsonExtractor`
- `GetNode`
- `GetNode`
- `GetImage`
- `GetImage`
- `GetNode`
- `GetImage`
- `ResolutionSelector`
- `GetNode`
- `YuanTool`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `SetNode`
- `TextGenerate`
- `StringConcatenate`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `PrimitiveNode`
- `YuanAudioList`
- `PrimitiveStringMultiline`
- `ImageScale`
- `LoadImage`
- `GetNode`
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `BasicGuider`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `MinimaxH3LatentUpscaler3D`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `easy float`
- `SetNode`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `YuanAudioSplit`
- `PrimitiveFloat`
- `YuanMultiImage`
- `SplitSigmas`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `StringConcatenate`
- `ToString`
- `JoinStringMulti`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `PurgeVRAM_UTK`
- `Any Switch (rgthree)`
- `SetNode`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `VHS_VideoCombine`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `SetNode`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTShotReplace`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `SaveImage`

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

覆盖率 **49%**（79/160）

**有卡**：`CLIPLoader`、`YUAN_TXTJsonExtractor`、`GetImage`、`ResolutionSelector`、`YuanTool`、`TextGenerate`、`StringConcatenate`、`YuanAudioList`、`ImageScale`、`LoadImage`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicGuider`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`RandomNoise`、`KSamplerSelect`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`BasicScheduler`、`MinimaxH3LatentUpscaler3D`、`ComfyMathExpression`、`easy float`、`MiniMaxH3ReferenceToVideo`、`YuanAudioSplit`、`YuanMultiImage`、`SplitSigmas`、`VAELoader`、`VHS_VideoCombine`、`ToString`、`JoinStringMulti`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`PurgeVRAM_UTK`、`llama_cpp_instruct_adv`、`YUAN_TXTParagraphSplitter`、`YUAN_TXTShotReplace`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
