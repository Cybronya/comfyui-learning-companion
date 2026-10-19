---
name: unknown_workflow_sampler_unet_vae_200
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.831
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, EasyCache, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3 网格图参考生视频_2084506699142094850.json, 视频生成/图生视频/Minimax H3 多图参考生视频_2084688978254581762.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_200

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3 网格图参考生视频_2084506699142094850.json、视频生成/图生视频/Minimax H3 多图参考生视频_2084688978254581762.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `EasyCache`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `AnySwitch` —— 1/2 个有
- `DuckHideNode` —— 1/2 个有
- `Fast Bypasser (rgthree)` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MiniMaxH3BlockCacheT8` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/2 个有
- `TTP_text_mix` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
