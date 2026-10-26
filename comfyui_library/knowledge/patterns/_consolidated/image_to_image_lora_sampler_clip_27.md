---
name: image_to_image_lora_sampler_clip_27
type: Image To Image
frequency: 8
level: moderate
coverage: 0.885875
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/5.其他类型-06.NSF+-06.FLUX.2-klein005.flux-2单-多图编辑_2026629947330142210.json, 图片生成/图生图/55.tonnie-flux2编辑图像_2008311211066138626.json, 图片生成/图生图/Flux-2-klein-图片编辑（三图）_2081417532673712130.json, 图片生成/图生图/Flux2 Klein最强高清修复 最适合模糊大到8k高清_2015071955560435713.json, 图片生成/图生图/Flux2+Klein控油高清放大加强细节_2043890754564661250.json, 图片生成/图生图/Flux2-Klein9B 无痕换头放大天花板_2026456875612508162.json, 图片生成/文生图/Flux2-Klein 换头放大版_2026341472559177729.json, 图片生成/文生图/Flux2-Klein9B 无痕换头放大大师版_2026299604819517442.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/5.其他类型-06.NSF+-06.FLUX.2-klein005.flux-2单-多图编辑_2026629947330142210.json、图片生成/图生图/55.tonnie-flux2编辑图像_2008311211066138626.json、图片生成/图生图/Flux-2-klein-图片编辑（三图）_2081417532673712130.json、图片生成/图生图/Flux2 Klein最强高清修复 最适合模糊大到8k高清_2015071955560435713.json、图片生成/图生图/Flux2+Klein控油高清放大加强细节_2043890754564661250.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `CR Prompt Text` —— 6/8 个有
- `FluxGuidance` —— 6/8 个有
- `easy cleanGpuUsed` —— 6/8 个有
- `GetImageSize` —— 5/8 个有
- `ImageScaleToTotalPixels` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `Image Comparer (rgthree)` —— 4/8 个有
- `Image To Mask` —— 3/8 个有
- `ImageResizeKJv2` —— 3/8 个有
- `LanPaint_KSampler` —— 3/8 个有
- `PrimitiveFloat` —— 3/8 个有
- `SetLatentNoiseMask` —— 3/8 个有
- `DualCLIPLoader` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `UnetLoaderGGUF` —— 2/8 个有
- `CLIPLoaderGGUF` —— 1/8 个有
- `Image Compare (mtb)` —— 1/8 个有
- `Int` —— 1/8 个有
- `ModelPatchTorchSettings` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 20 | 8 | 30% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 0.25 - 1 | 8 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 20，8 个样本，取值分散，一致性仅 30%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，8 个样本
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
