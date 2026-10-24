---
name: unknown_workflow_controlnet_upscale_latent_upscale_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9065
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, ImageScale, KSampler, LatentUpscaleBy, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SetUnionControlNetType, Text Concatenate (JPS), TextInput_, UNETLoader, VAEDecode, VAELoader, easy imageSize, easy imageSplitGrid, easy imagesSplitImage]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物一致性套图工作流一次4张（自动裁剪）_1923967592342745089.json, 图片生成/文生图/角色+姿势一致性_1901843149637967873.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_latent_upscale_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/人物一致性套图工作流一次4张（自动裁剪）_1923967592342745089.json、图片生成/文生图/角色+姿势一致性_1901843149637967873.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `ImageScale`
- `KSampler`
- `LatentUpscaleBy`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `Text Concatenate (JPS)`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`
- `easy imageSplitGrid`
- `easy imagesSplitImage`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `ApplyPulidFlux` —— 1/2 个有
- `FaceAnalysisModels` —— 1/2 个有
- `FaceBoundingBox` —— 1/2 个有
- `FaceDetailer` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `PulidFluxEvaClipLoader` —— 1/2 个有
- `PulidFluxInsightFaceLoader` —— 1/2 个有
- `PulidFluxModelLoader` —— 1/2 个有
- `SAMLoader` —— 1/2 个有
- `SUPIR_Upscale` —— 1/2 个有
- `UltralyticsDetectorProvider` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.65 | - | 2 | 92% |
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.75 | - | 2 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.65，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.75，样本不足，未给区间，2 个样本
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
