---
name: unknown_workflow_sampler_clip_unet_423
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.639
common_nodes: [BasicScheduler, CLIPTextEncode, ConfigureModifiedFlux, DisableNoise, DualCLIPLoader, FlowEditGuider, FlowEditSampler, FluxGuidance, GetNode, INTConstant, ImageScale, LoadImage, OutFluxModelSamplingPred, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/利用FLUXEDIT文字改内容_1900533680509722625.json, 图片生成/图生图/洗图工作流，魔改设计_1923697376870264834.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_423

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/利用FLUXEDIT文字改内容_1900533680509722625.json、图片生成/图生图/洗图工作流，魔改设计_1923697376870264834.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `ConfigureModifiedFlux`
- `DisableNoise`
- `DualCLIPLoader`
- `FlowEditGuider`
- `FlowEditSampler`
- `FluxGuidance`
- `GetNode`
- `INTConstant`
- `ImageScale`
- `LoadImage`
- `OutFluxModelSamplingPred`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Joy_caption_two` —— 1/2 个有
- `Joy_caption_two_load` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
