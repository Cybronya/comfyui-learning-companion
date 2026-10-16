---
key: 视频生成/图生视频/MiniMax-H3全栈式短剧生成V2.1_2084946150561501185.json
name: MiniMax-H3全栈式短剧生成V2.1_2084946150561501185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V2.1_2084946150561501185.json
hash: 6821dd0f4fc1cf07
coverage: 0.528926
learned_at: 2026-10-16 20:50:31
nodes: [INTConstant, INTConstant, GetNode, ComfySwitchNode, SetNode, SetNode, ComfySwitchNode, SetNode, SetNode, SetNode, easy positive, PrimitiveBoolean, PrimitiveFloat, INTConstant, INTConstant, PrimitiveBoolean, SetNode, PrimitiveStringMultiline, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, PrimitiveStringMultiline, GetNode, GetNode, GetImage, GetImage, GetImage, GetNode, YUAN_TXTParagraphSplitter, GetNode, YUAN_TXTConvertAny, RegexExtract, RegexExtract, YUAN_TXTAppearanceOrder, YUAN_TXTReplace, YUAN_TXTParagraphSplitter, SetNode, YUAN_TXTListNumber, RegexExtract, RegexExtract, RegexExtract, YUAN_TXTAppearanceOrder, YUAN_TXTReplace, YUAN_TXTParagraphSplitter, SetNode, RegexExtract, RegexExtract, YUAN_TXTReplace, SetNode, YUAN_TXTParagraphSplitter, RegexExtract, RegexExtract, ComfySwitchNode, StringReplace, StringConcatenate, StringReplace, YUAN_TXTParagraphSplitter, PrimitiveStringMultiline, GetNode, YUAN_TXTLength, SetNode, SetNode, YUAN_TXTConvertAny, RegexExtract, YUAN_TXTParagraphSplitter, YUAN_TXTConvertAny, ComfyMathExpression, GetNode, ComfyMathExpression, YUAN_TXTListNumber, GetNode, ComfySwitchNode, YUAN_TXTListNumber, YUAN_TXTParagraphSplitter, SetNode, GetNode, GetNode, GetNode, BasicGuider, SamplerCustomAdvanced, GetNode, KSamplerSelect, BasicScheduler, SetNode, VAEDecode, VAEDecodeAudio, GetNode, SetNode, SetNode, VHS_VideoCombine, MiniMaxH3MemoryEfficientSageAttentionPatch, SetNode, YuanTool, SetNode, Yuan_MiniMaxH3Video, ShowText|pysssss, GetNode, GetNode, ComfyMathExpression, GetNode, GetNode, YUAN_TXTReplace, ComfySwitchNode, ComfySwitchNode, CS-MultiImageLoader, CS-MultiImageLoader, CS-MultiImageLoader, UNETLoader, VAELoader, CLIPLoader, VAELoader, PrimitiveInt, PreviewImage, MarkdownNote, RandomNoise]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax-H3全栈式短剧生成V2.1_2084946150561501185.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V2.1_2084946150561501185.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（121 个）：
- `INTConstant`
- `INTConstant`
- `GetNode`
- `ComfySwitchNode`
- `SetNode`
- `SetNode`
- `ComfySwitchNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy positive`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `INTConstant`
- `INTConstant`
- `PrimitiveBoolean`
- `SetNode`
- `PrimitiveStringMultiline`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `GetNode`
- `GetNode`
- `GetImage`
- `GetImage`
- `GetImage`
- `GetNode`
- `YUAN_TXTParagraphSplitter`
- `GetNode`
- `YUAN_TXTConvertAny`
- `RegexExtract`
- `RegexExtract`
- `YUAN_TXTAppearanceOrder`
- `YUAN_TXTReplace`
- `YUAN_TXTParagraphSplitter`
- `SetNode`
- `YUAN_TXTListNumber`
- `RegexExtract`
- `RegexExtract`
- `RegexExtract`
- `YUAN_TXTAppearanceOrder`
- `YUAN_TXTReplace`
- `YUAN_TXTParagraphSplitter`
- `SetNode`
- `RegexExtract`
- `RegexExtract`
- `YUAN_TXTReplace`
- `SetNode`
- `YUAN_TXTParagraphSplitter`
- `RegexExtract`
- `RegexExtract`
- `ComfySwitchNode`
- `StringReplace`
- `StringConcatenate`
- `StringReplace`
- `YUAN_TXTParagraphSplitter`
- `PrimitiveStringMultiline`
- `GetNode`
- `YUAN_TXTLength`
- `SetNode`
- `SetNode`
- `YUAN_TXTConvertAny`
- `RegexExtract`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTConvertAny`
- `ComfyMathExpression`
- `GetNode`
- `ComfyMathExpression`
- `YUAN_TXTListNumber`
- `GetNode`
- `ComfySwitchNode`
- `YUAN_TXTListNumber`
- `YUAN_TXTParagraphSplitter`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SetNode`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SetNode`
- `YuanTool`
- `SetNode`
- `Yuan_MiniMaxH3Video`
- `ShowText|pysssss`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `YUAN_TXTReplace`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `CS-MultiImageLoader`
- `CS-MultiImageLoader`
- `CS-MultiImageLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `PrimitiveInt`
- `PreviewImage`
- `MarkdownNote`
- `RandomNoise`

## 知识

覆盖率 **53%**（64/121）

**有卡**：`INTConstant`、`easy positive`、`PrimitiveBoolean`、`GetImage`、`YUAN_TXTParagraphSplitter`、`YUAN_TXTConvertAny`、`RegexExtract`、`YUAN_TXTAppearanceOrder`、`YUAN_TXTReplace`、`YUAN_TXTListNumber`、`StringReplace`、`StringConcatenate`、`YUAN_TXTLength`、`ComfyMathExpression`、`BasicGuider`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`YuanTool`、`Yuan_MiniMaxH3Video`、`CS-MultiImageLoader`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`RandomNoise`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio、BasicGuider
