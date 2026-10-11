---
key: 视频生成/文生视频/MiniMax-H3全栈式短剧生成16.10修复_2089992232983162882.json
name: MiniMax-H3全栈式短剧生成16.10修复_2089992232983162882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax-H3全栈式短剧生成16.10修复_2089992232983162882.json
hash: 232f537b595330fe
coverage: 0.48
learned_at: 2026-10-11 21:19:46
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, YuanTool, SetNode, RegexExtract, YUAN_TXTListNumber, YUAN_TXTListNumber, ComfySwitchNode, YUAN_TXTAppearanceOrder, YUAN_TXTAppearanceOrder, StringReplace, StringReplace, PrimitiveStringMultiline, StringConcatenate, GetNode, YUAN_TXTParagraphSplitter, YUAN_TXTParagraphSplitter, GetNode, YUAN_TXTParagraphSplitter, GetImage, GetImage, ComfySwitchNode, INTConstant, ComfySwitchNode, GetNode, INTConstant, GetNode, GetNode, GetNode, GetNode, RegexExtract, SetNode, ComfySwitchNode, ComfySwitchNode, SetNode, SetNode, YUAN_TXTReplace, SetNode, PrimitiveBoolean, PrimitiveFloat, INTConstant, INTConstant, GetImage, PrimitiveStringMultiline, GetNode, YUAN_TXTParagraphSplitter, PrimitiveStringMultiline, GetNode, YUAN_TXTListNumber, RandomNoise, SetNode, SetNode, SetNode, SetNode, PrimitiveStringMultiline, SetNode, PrimitiveBoolean, SetNode, ComfySwitchNode, GetNode, GetNode, GetNode, ComfyMathExpression, GetNode, BasicGuider, KSamplerSelect, YUAN_TXTJsonExtractor, SetNode, SetNode, SetNode, RandomNoise, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, SetNode, YUAN_TXTParagraphSplitter, ShowText|pysssss, BasicGuider, GetNode, SamplerCustomAdvanced, VHS_VideoCombine, Yuan_MiniMaxH3Video, GetNode, GetNode, ComfyMathExpression, GetNode, KSamplerSelect, SamplerCustomAdvanced, GetNode, GetNode, SetNode, SetNode, ModelAttentionBackend, Yuan_H3MotionContext, GetNode, BasicScheduler, BasicScheduler, UNETLoader, VAELoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, Yuan_RTXVideoUpscaleH3, Yuan_H3MotionContextTrim, Yuan_H3MotionContextLoadLatent, MarkdownNote, GetNode, GetNode, YUAN_TXTJsonExtractor, YUAN_TXTJsonExtractor, YuanMultiImage, PreviewImage, GetNode, MemoryCleaner, VAEDecode, SetNode, MemoryCleaner, VAEDecodeAudio, PrimitiveStringMultiline, PrimitiveInt]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax-H3全栈式短剧生成16.10修复_2089992232983162882.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax-H3全栈式短剧生成16.10修复_2089992232983162882.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（125 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `YuanTool`
- `SetNode`
- `RegexExtract`
- `YUAN_TXTListNumber`
- `YUAN_TXTListNumber`
- `ComfySwitchNode`
- `YUAN_TXTAppearanceOrder`
- `YUAN_TXTAppearanceOrder`
- `StringReplace`
- `StringReplace`
- `PrimitiveStringMultiline`
- `StringConcatenate`
- `GetNode`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTParagraphSplitter`
- `GetNode`
- `YUAN_TXTParagraphSplitter`
- `GetImage`
- `GetImage`
- `ComfySwitchNode`
- `INTConstant`
- `ComfySwitchNode`
- `GetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RegexExtract`
- `SetNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `SetNode`
- `SetNode`
- `YUAN_TXTReplace`
- `SetNode`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `INTConstant`
- `INTConstant`
- `GetImage`
- `PrimitiveStringMultiline`
- `GetNode`
- `YUAN_TXTParagraphSplitter`
- `PrimitiveStringMultiline`
- `GetNode`
- `YUAN_TXTListNumber`
- `RandomNoise`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `SetNode`
- `PrimitiveBoolean`
- `SetNode`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `YUAN_TXTJsonExtractor`
- `SetNode`
- `SetNode`
- `SetNode`
- `RandomNoise`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `SetNode`
- `YUAN_TXTParagraphSplitter`
- `ShowText|pysssss`
- `BasicGuider`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `Yuan_MiniMaxH3Video`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ModelAttentionBackend`
- `Yuan_H3MotionContext`
- `GetNode`
- `BasicScheduler`
- `BasicScheduler`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `Yuan_RTXVideoUpscaleH3`
- `Yuan_H3MotionContextTrim`
- `Yuan_H3MotionContextLoadLatent`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `YUAN_TXTJsonExtractor`
- `YUAN_TXTJsonExtractor`
- `YuanMultiImage`
- `PreviewImage`
- `GetNode`
- `MemoryCleaner`
- `VAEDecode` ★核心
- `SetNode`
- `MemoryCleaner`
- `VAEDecodeAudio` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveInt`

## 知识

覆盖率 **48%**（60/125）

**有卡**：`YuanTool`、`RegexExtract`、`YUAN_TXTListNumber`、`YUAN_TXTAppearanceOrder`、`StringReplace`、`StringConcatenate`、`YUAN_TXTParagraphSplitter`、`GetImage`、`INTConstant`、`YUAN_TXTReplace`、`PrimitiveBoolean`、`RandomNoise`、`ComfyMathExpression`、`BasicGuider`、`KSamplerSelect`、`YUAN_TXTJsonExtractor`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`Yuan_MiniMaxH3Video`、`ModelAttentionBackend`、`Yuan_H3MotionContext`、`BasicScheduler`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`Yuan_RTXVideoUpscaleH3`、`Yuan_H3MotionContextTrim`、`Yuan_H3MotionContextLoadLatent`、`YuanMultiImage`、`MemoryCleaner`、`VAEDecode`、`VAEDecodeAudio`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio
