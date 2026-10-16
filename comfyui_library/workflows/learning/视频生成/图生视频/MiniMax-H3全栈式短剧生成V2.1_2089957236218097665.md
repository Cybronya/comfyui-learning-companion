---
key: 视频生成/图生视频/MiniMax-H3全栈式短剧生成V2.1_2089957236218097665.json
name: MiniMax-H3全栈式短剧生成V2.1_2089957236218097665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V2.1_2089957236218097665.json
hash: e106ab7d2e384e74
coverage: 0.528926
learned_at: 2026-10-16 22:02:06
nodes: [INTConstant, INTConstant, GetNode, ComfySwitchNode, SetNode, SetNode, ComfySwitchNode, SetNode, SetNode, SetNode, easy positive, PrimitiveBoolean, PrimitiveFloat, INTConstant, INTConstant, PrimitiveBoolean, SetNode, PrimitiveStringMultiline, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetImage, GetImage, GetImage, GetNode, YUAN_TXTParagraphSplitter, GetNode, YUAN_TXTConvertAny, RegexExtract, RegexExtract, YUAN_TXTAppearanceOrder, YUAN_TXTReplace, YUAN_TXTParagraphSplitter, SetNode, YUAN_TXTListNumber, RegexExtract, RegexExtract, RegexExtract, YUAN_TXTAppearanceOrder, YUAN_TXTReplace, YUAN_TXTParagraphSplitter, SetNode, RegexExtract, RegexExtract, YUAN_TXTReplace, SetNode, YUAN_TXTParagraphSplitter, RegexExtract, RegexExtract, ComfySwitchNode, StringReplace, StringConcatenate, StringReplace, YUAN_TXTParagraphSplitter, PrimitiveStringMultiline, GetNode, YUAN_TXTLength, SetNode, SetNode, YUAN_TXTConvertAny, RegexExtract, YUAN_TXTParagraphSplitter, YUAN_TXTConvertAny, ComfyMathExpression, GetNode, ComfyMathExpression, YUAN_TXTListNumber, GetNode, ComfySwitchNode, YUAN_TXTListNumber, YUAN_TXTParagraphSplitter, SetNode, GetNode, GetNode, GetNode, BasicGuider, SamplerCustomAdvanced, GetNode, KSamplerSelect, BasicScheduler, SetNode, VAEDecode, VAEDecodeAudio, GetNode, SetNode, SetNode, VHS_VideoCombine, MiniMaxH3MemoryEfficientSageAttentionPatch, SetNode, YuanTool, SetNode, Yuan_MiniMaxH3Video, GetNode, GetNode, ComfyMathExpression, GetNode, YUAN_TXTReplace, ComfySwitchNode, ComfySwitchNode, UNETLoader, VAELoader, CLIPLoader, VAELoader, MarkdownNote, RandomNoise, ShowText|pysssss, GetNode, GetNode, PreviewImage, CS-MultiImageLoader, CS-MultiImageLoader, PrimitiveStringMultiline, CS-MultiImageLoader, PrimitiveInt]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax-H3全栈式短剧生成V2.1_2089957236218097665.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3全栈式短剧生成V2.1_2089957236218097665.json`

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
- `SetNode`
- `SetNode`
- `GetNode`
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
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `YUAN_TXTReplace`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `MarkdownNote`
- `RandomNoise`
- `ShowText|pysssss`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `CS-MultiImageLoader`
- `CS-MultiImageLoader`
- `PrimitiveStringMultiline`
- `CS-MultiImageLoader`
- `PrimitiveInt`

## 知识

覆盖率 **53%**（64/121）

**有卡**：`INTConstant`、`easy positive`、`PrimitiveBoolean`、`GetImage`、`YUAN_TXTParagraphSplitter`、`YUAN_TXTConvertAny`、`RegexExtract`、`YUAN_TXTAppearanceOrder`、`YUAN_TXTReplace`、`YUAN_TXTListNumber`、`StringReplace`、`StringConcatenate`、`YUAN_TXTLength`、`ComfyMathExpression`、`BasicGuider`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`YuanTool`、`Yuan_MiniMaxH3Video`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`RandomNoise`、`CS-MultiImageLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio、BasicGuider
