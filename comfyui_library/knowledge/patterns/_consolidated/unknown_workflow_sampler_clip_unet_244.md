---
name: unknown_workflow_sampler_clip_unet_244
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8678
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/SDPP2.0专用全能证件照_2064166912707350529.json, 图片生成/图生图/flux-2-klein-9b双图编辑_2031371708669628417.json, 图片生成/图生图/flux2_klein_图生图-老照片修复_2057843818355052546.json, 图片生成/图生图/动漫到真人转换_2056398938592342018.json, 图片生成/图生图/动漫转写实cg Klein 9b 工作流_2015973646677843969.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_244

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/SDPP2.0专用全能证件照_2064166912707350529.json、图片生成/图生图/flux-2-klein-9b双图编辑_2031371708669628417.json、图片生成/图生图/flux2_klein_图生图-老照片修复_2057843818355052546.json、图片生成/图生图/动漫到真人转换_2056398938592342018.json、图片生成/图生图/动漫转写实cg Klein 9b 工作流_2015973646677843969.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 4/5 个有
- `Flux2Scheduler` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `Int` —— 3/5 个有
- `Label (rgthree)` —— 3/5 个有
- `GetImageSize` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `BasicScheduler` —— 1/5 个有
- `BiRefNet_Hugo` —— 1/5 个有
- `CR Prompt Text` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `RH_RhartImageG2ImageToImage` —— 1/5 个有
- `ShellAgentPluginInputFloat` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
