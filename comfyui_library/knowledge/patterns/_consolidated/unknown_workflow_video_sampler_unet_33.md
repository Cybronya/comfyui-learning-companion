---
name: unknown_workflow_video_sampler_unet_33
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.583583
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy float]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3｜单人高质量数字人｜音频驱动多图参考 MV_2096969226736193537.json, 视频生成/文生视频/0905万象+动漫短剧文戏（12秒横屏）_2096159965277933569.json, 视频生成/文生视频/0905万象+动漫短剧文戏（12秒竖屏）_2096418321116786689.json, 视频生成/文生视频/0906万象AI+Singularity新模型（12秒横屏960分辨率）_2096460541328973825.json, 视频生成/文生视频/0906万象AI+Singularity新模型（12秒横屏960分辨率）_2097340280092581890.json, 视频生成/文生视频/0906万象AI+Singularity新模型（12秒竖屏960分辨率）_2096477149321580546.json, 视频生成/文生视频/0912Singularity模型双采放大_2098568338380247042.json, 视频生成/文生视频/0916台词优化正反打镜头Singularity模型双采放大_2100172773640458242.json, 视频生成/文生视频/AIGC特异点-Minimax-H3多参考双采放大生成视频（Singularity）_2096091492187205633.json, 视频生成/文生视频/H3最强音频驱动对口型二采，吊打SelfLift_2107840856492429314.json, 视频生成/文生视频/Minimax H3 Singularity 超双采放大（参考生视频）_2098158457118609410.json, 视频生成/文生视频/Minimax H3 第三视角（游戏UI）_2100511191582994433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_33

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3｜单人高质量数字人｜音频驱动多图参考 MV_2096969226736193537.json、视频生成/文生视频/0905万象+动漫短剧文戏（12秒横屏）_2096159965277933569.json、视频生成/文生视频/0905万象+动漫短剧文戏（12秒竖屏）_2096418321116786689.json、视频生成/文生视频/0906万象AI+Singularity新模型（12秒横屏960分辨率）_2096460541328973825.json、视频生成/文生视频/0906万象AI+Singularity新模型（12秒横屏960分辨率）_2097340280092581890.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy float`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 11/12 个有
- `GetNode` —— 11/12 个有
- `MinimaxH3LatentUpscaler3D` —— 11/12 个有
- `PrimitiveFloat` —— 11/12 个有
- `SetNode` —— 11/12 个有
- `LoadAudio` —— 10/12 个有
- `VAEDecodeAudio` —— 10/12 个有
- `忽略多组孤海` —— 10/12 个有
- `VHS_LoadVideo` —— 9/12 个有
- `Lora Loader Stack (rgthree)` —— 8/12 个有
- `LoraLoaderModelOnly` —— 8/12 个有
- `ModelAttentionBackend` —— 8/12 个有
- `Text` —— 5/12 个有
- `BlockSparseAttention` —— 4/12 个有
- `DisableNoise` —— 4/12 个有
- `ExtendIntermediateSigmas` —— 4/12 个有
- `MiniMaxChunkFeedForward` —— 4/12 个有
- `MiniMaxLowVRAMAttention` —— 4/12 个有
- `PrimitiveStringMultiline` —— 4/12 个有
- `SolAttnMiniMax` —— 4/12 个有
- `Text Multiline` —— 3/12 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/12 个有
- `LatentUpscaleBy` —— 1/12 个有
- `SaveAudioAdvanced` —— 1/12 个有
- `TrimAudioDuration` —— 1/12 个有
- `VRAM_Debug` —— 1/12 个有
- `孤海注释` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
