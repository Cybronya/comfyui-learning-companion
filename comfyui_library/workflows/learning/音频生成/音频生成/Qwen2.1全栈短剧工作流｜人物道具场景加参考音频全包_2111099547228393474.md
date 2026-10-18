---
key: 音频生成/音频生成/Qwen2.1全栈短剧工作流｜人物道具场景加参考音频全包_2111099547228393474.json
name: Qwen2.1全栈短剧工作流｜人物道具场景加参考音频全包_2111099547228393474
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Qwen2.1全栈短剧工作流｜人物道具场景加参考音频全包_2111099547228393474.json
hash: 6aa3c4b045094015
coverage: 0.682171
learned_at: 2026-10-18 18:02:24
nodes: [YUAN_TXTConvertAny, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, GetNode, GetNode, StringReplace, StringConcatenate, PrimitiveStringMultiline, SetNode, SetNode, GetNode, ComfySwitchNode, ComfySwitchNode, YUAN_TXTParagraphSplitter, StringReplace, GetNode, StringConcatenate, StringReplace, SetNode, ComfyMathExpression, YUAN_TXTParagraphSplitter, YUAN_TXTConvertAny, GetNode, GetNode, StringConcatenate, StringReplace, PrimitiveInt, RegexExtract, YUAN_TXTParagraphSplitter, ComfySwitchNode, GetNode, SetNode, YUAN_TXTJsonExtractor, ComfyMathExpression, SetNode, GetNode, StringConcatenate, PrimitiveStringMultiline, SaveAudio, FB_Qwen3TTSVoiceDesign, YUAN_TXTReplace, PrimitiveStringMultiline, PrimitiveStringMultiline, YUAN_TXTPreviewContent, RegexExtract, PrimitiveStringMultiline, EmptyLatentImage, SetNode, EmptyLatentImage, GetNode, KSampler, VAEDecode, YUAN_TXTReplace, SaveImage, GetNode, YUAN_TXTParagraphSplitter, StringReplace, StringReplace, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, StringReplace, PrimitiveStringMultiline, KSampler, YUAN_TXTConvertAny, VAEEncode, TextEncodeQwenImage21, VAEDecode, SaveImage, TextEncodeQwenImage21, ResolutionSelector, PrimitiveStringMultiline, VAELoader, CLIPLoader, UNETLoader, CLIPLoader, VAELoader, UNETLoader, ResolutionSelector, PrimitiveNode, PrimitiveNode, YuanCustomCombo, PrimitiveStringMultiline, ComfySwitchNode, LoadImage, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 音频生成/音频生成/Qwen2.1全栈短剧工作流｜人物道具场景加参考音频全包_2111099547228393474.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Qwen2.1全栈短剧工作流｜人物道具场景加参考音频全包_2111099547228393474.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（129 个）：
- `YUAN_TXTConvertAny`
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
- `SaveAudio`
- `FB_Qwen3TTSVoiceDesign`
- `YUAN_TXTReplace`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `YUAN_TXTPreviewContent`
- `RegexExtract`
- `PrimitiveStringMultiline`
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
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `PrimitiveNode`
- `PrimitiveNode`
- `YuanCustomCombo`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `LoadImage`
- `PrimitiveStringMultiline`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **68%**（88/129）

**有卡**：`YUAN_TXTConvertAny`、`StringReplace`、`StringConcatenate`、`YUAN_TXTParagraphSplitter`、`ComfyMathExpression`、`RegexExtract`、`YUAN_TXTJsonExtractor`、`SaveAudio`、`FB_Qwen3TTSVoiceDesign`、`YUAN_TXTReplace`、`YUAN_TXTPreviewContent`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`VAEEncode`、`TextEncodeQwenImage21`、`ResolutionSelector`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`YuanCustomCombo`、`LoadImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
