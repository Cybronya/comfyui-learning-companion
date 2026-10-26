---
name: unknown_workflow_inpaint_sampler_clip_75
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.862
common_nodes: [Anything Everywhere, CLIPTextEncode, CheckpointLoaderSimple, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, Florence2Run, Florence2toCoordinates, GrowMask, Image Comparer (rgthree), ImageScaleToTotalPixels, InpaintModelConditioning, KSampler, LayerMask: MaskPreview, LoadImage, MaskFix+, Sam2Segmentation, SaveImage, SubtractMask, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/将普通人转换肌肉发达的身体_1905656574654730241.json, 图片生成/图生图/秒变肌肉健身爱好者，效果超赞_1938230916852420610.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_75

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/将普通人转换肌肉发达的身体_1905656574654730241.json、图片生成/图生图/秒变肌肉健身爱好者，效果超赞_1938230916852420610.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `Florence2Run`
- `Florence2toCoordinates`
- `GrowMask`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskPreview`
- `LoadImage`
- `MaskFix+`
- `Sam2Segmentation`
- `SaveImage`
- `SubtractMask`
- `VAEDecode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | dpmpp_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.5 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
