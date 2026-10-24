---
key: 图片生成/图生图/多图参考编辑-QWEN2.1_2108860155042557953.json
name: 多图参考编辑-QWEN2.1_2108860155042557953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多图参考编辑-QWEN2.1_2108860155042557953.json
hash: b18dc1aeb1c5d4c6
coverage: 0.781022
learned_at: 2026-10-23 12:45:04
nodes: [Int, Bjornulf_ShowInt, Bjornulf_ShowInt, Int, Bjornulf_ShowInt, Bjornulf_ShowInt, SimpleMath+, math_calculate, SimpleMath+, Int, Bjornulf_ShowInt, Bjornulf_ShowInt, math_calculate, Int, Bjornulf_ShowInt, math_calculate, Bjornulf_ShowInt, math_calculate, math_calculate, SimpleMath+, SimpleMath+, SimpleMath+, math_calculate, math_calculate, math_calculate, Bjornulf_ShowFloat, math_calculate, math_calculate, math_calculate, Bjornulf_ShowFloat, easy showAnything, SimpleMath+, SimpleMath+, SimpleMath+, Bjornulf_ShowFloat, Bjornulf_ShowFloat, easy showAnything, Boolean To Int [Dream], Boolean To Int [Dream], Int, Int, easy showAnything, easy showAnything, easy showAnything, Qwen3VLProcessor, Qwen3VLProcessor, Reroute, easy cleanGpuUsed, Reroute, easy cleanGpuUsed, easy clearCacheAll, llama_cpp_parameters, LayerUtility: PurgeVRAM V2, easy clearCacheAll, LayerUtility: PurgeVRAM V2, JoinStringMulti, PreviewAny, llama_cpp_instruct_adv, easy showAnything, llama_cpp_model_loader, Int, Int, CR Prompt Text, TTP_text_mix, TTP_text_mix, CR Aspect Ratio, UNETLoader, CLIPLoader, Reroute, Reroute, QwenImage21Cache, PrimitiveBoolean, ComfySwitchNode, KSampler, VAELoader, EmptyLatentImage, Bjornulf_ShowInt, Reroute, ImageFromBatch, Qwen3VLProcessor, TTP_text_mix, Qwen3VLProcessor, TTP_text_mix, TTP_text_mix, Reroute, TextEncodeQwenImage21, easy showAnything, Reroute, Reroute, Reroute, YYZPack_YYZ_Image_Blank, PreviewImage, Reroute, ImageBatchMulti, Reroute, Reroute, easy showAnything, Qwen3VLProcessor, Reroute, Reroute, ImageFromBatch, ImageFromBatch, ImageFromBatch, easy int, SaveImage, Reroute, GetImageSize+, ImpactMinMax, PreviewImage, TTP_text_mix, TTP_text_mix, TTP_text_mix, TTP_text_mix, LoadImage, LoadImage, LoadImage, LoadImage, CR Prompt Text, LayerUtility: ImageReel, GetImageSize+, ImpactMinMax, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, VAEDecode, Bjornulf_ShowInt, Reroute, ImageFromBatch, ImageFromBatch, LayerUtility: ImageReelComposit, ImageFromBatch, LayerUtility: ImageReel, SaveImage, easy showAnything, Reroute, ImageFromBatch]
patterns: []
missing: []
parameters: {"batch_size": 4, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1091707692079692, "steps": 25, "width": 1024}
---

# 图片生成/图生图/多图参考编辑-QWEN2.1_2108860155042557953.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多图参考编辑-QWEN2.1_2108860155042557953.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（137 个）：
- `Int`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `Int`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `SimpleMath+`
- `math_calculate`
- `SimpleMath+`
- `Int`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `math_calculate`
- `Int`
- `Bjornulf_ShowInt`
- `math_calculate`
- `Bjornulf_ShowInt`
- `math_calculate`
- `math_calculate`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `math_calculate`
- `math_calculate`
- `math_calculate`
- `Bjornulf_ShowFloat`
- `math_calculate`
- `math_calculate`
- `math_calculate`
- `Bjornulf_ShowFloat`
- `easy showAnything`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `Bjornulf_ShowFloat`
- `Bjornulf_ShowFloat`
- `easy showAnything`
- `Boolean To Int [Dream]`
- `Boolean To Int [Dream]`
- `Int`
- `Int`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `Qwen3VLProcessor`
- `Qwen3VLProcessor`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `llama_cpp_parameters`
- `LayerUtility: PurgeVRAM V2`
- `easy clearCacheAll`
- `LayerUtility: PurgeVRAM V2`
- `JoinStringMulti`
- `PreviewAny`
- `llama_cpp_instruct_adv`
- `easy showAnything`
- `llama_cpp_model_loader`
- `Int`
- `Int`
- `CR Prompt Text`
- `TTP_text_mix`
- `TTP_text_mix`
- `CR Aspect Ratio`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Reroute`
- `Reroute`
- `QwenImage21Cache`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `KSampler` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `Bjornulf_ShowInt`
- `Reroute`
- `ImageFromBatch`
- `Qwen3VLProcessor`
- `TTP_text_mix`
- `Qwen3VLProcessor`
- `TTP_text_mix`
- `TTP_text_mix`
- `Reroute`
- `TextEncodeQwenImage21`
- `easy showAnything`
- `Reroute`
- `Reroute`
- `Reroute`
- `YYZPack_YYZ_Image_Blank`
- `PreviewImage`
- `Reroute`
- `ImageBatchMulti`
- `Reroute`
- `Reroute`
- `easy showAnything`
- `Qwen3VLProcessor`
- `Reroute`
- `Reroute`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `easy int`
- `SaveImage`
- `Reroute`
- `GetImageSize+`
- `ImpactMinMax`
- `PreviewImage`
- `TTP_text_mix`
- `TTP_text_mix`
- `TTP_text_mix`
- `TTP_text_mix`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `LayerUtility: ImageReel`
- `GetImageSize+`
- `ImpactMinMax`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `VAEDecode` ★核心
- `Bjornulf_ShowInt`
- `Reroute`
- `ImageFromBatch`
- `ImageFromBatch`
- `LayerUtility: ImageReelComposit`
- `ImageFromBatch`
- `LayerUtility: ImageReel`
- `SaveImage`
- `easy showAnything`
- `Reroute`
- `ImageFromBatch`

## 关键参数

- `seed` = `1091707692079692`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `4`

## 知识

覆盖率 **78%**（107/137）

**有卡**：`Int`、`Bjornulf_ShowInt`、`SimpleMath+`、`math_calculate`、`Bjornulf_ShowFloat`、`Boolean To Int [Dream]`、`Qwen3VLProcessor`、`easy cleanGpuUsed`、`easy clearCacheAll`、`llama_cpp_parameters`、`LayerUtility: PurgeVRAM V2`、`JoinStringMulti`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`CR Prompt Text`、`TTP_text_mix`、`CR Aspect Ratio`、`UNETLoader`、`CLIPLoader`、`QwenImage21Cache`、`PrimitiveBoolean`、`KSampler`、`VAELoader`、`EmptyLatentImage`、`ImageFromBatch`、`TextEncodeQwenImage21`、`YYZPack_YYZ_Image_Blank`、`ImageBatchMulti`、`easy int`、`SaveImage`、`GetImageSize+`、`ImpactMinMax`、`LoadImage`、`LayerUtility: ImageReel`、`VAEDecode`、`LayerUtility: ImageReelComposit`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
