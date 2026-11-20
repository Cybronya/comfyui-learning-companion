---
name: image_to_image_sampler_clip_unet_147
type: Image To Image
frequency: 4
level: strong
coverage: 0.92875
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageStitch, KSampler, LoadImage, ReferenceLatent, SaveImage, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext 老年的你_1947231811882655745.json, 图片生成/图生图/Kontext 老年的你_1976488006263640065.json, 图片生成/图生图/flux kontext 三联图_1939285901316956162.json, 平台全量/老年面相_Kontext-DEV-LORA_1946483155244052482.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_147

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Kontext 老年的你_1947231811882655745.json、图片生成/图生图/Kontext 老年的你_1976488006263640065.json、图片生成/图生图/flux kontext 三联图_1939285901316956162.json、平台全量/老年面相_Kontext-DEV-LORA_1946483155244052482.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
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
- `DF_Integer` —— 3/4 个有
- `Int2String` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `StringReplace` —— 3/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `Get Image Size` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `easy imageScaleDownBy` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | ddim | - | 4 | 75% |
| 调度器 | ddim_uniform | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ddim，4 个样本，一致性 75%
- 调度器 最常用 ddim_uniform，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
