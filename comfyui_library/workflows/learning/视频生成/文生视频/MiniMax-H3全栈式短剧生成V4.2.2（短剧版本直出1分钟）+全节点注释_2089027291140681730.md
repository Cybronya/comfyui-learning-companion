---
key: 视频生成/文生视频/MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2089027291140681730.json
name: MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2089027291140681730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2089027291140681730.json
hash: 7f522f1595603ea2
coverage: 0.393162
learned_at: 2026-10-11 21:19:46
nodes: [PrimitiveFloat, ResolutionSelector, ResolutionSelector, PrimitiveInt, VHS_VideoCombine, KSamplerSelect, ModelAttentionBackend, MiniMaxChunkFeedForward, VAELoader, CLIPLoader, VAELoader, ComfyMathExpression, YuanAudioSplit, GetImage, GetImage, GetImage, BasicScheduler, UNETLoader, MiniMaxLowVRAMAttention, LoraLoaderModelOnly, RandomNoise, YUAN_TXTJsonSwitch, YuanAudioList, YUAN_TXTPreviewContent, ComfyMathExpression, YuanTool, YUAN_TXTJsonExtractor, SamplerCustomAdvanced, BasicGuider, KSamplerSelect, BasicScheduler, Yuan_H3Upscale3D, SamplerCustomAdvanced, Yuan_MiniMaxH3Video, BasicGuider, Yuan_H3MotionContextTrim, Yuan_H3MotionContext, CR Text, RandomNoise, AudioConcat, Int, Int, If ANY execute A else B, easy forLoopStart, EmptyAudio, easy isNone, easy batchAnything, easy forLoopEnd, easy mathInt, PreviewImage, YuanMultiImage, PrimitiveStringMultiline, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Int, Int, PrimitiveStringMultiline, Note, YuanMultiImage, Note, Note, Note, LoadImage, LoadImage, PrimitiveNode]
patterns: []
missing: [CR Text, If ANY execute A else B, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy isNone, easy mathInt]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `If ANY execute A else B` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2089027291140681730.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax-H3全栈式短剧生成V4.2.2（短剧版本直出1分钟）+全节点注释_2089027291140681730.json`

## 结构

**生成流程**：Model → Latent → Sampling → Process → Output → Other

**节点**（117 个）：
- `PrimitiveFloat`
- `ResolutionSelector`
- `ResolutionSelector`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `KSamplerSelect` ★核心
- `ModelAttentionBackend`
- `MiniMaxChunkFeedForward`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `ComfyMathExpression`
- `YuanAudioSplit`
- `GetImage`
- `GetImage`
- `GetImage`
- `BasicScheduler`
- `UNETLoader` ★核心
- `MiniMaxLowVRAMAttention`
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `YUAN_TXTJsonSwitch`
- `YuanAudioList`
- `YUAN_TXTPreviewContent`
- `ComfyMathExpression`
- `YuanTool`
- `YUAN_TXTJsonExtractor`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `Yuan_H3Upscale3D`
- `SamplerCustomAdvanced` ★核心
- `Yuan_MiniMaxH3Video`
- `BasicGuider`
- `Yuan_H3MotionContextTrim`
- `Yuan_H3MotionContext`
- `CR Text`
- `RandomNoise`
- `AudioConcat`
- `Int`
- `Int`
- `If ANY execute A else B`
- `easy forLoopStart`
- `EmptyAudio`
- `easy isNone`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy mathInt`
- `PreviewImage`
- `YuanMultiImage`
- `PrimitiveStringMultiline`
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
- `Note`
- `Note`
- `Note`
- `Note`
- `Int`
- `Int`
- `PrimitiveStringMultiline`
- `Note`
- `YuanMultiImage`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `PrimitiveNode`

## 知识

覆盖率 **39%**（46/117）

**有卡**：`ResolutionSelector`、`VHS_VideoCombine`、`KSamplerSelect`、`ModelAttentionBackend`、`MiniMaxChunkFeedForward`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`YuanAudioSplit`、`GetImage`、`BasicScheduler`、`UNETLoader`、`MiniMaxLowVRAMAttention`、`LoraLoaderModelOnly`、`RandomNoise`、`YUAN_TXTJsonSwitch`、`YuanAudioList`、`YUAN_TXTPreviewContent`、`YuanTool`、`YUAN_TXTJsonExtractor`、`SamplerCustomAdvanced`、`BasicGuider`、`Yuan_H3Upscale3D`、`Yuan_MiniMaxH3Video`、`Yuan_H3MotionContextTrim`、`Yuan_H3MotionContext`、`AudioConcat`、`Int`、`EmptyAudio`、`YuanMultiImage`、`LoadImage`

**缺卡**（7）：`CR Text`、`If ANY execute A else B`、`easy batchAnything`、`easy forLoopEnd`、`easy forLoopStart`、`easy isNone`、`easy mathInt`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `If ANY execute A else B` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
