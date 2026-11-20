---
name: unknown_workflow_lora_sampler_unet_276
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.988667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, GetVideoComponents, KSamplerSelect, LoadImage, LoadVideo, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3FaceRefineManual512RelativeBaselineT8Advanced, MiniMaxH3FaceRefineParityLatentT8Advanced, MiniMaxH3FaceRefineParityPlanT8Advanced, MiniMaxH3FaceRefineParityStitchT8Advanced, MiniMaxH3FaceRefinePerFrameDenoiseT8Advanced, MiniMaxH3SigmaShift, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [平台全量/Face_Refine_2108212328142565378.json, 平台全量/MiniMax H3脸崩修复（单人版）_2089574097431916545.json, 平台全量/MiniMax H3视频人脸高清修复（单人版）视频+参考图生视频_2089881294258921474.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_276

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Face_Refine_2108212328142565378.json、平台全量/MiniMax H3脸崩修复（单人版）_2089574097431916545.json、平台全量/MiniMax H3视频人脸高清修复（单人版）视频+参考图生视频_2089881294258921474.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `GetVideoComponents`
- `KSamplerSelect`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3FaceRefineManual512RelativeBaselineT8Advanced`
- `MiniMaxH3FaceRefineParityLatentT8Advanced`
- `MiniMaxH3FaceRefineParityPlanT8Advanced`
- `MiniMaxH3FaceRefineParityStitchT8Advanced`
- `MiniMaxH3FaceRefinePerFrameDenoiseT8Advanced`
- `MiniMaxH3SigmaShift`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/3 个有
- `ModelAttentionBackend` —— 2/3 个有
- `SolAttnMiniMax` —— 2/3 个有
- `MiniMaxH3FaceRefineManualReviewT8Advanced` —— 1/3 个有
- `MiniMaxH3FaceRefineSamplerMaskPatchV11T8Advanced` —— 1/3 个有
- `MiniMaxH3FaceRefineWindowExtractT8Advanced` —— 1/3 个有
- `MiniMaxH3FaceRefineWindowPlanT8Advanced` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
