---
name: image_to_image_sampler_clip_unet_10
type: Image To Image
frequency: 19
level: moderate
coverage: 0.944316
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-Klein图生图_2012141948076826625.json, 图片生成/图生图/Flux2-Klein真实人像质感御姐美女_2040676390156115969.json, 图片生成/图生图/Flux2-klein单图编辑_2012160766627028993.json, 图片生成/图生图/Flux2-klein单图编辑快速改图改动作改头发改衣服动画改图修复图片30秒完成_2012164663273852929.json, 图片生成/图生图/Flux2-klein材质替换_2012507605150736386.json, 图片生成/图生图/Flux2-klein洗图真实人像质感美女_2038109616621490178.json, 图片生成/图生图/Z image 图生图（洗图）_1993888000021037058.json, 图片生成/图生图/Z-Image-Turbo-人像去Ai味真实质感_1994013061161959425.json, 图片生成/图生图/Z-image图生图_1994327939347054594.json, 图片生成/图生图/cad平面图转彩图-室内设计专用-Flux2-klein_2012841471073853441.json, 图片生成/图生图/cos替换-klein9b_2029474740787748866.json, 图片生成/图生图/flux.2-klein-单图编辑工作流_2076574283811352577.json, 图片生成/图生图/东方阳台美女Flux2-Klein真实人像质感御姐美女_2040723148257107969.json, 图片生成/图生图/俯视户外Flux2-Klein真实人像质感御姐美女_2040703603123425281.json, 图片生成/图生图/古风美女Flux2-Klein真实人像质感御姐美女_2040758027002847234.json, 图片生成/图生图/吊带睡衣Flux2-Klein真实人像质感御姐美女_2040696643078590466.json, 图片生成/图生图/图片高清放大 Flux2-Klein！_2081342617417240577.json, 图片生成/图生图/室内-klein-平面图转彩图工作流_2040793589877317633.json, 图片生成/文生图/毛坯转效果图-室内设计专用-Flux2-klein_2012839162801557505.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_10

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein图生图_2012141948076826625.json、图片生成/图生图/Flux2-Klein真实人像质感御姐美女_2040676390156115969.json、图片生成/图生图/Flux2-klein单图编辑_2012160766627028993.json、图片生成/图生图/Flux2-klein单图编辑快速改图改动作改头发改衣服动画改图修复图片30秒完成_2012164663273852929.json、图片生成/图生图/Flux2-klein材质替换_2012507605150736386.json…）

- **类型**：Image To Image
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 17/19 个有
- `ImageScaleToTotalPixels` —— 9/19 个有
- `ReferenceLatent` —— 9/19 个有
- `LoraLoader` —— 8/19 个有
- `scale` —— 7/19 个有
- `PIP_图像联结` —— 6/19 个有
- `Image Comparer (rgthree)` —— 5/19 个有
- `LatentUpscaleBy` —— 2/19 个有
- `ImageCASharpening+` —— 1/19 个有
- `Text Multiline` —— 1/19 个有
- `easy float` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 2 - 10 | 19 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 19 | 98% |
| 采样算法 | euler | - | 19 | 95% |
| 调度器 | simple | - | 19 | 63% |
| 重绘幅度 | 0.75 | 0.19 - 1 | 19 | 49% |
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 8 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 2 - 10，19 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，19 个样本，取值集中（一致性 98%）
- 采样算法 最常用 euler，19 个样本，一致性 95%
- 调度器 最常用 simple，19 个样本，一致性 63%
- 重绘幅度 中位数 0.75，观测区间 0.19 - 1，19 个样本，取值分散，一致性仅 49%
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，8 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（18/19 个样本）：Steps较低可能导致细节不足
