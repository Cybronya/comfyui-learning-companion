---
key: 视频生成/图生视频/短剧直出1分钟｜MiniMax-H3全栈式生成V4.2.2图生视频_2092602046498299905.json
name: 短剧直出1分钟｜MiniMax-H3全栈式生成V4.2.2图生视频_2092602046498299905
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/短剧直出1分钟｜MiniMax-H3全栈式生成V4.2.2图生视频_2092602046498299905.json
hash: 0292999f156cd4c9
coverage: 0.810526
learned_at: 2026-10-16 23:00:09
nodes: [MiniMaxChunkFeedForward, LoraLoaderModelOnly, ModelAttentionBackend, PreviewImage, PreviewImage, BasicGuider, KSamplerSelect, BasicScheduler, Yuan_MiniMaxH3Video, Yuan_H3MotionContextLoadLatent, RandomNoise, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, RandomNoise, Reroute, CreateVideo, VHS_VideoCombine, PreviewImage, If ANY execute A else B, If ANY execute A else B, Int, Int, Yuan_H3MotionContext, ResolutionSelector, VAELoader, VAELoader, easy showAnything, GetImage, GetImage, easy showAnything, easy showAnything, easy showAnything, PreviewImage, MiniMaxLowVRAMAttention, BasicGuider, PrimitiveBoolean, PrimitiveNode, easy batchAnything, AudioConcat, VAEDecodeAudio, VAEDecode, easy forLoopEnd, EmptyAudio, If ANY execute A else B, Reroute, ResolutionSelector, Yuan_RTXVideoUpscaleH3, easy isNone, YUAN_TXTJsonExtractor, GetImage, MathExpression|pysssss, ResolutionSelector, CLIPLoader, UNETLoader, SamplerCustomAdvanced, Yuan_H3MotionContextTrim, YUAN_TXTShotReplace, MathExpression|pysssss, easy forLoopStart, Reroute, SaveVideo, YuanMultiImage, YUAN_TXTParagraphSplitter, YuanTool, easy showAnything, PrimitiveStringMultiline, RH_LLMAPI_Pro_Node, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/短剧直出1分钟｜MiniMax-H3全栈式生成V4.2.2图生视频_2092602046498299905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/短剧直出1分钟｜MiniMax-H3全栈式生成V4.2.2图生视频_2092602046498299905.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（95 个）：
- `MiniMaxChunkFeedForward`
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `PreviewImage`
- `PreviewImage`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `Yuan_MiniMaxH3Video`
- `Yuan_H3MotionContextLoadLatent`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `Reroute`
- `CreateVideo`
- `VHS_VideoCombine`
- `PreviewImage`
- `If ANY execute A else B`
- `If ANY execute A else B`
- `Int`
- `Int`
- `Yuan_H3MotionContext`
- `ResolutionSelector`
- `VAELoader`
- `VAELoader`
- `easy showAnything`
- `GetImage`
- `GetImage`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `PreviewImage`
- `MiniMaxLowVRAMAttention`
- `BasicGuider`
- `PrimitiveBoolean`
- `PrimitiveNode`
- `easy batchAnything`
- `AudioConcat`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `easy forLoopEnd`
- `EmptyAudio`
- `If ANY execute A else B`
- `Reroute`
- `ResolutionSelector`
- `Yuan_RTXVideoUpscaleH3`
- `easy isNone`
- `YUAN_TXTJsonExtractor`
- `GetImage`
- `MathExpression|pysssss`
- `ResolutionSelector`
- `CLIPLoader`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `Yuan_H3MotionContextTrim`
- `YUAN_TXTShotReplace`
- `MathExpression|pysssss`
- `easy forLoopStart`
- `Reroute`
- `SaveVideo`
- `YuanMultiImage`
- `YUAN_TXTParagraphSplitter`
- `YuanTool`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_Pro_Node`
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

覆盖率 **81%**（77/95）

**有卡**：`MiniMaxChunkFeedForward`、`LoraLoaderModelOnly`、`ModelAttentionBackend`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`Yuan_MiniMaxH3Video`、`Yuan_H3MotionContextLoadLatent`、`RandomNoise`、`SamplerCustomAdvanced`、`CreateVideo`、`VHS_VideoCombine`、`If ANY execute A else B`、`Int`、`Yuan_H3MotionContext`、`ResolutionSelector`、`VAELoader`、`GetImage`、`MiniMaxLowVRAMAttention`、`PrimitiveBoolean`、`easy batchAnything`、`AudioConcat`、`VAEDecodeAudio`、`VAEDecode`、`easy forLoopEnd`、`EmptyAudio`、`Yuan_RTXVideoUpscaleH3`、`easy isNone`、`YUAN_TXTJsonExtractor`、`MathExpression|pysssss`、`CLIPLoader`、`UNETLoader`、`Yuan_H3MotionContextTrim`、`YUAN_TXTShotReplace`、`easy forLoopStart`、`SaveVideo`、`YuanMultiImage`、`YUAN_TXTParagraphSplitter`、`YuanTool`、`RH_LLMAPI_Pro_Node`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
