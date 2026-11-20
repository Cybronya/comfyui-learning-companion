---
name: image_to_image_lora_sampler_clip_123
type: Image To Image
frequency: 4
level: strong
coverage: 0.87325
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageStitch, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, ReferenceLatent, SaveImage, Text Concatenate, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/flux_kontext_dev后视图+拆分_1995728587342876674.json, 平台全量/flux_kontext_dev角色坐下_1995734206581968897.json, 平台全量/flux_kontext_dev角色坐下拆分_1995739173308993538.json, 平台全量/角色拆分工作流v1_1946837637396066306.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_123

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/flux_kontext_dev后视图+拆分_1995728587342876674.json、平台全量/flux_kontext_dev角色坐下_1995734206581968897.json、平台全量/flux_kontext_dev角色坐下拆分_1995739173308993538.json、平台全量/角色拆分工作流v1_1946837637396066306.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

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
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `ReferenceLatent`
- `SaveImage`
- `Text Concatenate`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UnetLoaderGGUF` —— 3/4 个有
- `EmptySD3LatentImage` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Preview Chooser` —— 1/4 个有
- `UltimateSDUpscale` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | 20 - 25 | 4 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，观测区间 20 - 25，4 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
