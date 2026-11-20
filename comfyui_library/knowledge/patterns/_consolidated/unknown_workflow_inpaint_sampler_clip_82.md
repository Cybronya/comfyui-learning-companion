---
name: unknown_workflow_inpaint_sampler_clip_82
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.858333
common_nodes: [CLIPTextEncode, INPAINT_ApplyFooocusInpaint, INPAINT_InpaintWithModel, INPAINT_LoadFooocusInpaint, INPAINT_LoadInpaintModel, INPAINT_VAEEncodeInpaintConditioning, Image Comparer (rgthree), KSampler, LoadImage, Mask Fill Holes, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/SDXL FOOOCUS万物移除_1906693436093739010.json, 平台全量/fooocus 万物移除_1976915984865005569.json, 平台全量/万物移除工作流【AI小王子】_1912781551359459330.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_82

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/SDXL FOOOCUS万物移除_1906693436093739010.json、平台全量/fooocus 万物移除_1976915984865005569.json、平台全量/万物移除工作流【AI小王子】_1912781551359459330.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `INPAINT_ApplyFooocusInpaint`
- `INPAINT_InpaintWithModel`
- `INPAINT_LoadFooocusInpaint`
- `INPAINT_LoadInpaintModel`
- `INPAINT_VAEEncodeInpaintConditioning`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `Mask Fill Holes`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `BlendInpaint` —— 2/3 个有
- `CheckpointLoader|pysssss` —— 2/3 个有
- `CutForInpaint` —— 2/3 个有
- `GrowMask` —— 2/3 个有
- `Joy_caption_two` —— 2/3 个有
- `Joy_caption_two_load` —— 2/3 个有
- `MaskToImage` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 28 - 30 | 3 | 97% |
| Prompt 约束强度(CFG) | 5 | 1 - 5 | 3 | 49% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 3 | 67% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 0.75 | 0.75 - 1 | 3 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 28 - 30，3 个样本，取值集中（一致性 97%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 5，3 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 dpmpp_2m_sde_gpu，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 0.75，观测区间 0.75 - 1，3 个样本，取值集中（一致性 86%）
