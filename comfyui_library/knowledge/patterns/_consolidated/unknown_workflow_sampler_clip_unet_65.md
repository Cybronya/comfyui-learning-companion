---
name: unknown_workflow_sampler_clip_unet_65
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.726308
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/SDPP2.0专用全能证件照_2064166912707350529.json, 图片生成/图生图/flux-2-klein-9b双图编辑_2031371708669628417.json, 图片生成/图生图/flux-2-klein-base-9b城市设计_2054581666382925826.json, 图片生成/图生图/flux-2-klein-base-9b城市设计_2059472417961107458.json, 图片生成/图生图/flux-2-klein-base-9b城市设计_2059494781138587649.json, 图片生成/图生图/flux-2-klein-base-9b城市设计_2061286231631286274.json, 图片生成/图生图/flux-2-klein-base-9b城市设计_2062819546272198658.json, 图片生成/图生图/flux-2-klein-base-9b城市设计_2064557309329756162.json, 图片生成/图生图/klein-城市设计-lora4.0版本_2046223772444790786.json, 图片生成/图生图/klein_鸟瞰效果图生成平面图_2042849394952769537.json, 图片生成/图生图/klein_鸟瞰生成_2026259142662430721.json, 图片生成/图生图/图片一键换背景_2082397422550077441.json, 图片生成/图生图/建筑与室内效果图渲染_2021215392135389186.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_65

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/SDPP2.0专用全能证件照_2064166912707350529.json、图片生成/图生图/flux-2-klein-9b双图编辑_2031371708669628417.json、图片生成/图生图/flux-2-klein-base-9b城市设计_2054581666382925826.json、图片生成/图生图/flux-2-klein-base-9b城市设计_2059472417961107458.json、图片生成/图生图/flux-2-klein-base-9b城市设计_2059494781138587649.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `Flux2Scheduler` —— 12/13 个有
- `LayerUtility: ImageReel` —— 11/13 个有
- `LayerUtility: ImageReelComposit` —— 11/13 个有
- `LoraLoaderModelOnly` —— 10/13 个有
- `PreviewImage` —— 7/13 个有
- `Int` —— 6/13 个有
- `CR Prompt Text` —— 3/13 个有
- `ConditioningZeroOut` —— 2/13 个有
- `GetImageSize` —— 2/13 个有
- `INTConstant` —— 2/13 个有
- `BasicScheduler` —— 1/13 个有
- `BiRefNet_Hugo` —— 1/13 个有
- `Image Comparer (rgthree)` —— 1/13 个有
- `PrimitiveInt` —— 1/13 个有
- `RH_RhartImageG2ImageToImage` —— 1/13 个有
- `ShellAgentPluginInputFloat` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有
- `easy imageRemBg` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
