---
name: unknown_workflow_sampler_clip_unet_113
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9159
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein_模特局部特写_2045523124346691586.json, 图片生成/图生图/Klein动漫高清放大到4k分辨率保留细节_2060294265787469825.json, 图片生成/图生图/flux-2-klein-9B 图像编辑_2013804472748744705.json, 图片生成/图生图/flux2 klein 超实用高清放大_2075145254583488513.json, 图片生成/图生图/▶▶F2K-一致性图像细化+编辑_2055291592189202434.json, 图片生成/图生图/图片0色差0偏移高清放大_2080959572566700034.json, 图片生成/图生图/照片修复F2K-一致性图像细化+编辑1_2043974556662108162.json, 图片生成/图生图/老孙AI 零偏移溶图_2094232856351563777.json, 图片生成/图生图/黑鹤-0色差0位移放大-小志lord_2095493334134517761.json, 图片生成/图生图/黑鹤-0色差0位移放大-小志lord_2101693603444781057.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_113

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Klein_模特局部特写_2045523124346691586.json、图片生成/图生图/Klein动漫高清放大到4k分辨率保留细节_2060294265787469825.json、图片生成/图生图/flux-2-klein-9B 图像编辑_2013804472748744705.json、图片生成/图生图/flux2 klein 超实用高清放大_2075145254583488513.json、图片生成/图生图/▶▶F2K-一致性图像细化+编辑_2055291592189202434.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
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

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 9/10 个有
- `LoraLoaderModelOnly` —— 9/10 个有
- `LayerUtility: PurgeVRAM V2` —— 8/10 个有
- `easy int` —— 8/10 个有
- `ImageSmartSharpen+` —— 7/10 个有
- `Seed (rgthree)` —— 7/10 个有
- `easy imageColorMatch` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 5/10 个有
- `ImageScaleToTotalPixels` —— 3/10 个有
- `CR Prompt Text` —— 1/10 个有
- `CR Text` —— 1/10 个有
- `DuckHideNode` —— 1/10 个有
- `HAIGC_SaveImagesToZip` —— 1/10 个有
- `JDCN_StringToList` —— 1/10 个有
- `ProcessString` —— 1/10 个有
- `Text Concatenate` —— 1/10 个有
- `easy seed` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
