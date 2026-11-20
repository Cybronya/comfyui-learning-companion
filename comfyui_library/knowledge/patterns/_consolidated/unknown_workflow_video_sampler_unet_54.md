---
name: unknown_workflow_video_sampler_unet_54
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.6145
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/动作视频转深度控制视频MMH3_10eros_r2v_2095848275881582594.json, 视频生成/图生视频/MiniMax H3双图参考图生视频Org开源版_2084188486315372546.json, 视频生成/图生视频/MiniMax H3多参图生视频Org开源版_2084193196506173442.json, 视频生成/图生视频/MiniMax多图参考生成视频R2V_768_8步_2099766777768136705.json, 视频生成/图生视频/Minimax H3 音频驱动数字人超分V13_2096777449806843906.json, 视频生成/图生视频/音频驱动测试_2111325696218976257.json, 视频生成/文生视频/H3模型测试_singularity_2098910282218299394.json, 视频生成/文生视频/Minimax H3 文生图生参考万能超分V13_2096777434057236482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_54

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/动作视频转深度控制视频MMH3_10eros_r2v_2095848275881582594.json、视频生成/图生视频/MiniMax H3双图参考图生视频Org开源版_2084188486315372546.json、视频生成/图生视频/MiniMax H3多参图生视频Org开源版_2084193196506173442.json、视频生成/图生视频/MiniMax多图参考生成视频R2V_768_8步_2099766777768136705.json、视频生成/图生视频/Minimax H3 音频驱动数字人超分V13_2096777449806843906.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 7/8 个有
- `PrimitiveFloat` —— 7/8 个有
- `LoadAudio` —— 6/8 个有
- `ModelAttentionBackend` —— 6/8 个有
- `VHS_LoadVideo` —— 6/8 个有
- `GetNode` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `ResolutionSelector` —— 5/8 个有
- `SetNode` —— 5/8 个有
- `VAEDecodeAudio` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `PrimitiveStringMultiline` —— 4/8 个有
- `PurgeVRAM_UTK` —— 4/8 个有
- `Text` —— 4/8 个有
- `Int` —— 3/8 个有
- `RTXVideoSuperResolution` —— 3/8 个有
- `MiniMaxH3SigmaShift` —— 2/8 个有
- `SoundFlow_GetLength` —— 2/8 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/8 个有
- `CM_IntToFloat` —— 1/8 个有
- `DepthCrafter` —— 1/8 个有
- `DownloadAndLoadDepthCrafterModel` —— 1/8 个有
- `ExtendIntermediateSigmas` —— 1/8 个有
- `MiniMaxH3AddGuide` —— 1/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/8 个有
- `ModelPreviewOverrideKJ` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
