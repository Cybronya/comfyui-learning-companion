---
name: unknown_workflow_inpaint_sampler_clip_55
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8108
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, Image Blank, ImageConcanate, ImageToMask, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/万物迁移增强版_1950146234545823745.json, 平台全量/万物迁移工作流_1910258613200584706.json, 平台全量/万物迁移工作流_1917106990689226753.json, 平台全量/万物迁移工作流_1952996542606209026.json, 平台全量/商品一键替换_1928993821521035266.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_55

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/万物迁移增强版_1950146234545823745.json、平台全量/万物迁移工作流_1910258613200584706.json、平台全量/万物迁移工作流_1917106990689226753.json、平台全量/万物迁移工作流_1952996542606209026.json、平台全量/商品一键替换_1928993821521035266.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Blank`
- `ImageConcanate`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 4/5 个有
- `ImageCrop+` —— 3/5 个有
- `ImpactInt` —— 3/5 个有
- `easy imageInsetCrop` —— 2/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `Int` —— 1/5 个有
- `Joy_caption` —— 1/5 个有
- `Joy_caption_load` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `StringFunction|pysssss` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有
- `easy imageSize` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 5 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，5 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
