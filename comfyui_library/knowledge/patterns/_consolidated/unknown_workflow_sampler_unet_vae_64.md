---
name: unknown_workflow_sampler_unet_vae_64
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.874538
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VRGDG_MiniMaxH3AudioDrive]
problems: []
missing: []
members: [图片生成/图生图/MiniMaxH3 音频驱动&图片-数字人_2094029923441799170.json, 数字人/数字人/H3数字人单人可做MV、口播等_2084869137700052993.json, 数字人/数字人/MiniMAX3参考音频对口型-8月8日版_2086535599267344386.json, 数字人/数字人/MiniMax H3  数字人_单人版_2085223953907404802.json, 数字人/数字人/MiniMax H3-数字人_2084880448492228609.json, 数字人/数字人/MiniMax H3-数字人_2111474246617751554.json, 数字人/数字人/Minimax H3 数字人 支持单人&双人_2084819750131163138.json, 数字人/数字人/Minimax H3全能参考数字人双人_多人_2085721182447427585.json, 数字人/数字人/Minimax H3数字人三人_2093592345018195970.json, 数字人/数字人/Minimax H3数字人双人_多人（Lightx2v加速）_2084818471610839041.json, 视频生成/图生视频/MiniMax H3  数字人直播_单人版_2088601523713564674.json, 视频生成/图生视频/MinimaxH3音频驱动数字人单人版（lightx2v加速）_2094236523871952898.json, 视频生成/图生视频/数字人MV视频生成工作流_2094716000133537794.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_64

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/MiniMaxH3 音频驱动&图片-数字人_2094029923441799170.json、数字人/数字人/H3数字人单人可做MV、口播等_2084869137700052993.json、数字人/数字人/MiniMAX3参考音频对口型-8月8日版_2086535599267344386.json、数字人/数字人/MiniMax H3  数字人_单人版_2085223953907404802.json、数字人/数字人/MiniMax H3-数字人_2084880448492228609.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VRGDG_MiniMaxH3AudioDrive`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 12/13 个有
- `LoadImage` —— 12/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 12/13 个有
- `ResolutionSelector` —— 12/13 个有
- `SoundFlow_GetLength` —— 12/13 个有
- `VHS_VideoCombine` —— 11/13 个有
- `AudioCrop` —— 9/13 个有
- `PreviewAudio` —— 9/13 个有
- `PathchSageAttentionKJ` —— 7/13 个有
- `AudioConcat` —— 5/13 个有
- `EmptyAudio` —— 5/13 个有
- `LoraLoaderModelOnly` —— 5/13 个有
- `ModelAttentionBackend` —— 4/13 个有
- `ModelPreviewOverrideKJ` —— 4/13 个有
- `TrimAudioDuration` —— 4/13 个有
- `CreateVideo` —— 2/13 个有
- `SaveVideo` —— 2/13 个有
- `GetImageSizeAndCount` —— 1/13 个有
- `ImageResizeKJv2` —— 1/13 个有
- `SDVN Load Image Url` —— 1/13 个有
- `SaveAudio` —— 1/13 个有
- `SpectrumApplyMiniMaxH3` —— 1/13 个有
- `VHS_LoadAudio` —— 1/13 个有
- `easy int` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
