---
key: 视频生成/文生视频/MiniMax-H3全栈式短剧生成V4.2.2｜短剧直出1分钟全节点注释_2097933098980831233.json
name: MiniMax-H3全栈式短剧生成V4.2.2｜短剧直出1分钟全节点注释_2097933098980831233
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax-H3全栈式短剧生成V4.2.2｜短剧直出1分钟全节点注释_2097933098980831233.json
hash: 58972a74cc589d97
coverage: 0.917526
learned_at: 2026-10-15 22:46:24
nodes: [BasicGuider, KSamplerSelect, VAEDecodeAudio, RandomNoise, ModelAttentionBackend, SamplerCustomAdvanced, PrimitiveFloat, GetImage, GetImage, GetImage, YuanTool, ResolutionSelector, YuanPrimitive, ResolutionSelector, MiniMaxChunkFeedForward, Yuan_H3MotionContext, RandomNoise, BasicGuider, MiniMaxLowVRAMAttention, KSamplerSelect, BasicScheduler, VAEDecode, Yuan_H3MotionContextTrim, YUAN_TXTParagraphSplitter, YUAN_TXTShotReplace, Yuan_RTXVideoUpscaleH3, Yuan_H3MotionContextLoadLatent, BasicScheduler, SamplerCustomAdvanced, ResolutionSelector, UNETLoader, LoraLoaderModelOnly, VAELoader, CLIPLoader, VAELoader, ComfyMathExpression, PreviewImage, Yuan_MiniMaxH3Video, ShowText|pysssss, YUAN_TXTJsonExtractor, If ANY execute A else B, EmptyAudio, AudioConcat, easy forLoopEnd, VHS_VideoCombine, easy batchAnything, easy isNone, easy forLoopStart, easy mathInt, Int, Int, YuanMultiImage, YuanPrimitive, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MiniMax-H3全栈式短剧生成V4.2.2｜短剧直出1分钟全节点注释_2097933098980831233.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax-H3全栈式短剧生成V4.2.2｜短剧直出1分钟全节点注释_2097933098980831233.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（97 个）：
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAEDecodeAudio` ★核心
- `RandomNoise`
- `ModelAttentionBackend`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveFloat`
- `GetImage`
- `GetImage`
- `GetImage`
- `YuanTool`
- `ResolutionSelector`
- `YuanPrimitive`
- `ResolutionSelector`
- `MiniMaxChunkFeedForward`
- `Yuan_H3MotionContext`
- `RandomNoise`
- `BasicGuider`
- `MiniMaxLowVRAMAttention`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `Yuan_H3MotionContextTrim`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTShotReplace`
- `Yuan_RTXVideoUpscaleH3`
- `Yuan_H3MotionContextLoadLatent`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `ResolutionSelector`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `ComfyMathExpression`
- `PreviewImage`
- `Yuan_MiniMaxH3Video`
- `ShowText|pysssss`
- `YUAN_TXTJsonExtractor`
- `If ANY execute A else B`
- `EmptyAudio`
- `AudioConcat`
- `easy forLoopEnd`
- `VHS_VideoCombine`
- `easy batchAnything`
- `easy isNone`
- `easy forLoopStart`
- `easy mathInt`
- `Int`
- `Int`
- `YuanMultiImage`
- `YuanPrimitive`
- `PrimitiveStringMultiline`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
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

覆盖率 **92%**（89/97）

**有卡**：`BasicGuider`、`KSamplerSelect`、`VAEDecodeAudio`、`RandomNoise`、`ModelAttentionBackend`、`SamplerCustomAdvanced`、`GetImage`、`YuanTool`、`ResolutionSelector`、`YuanPrimitive`、`MiniMaxChunkFeedForward`、`Yuan_H3MotionContext`、`MiniMaxLowVRAMAttention`、`BasicScheduler`、`VAEDecode`、`Yuan_H3MotionContextTrim`、`YUAN_TXTParagraphSplitter`、`YUAN_TXTShotReplace`、`Yuan_RTXVideoUpscaleH3`、`Yuan_H3MotionContextLoadLatent`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`Yuan_MiniMaxH3Video`、`YUAN_TXTJsonExtractor`、`If ANY execute A else B`、`EmptyAudio`、`AudioConcat`、`easy forLoopEnd`、`VHS_VideoCombine`、`easy batchAnything`、`easy isNone`、`easy forLoopStart`、`easy mathInt`、`Int`、`YuanMultiImage`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
