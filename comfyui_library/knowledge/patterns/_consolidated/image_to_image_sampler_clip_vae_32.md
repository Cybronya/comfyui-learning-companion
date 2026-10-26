---
name: image_to_image_sampler_clip_vae_32
type: Image To Image
frequency: 6
level: strong
coverage: 0.944833
common_nodes: [AddLabel, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, GetImageSize, ImageBatch, ImageConcatFromBatch, ImpactStringSelector, KSampler, LoadImage, MathExpression|pysssss, NunchakuFluxDiTLoader, ReferenceLatent, SaveImage, StringConcatenate, VAEDecode, VAEEncode, VAELoader, easy compare, easy forLoopEnd, easy forLoopStart, easy ifElse, easy int]
problems: []
missing: []
members: [图片生成/图生图/22种图片风格化—批量出图_2045107973403447297.json, 图片生成/图生图/22种图片风格化—批量出图_2097862226160996354.json, 图片生成/图生图/22种图片风格化—批量出图_2099403929837723650.json, 图片生成/图生图/Flux Kontext批量出图_1943350529701388290.json, 图片生成/图生图/Flux Kontext批量出图_2054081574500610049.json, 图片生成/图生图/抽出线稿_1952570846181298177.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_32

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/22种图片风格化—批量出图_2045107973403447297.json、图片生成/图生图/22种图片风格化—批量出图_2097862226160996354.json、图片生成/图生图/22种图片风格化—批量出图_2099403929837723650.json、图片生成/图生图/Flux Kontext批量出图_1943350529701388290.json、图片生成/图生图/Flux Kontext批量出图_2054081574500610049.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `AddLabel`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetImageSize`
- `ImageBatch`
- `ImageConcatFromBatch`
- `ImpactStringSelector`
- `KSampler`
- `LoadImage`
- `MathExpression|pysssss`
- `NunchakuFluxDiTLoader`
- `ReferenceLatent`
- `SaveImage`
- `StringConcatenate`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy compare`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `AddWater_MarkNode` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
