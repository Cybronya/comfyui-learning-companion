---
name: image_to_image_sampler_clip_unet_138
type: Image To Image
frequency: 4
level: strong
coverage: 0.86
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/Z-IMAGE全自动反推洗图（极致真实，还原度可控）_1996994862434160642.json, 图片生成/图生图/Z-Image_ 图像反推生图_1999281406482280449.json, 图片生成/图生图/Z-Image超真实网红打造-洗图_1998985187780386817.json, 图片生成/文生图/Z-image洗图换明星脸_1993904921521094658.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_138

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/Z-IMAGE全自动反推洗图（极致真实，还原度可控）_1996994862434160642.json、图片生成/图生图/Z-Image_ 图像反推生图_1999281406482280449.json、图片生成/图生图/Z-Image超真实网红打造-洗图_1998985187780386817.json、图片生成/文生图/Z-image洗图换明星脸_1993904921521094658.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `Qwen3_VQA` —— 3/4 个有
- `easy int` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `easy float` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `JoinStrings` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `PurgeVRAM_UTK` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 0.7 - 1 | 4 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，4 个样本，取值集中（一致性 86%）
