---
name: unknown_workflow_video_upscale_latent_upscale_82
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.973
common_nodes: [BasicGuider, BasicScheduler, BlockSparseAttention, CLIPLoader, GoohaiMinimaxH3TiledSampler, H3DistanceAttentionPatcher, JZL_HailuoH3VideoParamsPro, JZL_MiniMaxH3CondSync, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3AudioConditioningT8, MiniMaxH3SemanticBridgeConfigT8, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, PlaySound|pysssss, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3 多参二采低显存直出2K视频工作流_2112166616527097858.json, 视频生成/图生视频/MiniMax-H3+fl2va二采首尾帧低显存2K视频直出_2113521855880581121.json, 视频生成/图生视频/MiniMax-H3+fl2va二采首帧低显存2K视频直出_2113555496669106178.json, 视频生成/文生视频/MiniMax-H3+fl2va 二采文生视频低显存2K直出_2113559601496023041.json, 视频生成/文生视频/MiniMax-H3+fl2va 二采文生视频低显存2K直出_2113645665246076930.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_82

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3 多参二采低显存直出2K视频工作流_2112166616527097858.json、视频生成/图生视频/MiniMax-H3+fl2va二采首尾帧低显存2K视频直出_2113521855880581121.json、视频生成/图生视频/MiniMax-H3+fl2va二采首帧低显存2K视频直出_2113555496669106178.json、视频生成/文生视频/MiniMax-H3+fl2va 二采文生视频低显存2K直出_2113559601496023041.json、视频生成/文生视频/MiniMax-H3+fl2va 二采文生视频低显存2K直出_2113645665246076930.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `GoohaiMinimaxH3TiledSampler`
- `H3DistanceAttentionPatcher`
- `JZL_HailuoH3VideoParamsPro`
- `JZL_MiniMaxH3CondSync`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3SemanticBridgeConfigT8`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `PlaySound|pysssss`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/5 个有
- `GoohaiRatioAndResolution` —— 4/5 个有
- `MiniMaxH3PromptEnhancerT8` —— 4/5 个有
- `StringToInt` —— 4/5 个有
- `LoadImage` —— 3/5 个有
- `JindouyunNumberSlider` —— 1/5 个有
- `ModelPreviewOverrideKJ` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `VHS_LoadAudioUpload` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `VRAM_Debug` —— 1/5 个有
- `忽略多组孤海` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
