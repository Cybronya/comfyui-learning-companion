---
key: 图片生成/图生图/单图编辑-Flux2 Klein+Qwen image2.1_2107726878978170881.json
name: 单图编辑-Flux2 Klein+Qwen image2.1_2107726878978170881
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/单图编辑-Flux2 Klein+Qwen image2.1_2107726878978170881.json
hash: 04292325767f02b4
coverage: 0.8
learned_at: 2026-10-21 00:50:43
nodes: [KSamplerSelect, RandomNoise, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, Flux2Scheduler, CFGGuider, UNETLoader, CLIPLoader, SamplerCustomAdvanced, CLIPTextEncode, easy clearCacheAll, VAEDecode, EmptyFlux2LatentImage, Int, Bjornulf_ShowInt, Bjornulf_ShowInt, Int, Bjornulf_ShowInt, Bjornulf_ShowInt, SimpleMath+, math_calculate, SimpleMath+, Int, Bjornulf_ShowInt, Bjornulf_ShowInt, math_calculate, Int, Bjornulf_ShowInt, math_calculate, Bjornulf_ShowInt, math_calculate, math_calculate, SimpleMath+, SimpleMath+, SimpleMath+, math_calculate, math_calculate, math_calculate, Bjornulf_ShowFloat, math_calculate, math_calculate, math_calculate, Bjornulf_ShowFloat, easy showAnything, SimpleMath+, SimpleMath+, SimpleMath+, Bjornulf_ShowFloat, Bjornulf_ShowFloat, easy showAnything, Boolean To Int [Dream], Boolean To Int [Dream], easy convertAnything, easy convertAnything, CR Prompt Text, JoinStringMulti, Int, Int, Reroute, Reroute, Reroute, Image Comparer (rgthree), easy cleanGpuUsed, Reroute, easy cleanGpuUsed, easy clearCacheAll, llama_cpp_parameters, llama_cpp_model_loader, LayerUtility: PurgeVRAM V2, easy clearCacheAll, LayerUtility: PurgeVRAM V2, easy showAnything, TTP_text_mix, easy showAnything, JoinStringMulti, PreviewAny, JoinStringMulti, llama_cpp_instruct_adv, easy showAnything, CR Prompt Text, easy showAnything, Qwen3VLProcessor, UNETLoader, CLIPLoader, Reroute, Reroute, Reroute, QwenImage21Cache, PrimitiveBoolean, ComfySwitchNode, VAEDecode, KSampler, VAELoader, Image Comparer (rgthree), EmptyLatentImage, Reroute, ConditioningZeroOut, Reroute, easy showAnything, easy showAnything, easy showAnything, CR Prompt Text, VAEEncode, ConditioningZeroOut, ReferenceLatent, VAELoader, Reroute, GetImageSize+, ImpactMinMax, Bjornulf_ShowInt, SaveImage, Int, Bjornulf_ShowInt, Bjornulf_ShowInt, Int, Bjornulf_ShowInt, Bjornulf_ShowInt, Int, Bjornulf_ShowInt, Bjornulf_ShowInt, math_calculate, Int, Bjornulf_ShowInt, math_calculate, math_calculate, math_calculate, SimpleMath+, math_calculate, math_calculate, math_calculate, Bjornulf_ShowFloat, math_calculate, Bjornulf_ShowFloat, SimpleMath+, SimpleMath+, Bjornulf_ShowFloat, Bjornulf_ShowFloat, easy showAnything, math_calculate, Bjornulf_ShowInt, math_calculate, easy showAnything, SimpleMath+, math_calculate, easy showAnything, easy showAnything, easy showAnything, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, GetImageSize+, Boolean To Int [Dream], Boolean To Int [Dream], Bjornulf_ShowInt, Reroute, Reroute, Reroute, easy showAnything, SaveImageAdvanced, Qwen3VLProcessor, CR Prompt Text, CR Prompt Text, CR Aspect Ratio, CR Aspect Ratio, Reroute, ReferenceLatent, CR Prompt Text, QwenImage21EditTextEncode_EditUtils, Bjornulf_ShowInt, SaveImage, CR Prompt Text, LoadImage, ImageResize+, 孤海注释, 孤海注释, easy int, Int, Int, 孤海注释]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 4, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 507962855940413, "steps": 25, "width": 1024}
---

# 图片生成/图生图/单图编辑-Flux2 Klein+Qwen image2.1_2107726878978170881.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/单图编辑-Flux2 Klein+Qwen image2.1_2107726878978170881.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（180 个）：
- `KSamplerSelect` ★核心
- `RandomNoise`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM V2`
- `Flux2Scheduler`
- `CFGGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `easy clearCacheAll`
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
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
- `easy convertAnything`
- `easy convertAnything`
- `CR Prompt Text`
- `JoinStringMulti`
- `Int`
- `Int`
- `Reroute`
- `Reroute`
- `Reroute`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `Reroute`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `LayerUtility: PurgeVRAM V2`
- `easy clearCacheAll`
- `LayerUtility: PurgeVRAM V2`
- `easy showAnything`
- `TTP_text_mix`
- `easy showAnything`
- `JoinStringMulti`
- `PreviewAny`
- `JoinStringMulti`
- `llama_cpp_instruct_adv`
- `easy showAnything`
- `CR Prompt Text`
- `easy showAnything`
- `Qwen3VLProcessor`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `QwenImage21Cache`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `Image Comparer (rgthree)`
- `EmptyLatentImage` ★核心
- `Reroute`
- `ConditioningZeroOut`
- `Reroute`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `CR Prompt Text`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAELoader`
- `Reroute`
- `GetImageSize+`
- `ImpactMinMax`
- `Bjornulf_ShowInt`
- `SaveImage`
- `Int`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `Int`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `Int`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `math_calculate`
- `Int`
- `Bjornulf_ShowInt`
- `math_calculate`
- `math_calculate`
- `math_calculate`
- `SimpleMath+`
- `math_calculate`
- `math_calculate`
- `math_calculate`
- `Bjornulf_ShowFloat`
- `math_calculate`
- `Bjornulf_ShowFloat`
- `SimpleMath+`
- `SimpleMath+`
- `Bjornulf_ShowFloat`
- `Bjornulf_ShowFloat`
- `easy showAnything`
- `math_calculate`
- `Bjornulf_ShowInt`
- `math_calculate`
- `easy showAnything`
- `SimpleMath+`
- `math_calculate`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `GetImageSize+`
- `Boolean To Int [Dream]`
- `Boolean To Int [Dream]`
- `Bjornulf_ShowInt`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy showAnything`
- `SaveImageAdvanced`
- `Qwen3VLProcessor`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Aspect Ratio`
- `CR Aspect Ratio`
- `Reroute`
- `ReferenceLatent`
- `CR Prompt Text`
- `QwenImage21EditTextEncode_EditUtils`
- `Bjornulf_ShowInt`
- `SaveImage`
- `CR Prompt Text`
- `LoadImage`
- `ImageResize+`
- `孤海注释`
- `孤海注释`
- `easy int`
- `Int`
- `Int`
- `孤海注释`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `507962855940413`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `4`

## 知识

覆盖率 **80%**（144/180）

**有卡**：`KSamplerSelect`、`RandomNoise`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`Flux2Scheduler`、`CFGGuider`、`UNETLoader`、`CLIPLoader`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`easy clearCacheAll`、`VAEDecode`、`EmptyFlux2LatentImage`、`Int`、`Bjornulf_ShowInt`、`SimpleMath+`、`math_calculate`、`Bjornulf_ShowFloat`、`Boolean To Int [Dream]`、`easy convertAnything`、`CR Prompt Text`、`JoinStringMulti`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`TTP_text_mix`、`llama_cpp_instruct_adv`、`Qwen3VLProcessor`、`QwenImage21Cache`、`PrimitiveBoolean`、`KSampler`、`VAELoader`、`EmptyLatentImage`、`ConditioningZeroOut`、`VAEEncode`、`ReferenceLatent`、`GetImageSize+`、`ImpactMinMax`、`SaveImage`、`SaveImageAdvanced`、`CR Aspect Ratio`、`QwenImage21EditTextEncode_EditUtils`、`LoadImage`、`ImageResize+`、`easy int`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
