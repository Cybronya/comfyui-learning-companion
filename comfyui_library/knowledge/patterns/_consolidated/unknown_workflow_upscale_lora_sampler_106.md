---
name: unknown_workflow_upscale_lora_sampler_106
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.846
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Float, Flux2Scheduler, FluxGuidance, FluxKontextImageScale, GetImageSize+, Image Comparer (rgthree), ImageUpscaleWithModel, ImpactInt, InversionDemoLazySwitch, JjkText, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy promptConcat]
problems: []
missing: []
members: [图片生成/图生图/Klein透视溶图+光影融合_2062773964757356545.json, 平台全量/光影融合V2_修复皮肤质感_2118217304621281282.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_106

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Klein透视溶图+光影融合_2062773964757356545.json、平台全量/光影融合V2_修复皮肤质感_2118217304621281282.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Float`
- `Flux2Scheduler`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `ImpactInt`
- `InversionDemoLazySwitch`
- `JjkText`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有
- `easy boolean` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
