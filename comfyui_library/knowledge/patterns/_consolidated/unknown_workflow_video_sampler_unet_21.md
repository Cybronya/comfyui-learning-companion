---
name: unknown_workflow_video_sampler_unet_21
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.867222
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SoundFlow_GetLength, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3 单人音频驱动数字人（最高15秒）_2085434809618358274.json, 视频生成/图生视频/MiniMax-H3 双人音频驱动数字人（双人最高15秒）_2085462125711024129.json, 视频生成/图生视频/MiniMax-H3_单人音频驱动数字人最高15秒_2099774570529120257.json, 视频生成/图生视频/MiniMax-H3_单人音频驱动数字人最高15秒_2100034040945537025.json, 视频生成/图生视频/Minimax H3 音频驱动数字人对口型_2087570594790465537.json, 视频生成/图生视频/Minimax H3数字人多人极速版_2085589743303225345.json, 视频生成/图生视频/Minimax H3音频驱动数字人_双人_多人版_2084886816611717121.json, 视频生成/图生视频/Minimax-H3-数字人-双人_三人-多条语音合并_2085298936998359041.json, 视频生成/图生视频/MinimaxH3-数字人-单人版-音频参考_2085298918895742977.json, 视频生成/图生视频/MinimaxH3开源版 音频驱动数字人唱歌单人版_2084952200182329345.json, 视频生成/图生视频/MinimaxH3开源版 音频驱动数字人唱歌对口型单人版_2084987771718029313.json, 视频生成/图生视频/MinimaxH3数字人 音频驱动单人版_2084904774553653249.json, 视频生成/图生视频/MinimaxH3音频驱动数字人单人版_2084835679577661441.json, 视频生成/图生视频/MinimaxH3音频驱动数字人单人版_2087022951702028289.json, 视频生成/图生视频/加速版 ！海螺H3！ 数字人对口型 ！两人！_2085574360487784450.json, 视频生成/图生视频/音频驱动数字人对口型_2089870047274688514.json, 视频生成/图生视频/音频驱动数字人对口型_2092803978378694657.json, 视频生成/文生视频/Digital Humans音频驱动数字人对口型_2094956968829083649.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_21

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3 单人音频驱动数字人（最高15秒）_2085434809618358274.json、视频生成/图生视频/MiniMax-H3 双人音频驱动数字人（双人最高15秒）_2085462125711024129.json、视频生成/图生视频/MiniMax-H3_单人音频驱动数字人最高15秒_2099774570529120257.json、视频生成/图生视频/MiniMax-H3_单人音频驱动数字人最高15秒_2100034040945537025.json、视频生成/图生视频/Minimax H3 音频驱动数字人对口型_2087570594790465537.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SoundFlow_GetLength`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 17/18 个有
- `PathchSageAttentionKJ` —— 16/18 个有
- `PreviewAudio` —— 15/18 个有
- `ComfyMathExpression` —— 14/18 个有
- `PrimitiveStringMultiline` —— 13/18 个有
- `AudioConcat` —— 9/18 个有
- `EmptyAudio` —— 9/18 个有
- `CR Prompt Text` —— 4/18 个有
- `LayerUtility: PurgeVRAM V2` —— 4/18 个有
- `MathExpression|pysssss` —— 4/18 个有
- `EasyCache` —— 2/18 个有
- `MiniMaxChunkFeedForward` —— 2/18 个有
- `MiniMaxLowVRAMAttention` —— 2/18 个有
- `ModelAttentionBackend` —— 2/18 个有
- `ModelPreviewOverrideKJ` —— 2/18 个有
- `PixaromaLabel` —— 2/18 个有
- `Fast Groups Muter (rgthree)` —— 1/18 个有
- `PainterVRAM` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
