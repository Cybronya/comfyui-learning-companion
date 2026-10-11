---
key: 视频生成/文生视频/MiniMax-H3 全栈式短剧 多图音频参考二采优化版V1.0_2096284114990223362.json
name: MiniMax-H3 全栈式短剧 多图音频参考二采优化版V1.0_2096284114990223362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax-H3 全栈式短剧 多图音频参考二采优化版V1.0_2096284114990223362.json
hash: 513af72800412a89
coverage: 0.365854
learned_at: 2026-10-11 21:41:46
nodes: [GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, MarkdownNote, CLIPLoader, YUAN_TXTJsonExtractor, GetNode, GetNode, GetImage, GetImage, GetNode, GetImage, ResolutionSelector, GetNode, YuanTool, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, YUAN_TXTParagraphSplitter, GetNode, GetNode, PrimitiveInt, SetNode, TextGenerate, StringConcatenate, PrimitiveStringMultiline, SetNode, ResolutionSelector, SetNode, SetNode, SetNode, GetNode, PreviewImage, YUAN_TXTShotReplace, ShowText|pysssss, GetNode, PrimitiveNode, YuanAudioList, PrimitiveStringMultiline, ImageScale, LoadImage, GetNode, Reroute, Reroute, GetNode, GetNode, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, SetNode, BasicGuider, SetNode, SetNode, SetNode, GetNode, LTXVConcatAVLatent, GetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, RandomNoise, 忽略多组孤海, KSamplerSelect, UNETLoader, SetNode, GetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, BasicScheduler, MinimaxH3LatentUpscaler3D, VAEDecode, VAEDecodeAudio, GetNode, GetNode, ComfyMathExpression, PrimitiveStringMultiline, SetNode, easy float, SetNode, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, PrimitiveFloat, ComfyMathExpression, SetNode, ResolutionSelector, SetNode, SetNode, Note, YuanAudioSplit, PrimitiveFloat, YuanMultiImage, SplitSigmas, SetNode, VAELoader, SetNode, SetNode, SetNode, VAELoader, SetNode, CLIPLoader, SetNode, LoraLoaderModelOnly, SetNode, SetNode, SetNode, VHS_VideoCombine]
patterns: []
missing: [easy float, 忽略多组孤海]
discoveries: [次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/MiniMax-H3 全栈式短剧 多图音频参考二采优化版V1.0_2096284114990223362.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax-H3 全栈式短剧 多图音频参考二采优化版V1.0_2096284114990223362.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（123 个）：
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
- `MarkdownNote`
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
- `YUAN_TXTParagraphSplitter`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `SetNode`
- `TextGenerate`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `YUAN_TXTShotReplace`
- `ShowText|pysssss`
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
- `忽略多组孤海`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `MinimaxH3LatentUpscaler3D`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `PrimitiveStringMultiline`
- `SetNode`
- `easy float`
- `SetNode`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `Note`
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

## 知识

覆盖率 **37%**（45/123）

**有卡**：`CLIPLoader`、`YUAN_TXTJsonExtractor`、`GetImage`、`ResolutionSelector`、`YuanTool`、`YUAN_TXTParagraphSplitter`、`TextGenerate`、`StringConcatenate`、`YUAN_TXTShotReplace`、`YuanAudioList`、`ImageScale`、`LoadImage`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicGuider`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`RandomNoise`、`KSamplerSelect`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`BasicScheduler`、`MinimaxH3LatentUpscaler3D`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`YuanAudioSplit`、`YuanMultiImage`、`SplitSigmas`、`VAELoader`

**缺卡**（2）：`easy float`、`忽略多组孤海`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
