---
name: unknown_workflow_sampler_unet_vae_158
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.820286
common_nodes: [CFGGuider, CLIPLoader, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/三图编辑（解禁模型）：Flux.2 Klein 9B_2051654833320542209.json, 图片生成/图生图/仅需四步，建筑效果图一键多风格_2030610127664979970.json, 图片生成/图生图/全能人物照片编辑头发人脸衣服服装更换变装变发型图生图升级版_2074339361214255106.json, 图片生成/图生图/动漫转写实cg Klein 9b 工作流_2015973646677843969.json, 图片生成/图生图/动漫转真人Klein 9b工作流_2032463178499624961.json, 图片生成/图生图/多图编辑换装电商人物添加人物物品装饰多图合一AI重绘_2074345357949104129.json, 图片生成/图生图/服装上身与场景生成_2060636969994113025.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_158

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/三图编辑（解禁模型）：Flux.2 Klein 9B_2051654833320542209.json、图片生成/图生图/仅需四步，建筑效果图一键多风格_2030610127664979970.json、图片生成/图生图/全能人物照片编辑头发人脸衣服服装更换变装变发型图生图升级版_2074339361214255106.json、图片生成/图生图/动漫转写实cg Klein 9b 工作流_2015973646677843969.json、图片生成/图生图/动漫转真人Klein 9b工作流_2032463178499624961.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 6/7 个有
- `Image Comparer (rgthree)` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `ReferenceLatent` —— 6/7 个有
- `VAEEncode` —— 6/7 个有
- `EmptyFlux2LatentImage` —— 5/7 个有
- `GetImageSize` —— 3/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `JjkText` —— 2/7 个有
- `PlaySound|pysssss` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `AIO_Preprocessor` —— 1/7 个有
- `FluxKontextImageScale` —— 1/7 个有
- `ImageInvert` —— 1/7 个有
- `ImpactSwitch` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `StringReplace` —— 1/7 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
