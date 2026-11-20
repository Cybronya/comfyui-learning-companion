---
name: unknown_workflow_video_lora_sampler_603
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.46375
common_nodes: [BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, GetNode, GoohaiUniversalSlider, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, ResolutionSelector, SetNode, Text, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/图生视频/自用文武双全音频驱动_2112933738454802433.json, 视频生成/文生视频/MiniMax H3 终极篇-文生视频_2113466253888282626.json, 视频生成/文生视频/MiniMax H3生成视频_2113923437487026177.json, 视频生成/文生视频/YZ金鱼-MiniMax+H3+终极篇-文武双全_2113310444478877698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_603

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/自用文武双全音频驱动_2112933738454802433.json、视频生成/文生视频/MiniMax H3 终极篇-文生视频_2113466253888282626.json、视频生成/文生视频/MiniMax H3生成视频_2113923437487026177.json、视频生成/文生视频/YZ金鱼-MiniMax+H3+终极篇-文武双全_2113310444478877698.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：46%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `GetNode`
- `GoohaiUniversalSlider`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `ResolutionSelector`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 3/4 个有
- `MiniMaxChunkFeedForward` —— 3/4 个有
- `PrimitiveFloat` —— 3/4 个有
- `SelfLiftH3Sampler` —— 3/4 个有
- `VAEDecodeAudio` —— 3/4 个有
- `LoadAudioFromUrl` —— 1/4 个有
- `MiniMaxH3AddGuide` —— 1/4 个有
- `SelfLiftAvatarH3Sampler` —— 1/4 个有
- `SoundFlow_GetLength` —— 1/4 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
