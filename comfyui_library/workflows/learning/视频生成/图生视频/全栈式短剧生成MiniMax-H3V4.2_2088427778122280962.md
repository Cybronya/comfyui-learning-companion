---
key: 视频生成/图生视频/全栈式短剧生成MiniMax-H3V4.2_2088427778122280962.json
name: 全栈式短剧生成MiniMax-H3V4.2_2088427778122280962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/全栈式短剧生成MiniMax-H3V4.2_2088427778122280962.json
hash: badf05f8a826d839
coverage: 0.467213
learned_at: 2026-10-16 21:43:45
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, YuanTool, SetNode, GetNode, RegexExtract, YUAN_TXTListNumber, YUAN_TXTListNumber, ComfySwitchNode, YUAN_TXTAppearanceOrder, YUAN_TXTAppearanceOrder, StringReplace, StringReplace, PrimitiveStringMultiline, StringConcatenate, GetNode, YUAN_TXTParagraphSplitter, YUAN_TXTParagraphSplitter, GetNode, YUAN_TXTParagraphSplitter, GetImage, GetImage, ComfySwitchNode, INTConstant, ComfySwitchNode, GetNode, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, RegexExtract, SetNode, ComfySwitchNode, ComfySwitchNode, SetNode, SetNode, YUAN_TXTReplace, SetNode, PrimitiveBoolean, PrimitiveFloat, INTConstant, INTConstant, GetImage, PrimitiveStringMultiline, YUAN_TXTParagraphSplitter, PrimitiveStringMultiline, GetNode, YUAN_TXTListNumber, RandomNoise, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ComfySwitchNode, GetNode, GetNode, GetNode, ComfyMathExpression, GetNode, BasicGuider, KSamplerSelect, YUAN_TXTJsonExtractor, SetNode, SetNode, SetNode, RandomNoise, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, SetNode, YUAN_TXTParagraphSplitter, ShowText|pysssss, BasicGuider, GetNode, SamplerCustomAdvanced, VHS_VideoCombine, Yuan_MiniMaxH3Video, GetNode, GetNode, ComfyMathExpression, GetNode, KSamplerSelect, GetNode, VAEDecode, GetNode, VAEDecodeAudio, SetNode, SetNode, ModelAttentionBackend, Yuan_H3MotionContext, GetNode, PrimitiveStringMultiline, BasicScheduler, BasicScheduler, UNETLoader, VAELoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, Yuan_RTXVideoUpscaleH3, Yuan_H3MotionContextTrim, PrimitiveInt, MarkdownNote, YuanMultiImage, PrimitiveStringMultiline, GetNode, LoadImage, PreviewImage, SamplerCustomAdvanced, Yuan_H3MotionContextLoadLatent, SetNode, PrimitiveBoolean]
patterns: []
missing: []
---

# 视频生成/图生视频/全栈式短剧生成MiniMax-H3V4.2_2088427778122280962.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/全栈式短剧生成MiniMax-H3V4.2_2088427778122280962.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（122 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `YuanTool`
- `SetNode`
- `GetNode`
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
- `YUAN_TXTParagraphSplitter`
- `PrimitiveStringMultiline`
- `GetNode`
- `YUAN_TXTListNumber`
- `RandomNoise`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
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
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `VAEDecodeAudio` ★核心
- `SetNode`
- `SetNode`
- `ModelAttentionBackend`
- `Yuan_H3MotionContext`
- `GetNode`
- `PrimitiveStringMultiline`
- `BasicScheduler`
- `BasicScheduler`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `Yuan_RTXVideoUpscaleH3`
- `Yuan_H3MotionContextTrim`
- `PrimitiveInt`
- `MarkdownNote`
- `YuanMultiImage`
- `PrimitiveStringMultiline`
- `GetNode`
- `LoadImage`
- `PreviewImage`
- `SamplerCustomAdvanced` ★核心
- `Yuan_H3MotionContextLoadLatent`
- `SetNode`
- `PrimitiveBoolean`

## 知识

覆盖率 **47%**（57/122）

**有卡**：`YuanTool`、`RegexExtract`、`YUAN_TXTListNumber`、`YUAN_TXTAppearanceOrder`、`StringReplace`、`StringConcatenate`、`YUAN_TXTParagraphSplitter`、`GetImage`、`INTConstant`、`YUAN_TXTReplace`、`PrimitiveBoolean`、`RandomNoise`、`ComfyMathExpression`、`BasicGuider`、`KSamplerSelect`、`YUAN_TXTJsonExtractor`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`Yuan_MiniMaxH3Video`、`VAEDecode`、`VAEDecodeAudio`、`ModelAttentionBackend`、`Yuan_H3MotionContext`、`BasicScheduler`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`Yuan_RTXVideoUpscaleH3`、`Yuan_H3MotionContextTrim`、`YuanMultiImage`、`LoadImage`、`Yuan_H3MotionContextLoadLatent`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
