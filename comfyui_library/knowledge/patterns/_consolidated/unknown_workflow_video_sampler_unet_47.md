---
name: unknown_workflow_video_sampler_unet_47
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.677667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/Minimax H3 RH 快速动作一镜到底 多图参考_2103351074445946881.json, 视频生成/图生视频/MiniMax MV 自定义歌曲音乐+MV视频生成工作流_2089775026592641025.json, 视频生成/图生视频/MiniMaxH3-多图参考生视频_2092494833108733954.json, 视频生成/图生视频/MinimaxH3_Char_Swap_视频角色替换_支持表情跟踪_ComfyUI_工作流_2114187327802273794.json, 视频生成/文生视频/Minimax-H3VDN-R2V 视频生成工作流（RH在线流）_2096816318430404609.json, 视频生成/文生视频/MinimaxH3_R2V-FaceRefinement-Basic （面部精修）图生视频工作流_2099479595887190018.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_47

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Minimax H3 RH 快速动作一镜到底 多图参考_2103351074445946881.json、视频生成/图生视频/MiniMax MV 自定义歌曲音乐+MV视频生成工作流_2089775026592641025.json、视频生成/图生视频/MiniMaxH3-多图参考生视频_2092494833108733954.json、视频生成/图生视频/MinimaxH3_Char_Swap_视频角色替换_支持表情跟踪_ComfyUI_工作流_2114187327802273794.json、视频生成/文生视频/Minimax-H3VDN-R2V 视频生成工作流（RH在线流）_2096816318430404609.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/6 个有
- `ImageResizeKJv2` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `MiniMaxChunkFeedForward` —— 5/6 个有
- `MiniMaxH3SigmaShift` —— 5/6 个有
- `PathchSageAttentionKJ` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `ModelPatchTorchSettings` —— 4/6 个有
- `StringConcatenate` —— 4/6 个有
- `Label (rgthree)` —— 3/6 个有
- `LoadAudio` —— 3/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/6 个有
- `MiniMaxLowVRAMAttention` —— 3/6 个有
- `MiniMaxH3VDNRuntimeAuditT8Advanced` —— 2/6 个有
- `ModelAttentionBackend` —— 2/6 个有
- `SeedNode` —— 2/6 个有
- `SolAttnPatch` —— 2/6 个有
- `EmptyImage` —— 1/6 个有
- `H3FaceStitch` —— 1/6 个有
- `H3FaceTrackCrop` —— 1/6 个有
- `H3InjectVideoLatent` —— 1/6 个有
- `H3PerFrameDenoise` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `TrimAudioDuration` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `VedaSparseAttention` —— 1/6 个有
- `XB_CanvasLabel` —— 1/6 个有
- `floatToInt _O` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
