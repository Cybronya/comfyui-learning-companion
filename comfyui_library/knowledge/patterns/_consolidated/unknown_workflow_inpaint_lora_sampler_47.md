---
name: unknown_workflow_inpaint_lora_sampler_47
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.89875
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CropFace, GrowMaskWithBlur, ImageCrop+, ImpactSimpleDetectorSEGS, InpaintModelConditioning, KSampler, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ReduxAdvanced, SAMLoader, SaveImage, SegsToCombinedMask, StyleModelLoader, UNETLoader, UltralyticsDetectorProvider, VAEDecode, easy makeImageForICLora]
problems: []
missing: []
members: [平台全量/FLUX-FILL模型+ACE++通过手动调整头部位置实现单人换场景_1915927724114771969.json, 平台全量/人像一致性切换景别切换姿势工作流（FIll+ace+拼图方案）_1922907436259184641.json, 平台全量/人像一致性切换景别切换姿势工作流（FIll+ace+拼图方案）_1948199221659860993.json, 平台全量/镜头切换器-面部0改变！_1917462403636989954.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_47

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/FLUX-FILL模型+ACE++通过手动调整头部位置实现单人换场景_1915927724114771969.json、平台全量/人像一致性切换景别切换姿势工作流（FIll+ace+拼图方案）_1922907436259184641.json、平台全量/人像一致性切换景别切换姿势工作流（FIll+ace+拼图方案）_1948199221659860993.json、平台全量/镜头切换器-面部0改变！_1917462403636989954.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CropFace`
- `GrowMaskWithBlur`
- `ImageCrop+`
- `ImpactSimpleDetectorSEGS`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReduxAdvanced`
- `SAMLoader`
- `SaveImage`
- `SegsToCombinedMask`
- `StyleModelLoader`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 3/4 个有
- `FluxGuidance` —— 3/4 个有
- `CLIPVisionEncode` —— 2/4 个有
- `Compositor3` —— 2/4 个有
- `CompositorConfig3` —— 2/4 个有
- `DualCLIPLoader` —— 2/4 个有
- `FastCanvas` —— 2/4 个有
- `FastCanvasTool` —— 2/4 个有
- `LayerUtility: CropByMask V2` —— 2/4 个有
- `RHHiddenNodes` —— 2/4 个有
- `RMBG` —— 2/4 个有
- `StyleModelApply` —— 2/4 个有
- `VAELoader` —— 2/4 个有
- `easy imageSize` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | 20 - 25 | 4 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，观测区间 20 - 25，4 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
