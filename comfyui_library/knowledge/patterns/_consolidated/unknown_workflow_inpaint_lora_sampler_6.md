---
name: unknown_workflow_inpaint_lora_sampler_6
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9477
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageCrop, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Mask Fill Holes, ReduxAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy makeImageForICLora]
problems: []
missing: []
members: [图片生成/图生图/Flux Fill+Redux 万物迁移（电商场景图制作）_2032340529047937025.json, 图片生成/图生图/产品图自由搭配AI模特_2002714024217309186.json, 图片生成/图生图/产品换背景 电商必备场景图制作_2008829886869282817.json, 图片生成/图生图/电商场景图制作（产品换背景）_1985610476090535937.json, 图片生成/图生图/电商场景图制作（产品换背景）_1990675120790396929.json, 图片生成/图生图/给产品自由搭配模特工作流_1990696481466322945.json, 图片生成/图生图/给产品自由搭配模特工作流_2097866694432739329.json, 图片生成/图生图/给产品自由搭配模特工作流_2099406218531004418.json, 图片生成/图生图/课件14：电商实战：产品换背景（上）_2098602158307500034.json, 图片生成/图生图/课件16：电商实战：给产品自由搭配Ai模特_2098948233119756290.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_6

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Flux Fill+Redux 万物迁移（电商场景图制作）_2032340529047937025.json、图片生成/图生图/产品图自由搭配AI模特_2002714024217309186.json、图片生成/图生图/产品换背景 电商必备场景图制作_2008829886869282817.json、图片生成/图生图/电商场景图制作（产品换背景）_1985610476090535937.json、图片生成/图生图/电商场景图制作（产品换背景）_1990675120790396929.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageCrop`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Mask Fill Holes`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `PMRF` —— 3/10 个有
- `LayerMask: MaskGrow` —— 1/10 个有
- `LayerMask: MaskPreview` —— 1/10 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/10 个有
- `LoraLoader` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 25 | 25 - 25 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
