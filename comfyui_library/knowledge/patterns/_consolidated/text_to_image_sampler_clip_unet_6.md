---
name: text_to_image_sampler_clip_unet_6
type: Text To Image
frequency: 9
level: moderate
coverage: 0.942556
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [PortraitMaster_中文版, easy positive]
members: [图片生成/文生图/1912760478278348801.json, 图片生成/文生图/1915239700771045377.json, 图片生成/文生图/1924680451447771137.json, 图片生成/文生图/1980482521886576641.json, 图片生成/文生图/1980484330449453058.json, 图片生成/文生图/1984195134919163905.json, 图片生成/文生图/1984209491019317249.json, 图片生成/文生图/1984613779646398466.json, 图片生成/文生图/FLUX工作流_2106376251710722050.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_6

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1912760478278348801.json、图片生成/文生图/1915239700771045377.json、图片生成/文生图/1924680451447771137.json、图片生成/文生图/1980482521886576641.json、图片生成/文生图/1980484330449453058.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 8/9 个有
- `DF_Text_Box` —— 7/9 个有
- `FluxLoraLoader` —— 5/9 个有
- `Image Comparer (rgthree)` —— 3/9 个有
- `LoraLoader` —— 3/9 个有
- `PMRF` —— 1/9 个有
- `PortraitMaster_中文版` —— 1/9 个有
- `easy positive` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 1024 | 9 | 88% |
| 高度 | 1024 | 1024 - 1536 | 9 | 82% |
| 采样步数 | 25 | 20 - 30 | 9 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 9 | 0% |
| 采样算法 | dpmpp_2m | - | 9 | 78% |
| 调度器 | sgm_uniform | - | 9 | 78% |
| 重绘幅度 | 1 | 0.8 - 1 | 9 | 94% |
| LoRA 模型强度 | 0.8 | 0.6 - 1 | 3 | 80% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 1024，9 个样本，取值集中（一致性 88%）
- 高度 中位数 1024，观测区间 1024 - 1536，9 个样本，取值集中（一致性 82%）
- 采样步数 中位数 25，观测区间 20 - 30，9 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，9 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 dpmpp_2m，9 个样本，一致性 78%
- 调度器 最常用 sgm_uniform，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，9 个样本，取值集中（一致性 94%）
- LoRA 模型强度 中位数 0.8，观测区间 0.6 - 1，3 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：PortraitMaster_中文版、easy positive
