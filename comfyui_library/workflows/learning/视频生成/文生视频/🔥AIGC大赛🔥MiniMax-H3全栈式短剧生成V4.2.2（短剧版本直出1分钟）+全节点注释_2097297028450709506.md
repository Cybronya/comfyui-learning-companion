---
key: 视频生成/文生视频/🔥AIGC大赛🔥MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2097297028450709506.json
name: 🔥AIGC大赛🔥MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2097297028450709506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/🔥AIGC大赛🔥MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2097297028450709506.json
hash: 8b292237bd20832a
coverage: 0.414414
learned_at: 2026-10-11 21:42:04
nodes: [BasicGuider, KSamplerSelect, VAEDecodeAudio, RandomNoise, ModelAttentionBackend, SamplerCustomAdvanced, PrimitiveFloat, GetImage, GetImage, GetImage, YuanTool, ResolutionSelector, YuanPrimitive, ResolutionSelector, MiniMaxChunkFeedForward, Yuan_H3MotionContext, RandomNoise, BasicGuider, MiniMaxLowVRAMAttention, KSamplerSelect, BasicScheduler, VAEDecode, Yuan_H3MotionContextTrim, YUAN_TXTParagraphSplitter, YUAN_TXTShotReplace, Yuan_RTXVideoUpscaleH3, Yuan_H3MotionContextLoadLatent, BasicScheduler, SamplerCustomAdvanced, ResolutionSelector, UNETLoader, LoraLoaderModelOnly, VAELoader, CLIPLoader, VAELoader, ComfyMathExpression, PreviewImage, Yuan_MiniMaxH3Video, ShowText|pysssss, YUAN_TXTJsonExtractor, If ANY execute A else B, EmptyAudio, AudioConcat, easy forLoopEnd, VHS_VideoCombine, easy batchAnything, easy isNone, easy forLoopStart, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, Note, easy mathInt, Int, Note, Note, Note, Note, YuanPrimitive, PrimitiveStringMultiline, YuanMultiImage, Int]
patterns: []
missing: [If ANY execute A else B, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy isNone, easy mathInt]
discoveries: [次要节点 `If ANY execute A else B` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识]
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

覆盖率 **41%**（46/111）

**有卡**：`BasicGuider`、`KSamplerSelect`、`VAEDecodeAudio`、`RandomNoise`、`ModelAttentionBackend`、`SamplerCustomAdvanced`、`GetImage`、`YuanTool`、`ResolutionSelector`、`YuanPrimitive`、`MiniMaxChunkFeedForward`、`Yuan_H3MotionContext`、`MiniMaxLowVRAMAttention`、`BasicScheduler`、`VAEDecode`、`Yuan_H3MotionContextTrim`、`YUAN_TXTParagraphSplitter`、`YUAN_TXTShotReplace`、`Yuan_RTXVideoUpscaleH3`、`Yuan_H3MotionContextLoadLatent`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`Yuan_MiniMaxH3Video`、`YUAN_TXTJsonExtractor`、`EmptyAudio`、`AudioConcat`、`VHS_VideoCombine`、`LoadImage`、`Int`、`YuanMultiImage`

**缺卡**（6）：`If ANY execute A else B`、`easy batchAnything`、`easy forLoopEnd`、`easy forLoopStart`、`easy isNone`、`easy mathInt`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `If ANY execute A else B` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
