---
key: 视频生成/文生视频/LTX2.3 15秒图生视频 氛围感长镜头 自动提示词 高清1K 舒缓的节奏，平和的运镜_2053275385588142082.json
name: LTX2.3 15秒图生视频 氛围感长镜头 自动提示词 高清1K 舒缓的节奏，平和的运镜_2053275385588142082
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 15秒图生视频 氛围感长镜头 自动提示词 高清1K 舒缓的节奏，平和的运镜_2053275385588142082.json
hash: 18aa80096e934e84
coverage: 0.714286
learned_at: 2026-10-11 19:49:36
nodes: [LTXVAudioVAELoader, LTXAVTextEncoderLoader, EmptyImage, ImageScaleBy, KSamplerSelect, LTXVConcatAVLatent, KSampler, GetImageSize, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConditioning, VAEDecode, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVLatentUpsampler, RandomNoise, LTXVScheduler, easy int, easy float, PrimitiveInt, MathExpression|pysssss, CLIPTextEncode, CFGGuider, LoraLoaderModelOnly, CheckpointLoaderSimple, RH_LLMAPI_Pro_Node, Int, LTXVImgToVideoInplace, GetImageSize, CLIPTextEncode, CR Prompt Text, easy showAnything, CR Prompt Text, MathExpression|pysssss, LatentUpscaleModelLoader, easy float, CreateVideo, LoadImage, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, Note, Note, easy int, SaveVideo]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, MathExpression|pysssss, easy float, easy float, easy int, easy int, CR Prompt Text, CR Prompt Text, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 121196318456263, "steps": 4, "width": 97}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX2.3 15秒图生视频 氛围感长镜头 自动提示词 高清1K 舒缓的节奏，平和的运镜_2053275385588142082.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 15秒图生视频 氛围感长镜头 自动提示词 高清1K 舒缓的节奏，平和的运镜_2053275385588142082.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `EmptyImage`
- `ImageScaleBy`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `KSampler` ★核心
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVConditioning`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `LTXVScheduler`
- `easy int`
- `easy float`
- `PrimitiveInt`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `RH_LLMAPI_Pro_Node`
- `Int`
- `LTXVImgToVideoInplace`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `easy showAnything`
- `CR Prompt Text`
- `MathExpression|pysssss`
- `LatentUpscaleModelLoader`
- `easy float`
- `CreateVideo`
- `LoadImage`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `Note`
- `easy int`
- `SaveVideo`

## 关键参数

- `seed` = `121196318456263`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **71%**（35/49）

**有卡**：`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`EmptyImage`、`ImageScaleBy`、`KSamplerSelect`、`LTXVConcatAVLatent`、`KSampler`、`GetImageSize`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVConditioning`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`RandomNoise`、`LTXVScheduler`、`CLIPTextEncode`、`CFGGuider`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`RH_LLMAPI_Pro_Node`、`Int`、`LatentUpscaleModelLoader`、`CreateVideo`、`LoadImage`、`SaveVideo`

**缺卡**（10）：`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`MathExpression|pysssss`、`easy float`、`easy float`、`easy int`、`easy int`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
