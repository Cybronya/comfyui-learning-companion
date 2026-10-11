---
key: 视频生成/文生视频/biaozhun6 accel jellyfish文生视频图生视频加速_2088205047762083842.json
name: biaozhun6 accel jellyfish文生视频图生视频加速_2088205047762083842
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/biaozhun6 accel jellyfish文生视频图生视频加速_2088205047762083842.json
hash: 0c2c3dcbdac611cb
coverage: 0.872093
learned_at: 2026-10-11 20:53:49
nodes: [VAEDecodeAudio, KSamplerSelect, BasicScheduler, BasicGuider, RandomNoise, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, DF_Int_to_Float, CreateVideo, LoadImage, UNETLoader, VAEDecode, PrimitiveFloat, ShowAnything|Mie, ShowAnything|Mie, LoadImage, LoadImage, SaveVideo, ImpactSwitch, EasyCache, ResolutionSelector, ComfyMathExpression, LoadAudio, LoadAudio, LoadAudio, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SamplerCustomAdvanced, PathchSageAttentionKJ, CLIPLoader, VAELoader, VAELoader, PrimitiveFloat, MiniMaxH3ReferenceToVideo, GetVideoComponents, GetVideoComponents, GetVideoComponents, LoadVideo, LoadVideo, LoadVideo, ImpactSwitch, CR Prompt Text, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: [ShowAnything|Mie, ShowAnything|Mie, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/biaozhun6 accel jellyfish文生视频图生视频加速_2088205047762083842.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/biaozhun6 accel jellyfish文生视频图生视频加速_2088205047762083842.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（86 个）：
- `VAEDecodeAudio` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `RandomNoise`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `CreateVideo`
- `LoadImage`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `PrimitiveFloat`
- `ShowAnything|Mie`
- `ShowAnything|Mie`
- `LoadImage`
- `LoadImage`
- `SaveVideo`
- `ImpactSwitch`
- `EasyCache`
- `ResolutionSelector`
- `ComfyMathExpression`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `PrimitiveFloat`
- `MiniMaxH3ReferenceToVideo`
- `GetVideoComponents`
- `GetVideoComponents`
- `GetVideoComponents`
- `LoadVideo`
- `LoadVideo`
- `LoadVideo`
- `ImpactSwitch`
- `CR Prompt Text`
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

覆盖率 **87%**（75/86）

**有卡**：`VAEDecodeAudio`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`RandomNoise`、`DF_Int_to_Float`、`CreateVideo`、`LoadImage`、`UNETLoader`、`VAEDecode`、`SaveVideo`、`EasyCache`、`ResolutionSelector`、`ComfyMathExpression`、`LoadAudio`、`SamplerCustomAdvanced`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`MiniMaxH3ReferenceToVideo`、`GetVideoComponents`、`LoadVideo`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**缺卡**（3）：`ShowAnything|Mie`、`ShowAnything|Mie`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
