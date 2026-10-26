---
name: image_to_image_sampler_clip_unet_72
type: Image To Image
frequency: 6
level: strong
coverage: 0.9255
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein-9B-小物品精准迁移_2047909146636324866.json, 图片生成/图生图/Klein-9B-换头一键封神！_2034251935917805570.json, 图片生成/图生图/Klein-Outpaint_2068689625572528130.json, 图片生成/图生图/flux-2-klein-outpainting_api_2100775712268570626.json, 图片生成/图生图/flux-2-klein-图像扩展流_2039560362802024450.json, 图片生成/图生图/👽老许Gary：Klein局部编辑丨最实用的工作流_2046092909593763841.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_72

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Klein-9B-小物品精准迁移_2047909146636324866.json、图片生成/图生图/Klein-9B-换头一键封神！_2034251935917805570.json、图片生成/图生图/Klein-Outpaint_2068689625572528130.json、图片生成/图生图/flux-2-klein-outpainting_api_2100775712268570626.json、图片生成/图生图/flux-2-klein-图像扩展流_2039560362802024450.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 5/6 个有
- `ColorMatch` —— 4/6 个有
- `DrawMaskOnImage` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `ImagePadForOutpaint` —— 3/6 个有
- `ImageScaleToTotalPixels` —— 3/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `CLIPLoaderGGUF` —— 1/6 个有
- `EasySizeSimpleImage` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `InpaintCrop` —— 1/6 个有
- `InpaintStitch` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 10 | 6 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 10，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
