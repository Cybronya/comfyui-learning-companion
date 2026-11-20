---
name: unknown_workflow_sampler_clip_unet_255
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.943
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize, easy int]
problems: []
missing: []
members: [图片生成/图生图/Flux2-klein-美甲迁移_2029843703233257474.json, 图片生成/图生图/Flux2-klein人物角色 任意变发型 发型迁移 假发模特_2025741951122808834.json, 图片生成/图生图/电商产品FLUX2精修_2094400191687385090.json, 图片生成/图生图/电商产品FLUX2精修_2096169386120925186.json, 图片生成/图生图/电商产品FLUX2精修_2096403269538115586.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_255

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux2-klein-美甲迁移_2029843703233257474.json、图片生成/图生图/Flux2-klein人物角色 任意变发型 发型迁移 假发模特_2025741951122808834.json、图片生成/图生图/电商产品FLUX2精修_2094400191687385090.json、图片生成/图生图/电商产品FLUX2精修_2096169386120925186.json、图片生成/图生图/电商产品FLUX2精修_2096403269538115586.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
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
- `easy imageSize`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 3/5 个有
- `FluxGuidance` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `LayerUtility: ImageMaskScaleAs` —— 3/5 个有
- `easy imageConcat` —— 3/5 个有
- `ImpactMakeAnyList` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `easy compare` —— 2/5 个有
- `easy ifElse` —— 2/5 个有
- `easy imageSizeBySide` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `PreviewAny` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
