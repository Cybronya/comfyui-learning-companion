---
name: unknown_workflow_lora_sampler_clip_21
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.758077
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein-马克笔转绘（清新日系）_2034116719706378241.json, 图片生成/图生图/Klein9B控制图片编辑6种LORA合集_2070689409061703682.json, 图片生成/图生图/Klein_模特局部特写_2045523124346691586.json, 图片生成/图生图/flux-2-klein-base-9b城市设计_2054581666382925826.json, 图片生成/图生图/flux-2-klein-base-9b城市设计_2059472417961107458.json, 图片生成/图生图/flux-2-klein-base-9b城市设计_2059494781138587649.json, 图片生成/图生图/flux-2-klein-base-9b城市设计_2061286231631286274.json, 图片生成/图生图/flux-2-klein-base-9b城市设计_2062819546272198658.json, 图片生成/图生图/flux-2-klein-base-9b城市设计_2064557309329756162.json, 图片生成/图生图/klein-城市设计-lora4.0版本_2046223772444790786.json, 图片生成/图生图/klein_鸟瞰效果图生成平面图_2042849394952769537.json, 图片生成/图生图/klein_鸟瞰生成_2026259142662430721.json, 图片生成/图生图/tang成熟手绘-Klein-马克笔转换_2032270065495707649.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Klein-马克笔转绘（清新日系）_2034116719706378241.json、图片生成/图生图/Klein9B控制图片编辑6种LORA合集_2070689409061703682.json、图片生成/图生图/Klein_模特局部特写_2045523124346691586.json、图片生成/图生图/flux-2-klein-base-9b城市设计_2054581666382925826.json、图片生成/图生图/flux-2-klein-base-9b城市设计_2059472417961107458.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 11/13 个有
- `LayerUtility: ImageReelComposit` —— 11/13 个有
- `PreviewImage` —— 7/13 个有
- `Int` —— 4/13 个有
- `ConditioningZeroOut` —— 2/13 个有
- `Text Multiline` —— 2/13 个有
- `AIO_Preprocessor` —— 1/13 个有
- `Any Switch (rgthree)` —— 1/13 个有
- `CR Prompt Text` —— 1/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `Fast Groups Muter (rgthree)` —— 1/13 个有
- `ImageResize+` —— 1/13 个有
- `JDCN_StringToList` —— 1/13 个有
- `ProcessString` —— 1/13 个有
- `Text Concatenate` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
