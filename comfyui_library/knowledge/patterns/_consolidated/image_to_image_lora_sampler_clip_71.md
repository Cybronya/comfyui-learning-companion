---
name: image_to_image_lora_sampler_clip_71
type: Image To Image
frequency: 5
level: strong
coverage: 0.9262
common_nodes: [CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, PMRF, ReferenceLatent, SaveImage, TeaCache, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/A-Flux Kontext Dev-邮票风格加速版+放大_1948559228809150466.json, 图片生成/图生图/Calligrapher图片文字修改_1944016181684502530.json, 图片生成/图生图/Calligrapher文字编辑+自引用+手动蒙版+Kontext修复_1949047873560879105.json, 图片生成/图生图/Calligrapher海报文字修改多步kontext修复版V1_1943973001291268097.json, 平台全量/PosterCraft海报封面生成+自动修改文字为中文-Calligrapher_1948677558505209857.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_71

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/A-Flux Kontext Dev-邮票风格加速版+放大_1948559228809150466.json、图片生成/图生图/Calligrapher图片文字修改_1944016181684502530.json、图片生成/图生图/Calligrapher文字编辑+自引用+手动蒙版+Kontext修复_1949047873560879105.json、图片生成/图生图/Calligrapher海报文字修改多步kontext修复版V1_1943973001291268097.json、平台全量/PosterCraft海报封面生成+自动修改文字为中文-Calligrapher_1948677558505209857.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
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
- `CalligrapherBlockSwap` —— 4/5 个有
- `CalligrapherImageProcesssor` —— 4/5 个有
- `CalligrapherLora` —— 4/5 个有
- `CalligrapherModelLoader` —— 4/5 个有
- `CalligrapherSampler` —— 4/5 个有
- `GrowMaskWithBlur` —— 4/5 个有
- `ImageResizeKJ` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `LayerUtility: PurgeVRAM` —— 4/5 个有
- `MaskToImage` —— 4/5 个有
- `PDIMAGE_LongerSize` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `ImageConcanate` —— 3/5 个有
- `ImageStitch` —— 3/5 个有
- `LayerUtility: PurgeVRAM V2` —— 3/5 个有
- `NunchakuFluxDiTLoader` —— 3/5 个有
- `NunchakuFluxLoraLoader` —— 3/5 个有
- `RH_Translator` —— 3/5 个有
- `GoogleTranslateTextNode` —— 2/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `UNETLoader` —— 2/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `GroupExecutorSender` —— 1/5 个有
- `GroupExecutorSingle` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `LoadImageOutput` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `RH_Prompter` —— 1/5 个有
- `RunningHub PosterCraft Pipeline` —— 1/5 个有
- `RunningHub PosterCraft Sampler` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `easy showAnything` —— 1/5 个有
- `ttN concat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 5 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
