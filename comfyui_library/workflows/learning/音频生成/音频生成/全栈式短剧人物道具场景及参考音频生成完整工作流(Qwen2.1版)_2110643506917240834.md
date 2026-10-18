---
key: 音频生成/音频生成/全栈式短剧人物道具场景及参考音频生成完整工作流(Qwen2.1版)_2110643506917240834.json
name: 全栈式短剧人物道具场景及参考音频生成完整工作流(Qwen2.1版)_2110643506917240834
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/全栈式短剧人物道具场景及参考音频生成完整工作流(Qwen2.1版)_2110643506917240834.json
hash: f845755fdac5a2fc
coverage: 0.521277
learned_at: 2026-10-18 18:02:37
nodes: [YUAN_TXTConvertAny, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, GetNode, GetNode, StringReplace, StringConcatenate, PrimitiveStringMultiline, SetNode, SetNode, GetNode, ComfySwitchNode, ComfySwitchNode, GetNode, YUAN_TXTParagraphSplitter, StringReplace, GetNode, StringConcatenate, StringReplace, SetNode, ComfyMathExpression, YUAN_TXTParagraphSplitter, YUAN_TXTConvertAny, GetNode, GetNode, StringConcatenate, StringReplace, PrimitiveInt, RegexExtract, YUAN_TXTParagraphSplitter, ComfySwitchNode, GetNode, SetNode, YUAN_TXTJsonExtractor, ComfyMathExpression, SetNode, GetNode, StringConcatenate, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, SaveAudio, FB_Qwen3TTSVoiceDesign, YUAN_TXTReplace, PrimitiveStringMultiline, PrimitiveStringMultiline, YUAN_TXTPreviewContent, RegexExtract, PrimitiveStringMultiline, MarkdownNote, EmptyLatentImage, SetNode, EmptyLatentImage, GetNode, KSampler, VAEDecode, YUAN_TXTReplace, SaveImage, GetNode, YUAN_TXTParagraphSplitter, StringReplace, StringReplace, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, StringReplace, PrimitiveStringMultiline, PrimitiveStringMultiline, KSampler, YUAN_TXTConvertAny, VAEEncode, TextEncodeQwenImage21, VAEDecode, SaveImage, TextEncodeQwenImage21, ResolutionSelector, PrimitiveStringMultiline, VAELoader, CLIPLoader, UNETLoader, MarkdownNote, CLIPLoader, VAELoader, UNETLoader, ResolutionSelector, PrimitiveNode, PrimitiveNode, YuanCustomCombo, PrimitiveStringMultiline, MarkdownNote, ComfySwitchNode, LoadImage, PrimitiveStringMultiline]
patterns: [image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 205559047198491, "steps": 25, "width": 1088}
---

# 音频生成/音频生成/全栈式短剧人物道具场景及参考音频生成完整工作流(Qwen2.1版)_2110643506917240834.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/全栈式短剧人物道具场景及参考音频生成完整工作流(Qwen2.1版)_2110643506917240834.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（94 个）：
- `YUAN_TXTConvertAny`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `GetNode`
- `GetNode`
- `StringReplace`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `SetNode`
- `SetNode`
- `GetNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `GetNode`
- `YUAN_TXTParagraphSplitter`
- `StringReplace`
- `GetNode`
- `StringConcatenate`
- `StringReplace`
- `SetNode`
- `ComfyMathExpression`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTConvertAny`
- `GetNode`
- `GetNode`
- `StringConcatenate`
- `StringReplace`
- `PrimitiveInt`
- `RegexExtract`
- `YUAN_TXTParagraphSplitter`
- `ComfySwitchNode`
- `GetNode`
- `SetNode`
- `YUAN_TXTJsonExtractor`
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `SaveAudio`
- `FB_Qwen3TTSVoiceDesign`
- `YUAN_TXTReplace`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `YUAN_TXTPreviewContent`
- `RegexExtract`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `SetNode`
- `EmptyLatentImage` ★核心
- `GetNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `YUAN_TXTReplace`
- `SaveImage`
- `GetNode`
- `YUAN_TXTParagraphSplitter`
- `StringReplace`
- `StringReplace`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `StringReplace`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `KSampler` ★核心
- `YUAN_TXTConvertAny`
- `VAEEncode` ★核心
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `PrimitiveNode`
- `PrimitiveNode`
- `YuanCustomCombo`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `ComfySwitchNode`
- `LoadImage`
- `PrimitiveStringMultiline`

**识别到的模式**：image_to_image

## 关键参数

- `width` = `1088`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `205559047198491`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **52%**（49/94）

**有卡**：`YUAN_TXTConvertAny`、`StringReplace`、`StringConcatenate`、`YUAN_TXTParagraphSplitter`、`ComfyMathExpression`、`RegexExtract`、`YUAN_TXTJsonExtractor`、`SaveAudio`、`FB_Qwen3TTSVoiceDesign`、`YUAN_TXTReplace`、`YUAN_TXTPreviewContent`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`VAEEncode`、`TextEncodeQwenImage21`、`ResolutionSelector`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`YuanCustomCombo`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
