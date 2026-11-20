---
name: image_to_image_lora_sampler_unet_37
type: Image To Image
frequency: 12
level: moderate
coverage: 0.9125
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/34.tonnie-Qwen edit物品迁移工作流_2003212052573429762.json, 图片生成/图生图/3D转绘-Qwen-Image-Edit图像编辑-Comfy官方_1970486961637105665.json, 图片生成/图生图/3D转绘-Qwen-Image-Edit图像编辑-Comfy官方_2018211066441900034.json, 图片生成/图生图/57.tonnie-2509换脸_2008688247454568450.json, 图片生成/图生图/FireRed Image edit_2030887570980212737.json, 图片生成/图生图/Put It Here v1 Qwen Edit万物融图_1965935009678954497.json, 图片生成/图生图/Put It Here v1 Qwen Edit融图_1994337831405502465.json, 图片生成/图生图/Qwen Edit图像融合_1966514470820458497.json, 图片生成/图生图/家具设计溶图-Put-It-Here-Qwen版_1962136791979593730.json, 图片生成/图生图/手持商品溶图-Put-It-Here-Qwen版_1962135540076318722.json, 图片生成/图生图/溶图Qwen版_1965249068194742273.json, 图片生成/图生图/溶图_1965258732785516546.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_37

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/34.tonnie-Qwen edit物品迁移工作流_2003212052573429762.json、图片生成/图生图/3D转绘-Qwen-Image-Edit图像编辑-Comfy官方_1970486961637105665.json、图片生成/图生图/3D转绘-Qwen-Image-Edit图像编辑-Comfy官方_2018211066441900034.json、图片生成/图生图/57.tonnie-2509换脸_2008688247454568450.json、图片生成/图生图/FireRed Image edit_2030887570980212737.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 10/12 个有
- `FastCanvas` —— 8/12 个有
- `FastCanvasTool` —— 8/12 个有
- `ImageStitch` —— 8/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/12 个有
- `TextEncodeQwenImageEditEnhanced` —— 7/12 个有
- `easy imageRemBg` —— 7/12 个有
- `PreviewImage` —— 6/12 个有
- `TextEncodeQwenImageEdit` —— 5/12 个有
- `ImageScaleDownToSize` —— 4/12 个有
- `TextEncodeQwenImageEditPlus` —— 4/12 个有
- `ConditioningZeroOut` —— 3/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `Fast Groups Muter (rgthree)` —— 1/12 个有
- `InspyrenetRembg` —— 1/12 个有
- `SeedVR2` —— 1/12 个有
- `SeedVR2BlockSwap` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 8 - 20 | 12 | 60% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 12 | 69% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 8 - 20，12 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
