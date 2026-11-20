---
name: text_to_image_sampler_clip_vae_14
type: Text To Image
frequency: 8
level: strong
coverage: 0.901875
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/16.tonnie-nunchaku文生图_1997621361398976513.json, 图片生成/文生图/FLUX 2 文生图_1993572229503975426.json, 图片生成/文生图/FLUX 2 电商文生图场景图_2043508628937777153.json, 图片生成/文生图/FLUX Kontext dev （Nunchaku 极速版）文生图工作流_1946446513008730114.json, 图片生成/文生图/FLUX Kontext 文生图工作流_1946442950954115073.json, 图片生成/文生图/FLUX Nunchaku 5倍噌噌噌加速工作流_1910971389912805378.json, 图片生成/文生图/Flux 文生图+放大_1946760909358555137.json, 图片生成/文生图/宝宝版 文生图_2009166166715011074.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_14

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/16.tonnie-nunchaku文生图_1997621361398976513.json、图片生成/文生图/FLUX 2 文生图_1993572229503975426.json、图片生成/文生图/FLUX 2 电商文生图场景图_2043508628937777153.json、图片生成/文生图/FLUX Kontext dev （Nunchaku 极速版）文生图工作流_1946446513008730114.json、图片生成/文生图/FLUX Kontext 文生图工作流_1946442950954115073.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/8 个有
- `DualCLIPLoader` —— 6/8 个有
- `FluxGuidance` —— 6/8 个有
- `UNETLoader` —— 6/8 个有
- `DeepTranslatorTextNode` —— 4/8 个有
- `NunchakuFluxDiTLoader` —— 4/8 个有
- `CLIPLoader` —— 3/8 个有
- `PreviewImage` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `PMRF` —— 1/8 个有
- `Text Multiline` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 800 - 1504 | 8 | 79% |
| 高度 | 1392 | 504 - 1920 | 8 | 68% |
| 采样步数 | 20 | 10 - 25 | 8 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 800 - 1504，8 个样本
- 高度 中位数 1392，观测区间 504 - 1920，8 个样本
- 采样步数 中位数 20，观测区间 10 - 25，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
