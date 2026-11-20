---
name: unknown_workflow_inpaint_lora_sampler_65
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.809667
common_nodes: [CLIPTextEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, ImageConcanate, ImageResizeKJ, ImageToMask, ImitationHueNode, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerMask: PersonMaskUltra V2, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskToImage, PreviewImage, ReduxAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageInsetCrop]
problems: []
missing: []
members: [图片生成/图生图/最强换脸型修改版_1914200514878238722.json, 图片生成/图生图/最强换脸！可换脸型！redux联动ace++_1915384122922176514.json, 平台全量/最强换脸！可换脸型！redux联动ace++_1904222500413415425.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_65

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/最强换脸型修改版_1914200514878238722.json、图片生成/图生图/最强换脸！可换脸型！redux联动ace++_1915384122922176514.json、平台全量/最强换脸！可换脸型！redux联动ace++_1904222500413415425.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
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
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageInsetCrop`

**可变部分**（部分 workflow 才有）：
- `MaskPreview+` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `ETN_Translate` —— 1/3 个有
- `GoogleTranslateTextNode` —— 1/3 个有
- `PreviewBridge` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 26 | 3 | 98% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 26，3 个样本，取值集中（一致性 98%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
