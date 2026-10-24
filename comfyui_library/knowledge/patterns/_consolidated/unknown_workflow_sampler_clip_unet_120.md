---
name: unknown_workflow_sampler_clip_unet_120
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.908222
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2-Klein-9B多图编辑 极速_2012409501634269185.json, 图片生成/图生图/flux-2-klein-9B 图像编辑_2013804472748744705.json, 图片生成/图生图/flux2-Klein-单图编辑（4B）_2012091014151938050.json, 图片生成/图生图/flux2-Klein-单图编辑（9B）_2012088384096833537.json, 图片生成/图生图/flux2多图编辑xingye（最多支持4图）_2013234040454782978.json, 图片生成/图生图/【建筑&室内&景观】超实用工作流合集-基于FLUX2-KLEIN_2097502244789899265.json, 图片生成/图生图/【🛫书墨】FLUX2-klein-9b-一、二、三、四图自由切换工作流_2012025238783004673.json, 图片生成/图生图/白模手绘生成效果图_Flux.2-klein_2062790730405474306.json, 图片生成/图生图/老照片高清修复-FLUX.2-Klein_2014556898728611842.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_120

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein-9B多图编辑 极速_2012409501634269185.json、图片生成/图生图/flux-2-klein-9B 图像编辑_2013804472748744705.json、图片生成/图生图/flux2-Klein-单图编辑（4B）_2012091014151938050.json、图片生成/图生图/flux2-Klein-单图编辑（9B）_2012088384096833537.json、图片生成/图生图/flux2多图编辑xingye（最多支持4图）_2013234040454782978.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `EmptyFlux2LatentImage` —— 7/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `ConditioningZeroOut` —— 6/9 个有
- `Image Comparer (rgthree)` —— 6/9 个有
- `FluxKontextImageScale` —— 5/9 个有
- `PrimitiveStringMultiline` —— 5/9 个有
- `PlaySound|pysssss` —— 4/9 个有
- `easy int` —— 4/9 个有
- `CR Image Grid Panel` —— 3/9 个有
- `Image Batch` —— 3/9 个有
- `LayerUtility: ImageMaskScaleAs` —— 3/9 个有
- `Any Switch (rgthree)` —— 2/9 个有
- `CR SDXL Aspect Ratio` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `Fast Groups Muter (rgthree)` —— 2/9 个有
- `CR Prompt Text` —— 1/9 个有
- `DifferentialDiffusion` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
