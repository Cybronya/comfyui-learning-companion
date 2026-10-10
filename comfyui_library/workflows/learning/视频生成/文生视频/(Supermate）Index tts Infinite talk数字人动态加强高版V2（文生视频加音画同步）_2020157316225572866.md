---
key: 视频生成/文生视频/(Supermate）Index tts Infinite talk数字人动态加强高版V2（文生视频加音画同步）_2020157316225572866.json
name: (Supermate）Index tts Infinite talk数字人动态加强高版V2（文生视频加音画同步）_2020157316225572866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/(Supermate）Index tts Infinite talk数字人动态加强高版V2（文生视频加音画同步）_2020157316225572866.json
hash: 95e01b5429c90aaa
coverage: 0.642857
learned_at: 2026-10-11 03:16:44
nodes: [DownloadAndLoadWav2VecModel, JWInteger, WanVideoImageToVideoMultiTalk, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoVAELoader, WanVideoModelLoader, MarkdownNote, Note, MultiTalkModelLoader, WanVideoLoraSelect, JWFloat, PreviewAny, AudioSeparation, Note, WanVideoDecode, WanVideoSampler, KSamplerAdvanced, VAELoader, CLIPLoader, UNETLoader, LoadWanVideoT5TextEncoder, LoadImage, Note, VAEDecode, AudioCrop, easy indexTTSGenerateSimple, MemoryCleaner, Reroute, MemoryCleaner, WanVideoTextEncode, Note, WanVideoLoraSelect, WanVideoBlockSwap, MultiTalkWav2VecEmbeds, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Note, Note, JWInteger, JWInteger, easy downloadIndexTTSAndLoadModel, Note, Note, Note, PreviewImage, VHS_VideoCombine, CR Text, CR Prompt Text, SaveAudio, Label (rgthree), LoadAudio, CR Text]
patterns: []
missing: [CR Text, CR Text, Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, easy downloadIndexTTSAndLoadModel, easy indexTTSGenerateSimple, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 10, "denoise": "simple", "height": 720, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed", "width": 1280}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy downloadIndexTTSAndLoadModel` 知识库中没有该节点类型的任何知识, 次要节点 `easy indexTTSGenerateSimple` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/(Supermate）Index tts Infinite talk数字人动态加强高版V2（文生视频加音画同步）_2020157316225572866.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/(Supermate）Index tts Infinite talk数字人动态加强高版V2（文生视频加音画同步）_2020157316225572866.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `DownloadAndLoadWav2VecModel`
- `JWInteger`
- `WanVideoImageToVideoMultiTalk`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `MarkdownNote`
- `Note`
- `MultiTalkModelLoader`
- `WanVideoLoraSelect`
- `JWFloat`
- `PreviewAny`
- `AudioSeparation`
- `Note`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadWanVideoT5TextEncoder`
- `LoadImage`
- `Note`
- `VAEDecode` ★核心
- `AudioCrop`
- `easy indexTTSGenerateSimple`
- `MemoryCleaner`
- `Reroute`
- `MemoryCleaner`
- `WanVideoTextEncode`
- `Note`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `MultiTalkWav2VecEmbeds`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `Note`
- `Note`
- `JWInteger`
- `JWInteger`
- `easy downloadIndexTTSAndLoadModel`
- `Note`
- `Note`
- `Note`
- `PreviewImage`
- `VHS_VideoCombine`
- `CR Text`
- `CR Prompt Text`
- `SaveAudio`
- `Label (rgthree)`
- `LoadAudio`
- `CR Text`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`

## 知识

覆盖率 **64%**（36/56）

**有卡**：`DownloadAndLoadWav2VecModel`、`JWInteger`、`WanVideoImageToVideoMultiTalk`、`GetImageSizeAndCount`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`WanVideoLoraSelect`、`JWFloat`、`AudioSeparation`、`WanVideoDecode`、`WanVideoSampler`、`KSamplerAdvanced`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`VAEDecode`、`AudioCrop`、`MemoryCleaner`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`MultiTalkWav2VecEmbeds`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyLatentImage`、`VHS_VideoCombine`、`SaveAudio`、`LoadAudio`

**缺卡**（7）：`CR Text`、`CR Text`、`Label (rgthree)`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy downloadIndexTTSAndLoadModel`、`easy indexTTSGenerateSimple`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage、UNETLoader

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy downloadIndexTTSAndLoadModel` 知识库中没有该节点类型的任何知识
- 次要节点 `easy indexTTSGenerateSimple` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
