---
name: unknown_workflow_sampler_clip_unet_219
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.926167
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/角色四视图-klein9b_2083577051046567937.json, 图片生成/图生图/角色正视图和三视图_2100255300451397633.json, 图片生成/图生图/（Supermate收藏）Klein9B深度+线稿+法线+硬边缘控制图片编辑_2082068130804887553.json, 图片生成/图生图/👾怪獸-Flux2Klein 去水印马赛克👾_2047809913426022401.json, 图片生成/图生图/🦄Klein9B姿态变换🎯天下无腰_2092246348958617602.json, 图片生成/文生图/Flux2-Klein 多图编辑工作流_2012031209374748673.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_219

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/角色四视图-klein9b_2083577051046567937.json、图片生成/图生图/角色正视图和三视图_2100255300451397633.json、图片生成/图生图/（Supermate收藏）Klein9B深度+线稿+法线+硬边缘控制图片编辑_2082068130804887553.json、图片生成/图生图/👾怪獸-Flux2Klein 去水印马赛克👾_2047809913426022401.json、图片生成/图生图/🦄Klein9B姿态变换🎯天下无腰_2092246348958617602.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
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
- `GetImageSize` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `Flux2Scheduler` —— 4/6 个有
- `ImageConcatMulti` —— 4/6 个有
- `ImageScaleToTotalPixels` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `AIO_Preprocessor` —— 2/6 个有
- `BasicScheduler` —— 2/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `AddLabel` —— 1/6 个有
- `ImagePadForOutpaint` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `JWImageResizeByLongerSide` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `ResolutionSelector` —— 1/6 个有
- `TextBox` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
