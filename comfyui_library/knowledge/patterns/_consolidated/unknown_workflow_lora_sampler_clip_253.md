---
name: unknown_workflow_lora_sampler_clip_253
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8275
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyHiDreamO1LatentImage, GetImageSize, GetNode, HiDreamO1ReferenceImages, ImageResizeKJv2, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelNoiseScale, ModelSamplingSD3, PreviewImage, SaveImage, SetNode, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/Hi-dreame O1-multiple-多图编辑工作流_2059997542808637442.json, 图片生成/图生图/Hidream O1-Edit-image-双图编辑（图生图）工作流_2059989511886688258.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_253

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Hi-dreame O1-multiple-多图编辑工作流_2059997542808637442.json、图片生成/图生图/Hidream O1-Edit-image-双图编辑（图生图）工作流_2059989511886688258.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `EmptyHiDreamO1LatentImage`
- `GetImageSize`
- `GetNode`
- `HiDreamO1ReferenceImages`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelNoiseScale`
- `ModelSamplingSD3`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 50% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
