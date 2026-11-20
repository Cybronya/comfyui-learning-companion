---
name: unknown_workflow_sampler_clip_unet_208
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.88
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/电商产品场景图生成_2016326407609131010.json, 平台全量/电商图片高清放大 flux2 klein_2017121628672499713.json, 平台全量/画风迁移_1890347817712668673.json, 平台全量/老照片修复，局部编辑｜Flux-Klein｜+多功能、一致性增强 LoRA_2044435605949521922.json, 平台全量/重新打光，照片过曝，光斑，上色，偏色，老照片修复，万能P图，去水印_2102336630823669761.json, 平台全量/高清放大 增加细节 去除AI塑料感 Flux2 Klein  优化皮肤 渲染现实_2022122766878646274.json, 数字人/数字人/Flux2 Klein 增强细节 动漫转真实照片_2048302003553570818.json, 数字人/数字人/Flux2 Klein 大熊超强多功能工作流_2060172149209526273.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_208

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/电商产品场景图生成_2016326407609131010.json、平台全量/电商图片高清放大 flux2 klein_2017121628672499713.json、平台全量/画风迁移_1890347817712668673.json、平台全量/老照片修复，局部编辑｜Flux-Klein｜+多功能、一致性增强 LoRA_2044435605949521922.json、平台全量/重新打光，照片过曝，光斑，上色，偏色，老照片修复，万能P图，去水印_2102336630823669761.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
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
- `EmptyFlux2LatentImage` —— 7/8 个有
- `GetImageSize` —— 7/8 个有
- `Image Comparer (rgthree)` —— 6/8 个有
- `ImageScaleToTotalPixels` —— 5/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `JjkText` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `PrimitiveFloat` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `GetNode` —— 1/8 个有
- `ImageScaleToMegapixels` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `Qwen2.5` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
