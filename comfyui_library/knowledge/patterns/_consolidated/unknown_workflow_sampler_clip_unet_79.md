---
name: unknown_workflow_sampler_clip_unet_79
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.927917
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/电商产品场景图生成_2069077696059105281.json, 图片生成/图生图/电商产品换材质 flux2 klein_2026838584275247105.json, 图片生成/图生图/电商产品精修快速版_2044583021092802562.json, 图片生成/图生图/电商产品精修美化细节高清放大_2069464540449959937.json, 图片生成/图生图/电商任意角度打光 flux2 klein_2012726242851692545.json, 图片生成/图生图/电商移除图片指定位置内容_2026115966425374721.json, 图片生成/图生图/老孙AI 产品精修_2090283355492413441.json, 图片生成/图生图/🦖Flux2-klein单图编辑_2013897331980111873.json, 图片生成/文生图/AI一键生成12张绝美新年写真集_2024044240682098690.json, 图片生成/文生图/FLUX.2 Klein 4B工作流，8G显存1秒生成1张图片！_2012164022556172289.json, 图片生成/文生图/FLUX2 Klein 9B Consistency 一致性工作流_2073316611037163521.json, 图片生成/文生图/Flux2-Klein全家桶-多功能版_2016042987171614722.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_79

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/电商产品场景图生成_2069077696059105281.json、图片生成/图生图/电商产品换材质 flux2 klein_2026838584275247105.json、图片生成/图生图/电商产品精修快速版_2044583021092802562.json、图片生成/图生图/电商产品精修美化细节高清放大_2069464540449959937.json、图片生成/图生图/电商任意角度打光 flux2 klein_2012726242851692545.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 12 个 workflow 都包含：
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
- `EmptyFlux2LatentImage` —— 11/12 个有
- `GetImageSize` —— 11/12 个有
- `Image Comparer (rgthree)` —— 8/12 个有
- `ImageScaleToTotalPixels` —— 8/12 个有
- `LoraLoaderModelOnly` —— 4/12 个有
- `ConstrainImage|pysssss` —— 3/12 个有
- `Fast Groups Bypasser (rgthree)` —— 3/12 个有
- `JjkText` —— 3/12 个有
- `Label (rgthree)` —— 2/12 个有
- `CR Latent Input Switch` —— 1/12 个有
- `Colored Image (mtb)` —— 1/12 个有
- `HAIGC_LoadImagesFromZip` —— 1/12 个有
- `InpaintModelConditioning` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `Qwen2.5` —— 1/12 个有
- `QwenMultiangleLightningNode` —— 1/12 个有
- `UnetLoaderGGUF` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有
- `easy imageColorMatch` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
