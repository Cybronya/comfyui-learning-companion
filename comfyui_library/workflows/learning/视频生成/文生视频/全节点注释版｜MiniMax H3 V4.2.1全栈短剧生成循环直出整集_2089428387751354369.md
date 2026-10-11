---
key: 视频生成/文生视频/全节点注释版｜MiniMax H3 V4.2.1全栈短剧生成循环直出整集_2089428387751354369.json
name: 全节点注释版｜MiniMax H3 V4.2.1全栈短剧生成循环直出整集_2089428387751354369
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/全节点注释版｜MiniMax H3 V4.2.1全栈短剧生成循环直出整集_2089428387751354369.json
hash: 039b40923739bfa3
coverage: 0.832061
learned_at: 2026-10-11 21:19:54
nodes: [YuanTool, RegexExtract, YUAN_TXTListNumber, ComfySwitchNode, YUAN_TXTAppearanceOrder, YUAN_TXTAppearanceOrder, StringReplace, StringReplace, PrimitiveStringMultiline, StringConcatenate, YUAN_TXTParagraphSplitter, YUAN_TXTParagraphSplitter, YUAN_TXTParagraphSplitter, GetImage, GetImage, ComfySwitchNode, INTConstant, ComfySwitchNode, INTConstant, RegexExtract, ComfySwitchNode, ComfySwitchNode, YUAN_TXTReplace, PrimitiveBoolean, INTConstant, INTConstant, GetImage, YUAN_TXTParagraphSplitter, YUAN_TXTListNumber, RandomNoise, PrimitiveBoolean, ComfySwitchNode, BasicGuider, YUAN_TXTJsonExtractor, RandomNoise, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, YUAN_TXTParagraphSplitter, ShowText|pysssss, BasicGuider, SamplerCustomAdvanced, ComfyMathExpression, KSamplerSelect, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, ModelAttentionBackend, Yuan_H3MotionContext, PrimitiveStringMultiline, BasicScheduler, BasicScheduler, UNETLoader, VAELoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, Yuan_RTXVideoUpscaleH3, PreviewImage, Yuan_H3MotionContextTrim, Yuan_H3MotionContextLoadLatent, YUAN_TXTListNumber, If ANY execute A else B, EmptyAudio, AudioConcat, easy forLoopEnd, VHS_VideoCombine, easy batchAnything, easy isNone, easy forLoopStart, SimpleMath+, LoadImage, LoadImage, Yuan_MiniMaxH3Video, YuanMultiImage, PrimitiveFloat, KSamplerSelect, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: [If ANY execute A else B, SimpleMath+, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy isNone]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `If ANY execute A else B` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/全节点注释版｜MiniMax H3 V4.2.1全栈短剧生成循环直出整集_2089428387751354369.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/全节点注释版｜MiniMax H3 V4.2.1全栈短剧生成循环直出整集_2089428387751354369.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（131 个）：
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
- `LoadImage`
- `LoadImage`
- `Yuan_MiniMaxH3Video`
- `YuanMultiImage`
- `PrimitiveFloat`
- `KSamplerSelect` ★核心
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `孤海注释`
- `孤海注释`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（109/131）

**有卡**：`YuanTool`、`RegexExtract`、`YUAN_TXTListNumber`、`YUAN_TXTAppearanceOrder`、`StringReplace`、`StringConcatenate`、`YUAN_TXTParagraphSplitter`、`GetImage`、`INTConstant`、`YUAN_TXTReplace`、`PrimitiveBoolean`、`RandomNoise`、`BasicGuider`、`YUAN_TXTJsonExtractor`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`KSamplerSelect`、`VAEDecode`、`VAEDecodeAudio`、`ModelAttentionBackend`、`Yuan_H3MotionContext`、`BasicScheduler`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`Yuan_RTXVideoUpscaleH3`、`Yuan_H3MotionContextTrim`、`Yuan_H3MotionContextLoadLatent`、`EmptyAudio`、`AudioConcat`、`VHS_VideoCombine`、`LoadImage`、`Yuan_MiniMaxH3Video`、`YuanMultiImage`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**缺卡**（6）：`If ANY execute A else B`、`SimpleMath+`、`easy batchAnything`、`easy forLoopEnd`、`easy forLoopStart`、`easy isNone`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `If ANY execute A else B` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
