---
name: unknown_workflow_inpaint_sampler_clip_12
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.77525
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), GrowMask, Image Blank, Image Comparer (rgthree), ImageScale, ImageScaleBy, ImageToMask, InpaintModelConditioning, InvertMask, JWImageResizeByLongerSide, JoinImageWithAlpha, KSampler, LayerUtility: ImageBlend V2, LoadImage, MaskToImage, MathExpression|pysssss, PreviewImage, PreviewMask_, SAMLoader, SaveImage, SubtractMask, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/一键生成产品白底图（边缘优化）_2061335000473227265.json, 图片生成/图生图/一键生成白底图_1971815284690644994.json, 图片生成/图生图/一键生成白底图_2003079237118623745.json, 图片生成/图生图/一键生成白底图_2006630796404199425.json, 图片生成/图生图/一键生成白底图（Flux版，边缘优化）-阿浩_2026901259466313730.json, 图片生成/图生图/一键生成白底图（Flux版，边缘优化）_1990626828060680193.json, 图片生成/图生图/一键证照换底色_2013558540216049666.json, 图片生成/图生图/课件13：一键抠图_批量抠图获取白底图_2098532004416548866.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/一键生成产品白底图（边缘优化）_2061335000473227265.json、图片生成/图生图/一键生成白底图_1971815284690644994.json、图片生成/图生图/一键生成白底图_2003079237118623745.json、图片生成/图生图/一键生成白底图_2006630796404199425.json、图片生成/图生图/一键生成白底图（Flux版，边缘优化）-阿浩_2026901259466313730.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMask`
- `Image Blank`
- `Image Comparer (rgthree)`
- `ImageScale`
- `ImageScaleBy`
- `ImageToMask`
- `InpaintModelConditioning`
- `InvertMask`
- `JWImageResizeByLongerSide`
- `JoinImageWithAlpha`
- `KSampler`
- `LayerUtility: ImageBlend V2`
- `LoadImage`
- `MaskToImage`
- `MathExpression|pysssss`
- `PreviewImage`
- `PreviewMask_`
- `SAMLoader`
- `SaveImage`
- `SubtractMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `DF_Text` —— 7/8 个有
- `CR Value` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/8 个有
- `TransparentImage` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | deis | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
