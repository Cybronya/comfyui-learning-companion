---
name: text_to_image_sampler_clip_unet_50
type: Text To Image
frequency: 12
level: moderate
coverage: 0.993583
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/2031276815041433602.json, 图片生成/文生图/F1文生图精细调节人像_1924680451447771137.json, 图片生成/文生图/FLUX1文生图260814_2088196242147987458.json, 图片生成/文生图/FLUX工作流_2106376251710722050.json, 图片生成/文生图/Flux文生图+高清放大工作流_1915239700771045377.json, 图片生成/文生图/Flux文生图工作流_1912760478278348801.json, 图片生成/文生图/Flux文生图工作流_1980482521886576641.json, 图片生成/文生图/Flux文生图工作流_1985255145997017090.json, 图片生成/文生图/Flux文生图工作流_2007992047759790082.json, 图片生成/文生图/Flux文生图工作流（带lora版）_2084186114449043458.json, 图片生成/文生图/flux+lora出图_1901871929287188482.json, 图片生成/文生图/flux文生图工作流_1980484330449453058.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_50

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/2031276815041433602.json、图片生成/文生图/F1文生图精细调节人像_1924680451447771137.json、图片生成/文生图/FLUX1文生图260814_2088196242147987458.json、图片生成/文生图/FLUX工作流_2106376251710722050.json、图片生成/文生图/Flux文生图+高清放大工作流_1915239700771045377.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 11/12 个有
- `DF_Text_Box` —— 9/12 个有
- `FluxLoraLoader` —— 7/12 个有
- `LoraLoaderModelOnly` —— 4/12 个有
- `FluxResolutionNode` —— 1/12 个有
- `PMRF` —— 1/12 个有
- `PortraitMaster_中文版` —— 1/12 个有
- `easy positive` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 1024 | 12 | 88% |
| 高度 | 1024 | 1024 - 1536 | 12 | 83% |
| 采样步数 | 25 | 20 - 30 | 12 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 12 | 0% |
| 采样算法 | dpmpp_2m | - | 12 | 75% |
| 调度器 | sgm_uniform | - | 12 | 75% |
| 重绘幅度 | 1 | 0.8 - 1 | 12 | 94% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 1024，12 个样本，取值集中（一致性 88%）
- 高度 中位数 1024，观测区间 1024 - 1536，12 个样本，取值集中（一致性 83%）
- 采样步数 中位数 25，观测区间 20 - 30，12 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，12 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 dpmpp_2m，12 个样本，一致性 75%
- 调度器 最常用 sgm_uniform，12 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，12 个样本，取值集中（一致性 94%）
