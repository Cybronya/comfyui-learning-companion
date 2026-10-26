---
name: unknown_workflow_lora_sampler_clip_150
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.88275
common_nodes: [Any Switch (rgthree), AspectRatio, CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, ImageResize+, ImageScaleToTotalPixels, Int, KSamplerSelect, LoadImage, LoraLoaderModelOnly_Any, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, TT_img_enc_v2, TwoWaySwitch, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/反推+变大-Flux2 Klein高质量洗图_2047521585283731458.json, 图片生成/图生图/天然重力-Flux2 Klein 图生图_2043887128060366849.json, 图片生成/文生图/COS真人-F2K文生图 平替全能图片 9B 质量 _支持两种出图方式_2051148070401921025.json, 图片生成/文生图/Flux2 Klein 文生图 平替全能图片 9B 质量 _支持两种出图方式_2029393137902292993.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_150

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/反推+变大-Flux2 Klein高质量洗图_2047521585283731458.json、图片生成/图生图/天然重力-Flux2 Klein 图生图_2043887128060366849.json、图片生成/文生图/COS真人-F2K文生图 平替全能图片 9B 质量 _支持两种出图方式_2051148070401921025.json、图片生成/文生图/Flux2 Klein 文生图 平替全能图片 9B 质量 _支持两种出图方式_2029393137902292993.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `AspectRatio`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `ImageResize+`
- `ImageScaleToTotalPixels`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly_Any`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TT_img_enc_v2`
- `TwoWaySwitch`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadLoraOnly` —— 2/4 个有
- `MergeLoraToModel` —— 2/4 个有
- `easy prompt` —— 2/4 个有
- `easy promptConcat` —— 2/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `Textbox` —— 1/4 个有
- `easy saveText` —— 1/4 个有
- `easy showAnything` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
