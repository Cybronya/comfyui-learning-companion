---
name: unknown_workflow_sampler_unet_vae_39
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.863667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VRGDG_MiniMaxH3AudioDrive]
problems: []
missing: []
members: [图片生成/图生图/MiniMaxH3 音频驱动&图片-数字人_2094029923441799170.json, 数字人/数字人/H3数字人单人可做MV、口播等_2084869137700052993.json, 数字人/数字人/MiniMAX3参考音频对口型-8月8日版_2086535599267344386.json, 数字人/数字人/MiniMax H3  数字人_单人版_2085223953907404802.json, 数字人/数字人/MiniMax H3-数字人_2084880448492228609.json, 数字人/数字人/MiniMax H3-数字人_2111474246617751554.json, 数字人/数字人/Minimax H3 数字人 支持单人&双人_2084819750131163138.json, 数字人/数字人/Minimax H3全能参考数字人双人_多人_2085721182447427585.json, 数字人/数字人/Minimax H3数字人三人_2093592345018195970.json, 数字人/数字人/Minimax H3数字人双人_多人（Lightx2v加速）_2084818471610839041.json, 数字人/数字人/MinimaxH3音频驱动数字人单人版_2084824920000909313.json, 视频生成/图生视频/MiniMax H3  数字人直播_单人版_2088601523713564674.json, 视频生成/图生视频/MinimaxH3音频驱动数字人单人版（lightx2v加速）_2094236523871952898.json, 视频生成/图生视频/数字人MV视频生成工作流_2094716000133537794.json, 视频生成/图生视频/音频数字人单人lightx2v加速版_2096834315270316033.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_39

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/MiniMaxH3 音频驱动&图片-数字人_2094029923441799170.json、数字人/数字人/H3数字人单人可做MV、口播等_2084869137700052993.json、数字人/数字人/MiniMAX3参考音频对口型-8月8日版_2086535599267344386.json、数字人/数字人/MiniMax H3  数字人_单人版_2085223953907404802.json、数字人/数字人/MiniMax H3-数字人_2084880448492228609.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 15 个 workflow 都包含：
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
- `LoadAudio` —— 14/15 个有
- `LoadImage` —— 14/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 14/15 个有
- `ResolutionSelector` —— 14/15 个有
- `SoundFlow_GetLength` —— 14/15 个有
- `VHS_VideoCombine` —— 13/15 个有
- `PreviewAudio` —— 11/15 个有
- `AudioCrop` —— 10/15 个有
- `PathchSageAttentionKJ` —— 8/15 个有
- `LoraLoaderModelOnly` —— 6/15 个有
- `AudioConcat` —— 5/15 个有
- `EmptyAudio` —— 5/15 个有
- `ModelAttentionBackend` —— 5/15 个有
- `ModelPreviewOverrideKJ` —— 5/15 个有
- `TrimAudioDuration` —— 5/15 个有
- `CreateVideo` —— 2/15 个有
- `SaveVideo` —— 2/15 个有
- `GetImageSizeAndCount` —— 1/15 个有
- `ImageResizeKJv2` —— 1/15 个有
- `SDVN Load Image Url` —— 1/15 个有
- `SaveAudio` —— 1/15 个有
- `SpectrumApplyMiniMaxH3` —— 1/15 个有
- `VHS_LoadAudio` —— 1/15 个有
- `easy int` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
