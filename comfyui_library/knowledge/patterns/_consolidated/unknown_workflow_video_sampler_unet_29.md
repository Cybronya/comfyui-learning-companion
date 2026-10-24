---
name: unknown_workflow_video_sampler_unet_29
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.920583
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MINIMAX-H3动漫画风加速低显存全功能工作流_2099295189230772226.json, 视频生成/图生视频/MiniMAX-H3-T8双时钟采样4步无损加速 图生视频 -zip_2086179408511062017.json, 视频生成/图生视频/MiniMAX-H3-T8双时钟采样4步无损加速+图生视频_2095722417233682433.json, 视频生成/图生视频/MiniMax H3 4步加速 图生视频 首尾帧生视频_2091730279948963841.json, 视频生成/图生视频/MiniMax H3 FL2VA 首尾帧生视频｜INT8 Turbo 4步极速版_2090795830067417090.json, 视频生成/图生视频/MiniMax H3 FL2VA 首尾帧生视频｜INT8 Turbo 8步加速版_2090756411985850369.json, 视频生成/图生视频/MiniMax H3开源版 去油版数字人_口播_唱歌_MV加速版_2088208371999657986.json, 视频生成/图生视频/MiniMax H3开源版 去油版数字人_口播_唱歌_MV加速版_2088234673238536194.json, 视频生成/图生视频/Minimax H3剪枝版BF16首帧生视频_2094406920504434690.json, 视频生成/图生视频/Minimax H3动作增强修复双采（包含脸部修复和高动态修复）_2098315228005093378.json, 视频生成/图生视频/Minimax H3超真实最强数字人_2102034695067365378.json, 视频生成/图生视频/高质量-Minimax H3音频驱动数字人BF16-max-手动提示词_2099743464232669186.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_29

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MINIMAX-H3动漫画风加速低显存全功能工作流_2099295189230772226.json、视频生成/图生视频/MiniMAX-H3-T8双时钟采样4步无损加速 图生视频 -zip_2086179408511062017.json、视频生成/图生视频/MiniMAX-H3-T8双时钟采样4步无损加速+图生视频_2095722417233682433.json、视频生成/图生视频/MiniMax H3 4步加速 图生视频 首尾帧生视频_2091730279948963841.json、视频生成/图生视频/MiniMax H3 FL2VA 首尾帧生视频｜INT8 Turbo 4步极速版_2090795830067417090.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 10/12 个有
- `LoraLoaderBypassModelOnly` —— 7/12 个有
- `MiniMaxH3DualClockSamplerT8` —— 7/12 个有
- `LoadAudio` —— 6/12 个有
- `BasicScheduler` —— 5/12 个有
- `KSamplerSelect` —— 5/12 个有
- `LoraLoaderModelOnly` —— 4/12 个有
- `GetImageSize` —— 2/12 个有
- `ImageScaleToTotalPixels` —— 2/12 个有
- `Int` —— 2/12 个有
- `LayerUtility: PurgeVRAM V2` —— 2/12 个有
- `ModelAttentionBackend` —— 2/12 个有
- `TrimAudioDuration` —— 2/12 个有
- `LTXVConcatAVLatent` —— 1/12 个有
- `LTXVSeparateAVLatent` —— 1/12 个有
- `MinimaxH3LatentUpscaler3D` —— 1/12 个有
- `solarL_SaveImagesToZip` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
