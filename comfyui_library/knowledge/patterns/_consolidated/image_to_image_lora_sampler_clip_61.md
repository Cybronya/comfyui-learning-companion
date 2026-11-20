---
name: image_to_image_lora_sampler_clip_61
type: Image To Image
frequency: 4
level: strong
coverage: 0.92575
common_nodes: [CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, PMRF, ReferenceLatent, SaveImage, TeaCache, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/A-Flux Kontext Dev-邮票风格加速版+放大_1948559228809150466.json, 图片生成/图生图/Calligrapher图片文字修改_1944016181684502530.json, 图片生成/图生图/Calligrapher文字编辑+自引用+手动蒙版+Kontext修复_1949047873560879105.json, 图片生成/图生图/Calligrapher海报文字修改多步kontext修复版V1_1943973001291268097.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_61

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/A-Flux Kontext Dev-邮票风格加速版+放大_1948559228809150466.json、图片生成/图生图/Calligrapher图片文字修改_1944016181684502530.json、图片生成/图生图/Calligrapher文字编辑+自引用+手动蒙版+Kontext修复_1949047873560879105.json、图片生成/图生图/Calligrapher海报文字修改多步kontext修复版V1_1943973001291268097.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PMRF`
- `ReferenceLatent`
- `SaveImage`
- `TeaCache`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CalligrapherBlockSwap` —— 3/4 个有
- `CalligrapherImageProcesssor` —— 3/4 个有
- `CalligrapherLora` —— 3/4 个有
- `CalligrapherModelLoader` —— 3/4 个有
- `CalligrapherSampler` —— 3/4 个有
- `GrowMaskWithBlur` —— 3/4 个有
- `ImageResizeKJ` —— 3/4 个有
- `ImageStitch` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `MaskToImage` —— 3/4 个有
- `PDIMAGE_LongerSize` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `GoogleTranslateTextNode` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `NunchakuFluxDiTLoader` —— 2/4 个有
- `NunchakuFluxLoraLoader` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `LoadImageOutput` —— 1/4 个有
- `Text Multiline` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 20 | 4 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
