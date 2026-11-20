---
name: image_to_image_inpaint_sampler_clip_15
type: Image To Image
frequency: 2
level: weak
coverage: 0.85
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, INPAINT_ApplyFooocusInpaint, INPAINT_InpaintWithModel, INPAINT_LoadFooocusInpaint, INPAINT_LoadInpaintModel, INPAINT_VAEEncodeInpaintConditioning, ImagePadForOutpaint, InpaintModelConditioning, KSampler, LoadImage, PreviewImage, SaveImage, SetLatentNoiseMask, VAEDecode, VAEEncode, VAEEncodeForInpaint]
problems: []
missing: []
members: [图片生成/图生图/局部重绘（大全）_1946045276593287170.json, 平台全量/局部重绘（大全）_2018151409727840257.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_clip_15

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/局部重绘（大全）_1946045276593287170.json、平台全量/局部重绘（大全）_2018151409727840257.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `INPAINT_ApplyFooocusInpaint`
- `INPAINT_InpaintWithModel`
- `INPAINT_LoadFooocusInpaint`
- `INPAINT_LoadInpaintModel`
- `INPAINT_VAEEncodeInpaintConditioning`
- `ImagePadForOutpaint`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SetLatentNoiseMask`
- `VAEDecode`
- `VAEEncode`
- `VAEEncodeForInpaint`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 26 | - | 2 | 77% |
| Prompt 约束强度(CFG) | 7.5 | - | 2 | 93% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 26，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 7.5，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
