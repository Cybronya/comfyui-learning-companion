---
name: unknown_workflow_sampler_clip_unet_385
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.887667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PrimitiveInt, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux2_klein4B&9B文生图_图生图_图像编辑合集_2012078185009127425.json, 图片生成/文生图/Klein 9B单、双、多图编辑_2018506313860386818.json, 图片生成/文生图/Klein 9b 文生图&编辑  工作流_2013047540010192898.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_385

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Flux2_klein4B&9B文生图_图生图_图像编辑合集_2012078185009127425.json、图片生成/文生图/Klein 9B单、双、多图编辑_2018506313860386818.json、图片生成/文生图/Klein 9b 文生图&编辑  工作流_2013047540010192898.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PrimitiveInt`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `Int` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
