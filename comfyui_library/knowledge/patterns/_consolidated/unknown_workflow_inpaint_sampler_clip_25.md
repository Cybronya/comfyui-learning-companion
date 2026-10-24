---
name: unknown_workflow_inpaint_sampler_clip_25
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.655
common_nodes: [Anything Everywhere, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, GetNode, ImageCrop, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, NunchakuFluxDiTLoader, PreviewImage, SaveImage, SetNode, StyleModelApply, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Redux+Fill换脸  效果一般  学习用_1920489532666613762.json, 图片生成/图生图/基于redux和fill的换装应用，自动蒙版_1930542132845793282.json, 图片生成/图生图/指定模特极速换装 Redux+Fill+Nunchaku_1919742744103948289.json, 图片生成/图生图/换装  万物迁移   超快速超自然_1917413045331759105.json, 图片生成/图生图/超自然换装  自动蒙版  Redux+Fill+Nunchaku_1917538234497437697.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_25

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Redux+Fill换脸  效果一般  学习用_1920489532666613762.json、图片生成/图生图/基于redux和fill的换装应用，自动蒙版_1930542132845793282.json、图片生成/图生图/指定模特极速换装 Redux+Fill+Nunchaku_1919742744103948289.json、图片生成/图生图/换装  万物迁移   超快速超自然_1917413045331759105.json、图片生成/图生图/超自然换装  自动蒙版  Redux+Fill+Nunchaku_1917538234497437697.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `ImageCrop`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RMBG` —— 4/5 个有
- `EmptyImage` —— 3/5 个有
- `ImageConcanate` —— 3/5 个有
- `ImageToMask` —— 3/5 个有
- `LayerMask: PersonMaskUltra V2` —— 3/5 个有
- `workflow>遮罩到图像` —— 3/5 个有
- `LayerMask: MaskPreview` —— 2/5 个有
- `easy makeImageForICLora` —— 2/5 个有
- `BodySegment` —— 1/5 个有
- `FaceAnalysisModels` —— 1/5 个有
- `FaceBoundingBox` —— 1/5 个有
- `ImageAndMaskPreview` —— 1/5 个有
- `Segment` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
