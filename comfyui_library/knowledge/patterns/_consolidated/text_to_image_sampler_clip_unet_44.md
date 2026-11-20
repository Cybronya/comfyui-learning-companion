---
name: text_to_image_sampler_clip_unet_44
type: Text To Image
frequency: 13
level: moderate
coverage: 0.973077
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/2031276815041433602.json, 图片生成/文生图/F1文生图精细调节人像_1924680451447771137.json, 图片生成/文生图/FLUX1文生图260814_2088196242147987458.json, 图片生成/文生图/FLUX工作流_2106376251710722050.json, 图片生成/文生图/Flux文生图+高清放大工作流_1915239700771045377.json, 图片生成/文生图/Flux文生图_2109172528118845442.json, 图片生成/文生图/Flux文生图_2115986281145659394.json, 图片生成/文生图/Flux文生图_2115999798758297602.json, 图片生成/文生图/Flux文生图工作流_1912760478278348801.json, 图片生成/文生图/Flux文生图工作流_1980482521886576641.json, 图片生成/文生图/Flux文生图工作流_1985255145997017090.json, 图片生成/文生图/Flux文生图工作流_2007992047759790082.json, 图片生成/文生图/flux文生图工作流_1980484330449453058.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_44

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/2031276815041433602.json、图片生成/文生图/F1文生图精细调节人像_1924680451447771137.json、图片生成/文生图/FLUX1文生图260814_2088196242147987458.json、图片生成/文生图/FLUX工作流_2106376251710722050.json、图片生成/文生图/Flux文生图+高清放大工作流_1915239700771045377.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 12/13 个有
- `DF_Text_Box` —— 8/13 个有
- `FluxLoraLoader` —— 7/13 个有
- `LoraLoaderModelOnly` —— 5/13 个有
- `JjkText` —— 3/13 个有
- `FluxResolutionNode` —— 1/13 个有
- `PMRF` —— 1/13 个有
- `PortraitMaster_中文版` —— 1/13 个有
- `easy positive` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 1024 | 13 | 86% |
| 高度 | 1024 | 1024 - 1536 | 13 | 80% |
| 采样步数 | 25 | 20 - 30 | 13 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 13 | 0% |
| 采样算法 | dpmpp_2m | - | 13 | 62% |
| 调度器 | sgm_uniform | - | 13 | 62% |
| 重绘幅度 | 1 | 0.8 - 1 | 13 | 95% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 1024，13 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 1024 - 1536，13 个样本
- 采样步数 中位数 25，观测区间 20 - 30，13 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，13 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 dpmpp_2m，13 个样本，一致性 62%
- 调度器 最常用 sgm_uniform，13 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，13 个样本，取值集中（一致性 95%）
