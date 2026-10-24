---
name: image_to_image_sampler_vae_15
type: Image To Image
frequency: 9
level: strong
coverage: 0.901889
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Nunchaku Qwen Edit  - 溶图_1988833609492598785.json, 图片生成/图生图/Nunchaku Qwen Edit - 为T恤添加图案_1988834629606051841.json, 图片生成/图生图/Nunchaku Qwen Edit - 白底转场景图_1988839326039543810.json, 图片生成/图生图/Nunchaku Qwen Edit - 移除物体_1988838379892649986.json, 图片生成/图生图/Nunchaku Qwen Edit - 重新打光_1988837448685858817.json, 图片生成/图生图/Nunchaku Qwen Edit-转为照片_1988832281752113153.json, 图片生成/图生图/Nunchaku-Qwen-edit-2511单图编辑_2021105302266978305.json, 视频生成/图生视频/Nunchaku Qwen Edit - 光影修复_1988835436825022465.json, 视频生成/图生视频/Nunchaku Qwen Edit - 多角度镜头_1988836664481026049.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_15

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Nunchaku Qwen Edit  - 溶图_1988833609492598785.json、图片生成/图生图/Nunchaku Qwen Edit - 为T恤添加图案_1988834629606051841.json、图片生成/图生图/Nunchaku Qwen Edit - 白底转场景图_1988839326039543810.json、图片生成/图生图/Nunchaku Qwen Edit - 移除物体_1988838379892649986.json、图片生成/图生图/Nunchaku Qwen Edit - 重新打光_1988837448685858817.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 8/9 个有
- `Image Comparer (rgthree)` —— 8/9 个有
- `Label (rgthree)` —— 8/9 个有
- `NunchakuQwenImageLoraLoader` —— 8/9 个有
- `StringConcatenate` —— 7/9 个有
- `NunchakuQwenImageLoraStackV3` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
