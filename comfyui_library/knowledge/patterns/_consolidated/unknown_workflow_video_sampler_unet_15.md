---
name: unknown_workflow_video_sampler_unet_15
type: Unknown Workflow
frequency: 22
level: moderate
coverage: 0.772727
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/minimax H3 武斗 10.14_2109929662204960769.json, 视频生成/图生视频/minimax+taomate_workflow_2099426301223456770.json, 视频生成/图生视频/minimax_h3_fast-清晰武戏-四图_2109487427214733314.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_2108036419896823810.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_2110569508896329729.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_2111011197268090882.json, 视频生成/图生视频/minimax_h3_i2v_fastH3_trim_latent_upscale_2109449701736140802.json, 视频生成/图生视频/minimax_h3_r2v_Latent%20Upscaler3_2090611335280287745.json, 视频生成/图生视频/minimax_h3_r2v_complex_camera_motion_2094372650780028929.json, 视频生成/图生视频/minimax_h3_r2v_story_board_2091816381816860674.json, 视频生成/图生视频/minimax_h3_r2v_video_edit_2092169538497503233.json, 视频生成/图生视频/minmax潜空间放大姿势迁移_2097668196026372098.json, 视频生成/图生视频/参考故事版生成视频 minimax H3_2092780996881113090.json, 视频生成/图生视频/多图生视频，超强数字人视频带货！可用于多人场景视频制作_2103095600538546178.json, 视频生成/图生视频/开源免费电商短视频带货 MiniMax-H3数字人视频带货！_2097216829407186945.json, 视频生成/图生视频/开源免费电商短视频带货 MiniMax-H3数字人视频带货！_2097872678001664001.json, 视频生成/图生视频/数字人视频带货 Images into Videos—Digital Avatars Drive S_2098219003369054210.json, 视频生成/图生视频/视频带货+Images+into+Videos—Digital+Avatars+Drive_2100028236955738114.json, 视频生成/图生视频/视频带货+Images+into+Videos—Digital+Avatars+Drive_2101558136091013122.json, 视频生成/文生视频/MiniMax-H3开源 数字人视频带货 H3多图生视频 口播带货视频_2098680337055444993.json, 视频生成/文生视频/MiniMaxH3数字人视频带货！H3多图生视频！_2098729617451479042.json, 视频生成/文生视频/Minimax_h3_i2v_latent+upscale+去油光Lora工作流_2093179059550380034.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_15

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/图生视频/minimax H3 武斗 10.14_2109929662204960769.json、视频生成/图生视频/minimax+taomate_workflow_2099426301223456770.json、视频生成/图生视频/minimax_h3_fast-清晰武戏-四图_2109487427214733314.json、视频生成/图生视频/minimax_h3_i2v_fastH3_2108036419896823810.json、视频生成/图生视频/minimax_h3_i2v_fastH3_2110569508896329729.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 22 个 workflow 都包含：
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
- `BasicScheduler` —— 21/22 个有
- `ManualSigmas` —— 18/22 个有
- `LTXVConcatAVLatent` —— 17/22 个有
- `LTXVSeparateAVLatent` —— 17/22 个有
- `MiniMaxH3ReferenceToVideo` —— 17/22 个有
- `MinimaxH3LatentUpscaler3D` —— 17/22 个有
- `LoraLoaderModelOnly` —— 13/22 个有
- `ModelAttentionBackend` —— 13/22 个有
- `PrimitiveStringMultiline` —— 13/22 个有
- `GetNode` —— 12/22 个有
- `MiniMaxH3SigmaShift` —— 12/22 个有
- `SetNode` —— 12/22 个有
- `SplitSigmas` —— 9/22 个有
- `JjkText` —— 8/22 个有
- `BlockSparseAttention` —— 7/22 个有
- `ModelPreviewOverrideKJ` —— 7/22 个有
- `MiniMaxH3ImageToVideo` —— 5/22 个有
- `ImageResizeKJv2` —— 4/22 个有
- `VHS_LoadVideo` —— 2/22 个有
- `EmptyImage` —— 1/22 个有
- `Label (rgthree)` —— 1/22 个有
- `LoadAudio` —— 1/22 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/22 个有
- `MiniMaxH3TurboLoRA` —— 1/22 个有
- `PreviewImage` —— 1/22 个有
- `SaveImage` —— 1/22 个有
- `Text` —— 1/22 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
