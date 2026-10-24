---
name: text_to_image_lora_sampler_clip_360
type: Text To Image
frequency: 5
level: strong
coverage: 0.9138
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/批量去水印v1.0_1997212139112828929.json, 图片生成/图生图/换角度（可以手动调角度）_2017499064656470018.json, 图片生成/图生图/沙雕熊猫头角色qwen_1988475955230498818.json, 图片生成/文生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2083015619733180417.json, 图片生成/文生图/图像编辑FireRed-Image-Edit-1.1_2053727183633432578.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_360

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/批量去水印v1.0_1997212139112828929.json、图片生成/图生图/换角度（可以手动调角度）_2017499064656470018.json、图片生成/图生图/沙雕熊猫头角色qwen_1988475955230498818.json、图片生成/文生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2083015619733180417.json、图片生成/文生图/图像编辑FireRed-Image-Edit-1.1_2053727183633432578.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `JjkText` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `PreviewImage` —— 2/5 个有
- `SeedVR2` —— 2/5 个有
- `ComfySwitchNode` —— 1/5 个有
- `CustomAddLabel` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `QwenMultiangleCameraNode` —— 1/5 个有
- `RHUploadZip_V2` —— 1/5 个有
- `RunningHub Deepcleaner` —— 1/5 个有
- `easy imageConcat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1440 | 1280 - 1920 | 5 | 82% |
| 高度 | 1080 | 720 - 1920 | 5 | 68% |
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1440，观测区间 1280 - 1920，5 个样本，取值集中（一致性 82%）
- 高度 中位数 1080，观测区间 720 - 1920，5 个样本
- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
