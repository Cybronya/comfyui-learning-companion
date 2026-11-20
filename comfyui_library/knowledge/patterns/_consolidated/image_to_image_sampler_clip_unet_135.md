---
name: image_to_image_sampler_clip_unet_135
type: Image To Image
frequency: 3
level: strong
coverage: 0.936667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageStitch, KSampler, LoadImage, ReferenceLatent, SaveImage, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext 老年的你_1947231811882655745.json, 图片生成/图生图/Kontext 老年的你_1976488006263640065.json, 图片生成/图生图/flux kontext 三联图_1939285901316956162.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_135

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Kontext 老年的你_1947231811882655745.json、图片生成/图生图/Kontext 老年的你_1976488006263640065.json、图片生成/图生图/flux kontext 三联图_1939285901316956162.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DF_Integer` —— 2/3 个有
- `Int2String` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `StringReplace` —— 2/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `Get Image Size` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `easy imageScaleDownBy` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | ddim | - | 3 | 67% |
| 调度器 | ddim_uniform | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ddim，3 个样本，一致性 67%
- 调度器 最常用 ddim_uniform，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
