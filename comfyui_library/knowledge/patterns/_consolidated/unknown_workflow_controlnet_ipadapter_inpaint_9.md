---
name: unknown_workflow_controlnet_ipadapter_inpaint_9
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.889
common_nodes: [ACN_AdvancedControlNetApply, AIO_Preprocessor, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, DifferentialDiffusion, GrowMaskWithBlur, IPAdapterAdvanced, IPAdapterUnifiedLoader, InpaintModelConditioning, KSampler, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LayerUtility: CropByMask V2, LayerUtility: ImageScaleRestore V2, LayerUtility: RestoreCropBox, LoadImage, PrepImageForClipVision, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/局部材质转换_1924371194194423810.json, 平台全量/一键局部材质转换_2034542136913301506.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_inpaint_9

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/局部材质转换_1924371194194423810.json、平台全量/一键局部材质转换_2034542136913301506.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `ACN_AdvancedControlNetApply`
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `DifferentialDiffusion`
- `GrowMaskWithBlur`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2Ultra`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `PrepImageForClipVision`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 5 | - | 2 | 100% |
| 采样算法 | dpmpp_sde_gpu | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde_gpu，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
