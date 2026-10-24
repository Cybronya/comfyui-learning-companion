---
name: unknown_workflow_sampler_clip_unet_259
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9254
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX.2 [Klein] 多图编辑_2074481156397035521.json, 图片生成/文生图/Flux2 Klein 图像编辑4B版V1_2012131213674287106.json, 图片生成/文生图/Flux2 Klein 图像编辑_2070333019503808513.json, 图片生成/文生图/Flux2 Klein 多图编辑&文生图 自由控制 平替全能图片 4B 极速 & 9B 质量_2012361850310107138.json, 图片生成/文生图/Flux2 Klein 文生图 平替全能图片 9B 质量 _支持两种出图方式_2029393137902292993.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_259

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/FLUX.2 [Klein] 多图编辑_2074481156397035521.json、图片生成/文生图/Flux2 Klein 图像编辑4B版V1_2012131213674287106.json、图片生成/文生图/Flux2 Klein 图像编辑_2070333019503808513.json、图片生成/文生图/Flux2 Klein 多图编辑&文生图 自由控制 平替全能图片 4B 极速 & 9B 质量_2012361850310107138.json、图片生成/文生图/Flux2 Klein 文生图 平替全能图片 9B 质量 _支持两种出图方式_2029393137902292993.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
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
- `ConditioningZeroOut` —— 4/5 个有
- `ImageScaleToTotalPixels` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `Any Switch (rgthree)` —— 2/5 个有
- `AspectRatio` —— 2/5 个有
- `GetImageSize` —— 2/5 个有
- `ImageConcanate` —— 2/5 个有
- `ImageResize+` —— 2/5 个有
- `Int` —— 2/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/5 个有
- `LoraLoaderModelOnly_Any` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `TT_img_enc_v2` —— 1/5 个有
- `TwoWaySwitch` —— 1/5 个有
- `孤海注释` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
