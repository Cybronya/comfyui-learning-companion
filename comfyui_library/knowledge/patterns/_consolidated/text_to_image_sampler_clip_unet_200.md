---
name: text_to_image_sampler_clip_unet_200
type: Text To Image
frequency: 3
level: strong
coverage: 0.833667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, MaraScottIsEmptyOrNone_v1, RH_Captioner, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Z-image文生图洗图自动化 （解决随机性差问题）_2000012292685168641.json, 图片生成/文生图/Z-image文生图洗图自动化_1993872494906064897.json, 图片生成/文生图/阿里z-image文生图，洗图_1993976067994091521.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_200

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image文生图洗图自动化 （解决随机性差问题）_2000012292685168641.json、图片生成/文生图/Z-image文生图洗图自动化_1993872494906064897.json、图片生成/文生图/阿里z-image文生图，洗图_1993976067994091521.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `MaraScottIsEmptyOrNone_v1`
- `RH_Captioner`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `easy int` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LatentColorMatch` —— 1/3 个有
- `easy imageListToImageBatch` —— 1/3 个有
- `ttN concat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
