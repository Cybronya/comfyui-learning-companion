---
name: unknown_workflow_video_sampler_unet_79
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.71425
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax_H3口型同步_2086253656294383617.json, 视频生成/文生视频/Minimax H3 全能参考丨本地版丨老许Gary🎉_2084187343426248705.json, 视频生成/文生视频/minimaxH3+访谈类数字人_2097651536854863873.json, 视频生成/文生视频/minimaxH3数字人工作流（音色参考）_2094688876832055298.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_79

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/MiniMax_H3口型同步_2086253656294383617.json、视频生成/文生视频/Minimax H3 全能参考丨本地版丨老许Gary🎉_2084187343426248705.json、视频生成/文生视频/minimaxH3+访谈类数字人_2097651536854863873.json、视频生成/文生视频/minimaxH3数字人工作流（音色参考）_2094688876832055298.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 3/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `VAEDecodeAudio` —— 3/4 个有
- `AudioCrop` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ModelPreviewOverrideKJ` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `DF_Int_to_Float` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `GetAudioDurationFromAudio` —— 1/4 个有
- `PainterVRAM` —— 1/4 个有
- `SDVN Any Show` —— 1/4 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
