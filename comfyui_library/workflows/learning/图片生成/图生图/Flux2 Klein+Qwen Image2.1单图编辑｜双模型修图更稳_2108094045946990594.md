---
key: 图片生成/图生图/Flux2 Klein+Qwen Image2.1单图编辑｜双模型修图更稳_2108094045946990594.json
name: Flux2 Klein+Qwen Image2.1单图编辑｜双模型修图更稳_2108094045946990594
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2 Klein+Qwen Image2.1单图编辑｜双模型修图更稳_2108094045946990594.json
hash: 74526311059ef8aa
coverage: 0.831818
learned_at: 2026-10-21 00:39:37
nodes: [KSamplerSelect, RandomNoise, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, Flux2Scheduler, CFGGuider, UNETLoader, CLIPLoader, SamplerCustomAdvanced, CLIPTextEncode, easy clearCacheAll, VAEDecode, EmptyFlux2LatentImage, Int, Bjornulf_ShowInt, Bjornulf_ShowInt, Int, Bjornulf_ShowInt, Bjornulf_ShowInt, SimpleMath+, math_calculate, SimpleMath+, Int, Bjornulf_ShowInt, Bjornulf_ShowInt, math_calculate, Int, Bjornulf_ShowInt, math_calculate, Bjornulf_ShowInt, math_calculate, math_calculate, SimpleMath+, SimpleMath+, SimpleMath+, math_calculate, math_calculate, math_calculate, Bjornulf_ShowFloat, math_calculate, math_calculate, math_calculate, Bjornulf_ShowFloat, easy showAnything, SimpleMath+, SimpleMath+, SimpleMath+, Bjornulf_ShowFloat, Bjornulf_ShowFloat, easy showAnything, Boolean To Int [Dream], Boolean To Int [Dream], easy convertAnything, easy convertAnything, CR Prompt Text, JoinStringMulti, Int, Int, Reroute, Reroute, Reroute, Image Comparer (rgthree), easy cleanGpuUsed, Reroute, easy cleanGpuUsed, easy clearCacheAll, llama_cpp_parameters, llama_cpp_model_loader, LayerUtility: PurgeVRAM V2, easy clearCacheAll, LayerUtility: PurgeVRAM V2, easy showAnything, TTP_text_mix, easy showAnything, JoinStringMulti, PreviewAny, JoinStringMulti, llama_cpp_instruct_adv, easy showAnything, CR Prompt Text, easy showAnything, Qwen3VLProcessor, UNETLoader, CLIPLoader, Reroute, Reroute, Reroute, QwenImage21Cache, PrimitiveBoolean, ComfySwitchNode, VAEDecode, KSampler, VAELoader, Image Comparer (rgthree), EmptyLatentImage, Reroute, ConditioningZeroOut, Reroute, easy showAnything, easy showAnything, easy showAnything, CR Prompt Text, VAEEncode, ConditioningZeroOut, ReferenceLatent, VAELoader, Reroute, GetImageSize+, ImpactMinMax, Bjornulf_ShowInt, SaveImage, Int, Bjornulf_ShowInt, Bjornulf_ShowInt, Int, Bjornulf_ShowInt, Bjornulf_ShowInt, Int, Bjornulf_ShowInt, Bjornulf_ShowInt, math_calculate, Int, Bjornulf_ShowInt, math_calculate, math_calculate, math_calculate, SimpleMath+, math_calculate, math_calculate, math_calculate, Bjornulf_ShowFloat, math_calculate, Bjornulf_ShowFloat, SimpleMath+, SimpleMath+, Bjornulf_ShowFloat, Bjornulf_ShowFloat, easy showAnything, math_calculate, Bjornulf_ShowInt, math_calculate, easy showAnything, SimpleMath+, math_calculate, easy showAnything, easy showAnything, easy showAnything, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, GetImageSize+, Boolean To Int [Dream], Boolean To Int [Dream], Bjornulf_ShowInt, Reroute, Reroute, Reroute, easy showAnything, SaveImageAdvanced, Qwen3VLProcessor, CR Prompt Text, CR Prompt Text, CR Aspect Ratio, CR Aspect Ratio, Reroute, ReferenceLatent, CR Prompt Text, QwenImage21EditTextEncode_EditUtils, Bjornulf_ShowInt, SaveImage, CR Prompt Text, LoadImage, ImageResize+, easy int, Int, Int, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux2 Klein+Qwen Image2.1单图编辑｜双模型修图更稳_2108094045946990594.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2 Klein+Qwen Image2.1单图编辑｜双模型修图更稳_2108094045946990594.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（220 个）：
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
- `easy int`
- `Int`
- `Int`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image、image_to_image

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

覆盖率 **83%**（183/220）

**有卡**：`KSamplerSelect`、`RandomNoise`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`Flux2Scheduler`、`CFGGuider`、`UNETLoader`、`CLIPLoader`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`easy clearCacheAll`、`VAEDecode`、`EmptyFlux2LatentImage`、`Int`、`Bjornulf_ShowInt`、`SimpleMath+`、`math_calculate`、`Bjornulf_ShowFloat`、`Boolean To Int [Dream]`、`easy convertAnything`、`CR Prompt Text`、`JoinStringMulti`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`TTP_text_mix`、`llama_cpp_instruct_adv`、`Qwen3VLProcessor`、`QwenImage21Cache`、`PrimitiveBoolean`、`KSampler`、`VAELoader`、`EmptyLatentImage`、`ConditioningZeroOut`、`VAEEncode`、`ReferenceLatent`、`GetImageSize+`、`ImpactMinMax`、`SaveImage`、`SaveImageAdvanced`、`CR Aspect Ratio`、`QwenImage21EditTextEncode_EditUtils`、`LoadImage`、`ImageResize+`、`easy int`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
