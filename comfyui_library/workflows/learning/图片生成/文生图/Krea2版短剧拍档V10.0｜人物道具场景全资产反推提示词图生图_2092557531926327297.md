---
key: 图片生成/文生图/Krea2版短剧拍档V10.0｜人物道具场景全资产反推提示词图生图_2092557531926327297.json
name: Krea2版短剧拍档V10.0｜人物道具场景全资产反推提示词图生图_2092557531926327297
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2版短剧拍档V10.0｜人物道具场景全资产反推提示词图生图_2092557531926327297.json
hash: 4fc67f2f618393b9
coverage: 0.880435
learned_at: 2026-10-20 01:19:09
nodes: [EmptyLatentImage, EmptyLatentImage, PrimitiveBoolean, CFGGuider, SamplerCustomAdvanced, YUAN_TXTParagraphSplitter, YUAN_TXTJsonExtractor, RegexExtract, CLIPTextEncode, VAEDecode, easy forLoopEnd, easy batchAnything, easy forLoopStart, PrimitiveInt, YUAN_TXTConvertAny, YUAN_TXTParagraphSplitter, YUAN_TXTParagraphSplitter, PrimitiveStringMultiline, YUAN_TXTParagraphSplitter, CFGGuider, SamplerCustomAdvanced, YUAN_TXTParagraphSplitter, YUAN_TXTParagraphSplitter, PrimitiveStringMultiline, YUAN_TXTParagraphSplitter, RegexExtract, CLIPTextEncode, VAEDecode, easy forLoopEnd, easy batchAnything, easy forLoopStart, PrimitiveInt, YUAN_TXTConvertAny, YUAN_TXTParagraphSplitter, CFGGuider, SamplerCustomAdvanced, YUAN_TXTParagraphSplitter, YUAN_TXTJsonExtractor, YUAN_TXTParagraphSplitter, RegexExtract, CLIPTextEncode, VAEDecode, easy forLoopEnd, easy batchAnything, easy forLoopStart, PrimitiveInt, YUAN_TXTConvertAny, YUAN_TXTParagraphSplitter, sch_split_text, sch_split_text, CLIPTextEncode, BasicScheduler, ComfySwitchNode, CLIPLoader, UNETLoader, KSamplerSelect, VAELoader, RandomNoise, sch_split_text, SaveImage, YUAN_TXTJsonExtractor, SaveImage, SaveImage, CR Text, JjkText, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Krea2版短剧拍档V10.0｜人物道具场景全资产反推提示词图生图_2092557531926327297.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2版短剧拍档V10.0｜人物道具场景全资产反推提示词图生图_2092557531926327297.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（92 个）：
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `PrimitiveBoolean`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTJsonExtractor`
- `RegexExtract`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `easy forLoopEnd`
- `easy batchAnything`
- `easy forLoopStart`
- `PrimitiveInt`
- `YUAN_TXTConvertAny`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTParagraphSplitter`
- `PrimitiveStringMultiline`
- `YUAN_TXTParagraphSplitter`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTParagraphSplitter`
- `PrimitiveStringMultiline`
- `YUAN_TXTParagraphSplitter`
- `RegexExtract`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `easy forLoopEnd`
- `easy batchAnything`
- `easy forLoopStart`
- `PrimitiveInt`
- `YUAN_TXTConvertAny`
- `YUAN_TXTParagraphSplitter`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTJsonExtractor`
- `YUAN_TXTParagraphSplitter`
- `RegexExtract`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `easy forLoopEnd`
- `easy batchAnything`
- `easy forLoopStart`
- `PrimitiveInt`
- `YUAN_TXTConvertAny`
- `YUAN_TXTParagraphSplitter`
- `sch_split_text`
- `sch_split_text`
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `ComfySwitchNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `VAELoader`
- `RandomNoise`
- `sch_split_text`
- `SaveImage`
- `YUAN_TXTJsonExtractor`
- `SaveImage`
- `SaveImage`
- `CR Text`
- `JjkText`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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
- `Note`

**识别到的模式**：text_to_image

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

覆盖率 **88%**（81/92）

**有卡**：`EmptyLatentImage`、`PrimitiveBoolean`、`CFGGuider`、`SamplerCustomAdvanced`、`YUAN_TXTParagraphSplitter`、`YUAN_TXTJsonExtractor`、`RegexExtract`、`CLIPTextEncode`、`VAEDecode`、`easy forLoopEnd`、`easy batchAnything`、`easy forLoopStart`、`YUAN_TXTConvertAny`、`sch_split_text`、`BasicScheduler`、`CLIPLoader`、`UNETLoader`、`KSamplerSelect`、`VAELoader`、`RandomNoise`、`SaveImage`、`CR Text`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
