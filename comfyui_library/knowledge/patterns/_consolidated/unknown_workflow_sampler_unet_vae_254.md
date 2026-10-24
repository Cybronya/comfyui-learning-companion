---
name: unknown_workflow_sampler_unet_vae_254
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.936
common_nodes: [CFGGuider, CLIPLoader, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PainterFluxImageEdit, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux-Klein单图编辑_2054474437596065794.json, 图片生成/图生图/Klein-9B-单图编辑+真实细节增加_2036060432284262401.json, 图片生成/图生图/Klein换衣服_2054474542659194882.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_254

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux-Klein单图编辑_2054474437596065794.json、图片生成/图生图/Klein-9B-单图编辑+真实细节增加_2036060432284262401.json、图片生成/图生图/Klein换衣服_2054474542659194882.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PainterFluxImageEdit`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `easy clearCacheAll` —— 2/3 个有
- `Mask Fill Holes` —— 1/3 个有
- `ModelScopeVisionPromptInversion_Sevr` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
