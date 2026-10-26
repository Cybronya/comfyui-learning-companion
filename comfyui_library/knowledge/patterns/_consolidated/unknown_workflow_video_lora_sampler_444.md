---
name: unknown_workflow_video_lora_sampler_444
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.66
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, CR Text, ConditioningZeroOut, Fast Groups Bypasser (rgthree), Fast Muter (rgthree), GetNode, H3SigmaRefiner, KSamplerSelect, Label (rgthree), LoraLoaderModelOnly, MemoryCleaner, MiniMaxChunkFeedForward, MiniMaxH3Unified, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewImage, RH_DLSS5Enhance, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_SelectImages, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/MinimaxH3超快数字人_2109460248967860226.json, 图片生成/文生图/Minimax_H3_直出_4K_LoRA_去油化_+_H3_统一插件_+_自提升渐进式采样工作流_2114320225515692033.json, 视频生成/图生视频/MinimaxH3超快数字人_2109085639286280194.json, 视频生成/文生视频/1002海螺H3三采极致高分辨率工作流（最长20秒放大到4K）_2105901782873493506.json, 视频生成/文生视频/文戏不油—三采极致高分辨率工作流_2104527536003833858.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_444

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/MinimaxH3超快数字人_2109460248967860226.json、图片生成/文生图/Minimax_H3_直出_4K_LoRA_去油化_+_H3_统一插件_+_自提升渐进式采样工作流_2114320225515692033.json、视频生成/图生视频/MinimaxH3超快数字人_2109085639286280194.json、视频生成/文生视频/1002海螺H3三采极致高分辨率工作流（最长20秒放大到4K）_2105901782873493506.json、视频生成/文生视频/文戏不油—三采极致高分辨率工作流_2104527536003833858.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 5 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `Fast Muter (rgthree)`
- `GetNode`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoraLoaderModelOnly`
- `MemoryCleaner`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3Unified`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewImage`
- `RH_DLSS5Enhance`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_SelectImages`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `FlashVSRInitPipe` —— 4/5 个有
- `FlashVSRNodeAdv` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `LTXVSeparateAVLatent` —— 4/5 个有
- `MiniMaxH3VAEDecodeFast` —— 4/5 个有
- `VOSR2ModelLoader` —— 4/5 个有
- `VOSR2Upscale` —— 4/5 个有
- `SelfLiftH3Sampler` —— 3/5 个有
- `VAEDecodeAudio` —— 3/5 个有
- `SelfLiftAvatarH3Sampler` —— 2/5 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/5 个有
- `EmptyImage` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
