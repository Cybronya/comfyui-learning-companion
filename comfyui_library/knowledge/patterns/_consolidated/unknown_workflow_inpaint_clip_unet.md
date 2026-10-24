---
name: unknown_workflow_inpaint_clip_unet
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.880353
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, ImageComposite+, InpaintModelConditioning, LayerMask: MaskGrow, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux-fill-Oneward超强扩图(原图无损)_2026103537175896065.json, 图片生成/图生图/Flux-fill-Oneward超强扩图(原图无损)_2087355637641601026.json, 图片生成/图生图/Flux-fill-Oneward超强扩图(原图无损)_2104172855121498114.json, 图片生成/图生图/FluxFillOneward无损扩图-neo和女友_1986903385825808386.json, 图片生成/图生图/ONEREWARD-FILL 扩图 - 接入SD-PPP实现 扩图创成式填充_2073608038434566145.json, 图片生成/图生图/OneReward-Fill-最强无损扩图_1979401617462169601.json, 图片生成/图生图/OneReward-Fill最强效果扩图_2007022422448410626.json, 图片生成/图生图/扩图效果超好的flux-OneReward2.0（加速版）_1986455556615532546.json, 图片生成/图生图/扩图效果超好的flux-OneReward（最新版）_1983317610471288833.json, 图片生成/图生图/扩图效果超好的flux-OneReward（最新版）_2035293357567643649.json, 图片生成/图生图/最新flux-OneReward扩图，效果最强，支持4k_1982007479674519554.json, 图片生成/图生图/最新flux-OneReward扩图，效果最强，支持4k_1983325087451521026.json, 图片生成/图生图/生图-图像扩图-OneReward-Fill_1979568427763404801.json, 图片生成/图生图/简单实用 Flux-fill-Oneward超强扩图(原图无损)_2028739201126109186.json, 图片生成/图生图/👾怪獸-flux-OneReward扩图，效果炸裂👾_1986437994863357953.json, 图片生成/图生图/🤖OneReward-Fill最强扩图【无损原图效果炸裂】_1978711043935457281.json, 图片生成/文生图/OneReward-Fill最强扩图【无损原图效果炸裂】_1990118350430851073.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_clip_unet

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Flux-fill-Oneward超强扩图(原图无损)_2026103537175896065.json、图片生成/图生图/Flux-fill-Oneward超强扩图(原图无损)_2087355637641601026.json、图片生成/图生图/Flux-fill-Oneward超强扩图(原图无损)_2104172855121498114.json、图片生成/图生图/FluxFillOneward无损扩图-neo和女友_1986903385825808386.json、图片生成/图生图/ONEREWARD-FILL 扩图 - 接入SD-PPP实现 扩图创成式填充_2073608038434566145.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `ImageComposite+`
- `InpaintModelConditioning`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 16/17 个有
- `CR Text` —— 12/17 个有
- `ImagePadForOutpaintMasked` —— 12/17 个有
- `KSampler` —— 12/17 个有
- `ImpactInt` —— 11/17 个有
- `PreviewImage` —— 11/17 个有
- `ImagePadForOutpaint` —— 5/17 个有
- `KSamplerAdvanced` —— 5/17 个有
- `LoraLoaderModelOnly` —— 5/17 个有
- `easy ifElse` —— 5/17 个有
- `ImageConcanate` —— 2/17 个有
- `Int` —— 1/17 个有
- `MaskPreview` —— 1/17 个有
- `MaskToImage` —— 1/17 个有
- `Note Plus (mtb)` —— 1/17 个有
- `easy showAnything` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27.5 | 25 - 30 | 12 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 17 | 0% |
| 采样算法 | er_sde | - | 17 | 71% |
| 调度器 | simple | - | 17 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 27.5，观测区间 25 - 30，12 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，17 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 er_sde，17 个样本，一致性 71%
- 调度器 最常用 simple，17 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
