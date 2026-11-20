---
name: unknown_workflow_sampler_clip_unet_229
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.917667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX.2 [Klein] 多图编辑_2074481156397035521.json, 图片生成/文生图/FLUX.2-klein-最快生图工作流_2012044466873442306.json, 图片生成/文生图/FLUX2 Klein 9B Image Edit_2073301759640035330.json, 图片生成/文生图/Flux2 Klein 图像编辑4B版V1_2012131213674287106.json, 图片生成/文生图/Flux2 Klein 图像编辑_2070333019503808513.json, 图片生成/文生图/Flux2 Klein｜图像编辑（角色一致性，保留角色全身特征）+防色彩偏移_2046845762285346817.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_229

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/FLUX.2 [Klein] 多图编辑_2074481156397035521.json、图片生成/文生图/FLUX.2-klein-最快生图工作流_2012044466873442306.json、图片生成/文生图/FLUX2 Klein 9B Image Edit_2073301759640035330.json、图片生成/文生图/Flux2 Klein 图像编辑4B版V1_2012131213674287106.json、图片生成/文生图/Flux2 Klein 图像编辑_2070333019503808513.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
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
- `ConditioningZeroOut` —— 5/6 个有
- `GetImageSize` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 5/6 个有
- `CR Text` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `ImageConcanate` —— 2/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `Flux2KleinColorAnchor` —— 1/6 个有
- `Flux2KleinRefLatentController` —— 1/6 个有
- `Flux2KleinTextRefBalance` —— 1/6 个有
- `FluxResolutionNode` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/6 个有
- `孤海注释` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
