---
name: unknown_workflow_lora_sampler_clip_291
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.815
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSamplerSelect, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Anima-702-护士长_2072661208766959618.json, 数字人/数字人/Flux2 Klein 大熊超强多功能工作流_2060172149209526273.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_291

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Anima-702-护士长_2072661208766959618.json、数字人/数字人/Flux2 Klein 大熊超强多功能工作流_2060172149209526273.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `FLS_SamplerV4` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `RTXVideoSuperResolution` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
