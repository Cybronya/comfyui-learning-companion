---
name: unknown_workflow_inpaint_sampler_clip_102
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6815
common_nodes: [ApplyFBCacheOnModel, CLIPTextEncode, CR Text, DualCLIPLoader, Image Comparer (rgthree), ImageResize+, InpaintModelConditioning, KSampler, LoadImage, RepeatLatentBatch, SaveImage, UNETLoader, VAEDecode, VAELoader, easy int]
problems: []
missing: []
members: [图片生成/图生图/fill(OneReward)图像修复、修手、修脸_1996607262741381121.json, 平台全量/010.修手_2004642447777038338.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_102

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/fill(OneReward)图像修复、修手、修脸_1996607262741381121.json、平台全量/010.修手_2004642447777038338.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFBCacheOnModel`
- `CLIPTextEncode`
- `CR Text`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `RepeatLatentBatch`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `LayerMask: LoadSAM2Model` —— 1/2 个有
- `LayerMask: ObjectDetectorYOLO8` —— 1/2 个有
- `LayerMask: SAM2UltraV2` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有
- `MaskPreview` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ResizeMask` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 31.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.675 | - | 2 | 52% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 31.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.675，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
