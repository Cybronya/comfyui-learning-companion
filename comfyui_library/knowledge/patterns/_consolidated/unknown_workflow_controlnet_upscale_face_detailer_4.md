---
name: unknown_workflow_controlnet_upscale_face_detailer_4
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7012
common_nodes: [ApplyPulidFlux, CLIPTextEncode, CR Text, ControlNetLoader, DualCLIPLoader, EmptySD3LatentImage, FaceDetailerPipe, FluxGuidance, ImageCrop, ImageScale, KSampler, LayerUtility: TextJoin, LoadImage, ModelSamplingFlux, PreviewImage, PulidFluxModelLoader, SaveImage, SetUnionControlNetType, ToDetailerPipe, UNETLoader, UltimateSDUpscale, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAELoader, easy seed]
problems: []
missing: []
members: [图片生成/图生图/人物一致性_1956372749646266370.json, 图片生成/图生图/人物多角度多表情 一键生成工作流_1932747727384317954.json, 图片生成/图生图/人物多角度多表情 一键生成工作流_1933846307452968962.json, 平台全量/CG迷-人物多角度多表情一键生成工作流_1927336141895131137.json, 平台全量/人物多角度多表情_2000842031490625538.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_face_detailer_4

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/人物一致性_1956372749646266370.json、图片生成/图生图/人物多角度多表情 一键生成工作流_1932747727384317954.json、图片生成/图生图/人物多角度多表情 一键生成工作流_1933846307452968962.json、平台全量/CG迷-人物多角度多表情一键生成工作流_1927336141895131137.json、平台全量/人物多角度多表情_2000842031490625538.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 5 个 workflow 都包含：
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `CR Text`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FaceDetailerPipe`
- `FluxGuidance`
- `ImageCrop`
- `ImageScale`
- `KSampler`
- `LayerUtility: TextJoin`
- `LoadImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `PulidFluxModelLoader`
- `SaveImage`
- `SetUnionControlNetType`
- `ToDetailerPipe`
- `UNETLoader`
- `UltimateSDUpscale`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 4/5 个有
- `ControlNetApplySD3` —— 4/5 个有
- `ExpressionEditor` —— 4/5 个有
- `Int Literal` —— 4/5 个有
- `LoraLoader` —— 4/5 个有
- `PulidFluxEvaClipLoader` —— 4/5 个有
- `PulidFluxInsightFaceLoader` —— 4/5 个有
- `easy int` —— 4/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `ControlNetApplyAdvanced` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `Int` —— 1/5 个有
- `PulidEvaClipLoader` —— 1/5 个有
- `PulidInsightFaceLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | 0.8 - 0.8 | 5 | 100% |
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | deis | - | 5 | 80% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.8，观测区间 0.8 - 0.8，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
