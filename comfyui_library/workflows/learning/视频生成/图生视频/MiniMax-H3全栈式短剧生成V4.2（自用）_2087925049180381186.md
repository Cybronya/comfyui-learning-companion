---
key: 视频生成/图生视频/MiniMax-H3全栈式短剧生成V4.2（自用）_2087925049180381186.json
name: MiniMax-H3全栈式短剧生成V4.2（自用）_2087925049180381186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V4.2（自用）_2087925049180381186.json
hash: 30cb953ec0c5fe96
coverage: 0.46281
learned_at: 2026-10-16 21:27:43
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, YuanTool, SetNode, GetNode, RegexExtract, YUAN_TXTListNumber, YUAN_TXTListNumber, ComfySwitchNode, YUAN_TXTAppearanceOrder, YUAN_TXTAppearanceOrder, StringReplace, StringReplace, PrimitiveStringMultiline, StringConcatenate, GetNode, YUAN_TXTParagraphSplitter, YUAN_TXTParagraphSplitter, GetNode, YUAN_TXTParagraphSplitter, GetImage, GetImage, ComfySwitchNode, INTConstant, ComfySwitchNode, GetNode, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, RegexExtract, SetNode, ComfySwitchNode, ComfySwitchNode, SetNode, SetNode, YUAN_TXTReplace, SetNode, PrimitiveBoolean, PrimitiveFloat, INTConstant, INTConstant, GetImage, PrimitiveStringMultiline, GetNode, YUAN_TXTParagraphSplitter, PrimitiveStringMultiline, GetNode, YUAN_TXTListNumber, RandomNoise, SetNode, SetNode, SetNode, SetNode, PrimitiveStringMultiline, SetNode, PrimitiveBoolean, SetNode, ComfySwitchNode, GetNode, GetNode, GetNode, ComfyMathExpression, GetNode, BasicGuider, KSamplerSelect, YUAN_TXTJsonExtractor, SetNode, SetNode, SetNode, RandomNoise, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, SetNode, YUAN_TXTParagraphSplitter, ShowText|pysssss, BasicGuider, GetNode, SamplerCustomAdvanced, VHS_VideoCombine, GetNode, GetNode, ComfyMathExpression, GetNode, KSamplerSelect, SamplerCustomAdvanced, GetNode, VAEDecode, GetNode, VAEDecodeAudio, SetNode, SetNode, SetNode, ModelAttentionBackend, Yuan_H3MotionContext, GetNode, BasicScheduler, BasicScheduler, UNETLoader, VAELoader, CLIPLoader, VAELoader, PreviewImage, Yuan_H3MotionContextTrim, Yuan_H3MotionContextLoadLatent, MarkdownNote, LoraLoaderModelOnly, Yuan_MiniMaxH3Video, Yuan_RTXVideoUpscaleH3, PrimitiveInt, PrimitiveStringMultiline, YuanMultiImage]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax-H3全栈式短剧生成V4.2（自用）_2087925049180381186.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V4.2（自用）_2087925049180381186.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（121 个）：
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
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `VAEDecodeAudio` ★核心
- `SetNode`
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
- `PreviewImage`
- `Yuan_H3MotionContextTrim`
- `Yuan_H3MotionContextLoadLatent`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `Yuan_MiniMaxH3Video`
- `Yuan_RTXVideoUpscaleH3`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `YuanMultiImage`

## 知识

覆盖率 **46%**（56/121）

**有卡**：`YuanTool`、`RegexExtract`、`YUAN_TXTListNumber`、`YUAN_TXTAppearanceOrder`、`StringReplace`、`StringConcatenate`、`YUAN_TXTParagraphSplitter`、`GetImage`、`INTConstant`、`YUAN_TXTReplace`、`PrimitiveBoolean`、`RandomNoise`、`ComfyMathExpression`、`BasicGuider`、`KSamplerSelect`、`YUAN_TXTJsonExtractor`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`VAEDecode`、`VAEDecodeAudio`、`ModelAttentionBackend`、`Yuan_H3MotionContext`、`BasicScheduler`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`Yuan_H3MotionContextTrim`、`Yuan_H3MotionContextLoadLatent`、`LoraLoaderModelOnly`、`Yuan_MiniMaxH3Video`、`Yuan_RTXVideoUpscaleH3`、`YuanMultiImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio
