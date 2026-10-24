---
name: unknown_workflow_sampler_clip_unet_276
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.96875
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX.2-KLEIN-单图编辑-高清直出_2019989626764664833.json, 图片生成/图生图/FLUX.2-KLEIN-双图编辑-高清直出_2019989419784146946.json, 图片生成/图生图/FLUX.2-klein_官方基础工作流（图像编辑）_2048613383078944770.json, 图片生成/图生图/FLUX2-KLEIN-换头_换脸工作流_2017152699401248770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_276

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX.2-KLEIN-单图编辑-高清直出_2019989626764664833.json、图片生成/图生图/FLUX.2-KLEIN-双图编辑-高清直出_2019989419784146946.json、图片生成/图生图/FLUX.2-klein_官方基础工作流（图像编辑）_2048613383078944770.json、图片生成/图生图/FLUX2-KLEIN-换头_换脸工作流_2017152699401248770.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CustomAddLabel` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `Label (rgthree)` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `SeedVR2` —— 2/4 个有
- `Text` —— 2/4 个有
- `ConcatTextOfUtils` —— 1/4 个有
- `ImpactInt` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
