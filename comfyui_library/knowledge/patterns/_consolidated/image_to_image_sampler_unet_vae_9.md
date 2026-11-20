---
name: image_to_image_sampler_unet_vae_9
type: Image To Image
frequency: 15
level: moderate
coverage: 0.927067
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【楚心钟陌】Qwen三次元转二次元_1999336961653473281.json, 图片生成/图生图/【老金驿站】精准4步三图Qwen Edit-2511-lighting工作流_2004092329285828609.json, 图片生成/图生图/【老金驿站】精准对齐Qwen-edit2509 P图工作流_1970843706431545345.json, 图片生成/图生图/【遇见AI】Firered-image-edit 基础工作流 带加速_2058110780435951617.json, 图片生成/图生图/【遇见AI】QWen-image-edit-2511 Qwen Multiangle Camera_2009873163982737410.json, 图片生成/图生图/二次元图片转真人Qwen_1977227595215458305.json, 图片生成/图生图/可单图可多图编辑命令Qwen Image Edit-2511_2031274430206316546.json, 图片生成/图生图/图片镜头切换_2016419512840626178.json, 图片生成/图生图/多角度_2038826670580310017.json, 图片生成/图生图/支持单图多图编辑融合-邻家AI大女孩_2045067988478464001.json, 图片生成/图生图/自定义编辑视角_2010740914263695362.json, 图片生成/图生图/设计工作流——旋转角度_2009263496592105474.json, 图片生成/文生图/Qwen-Edit-2509-多角度切换_1991129925849579521.json, 图片生成/文生图/测试v2_2028368389479075842.json, 数字人/数字人/Qwen Image Edit 2511-多图编辑_2061638633966358529.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_9

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/【楚心钟陌】Qwen三次元转二次元_1999336961653473281.json、图片生成/图生图/【老金驿站】精准4步三图Qwen Edit-2511-lighting工作流_2004092329285828609.json、图片生成/图生图/【老金驿站】精准对齐Qwen-edit2509 P图工作流_1970843706431545345.json、图片生成/图生图/【遇见AI】Firered-image-edit 基础工作流 带加速_2058110780435951617.json、图片生成/图生图/【遇见AI】QWen-image-edit-2511 Qwen Multiangle Camera_2009873163982737410.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 14/15 个有
- `ModelSamplingAuraFlow` —— 14/15 个有
- `LoraLoaderModelOnly` —— 13/15 个有
- `ImageScaleToTotalPixels` —— 12/15 个有
- `EmptySD3LatentImage` —— 8/15 个有
- `FluxKontextMultiReferenceLatentMethod` —— 8/15 个有
- `ImageConcanate` —— 8/15 个有
- `Image Comparer (rgthree)` —— 7/15 个有
- `QwenMultiangleCameraNode` —— 5/15 个有
- `ConditioningZeroOut` —— 4/15 个有
- `ImageConcatMulti` —— 4/15 个有
- `Text` —— 2/15 个有
- `Int` —— 1/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/15 个有
- `LoraLoader` —— 1/15 个有
- `LoraLoaderModelOnly_Any` —— 1/15 个有
- `ReferenceLatent` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有
- `easy imageSize` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 15 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 15 | 88% |
| 采样算法 | euler | - | 15 | 93% |
| 调度器 | simple | - | 15 | 87% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，15 个样本，取值集中（一致性 88%）
- 采样算法 最常用 euler，15 个样本，一致性 93%
- 调度器 最常用 simple，15 个样本，一致性 87%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（20/15 个样本）：Steps较低可能导致细节不足
