---
key: 视频生成/文生视频/MiniMax-H3全栈式短剧V4.2.1｜循环直出一集全节点注释修复版_2089388164245975042.json
name: MiniMax-H3全栈式短剧V4.2.1｜循环直出一集全节点注释修复版_2089388164245975042
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax-H3全栈式短剧V4.2.1｜循环直出一集全节点注释修复版_2089388164245975042.json
hash: b5763dc341fcedda
coverage: 0.851485
learned_at: 2026-10-15 22:46:23
nodes: [YuanTool, RegexExtract, YUAN_TXTListNumber, ComfySwitchNode, YUAN_TXTAppearanceOrder, YUAN_TXTAppearanceOrder, StringReplace, StringReplace, PrimitiveStringMultiline, StringConcatenate, YUAN_TXTParagraphSplitter, YUAN_TXTParagraphSplitter, YUAN_TXTParagraphSplitter, GetImage, GetImage, ComfySwitchNode, INTConstant, ComfySwitchNode, INTConstant, RegexExtract, ComfySwitchNode, ComfySwitchNode, YUAN_TXTReplace, PrimitiveBoolean, INTConstant, INTConstant, GetImage, YUAN_TXTParagraphSplitter, YUAN_TXTListNumber, RandomNoise, PrimitiveBoolean, ComfySwitchNode, BasicGuider, YUAN_TXTJsonExtractor, RandomNoise, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, YUAN_TXTParagraphSplitter, ShowText|pysssss, BasicGuider, SamplerCustomAdvanced, ComfyMathExpression, KSamplerSelect, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, ModelAttentionBackend, Yuan_H3MotionContext, PrimitiveStringMultiline, BasicScheduler, BasicScheduler, UNETLoader, VAELoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, Yuan_RTXVideoUpscaleH3, PreviewImage, Yuan_H3MotionContextTrim, Yuan_H3MotionContextLoadLatent, YUAN_TXTListNumber, If ANY execute A else B, EmptyAudio, AudioConcat, easy forLoopEnd, VHS_VideoCombine, easy batchAnything, easy isNone, easy forLoopStart, SimpleMath+, Yuan_MiniMaxH3Video, YuanMultiImage, PrimitiveFloat, KSamplerSelect, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MiniMax-H3全栈式短剧V4.2.1｜循环直出一集全节点注释修复版_2089388164245975042.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax-H3全栈式短剧V4.2.1｜循环直出一集全节点注释修复版_2089388164245975042.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（101 个）：
- `YuanTool`
- `RegexExtract`
- `YUAN_TXTListNumber`
- `ComfySwitchNode`
- `YUAN_TXTAppearanceOrder`
- `YUAN_TXTAppearanceOrder`
- `StringReplace`
- `StringReplace`
- `PrimitiveStringMultiline`
- `StringConcatenate`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTParagraphSplitter`
- `GetImage`
- `GetImage`
- `ComfySwitchNode`
- `INTConstant`
- `ComfySwitchNode`
- `INTConstant`
- `RegexExtract`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `YUAN_TXTReplace`
- `PrimitiveBoolean`
- `INTConstant`
- `INTConstant`
- `GetImage`
- `YUAN_TXTParagraphSplitter`
- `YUAN_TXTListNumber`
- `RandomNoise`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `BasicGuider`
- `YUAN_TXTJsonExtractor`
- `RandomNoise`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `YUAN_TXTParagraphSplitter`
- `ShowText|pysssss`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `ModelAttentionBackend`
- `Yuan_H3MotionContext`
- `PrimitiveStringMultiline`
- `BasicScheduler`
- `BasicScheduler`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `Yuan_RTXVideoUpscaleH3`
- `PreviewImage`
- `Yuan_H3MotionContextTrim`
- `Yuan_H3MotionContextLoadLatent`
- `YUAN_TXTListNumber`
- `If ANY execute A else B`
- `EmptyAudio`
- `AudioConcat`
- `easy forLoopEnd`
- `VHS_VideoCombine`
- `easy batchAnything`
- `easy isNone`
- `easy forLoopStart`
- `SimpleMath+`
- `Yuan_MiniMaxH3Video`
- `YuanMultiImage`
- `PrimitiveFloat`
- `KSamplerSelect` ★核心
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

覆盖率 **85%**（86/101）

**有卡**：`YuanTool`、`RegexExtract`、`YUAN_TXTListNumber`、`YUAN_TXTAppearanceOrder`、`StringReplace`、`StringConcatenate`、`YUAN_TXTParagraphSplitter`、`GetImage`、`INTConstant`、`YUAN_TXTReplace`、`PrimitiveBoolean`、`RandomNoise`、`BasicGuider`、`YUAN_TXTJsonExtractor`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`KSamplerSelect`、`VAEDecode`、`VAEDecodeAudio`、`ModelAttentionBackend`、`Yuan_H3MotionContext`、`BasicScheduler`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`Yuan_RTXVideoUpscaleH3`、`Yuan_H3MotionContextTrim`、`Yuan_H3MotionContextLoadLatent`、`If ANY execute A else B`、`EmptyAudio`、`AudioConcat`、`easy forLoopEnd`、`VHS_VideoCombine`、`easy batchAnything`、`easy isNone`、`easy forLoopStart`、`SimpleMath+`、`Yuan_MiniMaxH3Video`、`YuanMultiImage`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
