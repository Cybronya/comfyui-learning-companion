---
name: text_to_image_sampler_clip_unet_193
type: Text To Image
frequency: 3
level: moderate
coverage: 0.766333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2-图像生成 (T2I+I2I) Z-Image Turbo 工作流_2053397476975104001.json, 图片生成/文生图/Anima Base any-test-like控制生图_2073323335081095169.json, 图片生成/文生图/Z-image 文生图+反推洗图_1993920304986652673.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_193

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/2-图像生成 (T2I+I2I) Z-Image Turbo 工作流_2053397476975104001.json、图片生成/文生图/Anima Base any-test-like控制生图_2073323335081095169.json、图片生成/文生图/Z-image 文生图+反推洗图_1993920304986652673.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `AnimaLLLiteApply` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `Resize Image for SDXL` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 30 | 3 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 768 - 1344 | 3 | 77% |
| 高度 | 1024 | 768 - 1024 | 3 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 30，3 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1344，3 个样本
- 高度 中位数 1024，观测区间 768 - 1024，3 个样本，取值集中（一致性 87%）
