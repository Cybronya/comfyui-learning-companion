---
name: unknown_workflow_video_lora_sampler_691
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.513667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PT_H3ConcatAVLatent, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAEEncodeAudio, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/文生视频/H3高质量全能参考图片音频视频api版本_2089609638827347969.json, 视频生成/文生视频/MiniMax H3 双采样_2089982231854018561.json, 视频生成/文生视频/心然·寻源-Minimax H3 多模态参考生视频（双采加速版）_2087734113288679426.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_691

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/H3高质量全能参考图片音频视频api版本_2089609638827347969.json、视频生成/文生视频/MiniMax H3 双采样_2089982231854018561.json、视频生成/文生视频/心然·寻源-Minimax H3 多模态参考生视频（双采加速版）_2087734113288679426.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PT_H3ConcatAVLatent`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Float` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `LoadAudio` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Int` —— 1/3 个有
- `JWStringConcat` —— 1/3 个有
- `JjkShowText` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `MinNode` —— 1/3 个有
- `ModelAttentionBackend` —— 1/3 个有
- `ModelPatchTorchSettings` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RHLLMChatNode` —— 1/3 个有
- `Text` —— 1/3 个有
- `图像缩放V2_孤海` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
