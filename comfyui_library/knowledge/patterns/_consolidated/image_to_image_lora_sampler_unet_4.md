---
name: image_to_image_lora_sampler_unet_4
type: Image To Image
frequency: 6
level: strong
coverage: 0.811167
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [Bookmark (rgthree), easy imageSize]
members: [图片生成/图生图/2011705037017325569.json, 图片生成/图生图/2011767661780275201.json, 图片生成/图生图/2046950886362062849.json, 图片生成/文生图/1985126465392037890.json, 视频生成/图生视频/2010896559696777218.json, 视频生成/图生视频/图像转角度｜单张一致性LoRA_+_多角度LoRAQwen_Edit_2511_2100191664584351746.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_4

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/2011705037017325569.json、图片生成/图生图/2011767661780275201.json、图片生成/图生图/2046950886362062849.json、图片生成/文生图/1985126465392037890.json、视频生成/图生视频/2010896559696777218.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 4/6 个有
- `FluxKontextMultiReferenceLatentMethod` —— 4/6 个有
- `PreviewImage` —— 3/6 个有
- `QwenMultiangleCameraNode` —— 3/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `easy imageSize` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `Bookmark (rgthree)` —— 1/6 个有
- `EmptyImage` —— 1/6 个有
- `FluxKontextImageScale` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `easy promptList` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6.5 | 4 - 8 | 6 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6.5，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Bookmark (rgthree)、easy imageSize
