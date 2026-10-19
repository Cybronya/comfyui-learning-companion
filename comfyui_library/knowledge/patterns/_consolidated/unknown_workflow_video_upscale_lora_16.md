---
name: unknown_workflow_video_upscale_lora_16
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.657667
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, CR Text, ConditioningZeroOut, Fast Groups Bypasser (rgthree), Fast Muter (rgthree), FlashVSRInitPipe, FlashVSRNodeAdv, GetNode, H3SigmaRefiner, INTConstant, KSamplerSelect, LTXVSeparateAVLatent, Label (rgthree), LoraLoaderModelOnly, MemoryCleaner, MiniMaxChunkFeedForward, MiniMaxH3Unified, MiniMaxH3VAEDecodeFast, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewImage, RH_DLSS5Enhance, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_SelectImages, VHS_VideoCombine, VOSR2ModelLoader, VOSR2Upscale]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3超快数字人_2109085639286280194.json, 视频生成/文生视频/1002海螺H3三采极致高分辨率工作流（最长20秒放大到4K）_2105901782873493506.json, 视频生成/文生视频/文戏不油—三采极致高分辨率工作流_2104527536003833858.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_16

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3超快数字人_2109085639286280194.json、视频生成/文生视频/1002海螺H3三采极致高分辨率工作流（最长20秒放大到4K）_2105901782873493506.json、视频生成/文生视频/文戏不油—三采极致高分辨率工作流_2104527536003833858.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `Fast Muter (rgthree)`
- `FlashVSRInitPipe`
- `FlashVSRNodeAdv`
- `GetNode`
- `H3SigmaRefiner`
- `INTConstant`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `Label (rgthree)`
- `LoraLoaderModelOnly`
- `MemoryCleaner`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3Unified`
- `MiniMaxH3VAEDecodeFast`
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
- `VOSR2ModelLoader`
- `VOSR2Upscale`

**可变部分**（部分 workflow 才有）：
- `SelfLiftH3Sampler` —— 2/3 个有
- `VAEDecodeAudio` —— 2/3 个有
- `SelfLiftAvatarH3Sampler` —— 1/3 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
