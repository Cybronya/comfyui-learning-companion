---
name: unknown_workflow_inpaint_sampler_clip_53
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8274
common_nodes: [Anything Everywhere3, CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, ImageConcanate, ImageToMask, InpaintModelConditioning, InspyrenetRembg, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskPreview+, MaskToImage, PreviewImage, ReduxAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/LOGO迁移工作流_1898190146129317890.json, 平台全量/万物迁移工作流V2.0_1889492433296678913.json, 平台全量/万物迁移工作流_1880189586113536001.json, 平台全量/万物迁移工作流最新。_1891412821106892802.json, 平台全量/眼镜换模特工作流_1898979120033026049.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_53

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/LOGO迁移工作流_1898190146129317890.json、平台全量/万物迁移工作流V2.0_1889492433296678913.json、平台全量/万物迁移工作流_1880189586113536001.json、平台全量/万物迁移工作流最新。_1891412821106892802.json、平台全量/眼镜换模特工作流_1898979120033026049.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `ImageConcanate`
- `ImageToMask`
- `InpaintModelConditioning`
- `InspyrenetRembg`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 4/5 个有
- `GrowMask` —— 4/5 个有
- `Display Any (rgthree)` —— 3/5 个有
- `GetImageSize+` —— 3/5 个有
- `ImageCrop+` —— 3/5 个有
- `SimpleMath+` —— 3/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageCrop` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 1.1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
