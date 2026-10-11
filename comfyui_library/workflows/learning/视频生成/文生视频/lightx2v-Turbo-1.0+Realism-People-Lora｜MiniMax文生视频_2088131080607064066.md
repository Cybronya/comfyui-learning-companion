---
key: 视频生成/文生视频/lightx2v-Turbo-1.0+Realism-People-Lora｜MiniMax文生视频_2088131080607064066.json
name: lightx2v-Turbo-1.0+Realism-People-Lora｜MiniMax文生视频_2088131080607064066
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/lightx2v-Turbo-1.0+Realism-People-Lora｜MiniMax文生视频_2088131080607064066.json
hash: 9624cb4dafb40a81
coverage: 0.912281
learned_at: 2026-10-11 20:53:49
nodes: [ComfyMathExpression, CLIPLoader, VAELoader, VAELoader, RandomNoise, KSamplerSelect, BasicGuider, SamplerCustomAdvanced, Text Find and Replace, easy showAnything, KSamplerSelect, BasicGuider, RandomNoise, CreateVideo, BasicScheduler, KSamplerSelect, RandomNoise, BasicScheduler, CreateVideo, VAEDecode, SamplerCustomAdvanced, VAEDecode, KSamplerSelect, RandomNoise, SaveVideo, CreateVideo, BasicGuider, BasicScheduler, VAEDecode, VAEDecode, VAEDecodeAudio, SaveVideo, Seed (rgthree), ImageConcatMulti, SamplerCustomAdvanced, SaveVideo, SamplerCustomAdvanced, BasicScheduler, KSamplerSelect, SaveVideo, CreateVideo, BasicScheduler, VAEDecode, VAEDecodeAudio, SamplerCustomAdvanced, RandomNoise, BasicGuider, BasicGuider, KSamplerSelect, VAEDecodeAudio, CreateVideo, VAEDecode, SaveVideo, BasicGuider, SamplerCustomAdvanced, BasicScheduler, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, UNETLoader, LoraLoaderModelOnly, RandomNoise, SaveVideo, ImageConcatMulti, Reroute, ImageConcatMulti, VAEDecodeAudio, VAEDecodeAudio, CreateVideo, VAEDecodeAudio, PreviewAudio, PreviewAudio, PreviewAudio, PrimitiveFloat, RH_LLMAPI_Pro_Node, CR Text, ImageConcatMulti, TextOverlay, TextOverlay, TextOverlay, TextOverlay, TextOverlay, TextOverlay, ResolutionSelector, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: [CR Text, Text Find and Replace, Seed (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Text Find and Replace` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/lightx2v-Turbo-1.0+Realism-People-Lora｜MiniMax文生视频_2088131080607064066.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/lightx2v-Turbo-1.0+Realism-People-Lora｜MiniMax文生视频_2088131080607064066.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（114 个）：
- `ComfyMathExpression`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `Text Find and Replace`
- `easy showAnything`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `CreateVideo`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `BasicScheduler`
- `CreateVideo`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SaveVideo`
- `CreateVideo`
- `BasicGuider`
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SaveVideo`
- `Seed (rgthree)`
- `ImageConcatMulti`
- `SamplerCustomAdvanced` ★核心
- `SaveVideo`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `SaveVideo`
- `CreateVideo`
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `BasicGuider`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `SaveVideo`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3ImageToVideo`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `SaveVideo`
- `ImageConcatMulti`
- `Reroute`
- `ImageConcatMulti`
- `VAEDecodeAudio` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `VAEDecodeAudio` ★核心
- `PreviewAudio`
- `PreviewAudio`
- `PreviewAudio`
- `PrimitiveFloat`
- `RH_LLMAPI_Pro_Node`
- `CR Text`
- `ImageConcatMulti`
- `TextOverlay`
- `TextOverlay`
- `TextOverlay`
- `TextOverlay`
- `TextOverlay`
- `TextOverlay`
- `ResolutionSelector`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
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

覆盖率 **91%**（104/114）

**有卡**：`ComfyMathExpression`、`CLIPLoader`、`VAELoader`、`RandomNoise`、`KSamplerSelect`、`BasicGuider`、`SamplerCustomAdvanced`、`CreateVideo`、`BasicScheduler`、`VAEDecode`、`SaveVideo`、`VAEDecodeAudio`、`ImageConcatMulti`、`LoraLoaderModelOnly`、`MiniMaxH3ImageToVideo`、`UNETLoader`、`PreviewAudio`、`RH_LLMAPI_Pro_Node`、`TextOverlay`、`ResolutionSelector`、`VHS_VideoCombine`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**缺卡**（3）：`CR Text`、`Text Find and Replace`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Find and Replace` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
