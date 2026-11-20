---
name: image_to_image_sampler_clip_vae_20
type: Image To Image
frequency: 11
level: moderate
coverage: 0.939545
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Kontext-三视图_1938913966724669442.json, 图片生成/图生图/Kontext-动漫人物转绘_1940651426446209025.json, 图片生成/图生图/Kontext-本地版-中文输入_1962530753999450114.json, 图片生成/图生图/KontextDev转绘JOJO动画风格_1942013323561037825.json, 图片生成/图生图/KontextDev转绘美漫风格_1942043248150134785.json, 图片生成/图生图/Kontext【一键3D转2D】欧卡风_1979193772133224449.json, 图片生成/图生图/Kontext人物 苹果 EMoji 风格_1948220912014372865.json, 图片生成/图生图/Kontext改单图 - Nunchaku 加速_1954810310865633282.json, 图片生成/图生图/kontext（开源版）实现重打光效果，不改变人物动作场景_1938433384328921090.json, 图片生成/图生图/基础kontext工作流_2005321098000560130.json, 图片生成/图生图/真人转水彩画风格 - Kontext 一键转绘_1945351279969488898.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_20

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Kontext-三视图_1938913966724669442.json、图片生成/图生图/Kontext-动漫人物转绘_1940651426446209025.json、图片生成/图生图/Kontext-本地版-中文输入_1962530753999450114.json、图片生成/图生图/KontextDev转绘JOJO动画风格_1942013323561037825.json、图片生成/图生图/KontextDev转绘美漫风格_1942043248150134785.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 10/11 个有
- `UNETLoader` —— 9/11 个有
- `FluxKontextImageScale` —— 6/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/11 个有
- `Image Comparer (rgthree)` —— 5/11 个有
- `LoraLoaderModelOnly` —— 5/11 个有
- `ShowText|pysssss` —— 5/11 个有
- `easy imageConcat` —— 4/11 个有
- `EmptySD3LatentImage` —— 2/11 个有
- `LayerUtility: ImageMaskScaleAs` —— 2/11 个有
- `NunchakuFluxDiTLoader` —— 2/11 个有
- `ImageConcanate` —— 1/11 个有
- `ImageResize+` —— 1/11 个有
- `LayerUtility: PurgeVRAM` —— 1/11 个有
- `LoraLoader` —— 1/11 个有
- `Text Multiline` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 25 | 11 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 11 | 62% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 0.8 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 25，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
