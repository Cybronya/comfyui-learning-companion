---
name: unknown_workflow_video_lora_sampler_184
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.467154
common_nodes: [BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, GetNode, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, ResolutionSelector, SetNode, Text, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/自用文武双全音频+首尾帧_2116041093665091586.json, 视频生成/图生视频/自用文武双全音频驱动_2112933738454802433.json, 视频生成/图生视频/舒胖子终极篇-文武双全_2114921640390914049.json, 视频生成/图生视频/道真 H3 终极篇-多人多场景_2115835562472067074.json, 视频生成/图生视频/道真_H3_终极篇-多人多场景_2116024910475784194.json, 视频生成/图生视频/道真_H3_终极篇-多人多场景_2116033494441873409.json, 视频生成/图生视频/｜H3多图参考短片_2115993456261812226.json, 视频生成/图生视频/｜H3多图参考短片_2116008339372072961.json, 视频生成/文生视频/MiniMax H3 终极篇-文生视频_2113466253888282626.json, 视频生成/文生视频/MiniMax H3生成视频_2113923437487026177.json, 视频生成/文生视频/YZ金鱼-MiniMax+H3+终极篇-文武双全_2113310444478877698.json, 视频生成/文生视频/纯文生视频_2115261844284862465.json, 视频生成/视频生视频/自用文武双全音频+首尾帧_2112933738454802433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_184

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/自用文武双全音频+首尾帧_2116041093665091586.json、视频生成/图生视频/自用文武双全音频驱动_2112933738454802433.json、视频生成/图生视频/舒胖子终极篇-文武双全_2114921640390914049.json、视频生成/图生视频/道真 H3 终极篇-多人多场景_2115835562472067074.json、视频生成/图生视频/道真_H3_终极篇-多人多场景_2116024910475784194.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：47%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `GetNode`
- `KSamplerSelect`
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
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 12/13 个有
- `VHS_LoadVideo` —— 12/13 个有
- `忽略多组孤海` —— 12/13 个有
- `LoadAudio` —— 11/13 个有
- `GoohaiUniversalSlider` —— 10/13 个有
- `MiniMaxChunkFeedForward` —— 10/13 个有
- `PrimitiveFloat` —— 10/13 个有
- `SelfLiftH3Sampler` —— 10/13 个有
- `VAEDecodeAudio` —— 10/13 个有
- `MiniMaxH3AddGuide` —— 3/13 个有
- `SelfLiftAvatarH3Sampler` —— 3/13 个有
- `SoundFlow_GetLength` —— 3/13 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 3/13 个有
- `LoadAudioFromUrl` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
