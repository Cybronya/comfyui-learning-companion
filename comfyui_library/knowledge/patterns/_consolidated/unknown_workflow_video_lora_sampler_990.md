---
name: unknown_workflow_video_lora_sampler_990
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4255
common_nodes: [FeiHouEasyH3RHLoraStack, FeiHouEasyH3RHMedia, FeiHouEasyH3RHMotionCollect, FeiHouEasyH3RHMotionSegment, FeiHouEasyH3RHOutput, FeiHouEasyH3RHPromptPreview, FeiHouEasyH3RHRemixLoader, FeiHouEasyH3RHSampleEnhancer2nd, FeiHouEasyH3RHSetup, FeiHouEasyH3RHShotPrompts, GetNode, ModelPreviewOverrideKJ, PrimitiveInt, RandomSeedNoise, SamplerCustomAdvanced, SetNode, VAEDecode, VHS_VideoCombine, dc602dca-2389-4deb-9ca5-edf54daafb06]
problems: []
missing: []
members: [平台全量/【MiniMax-H3 Remix】FeiHou Easy H3 一键长视频自动替换工作流 v2_2119421820494508033.json, 平台全量/【MiniMax-H3 Remix】H3 一键长视频自动替换工作流 v1_2118973051508445185.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_990

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/【MiniMax-H3 Remix】FeiHou Easy H3 一键长视频自动替换工作流 v2_2119421820494508033.json、平台全量/【MiniMax-H3 Remix】H3 一键长视频自动替换工作流 v1_2118973051508445185.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：43%

## 共有节点

全部 2 个 workflow 都包含：
- `FeiHouEasyH3RHLoraStack`
- `FeiHouEasyH3RHMedia`
- `FeiHouEasyH3RHMotionCollect`
- `FeiHouEasyH3RHMotionSegment`
- `FeiHouEasyH3RHOutput`
- `FeiHouEasyH3RHPromptPreview`
- `FeiHouEasyH3RHRemixLoader`
- `FeiHouEasyH3RHSampleEnhancer2nd`
- `FeiHouEasyH3RHSetup`
- `FeiHouEasyH3RHShotPrompts`
- `GetNode`
- `ModelPreviewOverrideKJ`
- `PrimitiveInt`
- `RandomSeedNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `VAEDecode`
- `VHS_VideoCombine`
- `dc602dca-2389-4deb-9ca5-edf54daafb06`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
