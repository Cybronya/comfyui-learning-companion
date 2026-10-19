---
name: text_to_image_sampler_clip_checkpoint_8
type: Text To Image
frequency: 8
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/1965622186373468162.json, 图片生成/文生图/1967328708090531841.json, 图片生成/文生图/1967812820442165249.json, 图片生成/文生图/1968316592289394689.json, 图片生成/文生图/1969281537156018177.json, 图片生成/文生图/1969418975585202177.json, 图片生成/文生图/1970171244836515841.json, 图片生成/文生图/1970301959590866945.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_8

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1965622186373468162.json、图片生成/文生图/1967328708090531841.json、图片生成/文生图/1967812820442165249.json、图片生成/文生图/1968316592289394689.json、图片生成/文生图/1969281537156018177.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 2/8 个有
- `FaceRestoreCFWithModel` —— 1/8 个有
- `FaceRestoreModelLoader` —— 1/8 个有
- `UNETLoader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 1024 | 8 | 87% |
| 高度 | 1024 | 1024 - 1024 | 8 | 100% |
| 采样步数 | 20 | 20 - 20 | 8 | 100% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 8 | 48% |
| 采样算法 | dpmpp_2m_sde | - | 8 | 62% |
| 调度器 | karras | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 1024，8 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 1024 - 1024，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，8 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 dpmpp_2m_sde，8 个样本，一致性 62%
- 调度器 最常用 karras，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
