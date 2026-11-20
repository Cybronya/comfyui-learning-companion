---
name: text_to_image_face_detailer_sampler_clip
type: Text To Image
frequency: 4
level: strong
coverage: 0.824
common_nodes: [CFGZeroStar, CLIPLoader, CLIPTextEncode, DetailerForEach, DifferentialDiffusion, EditDetailerPipe, EmptyLatentImage, FaceDetailerPipe, Fast Groups Bypasser (rgthree), ImageResizeKJv2, ImpactSwitch, ImpactWildcardProcessor, KSampler, LoadImage, MaskToSEGS, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, SAMLoader, SaveImage, SolidMask, ToDetailerPipe, UNETLoader, UltralyticsDetectorProvider, VAEDecode, VAEEncode, VAELoader, easy int]
problems: []
missing: []
members: [图片生成/图生图/AnimaBasic_2114887714398105602.json, 图片生成/文生图/AnimaBasic_2107472171026173954.json, 图片生成/文生图/AnimaBasic_2109180267482140673.json, 平台全量/Anima basic V5全能版 脸部修复 + 手部修复等_2061722128055103490.json]
source: knowledge_consolidation
---

# text_to_image_face_detailer_sampler_clip

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/AnimaBasic_2114887714398105602.json、图片生成/文生图/AnimaBasic_2107472171026173954.json、图片生成/文生图/AnimaBasic_2109180267482140673.json、平台全量/Anima basic V5全能版 脸部修复 + 手部修复等_2061722128055103490.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `DetailerForEach`
- `DifferentialDiffusion`
- `EditDetailerPipe`
- `EmptyLatentImage`
- `FaceDetailerPipe`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `ImpactWildcardProcessor`
- `KSampler`
- `LoadImage`
- `MaskToSEGS`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SAMLoader`
- `SaveImage`
- `SolidMask`
- `ToDetailerPipe`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `SeedNode` —— 3/4 个有
- `easy hiresFix` —— 3/4 个有
- `CR Upscale Image` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 2/4 个有
- `easy anythingIndexSwitch` —— 2/4 个有
- `Lora Loader Stack (rgthree)` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
