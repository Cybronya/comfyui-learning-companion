---
key: 图片生成/图生图/人物图+衣服正面图+衣服细节图==换衣-QWEN2.1_2108843476371730434.json
name: 人物图+衣服正面图+衣服细节图==换衣-QWEN2.1_2108843476371730434
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/人物图+衣服正面图+衣服细节图==换衣-QWEN2.1_2108843476371730434.json
hash: a5b1abb8dc87340a
coverage: 0.768293
learned_at: 2026-10-23 12:09:51
nodes: [Int, Bjornulf_ShowInt, Bjornulf_ShowInt, Int, Bjornulf_ShowInt, Bjornulf_ShowInt, SimpleMath+, math_calculate, SimpleMath+, Int, Bjornulf_ShowInt, Bjornulf_ShowInt, math_calculate, Int, Bjornulf_ShowInt, math_calculate, Bjornulf_ShowInt, math_calculate, math_calculate, SimpleMath+, SimpleMath+, SimpleMath+, math_calculate, math_calculate, math_calculate, Bjornulf_ShowFloat, math_calculate, math_calculate, math_calculate, Bjornulf_ShowFloat, easy showAnything, SimpleMath+, SimpleMath+, SimpleMath+, Bjornulf_ShowFloat, Bjornulf_ShowFloat, easy showAnything, Boolean To Int [Dream], Boolean To Int [Dream], Int, Int, easy showAnything, easy showAnything, easy showAnything, Qwen3VLProcessor, Qwen3VLProcessor, Reroute, easy cleanGpuUsed, Reroute, easy cleanGpuUsed, easy clearCacheAll, llama_cpp_parameters, LayerUtility: PurgeVRAM V2, easy clearCacheAll, LayerUtility: PurgeVRAM V2, JoinStringMulti, PreviewAny, llama_cpp_instruct_adv, easy showAnything, llama_cpp_model_loader, Int, Int, easy showAnything, CR Prompt Text, TTP_text_mix, TTP_text_mix, Note, KSamplerSelect, RandomNoise, LayerUtility: PurgeVRAM V2, Flux2Scheduler, CFGGuider, UNETLoader, CLIPLoader, CLIPTextEncode, easy clearCacheAll, VAEDecode, VAEEncode, ReferenceLatent, ConditioningZeroOut, VAELoader, ReferenceLatent, Qwen3VLProcessor, TTP_text_mix, easy cleanGpuUsed, Reroute, easy cleanGpuUsed, easy clearCacheAll, llama_cpp_parameters, LayerUtility: PurgeVRAM V2, easy clearCacheAll, LayerUtility: PurgeVRAM V2, JoinStringMulti, PreviewAny, llama_cpp_instruct_adv, easy showAnything, llama_cpp_model_loader, easy showAnything, Note, Reroute, TTP_text_mix, CR Prompt Text, Qwen3VLProcessor, CR Aspect Ratio, easy cleanGpuUsed, EmptyFlux2LatentImage, Reroute, UNETLoader, CLIPLoader, Reroute, Reroute, QwenImage21Cache, PrimitiveBoolean, ComfySwitchNode, KSampler, VAELoader, EmptyLatentImage, Bjornulf_ShowInt, Reroute, ImageFromBatch, Qwen3VLProcessor, TTP_text_mix, Qwen3VLProcessor, TTP_text_mix, TTP_text_mix, TTP_text_mix, Reroute, Reroute, TextEncodeQwenImage21, CR Prompt Text, Note, TTP_text_mix, easy showAnything, Reroute, Reroute, Reroute, SamplerCustomAdvanced, SaveImage, YYZPack_YYZ_Image_Blank, PreviewImage, Reroute, ImageBatchMulti, Reroute, Reroute, easy showAnything, Qwen3VLProcessor, TTP_text_mix, Reroute, Reroute, ImageFromBatch, ImageFromBatch, ImageFromBatch, VAEDecode, LoadImage, LoadImage, LoadImage, LoadImage, easy int, SaveImage, Reroute, GetImageSize+, ImpactMinMax, CR Prompt Text, PreviewImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 4, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 98178791768545, "steps": 25, "width": 1024}
---

# 图片生成/图生图/人物图+衣服正面图+衣服细节图==换衣-QWEN2.1_2108843476371730434.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/人物图+衣服正面图+衣服细节图==换衣-QWEN2.1_2108843476371730434.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（164 个）：
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
- `easy showAnything`
- `CR Prompt Text`
- `TTP_text_mix`
- `TTP_text_mix`
- `Note`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LayerUtility: PurgeVRAM V2`
- `Flux2Scheduler`
- `CFGGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `easy clearCacheAll`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `VAELoader`
- `ReferenceLatent`
- `Qwen3VLProcessor`
- `TTP_text_mix`
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
- `easy showAnything`
- `Note`
- `Reroute`
- `TTP_text_mix`
- `CR Prompt Text`
- `Qwen3VLProcessor`
- `CR Aspect Ratio`
- `easy cleanGpuUsed`
- `EmptyFlux2LatentImage`
- `Reroute`
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
- `TTP_text_mix`
- `Reroute`
- `Reroute`
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `Note`
- `TTP_text_mix`
- `easy showAnything`
- `Reroute`
- `Reroute`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `YYZPack_YYZ_Image_Blank`
- `PreviewImage`
- `Reroute`
- `ImageBatchMulti`
- `Reroute`
- `Reroute`
- `easy showAnything`
- `Qwen3VLProcessor`
- `TTP_text_mix`
- `Reroute`
- `Reroute`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy int`
- `SaveImage`
- `Reroute`
- `GetImageSize+`
- `ImpactMinMax`
- `CR Prompt Text`
- `PreviewImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `98178791768545`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `4`

## 知识

覆盖率 **77%**（126/164）

**有卡**：`Int`、`Bjornulf_ShowInt`、`SimpleMath+`、`math_calculate`、`Bjornulf_ShowFloat`、`Boolean To Int [Dream]`、`Qwen3VLProcessor`、`easy cleanGpuUsed`、`easy clearCacheAll`、`llama_cpp_parameters`、`LayerUtility: PurgeVRAM V2`、`JoinStringMulti`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`CR Prompt Text`、`TTP_text_mix`、`KSamplerSelect`、`RandomNoise`、`Flux2Scheduler`、`CFGGuider`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAEDecode`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`VAELoader`、`CR Aspect Ratio`、`EmptyFlux2LatentImage`、`QwenImage21Cache`、`PrimitiveBoolean`、`KSampler`、`EmptyLatentImage`、`ImageFromBatch`、`TextEncodeQwenImage21`、`SamplerCustomAdvanced`、`SaveImage`、`YYZPack_YYZ_Image_Blank`、`ImageBatchMulti`、`LoadImage`、`easy int`、`GetImageSize+`、`ImpactMinMax`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
