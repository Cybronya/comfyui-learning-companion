---
name: text_to_image_sampler_clip_unet_100
type: Text To Image
frequency: 7
level: strong
coverage: 0.846
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image 图像反推+去AI感_1994614273647185921.json, 图片生成/图生图/Z-image 图像反推+去AI感_2084482159057915906.json, 图片生成/图生图/Z-image自动反推图生图+seedvr2放大工作流_1994759435346190337.json, 图片生成/图生图/z-image图提示词生图_1999347155796193281.json, 图片生成/图生图/老高Z-image + seedvr2 + 背景反推_2014303163351830530.json, 图片生成/文生图/Z-image + seedvr2 + 图片反推_1990637223408263169.json, 图片生成/文生图/Z-image 图像反推+去AI感_1994602887898669057.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_100

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Z-image 图像反推+去AI感_1994614273647185921.json、图片生成/图生图/Z-image 图像反推+去AI感_2084482159057915906.json、图片生成/图生图/Z-image自动反推图生图+seedvr2放大工作流_1994759435346190337.json、图片生成/图生图/z-image图提示词生图_1999347155796193281.json、图片生成/图生图/老高Z-image + seedvr2 + 背景反推_2014303163351830530.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 6/7 个有
- `ImageScaleToTotalPixels` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `Qwen3_VQA` —— 6/7 个有
- `SeedVR2` —— 6/7 个有
- `easy cleanGpuUsed` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `AddTextPrefix` —— 1/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `TT_img_enc` —— 1/7 个有
- `TextBox` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 9 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1080 | 1080 - 1920 | 7 | 76% |
| 高度 | 1920 | 1080 - 1920 | 7 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 9，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1920，7 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，7 个样本，取值集中（一致性 83%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
