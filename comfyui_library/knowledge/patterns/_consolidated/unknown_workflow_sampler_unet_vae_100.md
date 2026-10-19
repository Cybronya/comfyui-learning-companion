---
name: unknown_workflow_sampler_unet_vae_100
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.846
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/H3工作流_2088343591486840833.json, 视频生成/图生视频/Mini Max H3-9图参考生音视频-高质量加速版_2095466875982536706.json, 视频生成/图生视频/MiniMax H3 参考生视频lightx2v加速_2084156059366813698.json, 视频生成/图生视频/MiniMax H3 多参考图_视频生成视频_2088037369399300097.json, 视频生成/图生视频/MiniMax H3 多参考生视频（本地版）_2084663749595721729.json, 视频生成/图生视频/MiniMax_H3_00325_唱歌_2086448635486760962.json, 视频生成/图生视频/Minimax H3 多参 Lightx2v 加速_2087571144038764548.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_100

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/H3工作流_2088343591486840833.json、视频生成/图生视频/Mini Max H3-9图参考生音视频-高质量加速版_2095466875982536706.json、视频生成/图生视频/MiniMax H3 参考生视频lightx2v加速_2084156059366813698.json、视频生成/图生视频/MiniMax H3 多参考图_视频生成视频_2088037369399300097.json、视频生成/图生视频/MiniMax H3 多参考生视频（本地版）_2084663749595721729.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 5/7 个有
- `MiniMaxH3ReferenceToVideo` —— 5/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `LoraLoaderBypassModelOnly` —— 3/7 个有
- `PreviewAny` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `RH_LLMAPI_Pro_Node` —— 2/7 个有
- `RTXVideoSuperResolution` —— 2/7 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `ModelPreviewOverrideKJ` —— 1/7 个有
- `RHLLMChatNode` —— 1/7 个有
- `ResizeImagesByLongerEdge` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
