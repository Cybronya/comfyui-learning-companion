---
key: 视频生成/文生视频/🔥AIGC大赛🔥MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2097297028450709506.json
name: 🔥AIGC大赛🔥MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2097297028450709506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/🔥AIGC大赛🔥MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2097297028450709506.json
hash: 8b292237bd20832a
coverage: 0.468468
learned_at: 2026-10-15 22:49:14
nodes: [BasicGuider, KSamplerSelect, VAEDecodeAudio, RandomNoise, ModelAttentionBackend, SamplerCustomAdvanced, PrimitiveFloat, GetImage, GetImage, GetImage, YuanTool, ResolutionSelector, YuanPrimitive, ResolutionSelector, MiniMaxChunkFeedForward, Yuan_H3MotionContext, RandomNoise, BasicGuider, MiniMaxLowVRAMAttention, KSamplerSelect, BasicScheduler, VAEDecode, Yuan_H3MotionContextTrim, YUAN_TXTParagraphSplitter, YUAN_TXTShotReplace, Yuan_RTXVideoUpscaleH3, Yuan_H3MotionContextLoadLatent, BasicScheduler, SamplerCustomAdvanced, ResolutionSelector, UNETLoader, LoraLoaderModelOnly, VAELoader, CLIPLoader, VAELoader, ComfyMathExpression, PreviewImage, Yuan_MiniMaxH3Video, ShowText|pysssss, YUAN_TXTJsonExtractor, If ANY execute A else B, EmptyAudio, AudioConcat, easy forLoopEnd, VHS_VideoCombine, easy batchAnything, easy isNone, easy forLoopStart, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, Note, easy mathInt, Int, Note, Note, Note, Note, YuanPrimitive, PrimitiveStringMultiline, YuanMultiImage, Int]
patterns: []
missing: []
---

# 视频生成/文生视频/🔥AIGC大赛🔥MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2097297028450709506.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/🔥AIGC大赛🔥MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2097297028450709506.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（111 个）：
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
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `Note`
- `easy mathInt`
- `Int`
- `Note`
- `Note`
- `Note`
- `Note`
- `YuanPrimitive`
- `PrimitiveStringMultiline`
- `YuanMultiImage`
- `Int`

## 知识

覆盖率 **47%**（52/111）

**有卡**：`BasicGuider`、`KSamplerSelect`、`VAEDecodeAudio`、`RandomNoise`、`ModelAttentionBackend`、`SamplerCustomAdvanced`、`GetImage`、`YuanTool`、`ResolutionSelector`、`YuanPrimitive`、`MiniMaxChunkFeedForward`、`Yuan_H3MotionContext`、`MiniMaxLowVRAMAttention`、`BasicScheduler`、`VAEDecode`、`Yuan_H3MotionContextTrim`、`YUAN_TXTParagraphSplitter`、`YUAN_TXTShotReplace`、`Yuan_RTXVideoUpscaleH3`、`Yuan_H3MotionContextLoadLatent`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`Yuan_MiniMaxH3Video`、`YUAN_TXTJsonExtractor`、`If ANY execute A else B`、`EmptyAudio`、`AudioConcat`、`easy forLoopEnd`、`VHS_VideoCombine`、`easy batchAnything`、`easy isNone`、`easy forLoopStart`、`LoadImage`、`easy mathInt`、`Int`、`YuanMultiImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
