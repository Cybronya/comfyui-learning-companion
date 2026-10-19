---
name: unknown_workflow_video_sampler_unet_33
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.82575
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SoundFlow_GetLength, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/Minimax H3 数字人 支持单人&双人_2084819750131163138.json, 数字人/数字人/Minimax H3全能参考数字人双人_多人_2085721182447427585.json, 数字人/数字人/Minimax H3数字人三人_2093592345018195970.json, 数字人/数字人/Minimax H3数字人双人_多人（Lightx2v加速）_2084818471610839041.json, 数字人/数字人/MinimaxH3-数字人MV制作_2085594233104322561.json, 数字人/数字人/MinimaxH3音频驱动+语音克隆_2086995655117070338.json, 视频生成/图生视频/MinimaxH3音频+图片=口播数字人+全节点注释_2095797295269892098.json, 视频生成/图生视频/MinimaxH3音频驱动数字人单人版（lightx2v加速）_2094236523871952898.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_33

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/Minimax H3 数字人 支持单人&双人_2084819750131163138.json、数字人/数字人/Minimax H3全能参考数字人双人_多人_2085721182447427585.json、数字人/数字人/Minimax H3数字人三人_2093592345018195970.json、数字人/数字人/Minimax H3数字人双人_多人（Lightx2v加速）_2084818471610839041.json、数字人/数字人/MinimaxH3-数字人MV制作_2085594233104322561.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SoundFlow_GetLength`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `PreviewAudio` —— 7/8 个有
- `PrimitiveFloat` —— 7/8 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 7/8 个有
- `AudioCrop` —— 6/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `AudioConcat` —— 4/8 个有
- `EmptyAudio` —— 4/8 个有
- `ModelAttentionBackend` —— 4/8 个有
- `ModelPreviewOverrideKJ` —— 4/8 个有
- `CR Text` —— 2/8 个有
- `PathchSageAttentionKJ` —— 2/8 个有
- `TrimAudioDuration` —— 2/8 个有
- `AudioBeforeAfterSilence` —— 1/8 个有
- `HeartMuLa_Transcribe` —— 1/8 个有
- `MiniMaxH3SigmaShift` —— 1/8 个有
- `Qwen3TTSModelLoader` —— 1/8 个有
- `Qwen3TTSVoiceClone` —— 1/8 个有
- `SDVN Load Image Url` —— 1/8 个有
- `VHS_LoadAudio` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
