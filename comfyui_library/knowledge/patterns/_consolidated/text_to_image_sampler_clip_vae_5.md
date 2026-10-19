---
name: text_to_image_sampler_clip_vae_5
type: Text To Image
frequency: 3
level: moderate
coverage: 0.956667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, FluxGuidance, KSampler, NunchakuFluxDiTLoader, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1933900850979102721.json, 图片生成/文生图/1934093892570501121.json, 图片生成/文生图/1935576346364149761.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1933900850979102721.json、图片生成/文生图/1934093892570501121.json、图片生成/文生图/1935576346364149761.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `NunchakuFluxDiTLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `NunchakuFluxLoraLoader` —— 2/3 个有
- `NunchakuTextEncoderLoader` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `LatentUpscaleBy` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 576 - 1080 | 3 | 73% |
| 高度 | 1280 | 1024 - 1920 | 3 | 73% |
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 0.5 - 1 | 3 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 720，观测区间 576 - 1080，3 个样本
- 高度 中位数 1280，观测区间 1024 - 1920，3 个样本
- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，3 个样本
