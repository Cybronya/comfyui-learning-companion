---
name: unknown_workflow_upscale_lora_sampler_111
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.84
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, FluxKontextImageScale, Image Comparer (rgthree), ImitationHueNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy positive]
problems: []
missing: []
members: [图片生成/图生图/flux2-klein-二次元转三次元-100%复刻_2113799049806704642.json, 平台全量/flux2-klein-二次元转三次元-100%复刻_2020766539728822274.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_111

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/flux2-klein-二次元转三次元-100%复刻_2113799049806704642.json、平台全量/flux2-klein-二次元转三次元-100%复刻_2020766539728822274.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `ImitationHueNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
