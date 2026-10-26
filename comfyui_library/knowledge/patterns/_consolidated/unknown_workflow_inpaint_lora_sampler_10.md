---
name: unknown_workflow_inpaint_lora_sampler_10
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.893125
common_nodes: [CLIPLoader, FluxKontextImageScale, GrowMaskWithBlur, Image Comparer (rgthree), InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed-Image-edit1.1无痕扩图_1987748417499803649.json, 图片生成/图生图/Flux2_Klein-PS扩图_无需参数_2093889851933421569.json, 图片生成/图生图/Flux2_Klein-PS扩图_无需参数_2093908406183747586.json, 图片生成/图生图/小红书扩图工作流_2036288458133610498.json, 图片生成/图生图/无痕真实扩图  FireRed-Image-Edit 极限扩图 图像边界外扩v1.3_2032054868092919810.json, 图片生成/图生图/极限扩图 _ 图像边界外扩_2081607122642628609.json, 图片生成/图生图/极限扩图_图像边界外扩_2084970530326798338.json, 图片生成/图生图/极限扩图_图像边界外扩_2085175397221748737.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/FireRed-Image-edit1.1无痕扩图_1987748417499803649.json、图片生成/图生图/Flux2_Klein-PS扩图_无需参数_2093889851933421569.json、图片生成/图生图/Flux2_Klein-PS扩图_无需参数_2093908406183747586.json、图片生成/图生图/小红书扩图工作流_2036288458133610498.json、图片生成/图生图/无痕真实扩图  FireRed-Image-Edit 极限扩图 图像边界外扩v1.3_2032054868092919810.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `FluxKontextImageScale`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 7/8 个有
- `LayerUtility: ExtendCanvas` —— 5/8 个有
- `easy int` —— 5/8 个有
- `LayerUtility: ExtendCanvasV2` —— 3/8 个有
- `Int` —— 2/8 个有
- `Any Switch (rgthree)` —— 1/8 个有
- `GetImageSize` —— 1/8 个有
- `LayerMask: MaskInvert` —— 1/8 个有
- `LayerUtility: SaveImagePlusV2` —— 1/8 个有
- `SolidMask` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
