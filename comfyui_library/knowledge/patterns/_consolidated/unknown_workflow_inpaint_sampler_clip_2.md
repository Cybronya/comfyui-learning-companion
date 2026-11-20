---
name: unknown_workflow_inpaint_sampler_clip_2
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.931267
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageResize+, ImageToMask, InpaintModelConditioning, KSampler, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/F.1 模特换装工作流 Flux Fill + Redux_1908551372160311298.json, 图片生成/图生图/FLUX产品换背景+模特换装+产品加图案万物迁移_1924669048213131266.json, 图片生成/图生图/Fill+Redux+ACE 模特服装展示｜电商_1933869008892682241.json, 图片生成/图生图/Fill模特换装工作流_1989594426118950914.json, 图片生成/图生图/Fill模特换装工作流_1995496550623281154.json, 图片生成/图生图/Flux Fill+Redux换装工作流_1990374948038479874.json, 图片生成/图生图/Flux Fill+Redux换装工作流（本地运行）_2077818162678161409.json, 图片生成/图生图/Flux换装工作流(Flux+redux)_2003065173164400641.json, 图片生成/图生图/Flux最新换装工作流一键运行_1918569163147907073.json, 图片生成/图生图/换装10.6自己11_1974983541811490818.json, 图片生成/图生图/换装工作流_1969651961618460673.json, 图片生成/图生图/换装工作流_2106576886481645569.json, 图片生成/图生图/模特换装、局部修改工作流_2092984388773564418.json, 图片生成/图生图/模特换装、局部修改工作流_2093501336422801409.json, 图片生成/图生图/模特换装、局部修改工作流_2093541212350402562.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/F.1 模特换装工作流 Flux Fill + Redux_1908551372160311298.json、图片生成/图生图/FLUX产品换背景+模特换装+产品加图案万物迁移_1924669048213131266.json、图片生成/图生图/Fill+Redux+ACE 模特服装展示｜电商_1933869008892682241.json、图片生成/图生图/Fill模特换装工作流_1989594426118950914.json、图片生成/图生图/Fill模特换装工作流_1995496550623281154.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImageResize+`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 14/15 个有
- `Image Filter Adjustments` —— 13/15 个有
- `easy mathInt` —— 13/15 个有
- `Bjornulf_ShowInt` —— 10/15 个有
- `ImageCrop` —— 10/15 个有
- `easy imageInsetCrop` —— 5/15 个有
- `EmptyImage` —— 2/15 个有
- `Image Comparer (rgthree)` —— 2/15 个有
- `ConditioningZeroOut` —— 1/15 个有
- `DeepTranslatorTextNode` —— 1/15 个有
- `GrowMaskWithBlur` —— 1/15 个有
- `LayerUtility: CropByMask V2` —— 1/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/15 个有
- `LayerUtility: RestoreCropBox` —— 1/15 个有
- `LoraLoaderModelOnly` —— 1/15 个有
- `TeaCache` —— 1/15 个有
- `easy imageConcat` —— 1/15 个有
- `preview_mask` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 15 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 87% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，15 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 87%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
