---
name: unknown_workflow_inpaint_sampler_clip_61
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.87
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, MaskPreview+, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux全自动修手_1950826620573646850.json, 平台全量/AI一键消除工作流_1970897389135532034.json, 平台全量/flux局部重绘优化工作流_1922532226523873282.json, 数字人/数字人/flux局部重绘优化工作流-许老师专用_1981627396023558146.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_61

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/flux全自动修手_1950826620573646850.json、平台全量/AI一键消除工作流_1970897389135532034.json、平台全量/flux局部重绘优化工作流_1922532226523873282.json、数字人/数字人/flux局部重绘优化工作流-许老师专用_1981627396023558146.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `MaskPreview+`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `InpaintCrop` —— 3/4 个有
- `InpaintStitch` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `DeepTranslatorTextNode` —— 2/4 个有
- `GrowMask` —— 2/4 个有
- `ImpactGaussianBlurMask` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `DeepTranslatorCLIPTextEncodeNode` —— 1/4 个有
- `GroundingDinoModelLoader (segment anything)` —— 1/4 个有
- `GroundingDinoSAM2Segment (segment anything2)` —— 1/4 个有
- `ImageCompositeMasked` —— 1/4 个有
- `SAM2ModelLoader (segment anything2)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 20 | 4 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 0.9 | - | 2 | 89% |
| LoRA 文本强度 | 0.95 | - | 2 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 0.95，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
