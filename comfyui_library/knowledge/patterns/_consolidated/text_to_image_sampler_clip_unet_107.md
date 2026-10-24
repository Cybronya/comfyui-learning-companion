---
name: text_to_image_sampler_clip_unet_107
type: Text To Image
frequency: 6
level: moderate
coverage: 0.849333
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2 写实文生图_2069944402356817921.json, 图片生成/图生图/LH-DMT版本-2.生图片类-031.Z-image文生图 + 图像重绘_2016507574392197121.json, 图片生成/图生图/z-image-turbo-参考图生图_2057716109838733314.json, 图片生成/图生图/z-image-turbo_2034208282579050498.json, 图片生成/文生图/Krea2 写实文生图_2069839901595619329.json, 图片生成/文生图/Z-image 文生图+反推洗图_1993920304986652673.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_107

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Krea2 写实文生图_2069944402356817921.json、图片生成/图生图/LH-DMT版本-2.生图片类-031.Z-image文生图 + 图像重绘_2016507574392197121.json、图片生成/图生图/z-image-turbo-参考图生图_2057716109838733314.json、图片生成/图生图/z-image-turbo_2034208282579050498.json、图片生成/文生图/Krea2 写实文生图_2069839901595619329.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LoadImage` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `VAEEncode` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `AILab_QwenVL` —— 1/6 个有
- `Any Switch (rgthree)` —— 1/6 个有
- `Dapao_LlamaChat` —— 1/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 924 | 720 - 1280 | 6 | 75% |
| 高度 | 1152 | 720 - 1920 | 6 | 65% |
| 采样步数 | 10 | 8 - 10 | 6 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 0.65 - 1 | 6 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 924，观测区间 720 - 1280，6 个样本
- 高度 中位数 1152，观测区间 720 - 1920，6 个样本
- 采样步数 中位数 10，观测区间 8 - 10，6 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.65 - 1，6 个样本，取值集中（一致性 83%）
