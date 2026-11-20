---
name: unknown_workflow_controlnet_inpaint_sampler_16
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.88
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CLIPVisionLoader, CR Model Input Switch, ControlNetApplySD3, ControlNetLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GrowMask, ImageToMask, ImpactSwitch, InpaintModelConditioning, JanusImageUnderstanding, JanusModelLoader, KSampler, LayerMask: MaskPreview, LayerMask: MaskStroke, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, ModelMergeSimple, ReduxAdvanced, ResizeMask, SaveImage, SetUnionControlNetType, ShowText|pysssss, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/[人物精准换装]服装材质纹理迁移_1968504844363411458.json, 平台全量/服装材质纹理迁移_1927286651146424322.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/[人物精准换装]服装材质纹理迁移_1968504844363411458.json、平台全量/服装材质纹理迁移_1927286651146424322.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Model Input Switch`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMask`
- `ImageToMask`
- `ImpactSwitch`
- `InpaintModelConditioning`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerMask: MaskStroke`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelMergeSimple`
- `ReduxAdvanced`
- `ResizeMask`
- `SaveImage`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ArgosTranslateTextNode` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.6 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
