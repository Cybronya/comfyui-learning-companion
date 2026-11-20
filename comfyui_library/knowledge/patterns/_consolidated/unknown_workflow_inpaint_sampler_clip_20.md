---
name: unknown_workflow_inpaint_sampler_clip_20
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.952556
common_nodes: [BackgroundScaler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, ImageConcanate, ImageToMask, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, PreviewBridge, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageInsetCrop]
problems: []
missing: []
members: [图片生成/图生图/【AI由北】万物迁移 服装通用_1900752010574970881.json, 图片生成/图生图/【AI由北】万物迁移 电商产品通用_1901648013259857922.json, 图片生成/图生图/万物迁移_1922474027976183810.json, 图片生成/图生图/模特+首饰穿戴海报 一键生图系列_1909418174545338370.json, 图片生成/图生图/电商产品-万物迁移-指定场景_1939509036557508610.json, 平台全量/万物迁移 高适配度 不挑图片 电商场景应用_1889261914625859586.json, 平台全量/完美迁移服装 内衣_1910969826045587457.json, 平台全量/新版完美万物迁移，电商专用_1894287413974335489.json, 平台全量/电商-首饰更换_1909427755426193410.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/【AI由北】万物迁移 服装通用_1900752010574970881.json、图片生成/图生图/【AI由北】万物迁移 电商产品通用_1901648013259857922.json、图片生成/图生图/万物迁移_1922474027976183810.json、图片生成/图生图/模特+首饰穿戴海报 一键生图系列_1909418174545338370.json、图片生成/图生图/电商产品-万物迁移-指定场景_1939509036557508610.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `BackgroundScaler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `ImageConcanate`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `PreviewBridge`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageInsetCrop`

**可变部分**（部分 workflow 才有）：
- `InpaintCrop` —— 8/9 个有
- `InpaintStitch` —— 8/9 个有
- `SetNode` —— 6/9 个有
- `GetNode` —— 5/9 个有
- `LayerMask: BiRefNetUltra` —— 5/9 个有
- `LayerMask: BiRefNetUltraV2` —— 4/9 个有
- `LayerMask: LoadBiRefNetModelV2` —— 4/9 个有
- `LayerMask: MaskEdgeUltraDetail V2` —— 4/9 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
