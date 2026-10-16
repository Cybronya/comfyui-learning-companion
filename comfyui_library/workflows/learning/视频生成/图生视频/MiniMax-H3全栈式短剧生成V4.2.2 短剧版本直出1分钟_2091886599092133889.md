---
key: 视频生成/图生视频/MiniMax-H3全栈式短剧生成V4.2.2 短剧版本直出1分钟_2091886599092133889.json
name: MiniMax-H3全栈式短剧生成V4.2.2 短剧版本直出1分钟_2091886599092133889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V4.2.2 短剧版本直出1分钟_2091886599092133889.json
hash: 066287c8f1b927fd
coverage: 0.782609
learned_at: 2026-10-16 22:30:38
nodes: [MiniMaxChunkFeedForward, LoraLoaderModelOnly, ModelAttentionBackend, PreviewImage, PreviewImage, BasicGuider, KSamplerSelect, BasicScheduler, Yuan_MiniMaxH3Video, Yuan_H3MotionContextLoadLatent, RandomNoise, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, RandomNoise, Reroute, CreateVideo, VHS_VideoCombine, PreviewImage, If ANY execute A else B, If ANY execute A else B, Int, Int, Yuan_H3MotionContext, ResolutionSelector, VAELoader, VAELoader, easy showAnything, GetImage, GetImage, easy showAnything, easy showAnything, easy showAnything, PreviewImage, MiniMaxLowVRAMAttention, BasicGuider, PrimitiveBoolean, PrimitiveNode, easy batchAnything, AudioConcat, VAEDecodeAudio, VAEDecode, easy forLoopEnd, EmptyAudio, If ANY execute A else B, Reroute, ResolutionSelector, Yuan_RTXVideoUpscaleH3, easy isNone, YUAN_TXTJsonExtractor, GetImage, MathExpression|pysssss, ResolutionSelector, CLIPLoader, UNETLoader, SamplerCustomAdvanced, Yuan_H3MotionContextTrim, YUAN_TXTShotReplace, MathExpression|pysssss, easy forLoopStart, Reroute, SaveVideo, PrimitiveStringMultiline, YuanMultiImage, YUAN_TXTParagraphSplitter, YuanTool, easy showAnything, PrimitiveStringMultiline, RH_LLMAPI_Pro_Node]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax-H3全栈式短剧生成V4.2.2 短剧版本直出1分钟_2091886599092133889.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V4.2.2 短剧版本直出1分钟_2091886599092133889.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
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
- `PrimitiveStringMultiline`
- `YuanMultiImage`
- `YUAN_TXTParagraphSplitter`
- `YuanTool`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_Pro_Node`

## 知识

覆盖率 **78%**（54/69）

**有卡**：`MiniMaxChunkFeedForward`、`LoraLoaderModelOnly`、`ModelAttentionBackend`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`Yuan_MiniMaxH3Video`、`Yuan_H3MotionContextLoadLatent`、`RandomNoise`、`SamplerCustomAdvanced`、`CreateVideo`、`VHS_VideoCombine`、`If ANY execute A else B`、`Int`、`Yuan_H3MotionContext`、`ResolutionSelector`、`VAELoader`、`GetImage`、`MiniMaxLowVRAMAttention`、`PrimitiveBoolean`、`easy batchAnything`、`AudioConcat`、`VAEDecodeAudio`、`VAEDecode`、`easy forLoopEnd`、`EmptyAudio`、`Yuan_RTXVideoUpscaleH3`、`easy isNone`、`YUAN_TXTJsonExtractor`、`MathExpression|pysssss`、`CLIPLoader`、`UNETLoader`、`Yuan_H3MotionContextTrim`、`YUAN_TXTShotReplace`、`easy forLoopStart`、`SaveVideo`、`YuanMultiImage`、`YUAN_TXTParagraphSplitter`、`YuanTool`、`RH_LLMAPI_Pro_Node`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
