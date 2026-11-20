---
name: unknown_workflow_controlnet_lora_clip_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.857
common_nodes: [ApplyInstantID, CLIPTextEncode, CannyEdgePreprocessor, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DenoiseSchedulerDetailerHookProvider, DetailerForEachDebugPipe, FaceKeypointsPreprocessor, Image Comparer (rgthree), ImageResize, ImpactSEGSOrderedFilter, ImpactSimpleDetectorSEGS, InstantIDFaceAnalysis, InstantIDModelLoader, LoadImage, LoraLoader, PreviewImage, ReActorFaceSwap, ReActorMaskHelper, RescaleCFG, SAMLoader, SEGSPaste, SEGSPreview, SaveImage, SelfAttentionGuidance, ToBasicPipe, UltralyticsDetectorProvider, Zoe-DepthMapPreprocessor]
problems: []
missing: []
members: [平台全量/Better ReActor Face Swap + InstantID workflow_1868581753186304002.json, 平台全量/更好的换脸Better ReActor Face Swap + InstantID workflow_1840752302105001985.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_clip_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Better ReActor Face Swap + InstantID workflow_1868581753186304002.json、平台全量/更好的换脸Better ReActor Face Swap + InstantID workflow_1840752302105001985.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DenoiseSchedulerDetailerHookProvider`
- `DetailerForEachDebugPipe`
- `FaceKeypointsPreprocessor`
- `Image Comparer (rgthree)`
- `ImageResize`
- `ImpactSEGSOrderedFilter`
- `ImpactSimpleDetectorSEGS`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `ReActorFaceSwap`
- `ReActorMaskHelper`
- `RescaleCFG`
- `SAMLoader`
- `SEGSPaste`
- `SEGSPreview`
- `SaveImage`
- `SelfAttentionGuidance`
- `ToBasicPipe`
- `UltralyticsDetectorProvider`
- `Zoe-DepthMapPreprocessor`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 0.8 | - | 2 | 100% |
| ControlNet 权重 | 0.7 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
