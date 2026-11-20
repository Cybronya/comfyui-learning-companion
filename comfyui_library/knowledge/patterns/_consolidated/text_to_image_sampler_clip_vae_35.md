---
name: text_to_image_sampler_clip_vae_35
type: Text To Image
frequency: 3
level: strong
coverage: 0.951333
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, ReduxAdvanced, SaveImage, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/【阡陌】Nunchaku 加速flux  redux单图_多图风格参考_1951230291157393409.json, 平台全量/【阡陌】flux Krea redux单图_多图风格参考_1951535055288086529.json, 平台全量/宠物照转毛绒玩具_1940306986649174018.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_35

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/【阡陌】Nunchaku 加速flux  redux单图_多图风格参考_1951230291157393409.json、平台全量/【阡陌】flux Krea redux单图_多图风格参考_1951535055288086529.json、平台全量/宠物照转毛绒玩具_1940306986649174018.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 2/3 个有
- `DifferentialDiffusion` —— 2/3 个有
- `DualCLIPLoader` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `AutoDownloadBiRefNetModel` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `NunchakuFluxDiTLoader` —— 1/3 个有
- `NunchakuTextEncoderLoaderV2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RembgByBiRefNet` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 3 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 768 - 1024 | 3 | 87% |
| 高度 | 1024 | 1024 - 1536 | 3 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1024，3 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 1024 - 1536，3 个样本
