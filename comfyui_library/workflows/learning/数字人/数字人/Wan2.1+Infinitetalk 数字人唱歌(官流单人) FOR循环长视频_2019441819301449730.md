---
key: 数字人/数字人/Wan2.1+Infinitetalk 数字人唱歌(官流单人) FOR循环长视频_2019441819301449730.json
name: Wan2.1+Infinitetalk 数字人唱歌(官流单人) FOR循环长视频_2019441819301449730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.1+Infinitetalk 数字人唱歌(官流单人) FOR循环长视频_2019441819301449730.json
hash: 33d4a178dfbdb372
coverage: 0.466667
learned_at: 2026-10-26 01:57:47
nodes: [AudioEncoderLoader, MarkdownNote, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, KSamplerSelect, RandomNoise, CFGGuider, SetNode, SetNode, SetNode, SetNode, BasicScheduler, WanInfiniteTalkToVideo, INTConstant, INTConstant, GetNode, SamplerCustomAdvanced, GetNode, LoraLoaderModelOnly, ModelPatchLoader, VAELoader, UNETLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, Note, GetNode, GetNode, FloatConstant, SetNode, SetNode, INTConstant, WanInfiniteTalkToVideo, GetNode, ImageBatch, ImageFromBatch, RandomNoise, SamplerCustomAdvanced, easy forLoopStart, SetNode, AudioEncoderEncode, GetNode, SetNode, LoadImage, AudioCrop, SetNode, LoadAudio, MathExpression|pysssss, Note, Note, easy forLoopEnd, GetNode, VHS_VideoCombine, CR Prompt Text, VHS_VideoCombine, CLIPTextEncode, SetNode, CLIPLoader, VAEDecode, VAEDecode, GetNode, CFGGuider, BasicScheduler, KSamplerSelect, CLIPTextEncode, AudioSeparation, MathExpression|pysssss, Display Any (rgthree), SetNode, Note, INTConstant]
patterns: []
missing: []
---

# 数字人/数字人/Wan2.1+Infinitetalk 数字人唱歌(官流单人) FOR循环长视频_2019441819301449730.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.1+Infinitetalk 数字人唱歌(官流单人) FOR循环长视频_2019441819301449730.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（90 个）：
- `AudioEncoderLoader`
- `MarkdownNote`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `BasicScheduler`
- `WanInfiniteTalkToVideo`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `ModelPatchLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `GetNode`
- `GetNode`
- `FloatConstant`
- `SetNode`
- `SetNode`
- `INTConstant`
- `WanInfiniteTalkToVideo`
- `GetNode`
- `ImageBatch`
- `ImageFromBatch`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `easy forLoopStart`
- `SetNode`
- `AudioEncoderEncode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `AudioCrop`
- `SetNode`
- `LoadAudio`
- `MathExpression|pysssss`
- `Note`
- `Note`
- `easy forLoopEnd`
- `GetNode`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `SetNode`
- `CLIPLoader`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `CFGGuider`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `AudioSeparation`
- `MathExpression|pysssss`
- `Display Any (rgthree)`
- `SetNode`
- `Note`
- `INTConstant`

## 知识

覆盖率 **47%**（42/90）

**有卡**：`AudioEncoderLoader`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`BasicScheduler`、`WanInfiniteTalkToVideo`、`INTConstant`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`ModelPatchLoader`、`VAELoader`、`UNETLoader`、`FloatConstant`、`ImageBatch`、`ImageFromBatch`、`easy forLoopStart`、`AudioEncoderEncode`、`LoadImage`、`AudioCrop`、`LoadAudio`、`MathExpression|pysssss`、`easy forLoopEnd`、`VHS_VideoCombine`、`CR Prompt Text`、`CLIPTextEncode`、`CLIPLoader`、`VAEDecode`、`AudioSeparation`、`Display Any (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider
