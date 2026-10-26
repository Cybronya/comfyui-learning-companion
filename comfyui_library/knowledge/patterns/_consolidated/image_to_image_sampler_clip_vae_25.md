---
name: image_to_image_sampler_clip_vae_25
type: Image To Image
frequency: 9
level: strong
coverage: 0.95
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/kontext人物_2085922992378441729.json, 图片生成/图生图/kontext人物编辑_2085656932387475457.json, 图片生成/图生图/kontext图片编辑_1943613174111498242.json, 图片生成/图生图/kontext（dev）开源官方版本_1938409745747476482.json, 图片生成/图生图/kontext（dev）开源官方版本（双图）_1938414703502884866.json, 图片生成/图生图/丰乳肥臀工作流_1948441682168676354.json, 图片生成/图生图/文化墙一键生成展示效果图_2039158309990699009.json, 图片生成/图生图/文化墙设计图一键应用墙体展示效果_1948774790761984001.json, 图片生成/图生图/简易Kontext Dev （nunchaku加速）_1938911346601680897.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_25

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/kontext人物_2085922992378441729.json、图片生成/图生图/kontext人物编辑_2085656932387475457.json、图片生成/图生图/kontext图片编辑_1943613174111498242.json、图片生成/图生图/kontext（dev）开源官方版本_1938409745747476482.json、图片生成/图生图/kontext（dev）开源官方版本（双图）_1938414703502884866.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 8/9 个有
- `VAELoader` —— 8/9 个有
- `ImageStitch` —— 6/9 个有
- `NunchakuFluxDiTLoader` —— 6/9 个有
- `NunchakuFluxLoraLoader` —— 6/9 个有
- `UNETLoader` —— 5/9 个有
- `RH_Translator` —— 4/9 个有
- `PreviewImage` —— 3/9 个有
- `Text Multiline` —— 3/9 个有
- `LoadLatentEXR` —— 2/9 个有
- `SaveLatent` —— 2/9 个有
- `ttN text` —— 2/9 个有
- `AV_VAELoader` —— 1/9 个有
- `GoogleTranslator` —— 1/9 个有
- `ShowText|pysssss` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 28 | 9 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 28，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
