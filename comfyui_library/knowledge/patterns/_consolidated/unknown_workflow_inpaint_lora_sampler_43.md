---
name: unknown_workflow_inpaint_lora_sampler_43
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.843
common_nodes: [CLIPTextEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, DualCLIPLoaderGGUF, EmptyImage, Florence2ModelLoader, Florence2Run, FluxGuidance, Image Comparer (rgthree), ImageCompositeMasked, ImageConcanate, InpaintModelConditioning, JoinStrings, KSampler, LayerUtility: ExtendCanvas, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Mask Invert, MaskBlur+, MaskPreview+, PreviewImage, Primitive string [Crystools], ReduxAdvanced, SaveImage, ShowText|pysssss, StyleModelLoader, TeaCache, UNETLoader, UnetLoaderGGUF, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/万物迁移 高适配度 不挑图片 电商场景应用_1948191756880871426.json, 图片生成/图生图/万物迁移工作流，好用版细节保留99.9%_1896242102861234178.json, 图片生成/图生图/万物迁移工作流，好用版细节保留99.9%_1946168824493142017.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_43

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/万物迁移 高适配度 不挑图片 电商场景应用_1948191756880871426.json、图片生成/图生图/万物迁移工作流，好用版细节保留99.9%_1896242102861234178.json、图片生成/图生图/万物迁移工作流，好用版细节保留99.9%_1946168824493142017.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `DualCLIPLoaderGGUF`
- `EmptyImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageConcanate`
- `InpaintModelConditioning`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ExtendCanvas`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Invert`
- `MaskBlur+`
- `MaskPreview+`
- `PreviewImage`
- `Primitive string [Crystools]`
- `ReduxAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StyleModelLoader`
- `TeaCache`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
