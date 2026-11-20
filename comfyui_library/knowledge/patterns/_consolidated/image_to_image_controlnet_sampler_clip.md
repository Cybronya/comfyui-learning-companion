---
name: image_to_image_controlnet_sampler_clip
type: Image To Image
frequency: 12
level: strong
coverage: 0.886
common_nodes: [ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ChinesePrompt_Mix, ColorMatch, ControlNetLoader, CropFace, GroundingDinoModelLoader (segment anything2), GroundingDinoSAM2Segment (segment anything2), ImageBatch, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: MaskGrow, LoadImage, MaskPreview+, SAM2ModelLoader (segment anything2), SaveImage, SetLatentNoiseMask, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/极简快速换脸工作流 -instantID 换脸_1890344487271440385.json, 图片生成/图生图/极简快速换脸工作流 -instantID 换脸_2058516000424943618.json, 图片生成/图生图/极简快速换脸工作流 -instantID 换脸_2058525567506542593.json, 图片生成/图生图/极简快速换脸工作流 -instantID 换脸_2058531037537456130.json, 图片生成/图生图/极简快速换脸工作流 -instantID 换脸_2058535700001284098.json, 图片生成/图生图/极简快速换脸工作流 -instantID 换脸_2058539303722119169.json, 图片生成/图生图/极简快速换脸工作流 -instantID 换脸_2058541112536682497.json, 图片生成/图生图/极简快速换脸工作流 -instantID 换脸_2058541488895774721.json, 图片生成/图生图/极简快速换脸工作流 -instantID 换脸_2068983092467036161.json, 图片生成/图生图/极简快速换脸工作流 -instantID 换脸_2070797757035663361.json, 图片生成/图生图/极简快速换脸工作流 -instantID 换脸_2070798111320137730.json, 图片生成/文生图/极简快速换脸工作流_1935315293751136257.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/极简快速换脸工作流 -instantID 换脸_1890344487271440385.json、图片生成/图生图/极简快速换脸工作流 -instantID 换脸_2058516000424943618.json、图片生成/图生图/极简快速换脸工作流 -instantID 换脸_2058525567506542593.json、图片生成/图生图/极简快速换脸工作流 -instantID 换脸_2058531037537456130.json、图片生成/图生图/极简快速换脸工作流 -instantID 换脸_2058535700001284098.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ChinesePrompt_Mix`
- `ColorMatch`
- `ControlNetLoader`
- `CropFace`
- `GroundingDinoModelLoader (segment anything2)`
- `GroundingDinoSAM2Segment (segment anything2)`
- `ImageBatch`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: MaskGrow`
- `LoadImage`
- `MaskPreview+`
- `SAM2ModelLoader (segment anything2)`
- `SaveImage`
- `SetLatentNoiseMask`
- `VAEDecode`
- `VAEEncode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | euler_ancestral | - | 12 | 100% |
| 调度器 | sgm_uniform | - | 12 | 100% |
| 重绘幅度 | 0.34 | 0.34 - 0.34 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，12 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，12 个样本，一致性 100%
- 重绘幅度 中位数 0.34，观测区间 0.34 - 0.34，12 个样本，取值集中（一致性 100%）
