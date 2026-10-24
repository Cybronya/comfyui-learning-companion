---
name: image_to_image_lora_sampler_clip_55
type: Image To Image
frequency: 5
level: strong
coverage: 0.8502
common_nodes: [CLIPTextEncode, FluxGuidance, Image Comparer (rgthree), KSampler, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, PreviewImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Kontext 双图融合_1963833858867302402.json, 图片生成/图生图/kontext飞机场平胸变大胸_1949076513116303361.json, 图片生成/图生图/kontext，自动打光融图，加速版_1961256097522892801.json, 图片生成/图生图/去水印去车标v1.1_1963490714858524673.json, 图片生成/文生图/去水印、图案、文字，高清修复 (1)_1963133559307472898.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_55

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Kontext 双图融合_1963833858867302402.json、图片生成/图生图/kontext飞机场平胸变大胸_1949076513116303361.json、图片生成/图生图/kontext，自动打光融图，加速版_1961256097522892801.json、图片生成/图生图/去水印去车标v1.1_1963490714858524673.json、图片生成/文生图/去水印、图案、文字，高清修复 (1)_1963133559307472898.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
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
- `ImageStitch` —— 4/5 个有
- `Anything Everywhere3` —— 3/5 个有
- `LayerColor: BrightnessContrastV2` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `LoadImageOutput` —— 1/5 个有
- `NunchakuTextEncoderLoader` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `TextInput_` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 25 | 5 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 25，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
