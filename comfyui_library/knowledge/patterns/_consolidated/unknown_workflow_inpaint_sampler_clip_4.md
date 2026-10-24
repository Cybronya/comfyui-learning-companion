---
name: unknown_workflow_inpaint_sampler_clip_4
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.9315
common_nodes: [CLIPTextEncode, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z image-局部重绘_1996406494566432770.json, 图片生成/图生图/Z-image_局部重绘_1998016560675586050.json, 图片生成/图生图/Z-image局部重绘_1994770932847849474.json, 图片生成/图生图/Z-image局部重绘_1995667925262598145.json, 图片生成/图生图/Z-image局部重绘_1998549428036337666.json, 图片生成/图生图/Z-image局部重绘_2008078929575284737.json, 图片生成/图生图/Z-image局部重绘_2044248370755149826.json, 图片生成/图生图/Z-image局部重绘_2046509363543678977.json, 图片生成/图生图/Z-image开源-局部重绘【非edit模型】_1994233157631279106.json, 图片生成/图生图/[FLUX] 改变发型_1921732538652377090.json, 图片生成/图生图/flux fill 移除、局部重绘_2083238672299814914.json, 图片生成/图生图/一键移除工作流_2020033286864637954.json, 图片生成/图生图/完美遮罩移除功能 Removal 升级版_1983888624603332610.json, 图片生成/图生图/局部重绘 支持4K_1991035247468945410.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Z image-局部重绘_1996406494566432770.json、图片生成/图生图/Z-image_局部重绘_1998016560675586050.json、图片生成/图生图/Z-image局部重绘_1994770932847849474.json、图片生成/图生图/Z-image局部重绘_1995667925262598145.json、图片生成/图生图/Z-image局部重绘_1998549428036337666.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPTextEncode`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 13/14 个有
- `DifferentialDiffusion` —— 13/14 个有
- `FluxGuidance` —— 12/14 个有
- `MaskBlur+` —— 10/14 个有
- `CLIPLoader` —— 9/14 个有
- `Image Comparer (rgthree)` —— 6/14 个有
- `DualCLIPLoader` —— 5/14 个有
- `LoraLoaderModelOnly` —— 4/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/14 个有
- `Mask Fill Holes` —— 3/14 个有
- `GrowMaskWithBlur` —— 2/14 个有
- `ImageResize+` —— 2/14 个有
- `ImpactInt` —— 2/14 个有
- `CR Text` —— 1/14 个有
- `ColorCorrect` —— 1/14 个有
- `ImageAndMaskPreview` —— 1/14 个有
- `MaskPreview+` —— 1/14 个有
- `easy ifElse` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 25 | 14 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 86% |
| 调度器 | simple | - | 14 | 64% |
| 重绘幅度 | 0.85 | 0.75 - 1 | 14 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 25，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 86%
- 调度器 最常用 simple，14 个样本，一致性 64%
- 重绘幅度 中位数 0.85，观测区间 0.75 - 1，14 个样本，取值集中（一致性 91%）
