---
name: unknown_workflow_video_sampler_unet_50
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.77
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MultiRateSamplerEXPT8, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/单图-MiniMaxH3-图生视频-BV2-模板_2090031132980109314.json, 视频生成/图生视频/（3图）MINIMAX短剧_2111253911762989057.json, 视频生成/图生视频/（自用）全能参考一站式短剧创作工作流 minimax h3多模态加速_2086378261021548546.json, 视频生成/文生视频/H3-文生视频（16：9）_2085696662042931202.json, 视频生成/文生视频/MINIMAX-H3 全能参考生成视频｜文生｜图生｜首尾帧｜尾帧｜首帧_2085961446109831169.json, 视频生成/文生视频/MiniMax+H3！加速版！提速480%！全能参考！_2085641752681213953.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_50

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/单图-MiniMaxH3-图生视频-BV2-模板_2090031132980109314.json、视频生成/图生视频/（3图）MINIMAX短剧_2111253911762989057.json、视频生成/图生视频/（自用）全能参考一站式短剧创作工作流 minimax h3多模态加速_2086378261021548546.json、视频生成/文生视频/H3-文生视频（16：9）_2085696662042931202.json、视频生成/文生视频/MINIMAX-H3 全能参考生成视频｜文生｜图生｜首尾帧｜尾帧｜首帧_2085961446109831169.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MultiRateSamplerEXPT8`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `LoadAudio` —— 4/6 个有
- `LoraLoaderBypassModelOnly` —— 4/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `1hew_AnySwitchBool` —— 1/6 个有
- `AudioCrop` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `JjkConcat` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `UniBlockSwap` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `VRAMReserver` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
