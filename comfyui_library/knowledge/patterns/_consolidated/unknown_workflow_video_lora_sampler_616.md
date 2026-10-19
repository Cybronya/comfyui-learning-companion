---
name: unknown_workflow_video_lora_sampler_616
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.448
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax多图参考生成视频R2V_768_8步_2099766777768136705.json, 视频生成/图生视频/Minimax H3 N宫格视频_2098678084865183745.json, 视频生成/图生视频/心然·寻源-MiniMax H3 多模态参考数字人对口型_2090830886253195265.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_616

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax多图参考生成视频R2V_768_8步_2099766777768136705.json、视频生成/图生视频/Minimax H3 N宫格视频_2098678084865183745.json、视频生成/图生视频/心然·寻源-MiniMax H3 多模态参考数字人对口型_2090830886253195265.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `Float` —— 2/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `CM_IntToFloat` —— 1/3 个有
- `ExtendIntermediateSigmas` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `MiniMaxH3SigmaShift` —— 1/3 个有
- `ModelAttentionBackend` —— 1/3 个有
- `ModelPreviewOverrideKJ` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `SigmasGraph` —— 1/3 个有
- `ZNGB_AudioCrop` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
