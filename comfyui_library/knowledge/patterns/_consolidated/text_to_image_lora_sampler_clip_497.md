---
name: text_to_image_lora_sampler_clip_497
type: Text To Image
frequency: 3
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, EmptyLatentImage, ImageScaleDownToSize, KSampler, LoadImage, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/洗图 nunchaku Krea_1951260996935561218.json, 图片生成/图生图/精美图生图_2052188655065812993.json, 图片生成/图生图/脸部参考生图nunchaku+Krea_1951640241826377729.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_497

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/洗图 nunchaku Krea_1951260996935561218.json、图片生成/图生图/精美图生图_2052188655065812993.json、图片生成/图生图/脸部参考生图nunchaku+Krea_1951640241826377729.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageScaleDownToSize`
- `KSampler`
- `LoadImage`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 2/3 个有
- `ReduxAdvanced` —— 2/3 个有
- `StyleModelLoader` —— 2/3 个有
- `NunchakuPulidApply` —— 1/3 个有
- `NunchakuPulidLoader` —— 1/3 个有
- `RH_Translator` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 15 - 20 | 3 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 720 | 720 - 1024 | 3 | 83% |
| 高度 | 1280 | 1024 - 1280 | 3 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 15 - 20，3 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 720，观测区间 720 - 1024，3 个样本，取值集中（一致性 83%）
- 高度 中位数 1280，观测区间 1024 - 1280，3 个样本，取值集中（一致性 90%）
