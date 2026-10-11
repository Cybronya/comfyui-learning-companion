---
key: 视频生成/文生视频/全栈式短剧生成 MiniMax-H3 V4.2.3直出一分钟全节点注释_2094181672697810945.json
name: 全栈式短剧生成 MiniMax-H3 V4.2.3直出一分钟全节点注释_2094181672697810945
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/全栈式短剧生成 MiniMax-H3 V4.2.3直出一分钟全节点注释_2094181672697810945.json
hash: 46be87099bad470b
coverage: 0.831325
learned_at: 2026-10-11 21:30:33
nodes: [BasicGuider, KSamplerSelect, VAEDecodeAudio, RandomNoise, ModelAttentionBackend, SamplerCustomAdvanced, PrimitiveFloat, GetImage, GetImage, GetImage, YuanTool, ResolutionSelector, YuanPrimitive, ResolutionSelector, MiniMaxChunkFeedForward, Yuan_H3MotionContext, RandomNoise, BasicGuider, MiniMaxLowVRAMAttention, KSamplerSelect, BasicScheduler, VAEDecode, Yuan_H3MotionContextTrim, YUAN_TXTParagraphSplitter, YUAN_TXTShotReplace, Yuan_RTXVideoUpscaleH3, BasicScheduler, SamplerCustomAdvanced, ResolutionSelector, UNETLoader, LoraLoaderModelOnly, VAELoader, CLIPLoader, ComfyMathExpression, PreviewImage, Yuan_MiniMaxH3Video, ShowText|pysssss, YUAN_TXTJsonExtractor, If ANY execute A else B, EmptyAudio, AudioConcat, easy forLoopEnd, VHS_VideoCombine, easy batchAnything, easy isNone, easy forLoopStart, easy mathInt, Int, Int, YuanPrimitive, YuanMultiImage, PrimitiveStringMultiline, Yuan_H3MotionContextLoadLatent, VAELoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: [If ANY execute A else B, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy isNone, easy mathInt]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `If ANY execute A else B` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/全栈式短剧生成 MiniMax-H3 V4.2.3直出一分钟全节点注释_2094181672697810945.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/全栈式短剧生成 MiniMax-H3 V4.2.3直出一分钟全节点注释_2094181672697810945.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
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
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `ResolutionSelector`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
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
- `YuanPrimitive`
- `YuanMultiImage`
- `PrimitiveStringMultiline`
- `Yuan_H3MotionContextLoadLatent`
- `VAELoader`
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
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
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

覆盖率 **83%**（69/83）

**有卡**：`BasicGuider`、`KSamplerSelect`、`VAEDecodeAudio`、`RandomNoise`、`ModelAttentionBackend`、`SamplerCustomAdvanced`、`GetImage`、`YuanTool`、`ResolutionSelector`、`YuanPrimitive`、`MiniMaxChunkFeedForward`、`Yuan_H3MotionContext`、`MiniMaxLowVRAMAttention`、`BasicScheduler`、`VAEDecode`、`Yuan_H3MotionContextTrim`、`YUAN_TXTParagraphSplitter`、`YUAN_TXTShotReplace`、`Yuan_RTXVideoUpscaleH3`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`Yuan_MiniMaxH3Video`、`YUAN_TXTJsonExtractor`、`EmptyAudio`、`AudioConcat`、`VHS_VideoCombine`、`Int`、`YuanMultiImage`、`Yuan_H3MotionContextLoadLatent`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**缺卡**（6）：`If ANY execute A else B`、`easy batchAnything`、`easy forLoopEnd`、`easy forLoopStart`、`easy isNone`、`easy mathInt`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `If ANY execute A else B` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
