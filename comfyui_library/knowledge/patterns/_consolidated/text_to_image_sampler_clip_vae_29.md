---
name: text_to_image_sampler_clip_vae_29
type: Text To Image
frequency: 4
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/洗图 nunchaku Krea_1951260996935561218.json, 图片生成/图生图/精美图生图_2052188655065812993.json, 图片生成/图生图/脸部参考生图nunchaku+Krea_1951640241826377729.json, 平台全量/最快nunchaku-redux洗图_1939321483166457857.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_29

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/洗图 nunchaku Krea_1951260996935561218.json、图片生成/图生图/精美图生图_2052188655065812993.json、图片生成/图生图/脸部参考生图nunchaku+Krea_1951640241826377729.json、平台全量/最快nunchaku-redux洗图_1939321483166457857.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 3/4 个有
- `ImageScaleDownToSize` —— 3/4 个有
- `NunchakuFluxLoraLoader` —— 3/4 个有
- `ReduxAdvanced` —— 3/4 个有
- `StyleModelLoader` —— 3/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `FluxGuidance` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `NunchakuPulidApply` —— 1/4 个有
- `NunchakuPulidLoader` —— 1/4 个有
- `RH_Translator` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 15 - 25 | 4 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 720 | 512 - 1024 | 4 | 75% |
| 高度 | 1152 | 512 - 1280 | 4 | 69% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 15 - 25，4 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 720，观测区间 512 - 1024，4 个样本
- 高度 中位数 1152，观测区间 512 - 1280，4 个样本
