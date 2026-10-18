---
key: 视频生成/图生视频/MinimaxH3人物替换character swap，视频生视频精准换人_2110516163112423425.json
name: MinimaxH3人物替换character swap，视频生视频精准换人_2110516163112423425
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MinimaxH3人物替换character swap，视频生视频精准换人_2110516163112423425.json
hash: 9d0cefbad3c371fb
coverage: 0.809524
learned_at: 2026-10-18 00:23:41
nodes: [VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, UNETLoader, CLIPLoader, RandomNoise, ComfyMathExpression, MiniMaxH3ReferenceToVideo, PrimitiveInt, PrimitiveBoolean, PrimitiveInt, ComfySwitchNode, ComfySwitchNode, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveFloat, ResolutionSelector, LoadVideo, GetVideoComponents, PreviewImage, QwenH3PromptLocal, AnySwitch, PreviewAny, PrimitiveStringMultiline, CreateVideo, LoadImage, SaveVideo, Fast Bypasser (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MinimaxH3人物替换character swap，视频生视频精准换人_2110516163112423425.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MinimaxH3人物替换character swap，视频生视频精准换人_2110516163112423425.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（63 个）：
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `ComfyMathExpression`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `ResolutionSelector`
- `LoadVideo`
- `GetVideoComponents`
- `PreviewImage`
- `QwenH3PromptLocal`
- `AnySwitch`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `CreateVideo`
- `LoadImage`
- `SaveVideo`
- `Fast Bypasser (rgthree)`
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
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
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

覆盖率 **81%**（51/63）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`ResolutionSelector`、`LoadVideo`、`GetVideoComponents`、`QwenH3PromptLocal`、`AnySwitch`、`CreateVideo`、`LoadImage`、`SaveVideo`、`Fast Bypasser (rgthree)`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
