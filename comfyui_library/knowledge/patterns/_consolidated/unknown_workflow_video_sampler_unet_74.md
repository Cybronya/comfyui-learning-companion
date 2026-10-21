---
name: unknown_workflow_video_sampler_unet_74
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.773333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Text, ComfyMathExpression, Fast Groups Bypasser (rgthree), H3SigmaRefiner, Int, KSamplerSelect, Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MiniMaxH3ImageToVideo, ModelAttentionBackend, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SolAttnPatch, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/minimax首尾帧视频-加速_2095432472426270722.json, 视频生成/图生视频/minimax首尾帧视频_2096856647980380161.json, 视频生成/图生视频/新手喂饭！Minimax首尾帧工作流拆解（selfLift）_2101930359096176642.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_74

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/minimax首尾帧视频-加速_2095432472426270722.json、视频生成/图生视频/minimax首尾帧视频_2096856647980380161.json、视频生成/图生视频/新手喂饭！Minimax首尾帧工作流拆解（selfLift）_2101930359096176642.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `H3SigmaRefiner`
- `Int`
- `KSamplerSelect`
- `Label (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SolAttnPatch`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 2/3 个有
- `DF_Int_to_Float` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `Bookmark (rgthree)` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `ModelPreviewOverrideKJ` —— 1/3 个有
- `SeargeFloatConstant` —— 1/3 个有
- `SelfLiftH3Sampler` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
