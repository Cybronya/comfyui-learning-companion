---
name: unknown_workflow_video_sampler_unet_40
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.698125
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/Minimax H3 RH 快速动作一镜到底 多图参考_2103351074445946881.json, 视频生成/图生视频/MiniMax H3 超燃角色PV制作_2094985739380543489.json, 视频生成/图生视频/MiniMax MV 自定义歌曲音乐+MV视频生成工作流_2089775026592641025.json, 视频生成/图生视频/MiniMaxH3-多图参考生视频_2092494833108733954.json, 视频生成/图生视频/Minimax_H3_Character_Swap 角色替换_参考到视频工作流_2106641143629959169.json, 视频生成/图生视频/（新）MinimaxH3_R2V-2Stage-VEDA 加速 视频生成工作流_2109325714523774977.json, 视频生成/文生视频/Minimax-H3VDN-R2V 视频生成工作流（RH在线流）_2096816318430404609.json, 视频生成/视频生视频/Minimax_H3_Character_Swap 角色替换_参考到视频工作流_2106641143629959169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_40

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Minimax H3 RH 快速动作一镜到底 多图参考_2103351074445946881.json、视频生成/图生视频/MiniMax H3 超燃角色PV制作_2094985739380543489.json、视频生成/图生视频/MiniMax MV 自定义歌曲音乐+MV视频生成工作流_2089775026592641025.json、视频生成/图生视频/MiniMaxH3-多图参考生视频_2092494833108733954.json、视频生成/图生视频/Minimax_H3_Character_Swap 角色替换_参考到视频工作流_2106641143629959169.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `MiniMaxH3SigmaShift` —— 7/8 个有
- `PrimitiveStringMultiline` —— 7/8 个有
- `GetNode` —— 6/8 个有
- `ImageResizeKJv2` —— 6/8 个有
- `MiniMaxChunkFeedForward` —— 6/8 个有
- `PathchSageAttentionKJ` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/8 个有
- `ModelPatchTorchSettings` —— 5/8 个有
- `MMH3LatentUpscaleWithModelParams` —— 3/8 个有
- `MMH3SpatialSplitParams` —— 3/8 个有
- `MMH3TemporalSplitParams` —— 3/8 个有
- `MMH3UltimateUpscale` —— 3/8 个有
- `MiniMaxLowVRAMAttention` —— 3/8 个有
- `ModelAttentionBackend` —— 3/8 个有
- `SeedNode` —— 3/8 个有
- `StringConcatenate` —— 3/8 个有
- `VAEDecodeTiled` —— 3/8 个有
- `easy cleanGpuUsed` —— 3/8 个有
- `easy clearCacheAll` —— 3/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `LoadAudio` —— 2/8 个有
- `MiniMaxH3VDNRuntimeAuditT8Advanced` —— 2/8 个有
- `SolAttnPatch` —— 2/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `ModelPreviewOverrideKJ` —— 1/8 个有
- `Textbox` —— 1/8 个有
- `TrimAudioDuration` —— 1/8 个有
- `VedaSparseAttention` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
