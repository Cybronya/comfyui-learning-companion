---
name: image_to_image_lora_sampler_clip_129
type: Image To Image
frequency: 3
level: strong
coverage: 0.917333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, GoogleTranslateTextNode, KSampler, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, PreviewImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Kontext LORA训练对比工作流_1941711270368460801.json, 图片生成/图生图/Kontext扩图（扩下半身）_1968240084396978177.json, 数字人/数字人/01.Flux Kontext 人物方向调整_许老师专用_1976297487822622721.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_129

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Kontext LORA训练对比工作流_1941711270368460801.json、图片生成/图生图/Kontext扩图（扩下半身）_1968240084396978177.json、数字人/数字人/01.Flux Kontext 人物方向调整_许老师专用_1976297487822622721.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GoogleTranslateTextNode`
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
- `CR Prompt Text` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `ImageStitch` —— 2/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `Image Rembg (Remove Background)` —— 1/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `LoadImageOutput` —— 1/3 个有
- `easy seed` —— 1/3 个有
- `workflow>MaskColor` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
