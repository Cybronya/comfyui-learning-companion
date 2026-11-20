---
name: unknown_workflow_inpaint_sampler_clip_20
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.812333
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoaderGGUF, FluxGuidance, GrowMaskWithBlur, Image Blank, Image Comparer (rgthree), ImageConcanate, ImageCrop+, ImageResize+, ImageToMask, InpaintModelConditioning, KSampler, LoadImage, MaskPreview+, MaskToImage, PreviewImage, SaveImage, Seed (rgthree), StyleModelApply, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/万物迁移 人物一致性｜好用舒适版_1923254217191190529.json, 图片生成/图生图/万物迁移-3图_2054750336031707138.json, 图片生成/图生图/万物迁移-吊坠_2054462595725307906.json, 图片生成/图生图/万物迁移-吊坠_2059095154748911618.json, 图片生成/图生图/万物迁移第二版_2002004995228745730.json, 图片生成/图生图/换装极简redux工作流_1925596565598064641.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/万物迁移 人物一致性｜好用舒适版_1923254217191190529.json、图片生成/图生图/万物迁移-3图_2054750336031707138.json、图片生成/图生图/万物迁移-吊坠_2054462595725307906.json、图片生成/图生图/万物迁移-吊坠_2059095154748911618.json、图片生成/图生图/万物迁移第二版_2002004995228745730.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoaderGGUF`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `Image Blank`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageCrop+`
- `ImageResize+`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageCompositeMasked` —— 5/6 个有
- `Mask Crop Region` —— 5/6 个有
- `UnetLoaderGGUF` —— 5/6 个有
- `ACE_ImageGetSize` —— 1/6 个有
- `Image Save` —— 1/6 个有
- `ResizeImageMixlab` —— 1/6 个有
- `UNETLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 6 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | normal | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，6 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 normal，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
