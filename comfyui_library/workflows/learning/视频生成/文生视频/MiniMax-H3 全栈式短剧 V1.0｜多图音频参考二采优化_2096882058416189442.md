---
key: 视频生成/文生视频/MiniMax-H3 全栈式短剧 V1.0｜多图音频参考二采优化_2096882058416189442.json
name: MiniMax-H3 全栈式短剧 V1.0｜多图音频参考二采优化_2096882058416189442
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax-H3 全栈式短剧 V1.0｜多图音频参考二采优化_2096882058416189442.json
hash: 8c815b613d97fd15
coverage: 0.521739
learned_at: 2026-10-11 21:41:46
nodes: [GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, CLIPLoader, YUAN_TXTJsonExtractor, GetNode, GetNode, GetImage, GetImage, GetNode, GetImage, ResolutionSelector, GetNode, YuanTool, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, YUAN_TXTParagraphSplitter, GetNode, GetNode, PrimitiveInt, SetNode, TextGenerate, StringConcatenate, SetNode, ResolutionSelector, SetNode, SetNode, SetNode, GetNode, PreviewImage, YUAN_TXTShotReplace, ShowText|pysssss, GetNode, PrimitiveNode, YuanAudioList, PrimitiveStringMultiline, ImageScale, LoadImage, GetNode, Reroute, Reroute, GetNode, GetNode, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, SetNode, BasicGuider, SetNode, SetNode, SetNode, GetNode, LTXVConcatAVLatent, GetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, RandomNoise, KSamplerSelect, UNETLoader, SetNode, GetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, BasicScheduler, MinimaxH3LatentUpscaler3D, VAEDecode, VAEDecodeAudio, GetNode, GetNode, ComfyMathExpression, PrimitiveStringMultiline, SetNode, easy float, SetNode, MiniMaxH3ReferenceToVideo, PrimitiveFloat, ComfyMathExpression, SetNode, ResolutionSelector, SetNode, SetNode, YuanAudioSplit, PrimitiveFloat, YuanMultiImage, SplitSigmas, SetNode, VAELoader, SetNode, SetNode, SetNode, VAELoader, SetNode, CLIPLoader, SetNode, LoraLoaderModelOnly, SetNode, SetNode, SetNode, VHS_VideoCombine, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [easy float]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy float` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MiniMax-H3 全栈式短剧 V1.0｜多图音频参考二采优化_2096882058416189442.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax-H3 全栈式短剧 V1.0｜多图音频参考二采优化_2096882058416189442.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（161 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPLoader`
- `YUAN_TXTJsonExtractor`
- `GetNode`
- `GetNode`
- `GetImage`
- `GetImage`
- `GetNode`
- `GetImage`
- `ResolutionSelector`
- `GetNode`
- `YuanTool`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `YUAN_TXTParagraphSplitter`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `SetNode`
- `TextGenerate`
- `StringConcatenate`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `YUAN_TXTShotReplace`
- `ShowText|pysssss`
- `GetNode`
- `PrimitiveNode`
- `YuanAudioList`
- `PrimitiveStringMultiline`
- `ImageScale`
- `LoadImage`
- `GetNode`
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `BasicGuider`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `MinimaxH3LatentUpscaler3D`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `PrimitiveStringMultiline`
- `SetNode`
- `easy float`
- `SetNode`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `YuanAudioSplit`
- `PrimitiveFloat`
- `YuanMultiImage`
- `SplitSigmas`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
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

覆盖率 **52%**（84/161）

**有卡**：`CLIPLoader`、`YUAN_TXTJsonExtractor`、`GetImage`、`ResolutionSelector`、`YuanTool`、`YUAN_TXTParagraphSplitter`、`TextGenerate`、`StringConcatenate`、`YUAN_TXTShotReplace`、`YuanAudioList`、`ImageScale`、`LoadImage`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicGuider`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`RandomNoise`、`KSamplerSelect`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`BasicScheduler`、`MinimaxH3LatentUpscaler3D`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`YuanAudioSplit`、`YuanMultiImage`、`SplitSigmas`、`VAELoader`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**缺卡**（1）：`easy float`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
