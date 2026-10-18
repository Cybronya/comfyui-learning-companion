---
key: 视频生成/图生视频/MiniMax H3全栈式短剧生成V9.2 一站式短剧制作_2098294284297527297.json
name: MiniMax H3全栈式短剧生成V9.2 一站式短剧制作_2098294284297527297
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3全栈式短剧生成V9.2 一站式短剧制作_2098294284297527297.json
hash: 550541fd0770464e
coverage: 0.496774
learned_at: 2026-10-17 01:44:34
nodes: [GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetImage, GetImage, GetNode, GetImage, ResolutionSelector, YuanTool, SetNode, SetNode, GetNode, SetNode, ResolutionSelector, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, PrimitiveFloat, SetNode, SetNode, StringConcatenate, GetNode, PreviewAudio, ComfyMathExpression, GetNode, GetNode, GetNode, MiniMaxChunkFeedForward, SamplerCustomAdvanced, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, YuanAudioList, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, YUAN_TXTJsonSwitch, SetNode, YUAN_TXTShotDurations, PrimitiveStringMultiline, ComfyMathExpression, SamplerCustomAdvanced, RandomNoise, BasicGuider, GetNode, GetNode, SetNode, RandomNoise, BasicGuider, KSamplerSelect, GetNode, ManualSigmas, ManualSigmas, KSamplerSelect, ComfyMathExpression, SetNode, GetNode, ModelAttentionBackend, BasicScheduler, SplitSigmas, YuanAudioSplit, PrimitiveStringMultiline, YUAN_TXTPreviewContent, MiniMaxLowVRAMAttention, SetNode, SetNode, GetNode, PrimitiveBoolean, PrimitiveBoolean, PrimitiveInt, YuanAudioLoad, GetNode, YUAN_TXTJsonExtractor, Lora Loader Stack (rgthree), VAELoader, CLIPLoader, VAELoader, GetNode, SetNode, VAEDecodeAudio, GetNode, GetNode, ComfySwitchNode, GetNode, GetNode, GetNode, GetNode, Yuan_VideoUI, GetNode, GetNode, Yuan_H3Upscale3D, ImageFromBatch, GetNode, Yuan_MiniMaxH3Video, MiniMaxH3AddGuide, ComfySwitchNode, GetNode, GetNode, MiniMaxH3AddGuide, ComfySwitchNode, UNETLoader, StringReplace, YuanMultiImage, VAEDecode, SetNode, VHS_VideoCombine, PreviewImage, PrimitiveNode, ComfySwitchNode, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax H3全栈式短剧生成V9.2 一站式短剧制作_2098294284297527297.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3全栈式短剧生成V9.2 一站式短剧制作_2098294284297527297.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（155 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImage`
- `GetImage`
- `GetNode`
- `GetImage`
- `ResolutionSelector`
- `YuanTool`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `StringConcatenate`
- `GetNode`
- `PreviewAudio`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `MiniMaxChunkFeedForward`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `YuanAudioList`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `YUAN_TXTJsonSwitch`
- `SetNode`
- `YUAN_TXTShotDurations`
- `PrimitiveStringMultiline`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `BasicGuider`
- `GetNode`
- `GetNode`
- `SetNode`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `GetNode`
- `ManualSigmas`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `ModelAttentionBackend`
- `BasicScheduler`
- `SplitSigmas`
- `YuanAudioSplit`
- `PrimitiveStringMultiline`
- `YUAN_TXTPreviewContent`
- `MiniMaxLowVRAMAttention`
- `SetNode`
- `SetNode`
- `GetNode`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `YuanAudioLoad`
- `GetNode`
- `YUAN_TXTJsonExtractor`
- `Lora Loader Stack (rgthree)`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `SetNode`
- `VAEDecodeAudio` ★核心
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Yuan_VideoUI`
- `GetNode`
- `GetNode`
- `Yuan_H3Upscale3D`
- `ImageFromBatch`
- `GetNode`
- `Yuan_MiniMaxH3Video`
- `MiniMaxH3AddGuide`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `MiniMaxH3AddGuide`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `StringReplace`
- `YuanMultiImage`
- `VAEDecode` ★核心
- `SetNode`
- `VHS_VideoCombine`
- `PreviewImage`
- `PrimitiveNode`
- `ComfySwitchNode`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `Note`
- `SaveImage`

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

覆盖率 **50%**（77/155）

**有卡**：`GetImage`、`ResolutionSelector`、`YuanTool`、`StringConcatenate`、`PreviewAudio`、`ComfyMathExpression`、`MiniMaxChunkFeedForward`、`SamplerCustomAdvanced`、`YuanAudioList`、`YUAN_TXTJsonSwitch`、`YUAN_TXTShotDurations`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`ManualSigmas`、`ModelAttentionBackend`、`BasicScheduler`、`SplitSigmas`、`YuanAudioSplit`、`YUAN_TXTPreviewContent`、`MiniMaxLowVRAMAttention`、`PrimitiveBoolean`、`YuanAudioLoad`、`YUAN_TXTJsonExtractor`、`Lora Loader Stack (rgthree)`、`VAELoader`、`CLIPLoader`、`VAEDecodeAudio`、`Yuan_VideoUI`、`Yuan_H3Upscale3D`、`ImageFromBatch`、`Yuan_MiniMaxH3Video`、`MiniMaxH3AddGuide`、`UNETLoader`、`StringReplace`、`YuanMultiImage`、`VAEDecode`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
