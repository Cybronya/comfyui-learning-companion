---
name: text_to_image_sampler_clip_vae_14
type: Text To Image
frequency: 4
level: strong
coverage: 0.929
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, FluxGuidance, KSampler, NunchakuFluxDiTLoader, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1933900850979102721.json, 图片生成/文生图/1934093892570501121.json, 图片生成/文生图/1935576346364149761.json, 图片生成/文生图/1946446513008730114.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_14

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1933900850979102721.json、图片生成/文生图/1934093892570501121.json、图片生成/文生图/1935576346364149761.json、图片生成/文生图/1946446513008730114.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
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
- `DualCLIPLoader` —— 2/4 个有
- `NunchakuFluxLoraLoader` —— 2/4 个有
- `NunchakuTextEncoderLoader` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `LatentUpscaleBy` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 760 | 576 - 1080 | 4 | 77% |
| 高度 | 1264 | 1024 - 1920 | 4 | 76% |
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta | - | 4 | 50% |
| 重绘幅度 | 1 | 0.5 - 1 | 4 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 760，观测区间 576 - 1080，4 个样本
- 高度 中位数 1264，观测区间 1024 - 1920，4 个样本
- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，4 个样本
