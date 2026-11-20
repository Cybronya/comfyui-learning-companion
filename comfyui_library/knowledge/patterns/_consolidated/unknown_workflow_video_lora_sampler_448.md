---
name: unknown_workflow_video_lora_sampler_448
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.874571
common_nodes: [BasicScheduler, CLIPLoader, KSamplerSelect, LoraLoaderModelOnly, ModelAttentionBackend, ResolutionSelector, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive]
problems: []
missing: []
members: [视频生成/图生视频/Minimax-H3-双采数字人(Unified节点简洁版)_2109215715042611202.json, 视频生成/图生视频/Minimax-H3-双采数字人_2109270106537816065.json, 视频生成/图生视频/MinimaxH3-数字人(单人加速版)_2084976133631729665.json, 视频生成/图生视频/MinimaxH3音频驱动数字人单人版（lightx2v加速）_2094236523871952898.json, 视频生成/图生视频/MinimaxH3音频驱动数字人单人版（lightx2v加速）_2095193353284575233.json, 视频生成/图生视频/数字人MV视频生成工作流_2094716000133537794.json, 视频生成/图生视频/音频数字人单人lightx2v加速版_2096834315270316033.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_448

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Minimax-H3-双采数字人(Unified节点简洁版)_2109215715042611202.json、视频生成/图生视频/Minimax-H3-双采数字人_2109270106537816065.json、视频生成/图生视频/MinimaxH3-数字人(单人加速版)_2084976133631729665.json、视频生成/图生视频/MinimaxH3音频驱动数字人单人版（lightx2v加速）_2094236523871952898.json、视频生成/图生视频/MinimaxH3音频驱动数字人单人版（lightx2v加速）_2095193353284575233.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 6/7 个有
- `MiniMaxH3ReferenceToVideo` —— 6/7 个有
- `ModelPreviewOverrideKJ` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `TrimAudioDuration` —— 6/7 个有
- `BasicGuider` —— 5/7 个有
- `LoadAudio` —— 5/7 个有
- `LoadImage` —— 5/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/7 个有
- `RandomNoise` —— 5/7 个有
- `SamplerCustomAdvanced` —— 5/7 个有
- `PreviewAudio` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `SoundFlow_GetLength` —— 4/7 个有
- `ConditioningZeroOut` —— 2/7 个有
- `H3SigmaRefiner` —— 2/7 个有
- `MiniMaxChunkFeedForward` —— 2/7 个有
- `MiniMaxLowVRAMAttention` —— 2/7 个有
- `SelfLiftAvatarH3Sampler` —— 2/7 个有
- `MiniMaxH3Unified` —— 1/7 个有
- `SDVN Load Image Url` —— 1/7 个有
- `VHS_LoadAudio` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
