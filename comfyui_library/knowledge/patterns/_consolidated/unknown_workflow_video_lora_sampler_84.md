---
name: unknown_workflow_video_lora_sampler_84
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.4565
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), GetNode, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PreviewImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, Text, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, RunningHub Deepcleaner]
members: [图片生成/图生图/2087902401587138562.json, 图片生成/文生图/YZ金鱼-MiniMax H3超级多合一工作流-官方版_2084514856253874178.json, 图片生成/文生图/手动+反推+高清超强生图_1995038070712020993.json, 数字人/数字人/minimax-h3-多参考口播-z_2102289509139439617.json, 数字人/数字人/video3 自用_2089588273210544130.json, 视频生成/图生视频/720P-MiniMax H3超级多合一工作流-官方版_2094765092280819714.json, 视频生成/图生视频/API用-多参考-MiniMax H3工作流_2087940945802252290.json, 视频生成/图生视频/H3全能参考+二采放大8898_2089605189635502082.json, 视频生成/图生视频/MINIMAX-H3 全能参考去油防脸崩工作流_2086816639672213505.json, 视频生成/图生视频/MiniMax H3 多参2采8步加速_2091503467927007234.json, 视频生成/图生视频/MiniMax H3-TVC成片（15秒视频5毛成本吊打官方版本）_2087056799617863682.json, 视频生成/图生视频/MiniMax H3多图参考视频生成工作流双采去水印版_2093297157603414018.json, 视频生成/图生视频/MiniMax H3超级多合一工作流-官方版_2086606573383806978.json, 视频生成/图生视频/MiniMax H3超级多合一工作流-官方版james003_4K###_2110535182506872833.json, 视频生成/文生视频/GS高尚-MiniMax H3多参二次采样放大工作流_2086726756911898625.json, 视频生成/文生视频/MiniMax H3开源 超级多合一 文生图生多参合一工作流-官方版_2086415506692722689.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_84

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/2087902401587138562.json、图片生成/文生图/YZ金鱼-MiniMax H3超级多合一工作流-官方版_2084514856253874178.json、图片生成/文生图/手动+反推+高清超强生图_1995038070712020993.json、数字人/数字人/minimax-h3-多参考口播-z_2102289509139439617.json、数字人/数字人/video3 自用_2089588273210544130.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：46%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PreviewImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 15/16 个有
- `LoadAudio` —— 15/16 个有
- `VAEEncode` —— 15/16 个有
- `VAEEncodeAudio` —— 15/16 个有
- `VHS_LoadVideo` —— 15/16 个有
- `VAEDecodeAudio` —— 11/16 个有
- `MiniMaxH3ImageToVideo` —— 10/16 个有
- `PT_H3ConcatAVLatent` —— 9/16 个有
- `RunningHub Deepcleaner` —— 9/16 个有
- `ModelAttentionBackend` —— 7/16 个有
- `孤海注释` —— 7/16 个有
- `LTXVConcatAVLatent` —— 6/16 个有
- `easy cleanGpuUsed` —— 6/16 个有
- `MiniMaxH3AVDecodeT8` —— 5/16 个有
- `Any Switch (rgthree)` —— 1/16 个有
- `CRTFirstLastFrameSelector` —— 1/16 个有
- `EmptyImage` —— 1/16 个有
- `Fast Groups Muter (rgthree)` —— 1/16 个有
- `FlashVSRNode` —— 1/16 个有
- `MiniMaxH3AddGuide` —— 1/16 个有
- `PathchSageAttentionKJ` —— 1/16 个有
- `SaveVideo` —— 1/16 个有
- `TrimAudioDuration` —— 1/16 个有
- `XB_VideoLoader` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、RunningHub Deepcleaner
