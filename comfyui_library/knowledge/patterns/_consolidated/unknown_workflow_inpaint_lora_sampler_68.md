---
name: unknown_workflow_inpaint_lora_sampler_68
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.796
common_nodes: [CLIPTextEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, ImageConcanate, ImageResizeKJ, ImageToMask, ImitationHueNode, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerMask: PersonMaskUltra V2, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskToImage, PreviewImage, ReduxAdvanced, SaveImage, ShowText|pysssss, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageInsetCrop]
problems: []
missing: []
members: [图片生成/图生图/最强换脸型修改版_1914200514878238722.json, 图片生成/图生图/最强换脸！可换脸型！redux联动ace++_1915384122922176514.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_68

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/最强换脸型修改版_1914200514878238722.json、图片生成/图生图/最强换脸！可换脸型！redux联动ace++_1915384122922176514.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `ImageConcanate`
- `ImageResizeKJ`
- `ImageToMask`
- `ImitationHueNode`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskToImage`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageInsetCrop`

**可变部分**（部分 workflow 才有）：
- `ETN_Translate` —— 1/2 个有
- `GoogleTranslateTextNode` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `PreviewBridge` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25.5 | - | 2 | 98% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25.5，样本不足，未给区间，2 个样本，取值集中（一致性 98%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
