---
name: image_to_image_sampler_clip_vae_36
type: Image To Image
frequency: 5
level: strong
coverage: 0.8836
common_nodes: [CLIPTextEncode, FluxGuidance, ImageStitch, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext 双图融合_1963833858867302402.json, 图片生成/图生图/Nunchaku-FLUX加速改图_1942403095311626241.json, 图片生成/图生图/kontext _ 基础开源版_1938657888149950466.json, 图片生成/图生图/kontext dev系列-黑红剪影风转绘_1945695804692811778.json, 图片生成/图生图/kontext_全能精修丨产品精修丨人像精修丨婚纱照精修全能精修V1_1947931579113975809.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_36

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Kontext 双图融合_1963833858867302402.json、图片生成/图生图/Nunchaku-FLUX加速改图_1942403095311626241.json、图片生成/图生图/kontext _ 基础开源版_1938657888149950466.json、图片生成/图生图/kontext dev系列-黑红剪影风转绘_1945695804692811778.json、图片生成/图生图/kontext_全能精修丨产品精修丨人像精修丨婚纱照精修全能精修V1_1947931579113975809.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `FluxGuidance`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `DualCLIPLoader` —— 4/5 个有
- `FluxKontextImageScale` —— 4/5 个有
- `NunchakuFluxDiTLoader` —— 3/5 个有
- `RH_Translator` —— 3/5 个有
- `UNETLoader` —— 3/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `NunchakuFluxLoraLoader` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `NunchakuTextEncoderLoader` —— 1/5 个有
- `easy promptConcat` —— 1/5 个有
- `easy textSwitch` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 12 - 20 | 5 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 12 - 20，5 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
