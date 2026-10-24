---
name: image_to_image_upscale_sampler_clip_17
type: Image To Image
frequency: 6
level: weak
coverage: 0.557
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingFlux, ReferenceLatent, SaveImage, SetNode, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F.2Klein 9b增强细节，高清真实皮肤质感_2056567735584382978.json, "图片生成/图生图/去AI感, 高清修复, 细节增强 Flux2_2070499201896771585.json", 图片生成/图生图/老孙AI  去AI感  高清修复  细节增强_2087085834855084034.json, 图片生成/图生图/高清修复_细节增强 去AI感（flux2极速出图）_2016831625438433282.json, 图片生成/图生图/高清修复_细节增强 去AI感（flux2极速出图）_2047172994874740738.json, 图片生成/图生图/高清修复flux2_2026831925956059137.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/F.2Klein 9b增强细节，高清真实皮肤质感_2056567735584382978.json、图片生成/图生图/去AI感, 高清修复, 细节增强 Flux2_2070499201896771585.json、图片生成/图生图/老孙AI  去AI感  高清修复  细节增强_2087085834855084034.json、图片生成/图生图/高清修复_细节增强 去AI感（flux2极速出图）_2016831625438433282.json、图片生成/图生图/高清修复_细节增强 去AI感（flux2极速出图）_2047172994874740738.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingFlux`
- `ReferenceLatent`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `TextBox1` —— 5/6 个有
- `easy imageConcat` —— 5/6 个有
- `CR Text` —— 1/6 个有
- `Int` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 2 | 2 - 8 | 6 | 25% |
| Prompt 约束强度(CFG) | 1.4 | 1 - 1.4 | 6 | 89% |
| 采样算法 | euler_ancestral | - | 6 | 83% |
| 调度器 | beta57 | - | 6 | 83% |
| 重绘幅度 | 0.25 | 0.25 - 1 | 6 | 34% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 2，观测区间 2 - 8，6 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 1.4，观测区间 1 - 1.4，6 个样本，取值集中（一致性 89%）
- 采样算法 最常用 euler_ancestral，6 个样本，一致性 83%
- 调度器 最常用 beta57，6 个样本，一致性 83%
- 重绘幅度 中位数 0.25，观测区间 0.25 - 1，6 个样本，取值分散，一致性仅 34%
- 高发问题（12/6 个样本）：Steps较低可能导致细节不足
