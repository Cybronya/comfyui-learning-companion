---
name: text_to_image_lora_sampler_clip_508
type: Text To Image
frequency: 3
level: strong
coverage: 0.946667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, RH_Translator, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext-图案提取_1948678862908588034.json, 图片生成/图生图/KontextNunchakuDevInpainting头发变金色_1944280237490442241.json, 图片生成/图生图/KontextNunchakuDevInpainting换成剃须刀_1944997524240523265.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_508

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Kontext-图案提取_1948678862908588034.json、图片生成/图生图/KontextNunchakuDevInpainting头发变金色_1944280237490442241.json、图片生成/图生图/KontextNunchakuDevInpainting换成剃须刀_1944997524240523265.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Kontext Inpainting Conditioning` —— 2/3 个有
- `ModelSamplingFlux` —— 2/3 个有
- `NunchakuFluxDiTLoader` —— 2/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `JjkShowText` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `Text Find and Replace` —— 1/3 个有
- `TextInput_` —— 1/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1248 | 3 | 90% |
| 高度 | 1536 | 832 - 1536 | 3 | 74% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1248，3 个样本，取值集中（一致性 90%）
- 高度 中位数 1536，观测区间 832 - 1536，3 个样本
