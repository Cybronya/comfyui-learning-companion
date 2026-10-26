---
name: image_to_image_lora_sampler_clip_73
type: Image To Image
frequency: 4
level: weak
coverage: 0.97925
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/kontext放大图片工作流_1967790948103127042.json, 图片生成/图生图/生图-图片移除字幕-kontext_nunchaku_1972652889376268289.json, 图片生成/图生图/穆寒_2072683428708966401.json, 图片生成/文生图/Flux Kontext扩展画布【入档】_2111193679372312578.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_73

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/kontext放大图片工作流_1967790948103127042.json、图片生成/图生图/生图-图片移除字幕-kontext_nunchaku_1972652889376268289.json、图片生成/图生图/穆寒_2072683428708966401.json、图片生成/文生图/Flux Kontext扩展画布【入档】_2111193679372312578.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `ReferenceLatent` —— 3/4 个有
- `FluxKontextImageScale` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `CR Upscale Image` —— 1/4 个有
- `Color (hexadecimal)` —— 1/4 个有
- `JWInteger` —— 1/4 个有
- `LayerUtility: ExtendCanvas` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `ShowText` —— 1/4 个有
- `WD14Tagger|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 8 - 4.9468e+14 | 4 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 0.4 - 1 | 4 | 69% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 8 - 4.9468e+14，4 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，4 个样本
- 风险：采样步数 观测到 4.9468e+14，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
