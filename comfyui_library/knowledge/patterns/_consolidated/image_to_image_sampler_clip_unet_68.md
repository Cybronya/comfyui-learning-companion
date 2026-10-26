---
name: image_to_image_sampler_clip_unet_68
type: Image To Image
frequency: 6
level: strong
coverage: 0.980333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, RH_Translator, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux Kontext Dev三图编辑_1940692934268448770.json, 图片生成/图生图/Flux Kontext Dev光线变换+放大_1939254602929774593.json, 图片生成/图生图/Flux Kontext Dev单图风格转绘及放大修复_1938565629152518145.json, 图片生成/图生图/Flux Kontext Dev卡通变真人加速版+放大（单图）_1939950003525689345.json, 图片生成/图生图/Flux Kontext Dev双图风格参考迁移+放大_1938914168588455937.json, 图片生成/图生图/Flux Kontext Dev双图风格参考迁移及放大修复_1938567521966415873.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_68

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux Kontext Dev三图编辑_1940692934268448770.json、图片生成/图生图/Flux Kontext Dev光线变换+放大_1939254602929774593.json、图片生成/图生图/Flux Kontext Dev单图风格转绘及放大修复_1938565629152518145.json、图片生成/图生图/Flux Kontext Dev卡通变真人加速版+放大（单图）_1939950003525689345.json、图片生成/图生图/Flux Kontext Dev双图风格参考迁移+放大_1938914168588455937.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 5/6 个有
- `ImageConcatMulti` —— 5/6 个有
- `PMRF` —— 5/6 个有
- `Text Multiline` —— 5/6 个有
- `ImageStitch` —— 4/6 个有
- `ShowText|pysssss` —— 2/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `DF_Get_image_size` —— 1/6 个有
- `ImageCrop+` —— 1/6 个有
- `ImagePadForOutpaint` —— 1/6 个有
- `JWInteger` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `NunchakuFluxDiTLoader` —— 1/6 个有
- `NunchakuFluxLoraLoader` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `TextInputBasic` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 6 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
