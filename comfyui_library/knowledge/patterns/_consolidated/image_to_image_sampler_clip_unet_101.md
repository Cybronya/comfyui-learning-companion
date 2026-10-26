---
name: image_to_image_sampler_clip_unet_101
type: Image To Image
frequency: 5
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物换装   Klein_2029535177847869442.json, 图片生成/图生图/嘟嘟-Flux2多图编辑_1994409685237239809.json, 图片生成/图生图/星蝶Q版画风一键转换工作流_1945724032648093697.json, 图片生成/图生图/老照片修复-Flux-Kontext图像编辑-老照片上色_1943519646446481409.json, 图片生成/图生图/转手办_1950076112036651010.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_101

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/人物换装   Klein_2029535177847869442.json、图片生成/图生图/嘟嘟-Flux2多图编辑_1994409685237239809.json、图片生成/图生图/星蝶Q版画风一键转换工作流_1945724032648093697.json、图片生成/图生图/老照片修复-Flux-Kontext图像编辑-老照片上色_1943519646446481409.json、图片生成/图生图/转手办_1950076112036651010.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
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
- `FluxGuidance` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `Text Multiline` —— 4/5 个有
- `DualCLIPLoader` —— 3/5 个有
- `FluxKontextImageScale` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `CLIPLoader` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `EmptyFlux2LatentImage` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `ImageStitch` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 5 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 0.875 | - | 2 | 97% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.875，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
