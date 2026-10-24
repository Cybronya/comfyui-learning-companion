---
name: text_to_image_sampler_clip_vae_17
type: Text To Image
frequency: 8
level: strong
coverage: 0.8695
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/16.tonnie-nunchaku文生图_1997621361398976513.json, 图片生成/文生图/FLUX GGUF Q4 更节约显存，出图更快_1829532907324231681.json, 图片生成/文生图/FLUX GGUF Q4_1961449815852957697.json, 图片生成/文生图/FLUX Kontext dev （Nunchaku 极速版）文生图工作流_1946446513008730114.json, 图片生成/文生图/FLUX Kontext 文生图工作流_1946442950954115073.json, 图片生成/文生图/FLUX Nunchaku 5倍噌噌噌加速工作流_1910971389912805378.json, 图片生成/文生图/Flux 文生图+放大_1946760909358555137.json, 图片生成/文生图/nunchaku_flux1对比未加速_2005576570435764226.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_17

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/16.tonnie-nunchaku文生图_1997621361398976513.json、图片生成/文生图/FLUX GGUF Q4 更节约显存，出图更快_1829532907324231681.json、图片生成/文生图/FLUX GGUF Q4_1961449815852957697.json、图片生成/文生图/FLUX Kontext dev （Nunchaku 极速版）文生图工作流_1946446513008730114.json、图片生成/文生图/FLUX Kontext 文生图工作流_1946442950954115073.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 6/8 个有
- `ConditioningZeroOut` —— 5/8 个有
- `NunchakuFluxDiTLoader` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `UNETLoader` —— 4/8 个有
- `DeepTranslatorTextNode` —— 3/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `UnetLoaderGGUF` —— 2/8 个有
- `NunchakuFluxLoraLoader` —— 1/8 个有
- `PMRF` —— 1/8 个有
- `Text Multiline` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 912 | 768 - 1280 | 8 | 82% |
| 高度 | 1136 | 1024 - 1920 | 8 | 76% |
| 采样步数 | 20 | 20 - 25 | 8 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 912，观测区间 768 - 1280，8 个样本，取值集中（一致性 82%）
- 高度 中位数 1136，观测区间 1024 - 1920，8 个样本
- 采样步数 中位数 20，观测区间 20 - 25，8 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
