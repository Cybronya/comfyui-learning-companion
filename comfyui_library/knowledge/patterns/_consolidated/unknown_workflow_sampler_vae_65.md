---
name: unknown_workflow_sampler_vae_65
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.814667
common_nodes: [BasicGuider, EmptyFlux2LatentImage, KSamplerSelect, LoadImage, RHFibo2EditConditioning, RHFibo2ModelLoader, RHFibo2Scheduler, RHFibo2TextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Fibo2工作流修改图片_2111991292468228098.json, 图片生成/图生图/pandy-FIBO2-Turbo4步图像编辑_2114251172331741186.json, 平台全量/Fibo2图片编辑_2113156964275544065.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_65

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Fibo2工作流修改图片_2111991292468228098.json、图片生成/图生图/pandy-FIBO2-Turbo4步图像编辑_2114251172331741186.json、平台全量/Fibo2图片编辑_2113156964275544065.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `EmptyFlux2LatentImage`
- `KSamplerSelect`
- `LoadImage`
- `RHFibo2EditConditioning`
- `RHFibo2ModelLoader`
- `RHFibo2Scheduler`
- `RHFibo2TextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 2/3 个有
- `RHFibo2KeepOutsideMask` —— 2/3 个有
- `GetImageSize` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `LoadAndResizeImage` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
