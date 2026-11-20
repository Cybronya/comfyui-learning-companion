---
name: unknown_workflow_video_lora_sampler_693
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.91575
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, H3SigmaRefiner, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/上传音频双采完美数字人-seiflite版_2119266434378461185.json, 平台全量/双采参考生视频_2117523762236186625.json, 视频生成/图生视频/H3-fasth3-omniref-图生视频_2114720509798731777.json, 视频生成/图生视频/Minimax 参考图模式_2109199755543924737.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_693

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/上传音频双采完美数字人-seiflite版_2119266434378461185.json、平台全量/双采参考生视频_2117523762236186625.json、视频生成/图生视频/H3-fasth3-omniref-图生视频_2114720509798731777.json、视频生成/图生视频/Minimax 参考图模式_2109199755543924737.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `LoadAudio` —— 3/4 个有
- `SelfLiftH3Sampler` —— 3/4 个有
- `VAEDecodeAudio` —— 3/4 个有
- `BasicGuider` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `RandomNoise` —— 2/4 个有
- `BlockSparseAttention` —— 1/4 个有
- `Bookmark (rgthree)` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `MiniMaxH3NativeAudioLock` —— 1/4 个有
- `SamplerCustomAdvanced` —— 1/4 个有
- `SelfLiftAvatarH3Sampler` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
