---
name: unknown_workflow_video_sampler_unet_64
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.431
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3-ref2va超级加速版-仅支持1.0分辨率_2089629306782834690.json, 视频生成/图生视频/子悟-MiniMaxH3-ref2va多参考生视频_2085657515655782402.json, 视频生成/文生视频/AITUDOU-MiniMax H3(全能参考)_2084222366611234818.json, 视频生成/文生视频/承象-MiniMax H3(全能单图多图参考)真人短剧极速版_2084992442926981122.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_64

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3-ref2va超级加速版-仅支持1.0分辨率_2089629306782834690.json、视频生成/图生视频/子悟-MiniMaxH3-ref2va多参考生视频_2085657515655782402.json、视频生成/文生视频/AITUDOU-MiniMax H3(全能参考)_2084222366611234818.json、视频生成/文生视频/承象-MiniMax H3(全能单图多图参考)真人短剧极速版_2084992442926981122.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：43%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
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
- `KSamplerSelect` —— 3/4 个有
- `Label (rgthree)` —— 3/4 个有
- `EasyCache` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/4 个有
- `ModelPatchTorchSettings` —— 2/4 个有
- `Text` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `ImageScale` —— 1/4 个有
- `MiniMaxH3TurboLoRA` —— 1/4 个有
- `MiniMaxH3TurboSampler` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `easy compare` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
