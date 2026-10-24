---
name: unknown_workflow_sampler_clip_unet_151
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.9215
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux-2-klein自拍照一键生成证件照_2019656662927286274.json, 图片生成/图生图/flux2-klein 单图编辑_2051866752035897345.json, 图片生成/图生图/flux2_klein_9b_kv图编辑_2062349239690293250.json, 图片生成/图生图/flux2_klein_image_edit mutiple Ref 多图参考编辑_2044462579120087042.json, 图片生成/图生图/flux2_klein_图生图_runninghub_2030497319736578050.json, 图片生成/图生图/flux2_klein_图生图_基础工作流_2030890083406057474.json, 图片生成/图生图/flux单图v2_2103034191372963842.json, 图片生成/图生图/自拍照+服装参考图一键生成证件照_2020047100834226178.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_151

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/flux-2-klein自拍照一键生成证件照_2019656662927286274.json、图片生成/图生图/flux2-klein 单图编辑_2051866752035897345.json、图片生成/图生图/flux2_klein_9b_kv图编辑_2062349239690293250.json、图片生成/图生图/flux2_klein_image_edit mutiple Ref 多图参考编辑_2044462579120087042.json、图片生成/图生图/flux2_klein_图生图_runninghub_2030497319736578050.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 7/8 个有
- `GetImageSize` —— 4/8 个有
- `ImageScaleToTotalPixels` —— 4/8 个有
- `PrimitiveStringMultiline` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `PrimitiveString` —— 2/8 个有
- `StringReplace` —— 2/8 个有
- `FluxKVCache` —— 1/8 个有
- `ImageBatch` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `easy boolean` —— 1/8 个有
- `easy ifElse` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
