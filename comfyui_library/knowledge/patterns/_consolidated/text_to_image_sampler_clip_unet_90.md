---
name: text_to_image_sampler_clip_unet_90
type: Text To Image
frequency: 7
level: strong
coverage: 0.848571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, SeedVR2, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image 图像反推+去AI感_1994614273647185921.json, 图片生成/图生图/Z-image 图像反推+去AI感_2084482159057915906.json, 图片生成/图生图/Z-image自动反推图生图+seedvr2放大工作流_1994759435346190337.json, 图片生成/图生图/seedance2.0真人过审-Sim制作_2053052803047804930.json, 图片生成/图生图/人物三视图-FireRed-Image-Edit 1.1-高清直出_2036824180422873090.json, 图片生成/图生图/光影重塑-图片重新打光-FireRed-Image-Edit 1.1-图生图_2061065889038032897.json, 图片生成/图生图/光影重塑-图片重新打光-V2-FireRed-Image-Edit 1.1-图生图_2061104265892024321.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_90

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Z-image 图像反推+去AI感_1994614273647185921.json、图片生成/图生图/Z-image 图像反推+去AI感_2084482159057915906.json、图片生成/图生图/Z-image自动反推图生图+seedvr2放大工作流_1994759435346190337.json、图片生成/图生图/seedance2.0真人过审-Sim制作_2053052803047804930.json、图片生成/图生图/人物三视图-FireRed-Image-Edit 1.1-高清直出_2036824180422873090.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `SeedVR2`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `JjkText` —— 4/7 个有
- `TextEncodeQwenImageEditPlus` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `ConditioningZeroOut` —— 3/7 个有
- `GetImageSize` —— 3/7 个有
- `Image Comparer (rgthree)` —— 3/7 个有
- `Int` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `Qwen3_VQA` —— 2/7 个有
- `Text` —— 2/7 个有
- `llama_cpp_instruct_adv` —— 2/7 个有
- `llama_cpp_model_loader` —— 2/7 个有
- `llama_cpp_parameters` —— 2/7 个有
- `CustomAddLabel` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 9 | 7 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 720 | 720 - 1080 | 7 | 80% |
| 高度 | 1280 | 1280 - 1920 | 7 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 9，7 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 720，观测区间 720 - 1080，7 个样本
- 高度 中位数 1280，观测区间 1280 - 1920，7 个样本，取值集中（一致性 81%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
