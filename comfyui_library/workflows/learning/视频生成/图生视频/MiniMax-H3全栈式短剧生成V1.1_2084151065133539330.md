---
key: 视频生成/图生视频/MiniMax-H3全栈式短剧生成V1.1_2084151065133539330.json
name: MiniMax-H3全栈式短剧生成V1.1_2084151065133539330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V1.1_2084151065133539330.json
hash: c6568b8376619260
coverage: 0.529412
learned_at: 2026-10-16 19:52:16
nodes: [INTConstant, INTConstant, GetNode, ComfySwitchNode, SetNode, SetNode, ComfySwitchNode, RegexExtract, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, easy positive, PrimitiveBoolean, PrimitiveFloat, INTConstant, INTConstant, PrimitiveBoolean, RegexExtract, StringReplace, YUAN_TXTAppearanceOrder, PrimitiveStringMultiline, YUAN_TXTParagraphSplitter, YUAN_TXTReplace, StringLength, YUAN_TXTConvertAny, ComfySwitchNode, ComfySwitchNode, GetNode, GetNode, ComfyNotNode, ImageBatchMulti, ComfyAndNode, GetNode, ComfyMathExpression, SetNode, StringConcatenate, RegexExtract, RegexExtract, RegexExtract, SetNode, SetNode, SetNode, PrimitiveStringMultiline, YUAN_TXTReplace, GetNode, GetNode, GetNode, PrimitiveStringMultiline, GetImage, RegexExtract, YUAN_TXTParagraphSplitter, YUAN_TXTParagraphSplitter, ComfySwitchNode, ComfySwitchNode, GetNode, RegexExtract, YUAN_TXTReplace, YUAN_TXTReplace, YUAN_TXTParagraphSplitter, RegexExtract, SetNode, VAEDecodeAudio, ComfySwitchNode, SetNode, StringReplace, GetNode, YUAN_TXTReplace, SetNode, ComfySwitchNode, YUAN_TXTListNumber, GetNode, GetNode, RegexExtract, YUAN_TXTParagraphSplitter, YUAN_TXTAppearanceOrder, YUAN_TXTParagraphSplitter, YUAN_TXTListNumber, ComfyMathExpression, RegexExtract, YUAN_TXTParagraphSplitter, YUAN_TXTConvertAny, SetNode, easy indexAnything, RegexExtract, YUAN_TXTConvertAny, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, YUAN_TXTParagraphSplitter, GetNode, ComfyMathExpression, YUAN_TXTListNumber, ComfyMathExpression, SetNode, VAEDecode, SetNode, SetNode, BasicScheduler, GetImage, GetImage, ComfySwitchNode, ComfySwitchNode, CS-MultiImageLoader, CS-MultiImageLoader, CS-MultiImageLoader, PrimitiveInt, VAELoader, VAELoader, ShowText|pysssss, VHS_VideoCombine, SamplerCustomAdvanced, GetNode, GetNode, BasicGuider, SetNode, UNETLoader, SetNode, SetNode, SetNode, CLIPLoader, GetNode, GetNode, KSamplerSelect, easy imagesSplitImage, MiniMaxH3ReferenceToVideo, YuanTool, RandomNoise, PreviewImage, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax-H3全栈式短剧生成V1.1_2084151065133539330.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V1.1_2084151065133539330.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（136 个）：
- `INTConstant`
- `INTConstant`
- `GetNode`
- `ComfySwitchNode`
- `SetNode`
- `SetNode`
- `ComfySwitchNode`
- `RegexExtract`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy positive`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `INTConstant`
- `INTConstant`
- `PrimitiveBoolean`
- `RegexExtract`
- `StringReplace`
- `YUAN_TXTAppearanceOrder`
- `PrimitiveStringMultiline`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTReplace`
- `StringLength`
- `YUAN_TXTConvertAny`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `ComfyNotNode`
- `ImageBatchMulti`
- `ComfyAndNode`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `StringConcatenate`
- `RegexExtract`
- `RegexExtract`
- `RegexExtract`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `YUAN_TXTReplace`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `GetImage`
- `RegexExtract`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTParagraphSplitter`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `GetNode`
- `RegexExtract`
- `YUAN_TXTReplace`
- `YUAN_TXTReplace`
- `YUAN_TXTParagraphSplitter`
- `RegexExtract`
- `SetNode`
- `VAEDecodeAudio` ★核心
- `ComfySwitchNode`
- `SetNode`
- `StringReplace`
- `GetNode`
- `YUAN_TXTReplace`
- `SetNode`
- `ComfySwitchNode`
- `YUAN_TXTListNumber`
- `GetNode`
- `GetNode`
- `RegexExtract`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTAppearanceOrder`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTListNumber`
- `ComfyMathExpression`
- `RegexExtract`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTConvertAny`
- `SetNode`
- `easy indexAnything`
- `RegexExtract`
- `YUAN_TXTConvertAny`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `YUAN_TXTParagraphSplitter`
- `GetNode`
- `ComfyMathExpression`
- `YUAN_TXTListNumber`
- `ComfyMathExpression`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `BasicScheduler`
- `GetImage`
- `GetImage`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `CS-MultiImageLoader`
- `CS-MultiImageLoader`
- `CS-MultiImageLoader`
- `PrimitiveInt`
- `VAELoader`
- `VAELoader`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `BasicGuider`
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `easy imagesSplitImage`
- `MiniMaxH3ReferenceToVideo`
- `YuanTool`
- `RandomNoise`
- `PreviewImage`
- `MarkdownNote`

## 知识

覆盖率 **53%**（72/136）

**有卡**：`INTConstant`、`RegexExtract`、`easy positive`、`PrimitiveBoolean`、`StringReplace`、`YUAN_TXTAppearanceOrder`、`YUAN_TXTParagraphSplitter`、`YUAN_TXTReplace`、`StringLength`、`YUAN_TXTConvertAny`、`ComfyNotNode`、`ImageBatchMulti`、`ComfyAndNode`、`ComfyMathExpression`、`StringConcatenate`、`GetImage`、`VAEDecodeAudio`、`YUAN_TXTListNumber`、`easy indexAnything`、`VAEDecode`、`BasicScheduler`、`CS-MultiImageLoader`、`VAELoader`、`VHS_VideoCombine`、`SamplerCustomAdvanced`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`KSamplerSelect`、`easy imagesSplitImage`、`MiniMaxH3ReferenceToVideo`、`YuanTool`、`RandomNoise`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio、BasicGuider
