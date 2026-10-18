---
key: 视频生成/图生视频/Qwen雄奶96生日风Lora系列之【lightx2vWan2.2首尾帧输出10秒视频】_1987677949203779585.json
name: Qwen雄奶96生日风Lora系列之【lightx2vWan2.2首尾帧输出10秒视频】_1987677949203779585.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen雄奶96生日风Lora系列之【lightx2vWan2.2首尾帧输出10秒视频】_1987677949203779585.json
hash: 67332c749e13884c
coverage: 0.6
learned_at: 2026-10-15 22:32:59
nodes: [SetNode, SetNode, Text Concatenate, SetNode, SetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, GetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, SetNode, easy showAnything, LayerUtility: ImageMaskScaleAs, WanVideoVAELoader, SetNode, WanVideoEncodeLatentBatch, WanVideoBlockSwap, SetNode, WanVideoModelLoader, WanVideoModelLoader, SetNode, GetNode, SetNode, WanVideoSigmaToStep, INTConstant, CreateCFGScheduleFloatList, GetNode, WanVideoScheduler, WanVideoScheduler, SimpleMath+, Int, GetNode, easy showAnything, ImageStitch, GetNode, GetNode, RH_Captioner, WanVideoSampler, GetNode, WanVideoImageToVideoEncode, GetNode, VHS_VideoCombine, ImageUpscaleWithModel, UpscaleModelLoader, RH_Translator, WanVideoSampler, GetNode, LayerUtility: PurgeVRAM V2, NormalizeAudioLoudness, Int, SetNode, MathExpression|pysssss, GetNode, GetNode, WanVideoDecode, HunyuanVideoFoley, CR Prompt Text, LayerUtility: ImageMaskScaleAs, WanVideoContextOptions, EmptyLatentImage, KSampler, GetImageSizeAndCount, TextEncodeQwenImageEditPlus, GetNode, GetNode, PreviewImage, VAEDecode, Int, LoadImage, LoadImage, WanVideoTextEncode, TextEncodeQwenImageEditPlus, GetNode, GetNode, GetNode, SetNode, LoadWanVideoT5TextEncoder, CheckpointLoaderSimple, LoraLoaderModelOnly, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, StringToFloatList, Text Multiline, RH_Captioner, RH_Captioner, LoadImage, Float]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-SFW-v5.safetensors", "denoise": 1, "height": 1248, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 1063895449308307, "steps": 4, "width": 832}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen雄奶96生日风Lora系列之【lightx2vWan2.2首尾帧输出10秒视频】_1987677949203779585.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1987677949203779585.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（95 个）：
- `SetNode`
- `SetNode`
- `Text Concatenate`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `LayerUtility: ImageMaskScaleAs`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoEncodeLatentBatch`
- `WanVideoBlockSwap`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `WanVideoSigmaToStep`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `WanVideoScheduler`
- `WanVideoScheduler`
- `SimpleMath+`
- `Int`
- `GetNode`
- `easy showAnything`
- `ImageStitch`
- `GetNode`
- `GetNode`
- `RH_Captioner`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `VHS_VideoCombine`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `RH_Translator`
- `WanVideoSampler` ★核心
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `NormalizeAudioLoudness`
- `Int`
- `SetNode`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `HunyuanVideoFoley`
- `CR Prompt Text`
- `LayerUtility: ImageMaskScaleAs`
- `WanVideoContextOptions`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `GetImageSizeAndCount`
- `TextEncodeQwenImageEditPlus`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `VAEDecode` ★核心
- `Int`
- `LoadImage`
- `LoadImage`
- `WanVideoTextEncode`
- `TextEncodeQwenImageEditPlus`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `StringToFloatList`
- `Text Multiline`
- `RH_Captioner`
- `RH_Captioner`
- `LoadImage`
- `Float`

## 关键参数

- `width` = `832`
- `height` = `1248`
- `batch_size` = `1`
- `seed` = `1063895449308307`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-SFW-v5.safetensors`

## 知识

覆盖率 **60%**（57/95）

**有卡**：`Text Concatenate`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageMaskScaleAs`、`WanVideoVAELoader`、`WanVideoEncodeLatentBatch`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSigmaToStep`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoScheduler`、`SimpleMath+`、`Int`、`ImageStitch`、`RH_Captioner`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`RH_Translator`、`LayerUtility: PurgeVRAM V2`、`NormalizeAudioLoudness`、`MathExpression|pysssss`、`WanVideoDecode`、`HunyuanVideoFoley`、`CR Prompt Text`、`WanVideoContextOptions`、`EmptyLatentImage`、`KSampler`、`GetImageSizeAndCount`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`LoadImage`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`WanVideoLoraSelect`、`StringToFloatList`、`Text Multiline`、`Float`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、EmptyLatentImage、LoadImage、WanVideoSampler、CreateCFGScheduleFloatList

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
