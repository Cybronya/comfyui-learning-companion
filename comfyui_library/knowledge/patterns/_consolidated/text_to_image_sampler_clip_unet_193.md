---
name: text_to_image_sampler_clip_unet_193
type: Text To Image
frequency: 3
level: strong
coverage: 0.974333
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/longCat-基础文生图_2028462654980886530.json, 图片生成/文生图/longCat-自动文生图_2028819655418187778.json, 图片生成/文生图/longcat-image_2028365950126395393.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_193

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/longCat-基础文生图_2028462654980886530.json、图片生成/文生图/longCat-自动文生图_2028819655418187778.json、图片生成/文生图/longcat-image_2028365950126395393.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/3 个有
- `ApplySageAttention` —— 1/3 个有
- `Int` —— 1/3 个有
- `JDCN_StringToList` —— 1/3 个有
- `ModelSamplingFlux` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta57 | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 904 | 904 - 1024 | 3 | 94% |
| 高度 | 1280 | 1024 - 1280 | 3 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta57，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 904，观测区间 904 - 1024，3 个样本，取值集中（一致性 94%）
- 高度 中位数 1280，观测区间 1024 - 1280，3 个样本，取值集中（一致性 90%）
