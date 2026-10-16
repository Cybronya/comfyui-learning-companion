---
key: 视频生成/图生视频/MiniMax H3全栈式短剧视频生成V4.2图生视频工作流_2088289186230128641.json
name: MiniMax H3全栈式短剧视频生成V4.2图生视频工作流_2088289186230128641
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3全栈式短剧视频生成V4.2图生视频工作流_2088289186230128641.json
hash: 214701c1bf10a00b
coverage: 0.543624
learned_at: 2026-10-16 21:43:26
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, YuanTool, SetNode, GetNode, RegexExtract, YUAN_TXTListNumber, YUAN_TXTListNumber, ComfySwitchNode, YUAN_TXTAppearanceOrder, YUAN_TXTAppearanceOrder, StringReplace, StringReplace, PrimitiveStringMultiline, StringConcatenate, GetNode, YUAN_TXTParagraphSplitter, YUAN_TXTParagraphSplitter, GetNode, YUAN_TXTParagraphSplitter, GetImage, GetImage, ComfySwitchNode, INTConstant, ComfySwitchNode, GetNode, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, RegexExtract, SetNode, ComfySwitchNode, ComfySwitchNode, SetNode, SetNode, YUAN_TXTReplace, SetNode, PrimitiveBoolean, PrimitiveFloat, INTConstant, INTConstant, GetImage, PrimitiveStringMultiline, GetNode, YUAN_TXTParagraphSplitter, PrimitiveStringMultiline, GetNode, YUAN_TXTListNumber, RandomNoise, SetNode, SetNode, SetNode, SetNode, PrimitiveStringMultiline, SetNode, PrimitiveBoolean, SetNode, ComfySwitchNode, GetNode, GetNode, GetNode, ComfyMathExpression, GetNode, BasicGuider, KSamplerSelect, YUAN_TXTJsonExtractor, SetNode, SetNode, SetNode, RandomNoise, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, SetNode, YUAN_TXTParagraphSplitter, ShowText|pysssss, BasicGuider, GetNode, SamplerCustomAdvanced, VHS_VideoCombine, Yuan_MiniMaxH3Video, GetNode, GetNode, ComfyMathExpression, GetNode, KSamplerSelect, SamplerCustomAdvanced, GetNode, VAEDecode, GetNode, VAEDecodeAudio, SetNode, SetNode, SetNode, ModelAttentionBackend, Yuan_H3MotionContext, GetNode, PrimitiveStringMultiline, YuanMultiImage, BasicScheduler, BasicScheduler, UNETLoader, VAELoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, Yuan_RTXVideoUpscaleH3, PreviewImage, Yuan_H3MotionContextTrim, PrimitiveInt, Yuan_H3MotionContextLoadLatent, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax H3全栈式短剧视频生成V4.2图生视频工作流_2088289186230128641.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3全栈式短剧视频生成V4.2图生视频工作流_2088289186230128641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（149 个）：
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
- `Yuan_MiniMaxH3Video`
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
- `PrimitiveStringMultiline`
- `YuanMultiImage`
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
- `PrimitiveInt`
- `Yuan_H3MotionContextLoadLatent`
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

覆盖率 **54%**（81/149）

**有卡**：`YuanTool`、`RegexExtract`、`YUAN_TXTListNumber`、`YUAN_TXTAppearanceOrder`、`StringReplace`、`StringConcatenate`、`YUAN_TXTParagraphSplitter`、`GetImage`、`INTConstant`、`YUAN_TXTReplace`、`PrimitiveBoolean`、`RandomNoise`、`ComfyMathExpression`、`BasicGuider`、`KSamplerSelect`、`YUAN_TXTJsonExtractor`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`、`SamplerCustomAdvanced`、`VHS_VideoCombine`、`Yuan_MiniMaxH3Video`、`VAEDecode`、`VAEDecodeAudio`、`ModelAttentionBackend`、`Yuan_H3MotionContext`、`YuanMultiImage`、`BasicScheduler`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`Yuan_RTXVideoUpscaleH3`、`Yuan_H3MotionContextTrim`、`Yuan_H3MotionContextLoadLatent`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
