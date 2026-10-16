---
key: 视频生成/图生视频/Skill双阶段版V7.2｜MiniMax-H3全栈式短剧生成_2094024013784903681.json
name: Skill双阶段版V7.2｜MiniMax-H3全栈式短剧生成_2094024013784903681
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Skill双阶段版V7.2｜MiniMax-H3全栈式短剧生成_2094024013784903681.json
hash: 94d948a267862249
coverage: 0.538462
learned_at: 2026-10-16 23:42:25
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, BasicGuider, CLIPLoader, RandomNoise, YUAN_TXTJsonExtractor, SamplerCustomAdvanced, KSamplerSelect, GetNode, GetNode, GetImage, GetImage, GetNode, GetImage, ResolutionSelector, GetNode, YuanTool, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, YUAN_TXTParagraphSplitter, GetNode, GetNode, ComfyMathExpression, GetNode, GetNode, YuanAudioSplit, PrimitiveInt, KSamplerSelect, SetNode, BasicGuider, TextGenerate, GetNode, GetNode, VAEDecodeAudio, VAEDecode, GetNode, StringConcatenate, SetNode, ResolutionSelector, SetNode, SetNode, SetNode, PrimitiveFloat, GetNode, PreviewImage, YUAN_TXTShotReplace, Yuan_H3Upscale3D, YuanAudioList, GetNode, ComfyMathExpression, Yuan_H3MotionContextLoadLatent, GetNode, Yuan_H3MotionContextTrim, SamplerCustomAdvanced, GetNode, VHS_VideoCombine, RandomNoise, PrimitiveStringMultiline, PrimitiveStringMultiline, Yuan_MiniMaxH3Video, ShowText|pysssss, GetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, SetNode, SetNode, ModelAttentionBackend, MiniMaxChunkFeedForward, VAELoader, CLIPLoader, VAELoader, SetNode, SetNode, ResolutionSelector, YuanMultiImage, GetNode, PrimitiveNode, Yuan_H3MotionContext, BasicScheduler, BasicScheduler, MiniMaxLowVRAMAttention, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, SetNode, UNETLoader, UNETLoader, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Skill双阶段版V7.2｜MiniMax-H3全栈式短剧生成_2094024013784903681.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Skill双阶段版V7.2｜MiniMax-H3全栈式短剧生成_2094024013784903681.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（130 个）：
- `GetNode`
- `GetNode`
- `GetNode`
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
- `SetNode`
- `SetNode`
- `BasicGuider`
- `CLIPLoader`
- `RandomNoise`
- `YUAN_TXTJsonExtractor`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
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
- `YUAN_TXTParagraphSplitter`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `YuanAudioSplit`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `SetNode`
- `BasicGuider`
- `TextGenerate`
- `GetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `StringConcatenate`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `GetNode`
- `PreviewImage`
- `YUAN_TXTShotReplace`
- `Yuan_H3Upscale3D`
- `YuanAudioList`
- `GetNode`
- `ComfyMathExpression`
- `Yuan_H3MotionContextLoadLatent`
- `GetNode`
- `Yuan_H3MotionContextTrim`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `RandomNoise`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `Yuan_MiniMaxH3Video`
- `ShowText|pysssss`
- `GetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SetNode`
- `SetNode`
- `ModelAttentionBackend`
- `MiniMaxChunkFeedForward`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `ResolutionSelector`
- `YuanMultiImage`
- `GetNode`
- `PrimitiveNode`
- `Yuan_H3MotionContext`
- `BasicScheduler`
- `BasicScheduler`
- `MiniMaxLowVRAMAttention`
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
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
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **54%**（70/130）

**有卡**：`BasicGuider`、`CLIPLoader`、`RandomNoise`、`YUAN_TXTJsonExtractor`、`SamplerCustomAdvanced`、`KSamplerSelect`、`GetImage`、`ResolutionSelector`、`YuanTool`、`YUAN_TXTParagraphSplitter`、`ComfyMathExpression`、`YuanAudioSplit`、`TextGenerate`、`VAEDecodeAudio`、`VAEDecode`、`StringConcatenate`、`YUAN_TXTShotReplace`、`Yuan_H3Upscale3D`、`YuanAudioList`、`Yuan_H3MotionContextLoadLatent`、`Yuan_H3MotionContextTrim`、`VHS_VideoCombine`、`Yuan_MiniMaxH3Video`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`MiniMaxChunkFeedForward`、`VAELoader`、`YuanMultiImage`、`Yuan_H3MotionContext`、`BasicScheduler`、`MiniMaxLowVRAMAttention`、`LoraLoaderBypassModelOnly`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
