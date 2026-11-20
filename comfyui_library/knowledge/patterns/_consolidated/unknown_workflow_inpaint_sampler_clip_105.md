---
name: unknown_workflow_inpaint_sampler_clip_105
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7985
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, GrowMask, INPAINT_ApplyFooocusInpaint, INPAINT_InpaintWithModel, INPAINT_LoadFooocusInpaint, INPAINT_LoadInpaintModel, INPAINT_VAEEncodeInpaintConditioning, Image Comparer (rgthree), ImageCompositeMasked, Joy_caption_two, Joy_caption_two_load, KSampler (Efficient), LayerMask: MaskGrow, LoadImage, Mask Fill Holes, PreviewImage, SaveImage, Seed_, ShowText|pysssss]
problems: []
missing: []
members: [图片生成/图生图/【CQ808】物体消除，去水印_2011400025540141057.json, 平台全量/物体消除_2051134212018843649.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_105

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【CQ808】物体消除，去水印_2011400025540141057.json、平台全量/物体消除_2051134212018843649.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `GrowMask`
- `INPAINT_ApplyFooocusInpaint`
- `INPAINT_InpaintWithModel`
- `INPAINT_LoadFooocusInpaint`
- `INPAINT_LoadInpaintModel`
- `INPAINT_VAEEncodeInpaintConditioning`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler (Efficient)`
- `LayerMask: MaskGrow`
- `LoadImage`
- `Mask Fill Holes`
- `PreviewImage`
- `SaveImage`
- `Seed_`
- `ShowText|pysssss`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 100% |
| 采样算法 | dpmpp_sde_gpu | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde_gpu，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
