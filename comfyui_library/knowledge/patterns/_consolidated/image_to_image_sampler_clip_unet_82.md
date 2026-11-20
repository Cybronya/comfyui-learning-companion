---
name: image_to_image_sampler_clip_unet_82
type: Image To Image
frequency: 6
level: strong
coverage: 0.977333
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/2031316609993805825.json, 图片生成/文生图/87time # 34 写实人像 细腻皮肤 不油腻_1959641912976289793.json, 图片生成/文生图/FLUX图生图（洗图）工作流_2048585634318651394.json, 图片生成/文生图/FLUX工作流_2100147250554040322.json, 图片生成/文生图/FLUX模型工作流搭建-文生图、图生图（洗图）_1962526879636959233.json, 数字人/数字人/FLUX工作流以及文生图洗图_2065662763309031426.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_82

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/2031316609993805825.json、图片生成/文生图/87time # 34 写实人像 细腻皮肤 不油腻_1959641912976289793.json、图片生成/文生图/FLUX图生图（洗图）工作流_2048585634318651394.json、图片生成/文生图/FLUX工作流_2100147250554040322.json、图片生成/文生图/FLUX模型工作流搭建-文生图、图生图（洗图）_1962526879636959233.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 4/6 个有
- `EmptyLatentImage` —— 2/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `ImageUpscaleWithModel` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `UpscaleModelLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 16 - 25 | 6 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 0.7 | 0.35 - 1 | 6 | 56% |
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 16 - 25，6 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 0.7，观测区间 0.35 - 1，6 个样本
- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
