---
name: unknown_workflow_inpaint_lora_sampler_120
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.769
common_nodes: [Anything Everywhere3, CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, Cut By Mask, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, GrowMask, ImageConcanate, ImageInvert, ImageToMask, InpaintModelConditioning, KSampler, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskToImage, PreviewImage, ReduxAdvanced, SaveImage, ShowText|pysssss, String, StyleModelLoader, Text Concatenate, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/【万能迁移】Redux-Ace++产品迁移_1907688209579405313.json, 平台全量/万能迁移Redux-Ace++工作流V1_1890735884956999681.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_120

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/【万能迁移】Redux-Ace++产品迁移_1907688209579405313.json、平台全量/万能迁移Redux-Ace++工作流V1_1890735884956999681.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `Cut By Mask`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `GrowMask`
- `ImageConcanate`
- `ImageInvert`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `String`
- `StyleModelLoader`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `Image Compare (mtb)` —— 1/2 个有
- `Joy_caption_two` —— 1/2 个有
- `Joy_caption_two_load` —— 1/2 个有
- `LayerMask: LoadFlorence2Model` —— 1/2 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
