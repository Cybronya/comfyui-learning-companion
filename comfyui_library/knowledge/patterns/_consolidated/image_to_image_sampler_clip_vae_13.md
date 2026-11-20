---
name: image_to_image_sampler_clip_vae_13
type: Image To Image
frequency: 17
level: strong
coverage: 0.961294
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, NunchakuFluxDiTLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/kontext 手拿产品姿势生成_1976644315327893505.json, 图片生成/图生图/kontextNunchakuDev转绘像素艺术_1940592142769352705.json, 图片生成/图生图/kontextNunchakuDev转绘元素艺术_1940607114458935297.json, 图片生成/图生图/kontextNunchakuDev转绘动态插画_1940603858894696450.json, 图片生成/图生图/kontextNunchakuDev转绘古代插画_1940610524772200450.json, 图片生成/图生图/kontextNunchakuDev转绘史诗电影风格_1940597701073416194.json, 图片生成/图生图/kontextNunchakuDev转绘折纸艺术_1940246673190993921.json, 图片生成/图生图/kontextNunchakuDev转绘空间艺术_1940609295543332866.json, 图片生成/图生图/kontextNunchakuDev转绘纹理艺术_1940594910586187778.json, 图片生成/图生图/kontextNunchakuDev转绘艺术视觉风格_1940599249056985089.json, 图片生成/图生图/kontextNunchakuDev转绘超现实主义绘画风格_1940601783699877890.json, 图片生成/图生图/kontextNunchakuDev转绘遗忘艺术家作品_1940605971251048449.json, 图片生成/图生图/kontextnunchakudevlora全能图片G4o同款icon头像_1943141910594666498.json, 图片生成/图生图/kontext飞机场平胸变大胸_1949076513116303361.json, 图片生成/图生图/kontext，自动打光融图，加速版_1961256097522892801.json, 图片生成/图生图/去水印去车标v1.1_1963490714858524673.json, 图片生成/文生图/去水印、图案、文字，高清修复 (1)_1963133559307472898.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_13

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/kontext 手拿产品姿势生成_1976644315327893505.json、图片生成/图生图/kontextNunchakuDev转绘像素艺术_1940592142769352705.json、图片生成/图生图/kontextNunchakuDev转绘元素艺术_1940607114458935297.json、图片生成/图生图/kontextNunchakuDev转绘动态插画_1940603858894696450.json、图片生成/图生图/kontextNunchakuDev转绘古代插画_1940610524772200450.json…）

- **类型**：Image To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 16/17 个有
- `RH_Translator` —— 14/17 个有
- `ModelSamplingFlux` —— 12/17 个有
- `NunchakuFluxLoraLoader` —— 5/17 个有
- `PreviewImage` —— 5/17 个有
- `Image Comparer (rgthree)` —— 4/17 个有
- `Anything Everywhere3` —— 3/17 个有
- `ImageStitch` —— 3/17 个有
- `LayerColor: BrightnessContrastV2` —— 2/17 个有
- `LayerUtility: PurgeVRAM V2` —— 2/17 个有
- `TextInput_` —— 2/17 个有
- `CR Text Concatenate` —— 1/17 个有
- `ImageBBoxOverlayByMask` —— 1/17 个有
- `LoadImageOutput` —— 1/17 个有
- `LoraLoaderModelOnly` —— 1/17 个有
- `ShowText|pysssss` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 25 | 17 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 17 | 100% |
| 采样算法 | euler | - | 17 | 100% |
| 调度器 | simple | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 25，17 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，17 个样本，一致性 100%
- 调度器 最常用 simple，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
