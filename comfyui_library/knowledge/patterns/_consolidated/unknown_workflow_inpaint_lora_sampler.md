---
name: unknown_workflow_inpaint_lora_sampler
type: Unknown Workflow
frequency: 28
level: strong
coverage: 0.9475
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageCrop, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Mask Fill Holes, ReduxAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy makeImageForICLora]
problems: []
missing: []
members: [图片生成/图生图/Flux Fill+Redux 万物迁移（电商场景图制作）_2032340529047937025.json, 图片生成/图生图/产品图自由搭配AI模特_2002714024217309186.json, 图片生成/图生图/产品换背景 电商必备场景图制作_2008829886869282817.json, 图片生成/图生图/电商场景图制作（产品换背景）_1985610476090535937.json, 图片生成/图生图/电商场景图制作（产品换背景）_1990675120790396929.json, 图片生成/图生图/给产品自由搭配模特工作流_1990696481466322945.json, 图片生成/图生图/给产品自由搭配模特工作流_2097866694432739329.json, 图片生成/图生图/给产品自由搭配模特工作流_2099406218531004418.json, 图片生成/图生图/给产品自由搭配模特工作流_2113775096480489474.json, 图片生成/图生图/给产品自由搭配模特工作流_2113812192247242754.json, 图片生成/图生图/课件14：电商实战：产品换背景（上）_2098602158307500034.json, 图片生成/图生图/课件16：电商实战：给产品自由搭配Ai模特_2098948233119756290.json, 平台全量/Fill One reward万物迁移工作流_1966520903217688578.json, 平台全量/flux万物迁移工作流_1925026865587941378.json, 平台全量/产品图自由搭配AI模特_1985639211757907969.json, 平台全量/产品图自由搭配AI模特_2008008715085029377.json, 平台全量/产品自由搭配AI模特_2061373111307689985.json, 平台全量/产品自由搭配模特工作流_1980486106070302721.json, 平台全量/工作流进阶功能篇3-Flux Fill+Redux 万物迁移（电商场景图制作）_2036340650806874113.json, 平台全量/工作流项目篇6-电商场景图制作(产品换背景)_2016447728728940546.json, 平台全量/工作流项目篇8-产品图自由搭配A模特_2016698045294977026.json, 平台全量/更新_电商场景图制作（自动扣遮罩版）_2031636571551698946.json, 平台全量/更新_电商场景图制作（超强万物迁移）_2031634203158257665.json, 平台全量/电商产品+模特图制作_1945812265616502786.json, 平台全量/电商产品换背景_2061369989797601281.json, 平台全量/电商场景图制作（产品换背景）_1945772310512988162.json, 平台全量/电商场景图制作（产品换背景）_1980431566117777410.json, 平台全量/给产品自由搭配模特工作流_1955443305347780609.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/图生图/Flux Fill+Redux 万物迁移（电商场景图制作）_2032340529047937025.json、图片生成/图生图/产品图自由搭配AI模特_2002714024217309186.json、图片生成/图生图/产品换背景 电商必备场景图制作_2008829886869282817.json、图片生成/图生图/电商场景图制作（产品换背景）_1985610476090535937.json、图片生成/图生图/电商场景图制作（产品换背景）_1990675120790396929.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 28 个 workflow 都包含：
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
- `PMRF` —— 6/28 个有
- `LoraLoader` —— 4/28 个有
- `LayerMask: MaskGrow` —— 3/28 个有
- `LayerMask: MaskPreview` —— 3/28 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/28 个有
- `EmptyImage` —— 2/28 个有
- `PreviewImage` —— 2/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 采样步数 | 25 | 25 - 25 | 28 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 28 | 100% |
| 采样算法 | euler | - | 28 | 100% |
| 调度器 | beta | - | 28 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 28 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，28 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，28 个样本，一致性 100%
- 调度器 最常用 beta，28 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
