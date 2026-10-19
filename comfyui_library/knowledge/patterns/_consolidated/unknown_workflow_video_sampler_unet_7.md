---
name: unknown_workflow_video_sampler_unet_7
type: Unknown Workflow
frequency: 30
level: moderate
coverage: 0.642333
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/minimax H3 武斗 10.14_2109929662204960769.json, 视频生成/图生视频/minimax h3 参考生视频_2085558159850172417.json, 视频生成/图生视频/minimax+taomate_workflow_2099426301223456770.json, 视频生成/图生视频/minimax_h3_fast-清晰武戏-四图_2109487427214733314.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_2108036419896823810.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_2110569508896329729.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_2111011197268090882.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_trim_latent_upscale_2109449701736140802.json, 视频生成/图生视频/minimax_h3_r2v_Latent%20Upscaler3_2090611335280287745.json, 视频生成/图生视频/minimax_h3_r2v_complex_camera_motion_2094372650780028929.json, 视频生成/图生视频/minimax_h3_r2v_story_board_2091816381816860674.json, 视频生成/图生视频/minimax_h3_r2v_video_edit_2092169538497503233.json, 视频生成/图生视频/minmax潜空间放大姿势迁移_2097668196026372098.json, 视频生成/图生视频/参考故事版生成视频 minimax H3_2092780996881113090.json, 视频生成/图生视频/多图生视频，超强数字人视频带货！可用于多人场景视频制作_2103095600538546178.json, 视频生成/图生视频/开源免费电商短视频带货 MiniMax-H3数字人视频带货！_2097216829407186945.json, 视频生成/图生视频/开源免费电商短视频带货 MiniMax-H3数字人视频带货！_2097872678001664001.json, 视频生成/图生视频/数字人视频带货 Images into Videos—Digital Avatars Drive S_2098219003369054210.json, 视频生成/图生视频/视频带货+Images+into+Videos—Digital+Avatars+Drive_2100028236955738114.json, 视频生成/文生视频/MiniMax H3 全能视频V3_2095061357325545474.json, 视频生成/文生视频/MiniMax H3 多合一全能生视频极速+二采优化版_2097343290071928833.json, 视频生成/文生视频/MiniMax H3 武戏全能视频V3_2095388978387185666.json, 视频生成/文生视频/MiniMax H3-多参生视频二采15秒，24g可跑_2098839012025917442.json, 视频生成/文生视频/MiniMax H3-多参考生视频-优化版_2096048331687555073.json, 视频生成/文生视频/MiniMax H3-多参考生视频-优化版_2104154909896699906.json, 视频生成/文生视频/MiniMax H3-多参考生视频-最新优化版_2104888496719745025.json, 视频生成/文生视频/MiniMax H3-多参考生视频_2095195704401682433.json, 视频生成/文生视频/MiniMax H3-多图多音频视频参考生视频-无水印优化版_2095090395578462210.json, 视频生成/文生视频/MiniMax+H3-多参考生视频（9图片+3视频+3音频）_2101587742454009857.json, 视频生成/文生视频/Minimax H3 双采万能流_2094836628819894274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_7

> 由 `engine/knowledge_consolidation` 从 30 个 workflow 归纳得出（视频生成/图生视频/minimax H3 武斗 10.14_2109929662204960769.json、视频生成/图生视频/minimax h3 参考生视频_2085558159850172417.json、视频生成/图生视频/minimax+taomate_workflow_2099426301223456770.json、视频生成/图生视频/minimax_h3_fast-清晰武戏-四图_2109487427214733314.json、视频生成/图生视频/minimax_h3_i2v_fastH3_2108036419896823810.json…）

- **类型**：Unknown Workflow
- **样本数**：30
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 30 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 29/30 个有
- `MiniMaxH3ReferenceToVideo` —— 26/30 个有
- `LTXVConcatAVLatent` —— 24/30 个有
- `LTXVSeparateAVLatent` —— 24/30 个有
- `MinimaxH3LatentUpscaler3D` —— 24/30 个有
- `GetNode` —— 20/30 个有
- `LoraLoaderModelOnly` —— 20/30 个有
- `SetNode` —— 20/30 个有
- `SplitSigmas` —— 18/30 个有
- `ModelAttentionBackend` —— 16/30 个有
- `ManualSigmas` —— 14/30 个有
- `LoadAudio` —— 13/30 个有
- `PrimitiveStringMultiline` —— 13/30 个有
- `VHS_LoadVideo` —— 13/30 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 12/30 个有
- `MiniMaxH3SigmaShift` —— 11/30 个有
- `Text` —— 11/30 个有
- `easy float` —— 10/30 个有
- `忽略多组孤海` —— 10/30 个有
- `ModelPreviewOverrideKJ` —— 8/30 个有
- `BlockSparseAttention` —— 7/30 个有
- `JjkText` —— 5/30 个有
- `MiniMaxH3ImageToVideo` —— 4/30 个有
- `ImageResizeKJv2` —— 3/30 个有
- `ExtendIntermediateSigmas` —— 1/30 个有
- `Fast Groups Bypasser (rgthree)` —— 1/30 个有
- `H3SigmaRefiner` —— 1/30 个有
- `MiniMaxH3TurboLoRA` —— 1/30 个有
- `SaveImage` —— 1/30 个有
- `easy sleep` —— 1/30 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
