---
key: 图片生成/文生图/ImmersivePoeticAgent_1949502290826272769.json
name: ImmersivePoeticAgent_1949502290826272769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ImmersivePoeticAgent_1949502290826272769.json
hash: cf79ce6865583b48
coverage: 0.596774
learned_at: 2026-10-10 20:58:40
nodes: [Reroute, EmptySD3LatentImage, KSamplerSelect, BasicScheduler, easy cleanGpuUsed, RandomNoise, ModelSamplingFlux, PrimitiveNode, PrimitiveNode, BasicGuider, Text Concatenate, FluxGuidance, easy cleanGpuUsed, easy cleanGpuUsed, Reroute, CLIPTextEncode, ACEStepGen, easy cleanGpuUsed, Reroute, Reroute, TeaCache, MultiLinePromptACES, SamplerCustomAdvanced, easy cleanGpuUsed, LoraLoader, JjkText, CheckpointLoaderSimple, ShowText, GetTextFromJson, GetTextFromJson, GetTextFromJson, ShowText, LoadJsonFromText, ReplaceText, ReplaceText, ShowText, TextCombinerTwo, RH_LLMAPI_NODE, SaveAudio, RH_Captioner, GenerationParameters, CR Overlay Text, LayerFilter: MotionBlur, SaveImage, ETN_CropImage, CR Vignette Filter, VAEDecode, CR Overlay Text, ImageScaleBy, SaveImage, JjkText, JjkText, JjkText, LoadImage, BrightnessNode, Text Concatenate, JjkText, ShowText, ShowText, Reroute, Reroute, Reroute]
patterns: [lora]
missing: [CR Overlay Text, CR Overlay Text, CR Vignette Filter, LayerFilter: MotionBlur, Text Concatenate, Text Concatenate, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed]
parameters: {"checkpoint": "flux1-dev-fp8-with_clip_vae.safetensors", "lora_name": "纪实摄影 F.1_v1.0.safetensors", "strength_clip": 1.0100000000000002, "strength_model": 0.8000000000000002}
discoveries: [次要节点 `CR Overlay Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Overlay Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Vignette Filter` 知识库中没有该节点类型的任何知识, 次要节点 `LayerFilter: MotionBlur` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/ImmersivePoeticAgent_1949502290826272769.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ImmersivePoeticAgent_1949502290826272769.json`

## 结构

**节点**（62 个）：
- `Reroute`
- `EmptySD3LatentImage`
- `KSamplerSelect`
- `BasicScheduler`
- `easy cleanGpuUsed`
- `RandomNoise`
- `ModelSamplingFlux`
- `PrimitiveNode`
- `PrimitiveNode`
- `BasicGuider`
- `Text Concatenate`
- `FluxGuidance`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `Reroute`
- `CLIPTextEncode`
- `ACEStepGen`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `TeaCache`
- `MultiLinePromptACES`
- `SamplerCustomAdvanced`
- `easy cleanGpuUsed`
- `LoraLoader`
- `JjkText`
- `CheckpointLoaderSimple`
- `ShowText`
- `GetTextFromJson`
- `GetTextFromJson`
- `GetTextFromJson`
- `ShowText`
- `LoadJsonFromText`
- `ReplaceText`
- `ReplaceText`
- `ShowText`
- `TextCombinerTwo`
- `RH_LLMAPI_NODE`
- `SaveAudio`
- `RH_Captioner`
- `GenerationParameters`
- `CR Overlay Text`
- `LayerFilter: MotionBlur`
- `SaveImage`
- `ETN_CropImage`
- `CR Vignette Filter`
- `VAEDecode`
- `CR Overlay Text`
- `ImageScaleBy`
- `SaveImage`
- `JjkText`
- `JjkText`
- `JjkText`
- `LoadImage`
- `BrightnessNode`
- `Text Concatenate`
- `JjkText`
- `ShowText`
- `ShowText`
- `Reroute`
- `Reroute`
- `Reroute`

**识别到的模式**：lora

## 关键参数

- `checkpoint` = `flux1-dev-fp8-with_clip_vae.safetensors`
- `lora_name` = `纪实摄影 F.1_v1.0.safetensors`
- `strength_clip` = `1.0100000000000002`
- `strength_model` = `0.8000000000000002`

## 知识

覆盖率 **60%**（37/62）

**有卡**：`Reroute`、`EmptySD3LatentImage`、`KSamplerSelect`、`BasicScheduler`、`easy cleanGpuUsed`、`RandomNoise`、`ModelSamplingFlux`、`PrimitiveNode`、`BasicGuider`、`Text Concatenate`、`FluxGuidance`、`CLIPTextEncode`、`ACEStepGen`、`TeaCache`、`MultiLinePromptACES`、`SamplerCustomAdvanced`、`LoraLoader`、`JjkText`、`CheckpointLoaderSimple`、`ShowText`、`GetTextFromJson`、`LoadJsonFromText`、`ReplaceText`、`TextCombinerTwo`

**缺卡**（11）：`CR Overlay Text`、`CR Overlay Text`、`CR Vignette Filter`、`LayerFilter: MotionBlur`、`Text Concatenate`、`Text Concatenate`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

## 学习发现

- 次要节点 `CR Overlay Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Overlay Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Vignette Filter` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerFilter: MotionBlur` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
