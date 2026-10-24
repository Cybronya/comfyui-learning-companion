---
name: unknown_workflow_sampler_unet_vae_91
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8978
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Fire Red Image Edit三图参考图编辑_2028311979135344641.json, 图片生成/图生图/FireRed-Image-Edit-1.0 人物换装_2026821364107190274.json, 图片生成/图生图/FireRed-edit-单图编辑_2020792649099251713.json, 图片生成/图生图/FireRed-edit-多图编辑_2027000392680218626.json, 图片生成/图生图/FireRed-edit1.1-单图编辑_2029538924632219649.json, 图片生成/图生图/Qwen 2511最强开源图像编辑工作流_2054749060900376577.json, 图片生成/图生图/Qwen 2511最强开源图像编辑工作流_2055186368539709441.json, 图片生成/图生图/Qwen-Edit-2511-真人转动漫_2082801924931411970.json, 图片生成/图生图/千问两步编辑，手机壳图案_2084596915836116993.json, 图片生成/图生图/千问编辑手机壳图案_2086993892540506113.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_91

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Fire Red Image Edit三图参考图编辑_2028311979135344641.json、图片生成/图生图/FireRed-Image-Edit-1.0 人物换装_2026821364107190274.json、图片生成/图生图/FireRed-edit-单图编辑_2020792649099251713.json、图片生成/图生图/FireRed-edit-多图编辑_2027000392680218626.json、图片生成/图生图/FireRed-edit1.1-单图编辑_2029538924632219649.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/10 个有
- `ConditioningZeroOut` —— 8/10 个有
- `Image Comparer (rgthree)` —— 7/10 个有
- `TextEncodeQwenImageEditPlus` —— 6/10 个有
- `FluxKontextImageScale` —— 5/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/10 个有
- `Text Multiline` —— 4/10 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 4/10 个有
- `GetImageSize` —— 2/10 个有
- `MuyeTextEditOutput` —— 2/10 个有
- `ImageScaleToTotalPixels` —— 1/10 个有
- `LoraLoader` —— 1/10 个有
- `easy int` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1280 | 10 | 54% |
| 高度 | 512 | 512 - 1280 | 10 | 54% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 8 | 4 - 15 | 10 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1280，10 个样本
- 高度 中位数 512，观测区间 512 - 1280，10 个样本
- 采样步数 中位数 8，观测区间 4 - 15，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
