---
name: unknown_workflow_video_sampler_vae_8
type: Unknown Workflow
frequency: 27
level: moderate
coverage: 0.882481
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SoundFlow_GetLength, VAEDecode, VAELoader, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive]
problems: []
missing: []
members: [数字人/数字人/minimaxH3动态数字人1_2087111145051217921.json, 数字人/数字人/minimaxh3高动态数字人2_2087118803158257665.json, 数字人/数字人/一致性超强-H3数字人单人_2086308817486303234.json, 数字人/数字人/方格智联-MINI-H3数字人_2086681804894986242.json, 数字人/数字人/音频驱动数字人对口型-张老师_2089026075883040769.json, 视频生成/图生视频/H3_全能参考_2107892757984538626.json, 视频生成/图生视频/H3全能多参&音频驱动_2093425873709002754.json, 视频生成/图生视频/MiniMax H3-数字人 唱歌 口播_2089931741619380225.json, 视频生成/图生视频/Minimax H3 乐器表演MV极速版_2084906264412381186.json, 视频生成/图生视频/Minimax H3 乐器表演MV极速版_2100432995860697090.json, 视频生成/图生视频/Minimax H3 音频驱动数字人对口型_2085324362105835522.json, 视频生成/图生视频/Minimax H3 音频驱动数字人对口型_2087570594790465537.json, 视频生成/图生视频/Minimax H3 音频驱动数字人对口型_2087800628679630849.json, 视频生成/图生视频/Minimax H3 音频驱动数字人对口型_2089292719402348545.json, 视频生成/图生视频/Minimax H3 音频驱动数字人对口型_2090338216959373313.json, 视频生成/图生视频/Minimax H3 音频驱动数字人对口型_2090621488088047618.json, 视频生成/图生视频/Minimax H3 音频驱动数字人对口型_2092061086244753409.json, 视频生成/图生视频/Minimax H3 音频驱动数字人对口型_2097490216427810818.json, 视频生成/图生视频/Minimax H3开源 音频驱动数字人对口型 图生视频_2089311171798192129.json, 视频生成/图生视频/Minimax H3开源版 数字人双人_多人对话视频生成_2084955772458459137.json, 视频生成/图生视频/Minimax H3开源版 数字人双人_多人对话视频生成_2084990595327676418.json, 视频生成/图生视频/Minimax H3数字人双人_多人_2084872893997076481.json, 视频生成/图生视频/Minimax H3数字人双人_多人_2087072390349156353.json, 视频生成/图生视频/Minimax H3数字人双人_多人_2089718644019388418.json, 视频生成/图生视频/MinimaxH3音频驱动数字人单人加速版_2088648115644620802.json, 视频生成/图生视频/数字人MV视频生成工作流_2094716000133537794.json, 视频生成/图生视频/音频数字人单人lightx2v加速版_2096834315270316033.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_8

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（数字人/数字人/minimaxH3动态数字人1_2087111145051217921.json、数字人/数字人/minimaxh3高动态数字人2_2087118803158257665.json、数字人/数字人/一致性超强-H3数字人单人_2086308817486303234.json、数字人/数字人/方格智联-MINI-H3数字人_2086681804894986242.json、数字人/数字人/音频驱动数字人对口型-张老师_2089026075883040769.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 27 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SoundFlow_GetLength`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 26/27 个有
- `PreviewAudio` —— 26/27 个有
- `AudioCrop` —— 25/27 个有
- `UNETLoader` —— 25/27 个有
- `PrimitiveStringMultiline` —— 24/27 个有
- `PathchSageAttentionKJ` —— 21/27 个有
- `AudioConcat` —— 15/27 个有
- `EmptyAudio` —— 15/27 个有
- `LoraLoaderModelOnly` —— 10/27 个有
- `ModelAttentionBackend` —— 4/27 个有
- `ModelPreviewOverrideKJ` —— 3/27 个有
- `EnhancedLoadDiffusionModel` —— 2/27 个有
- `RHHiddenNodes` —— 2/27 个有
- `Text` —— 2/27 个有
- `TrimAudioDuration` —— 2/27 个有
- `Label (rgthree)` —— 1/27 个有
- `RHLLMChatNode` —— 1/27 个有
- `VHS_LoadVideo` —— 1/27 个有
- `easy showAnything` —— 1/27 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
