---
name: unknown_workflow_sampler_unet_vae_330
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7905
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyAndNode, ComfyMathExpression, CreateVideo, EasyCache, EmptyImage, KSamplerSelect, Light-Tool: LoadImageFromURL, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, StringFromList, StringLength, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy compare, easy ifElse, easy int, easy lengthAnything, easy promptLine, easy string]
problems: []
missing: []
members: [视频生成/文生视频/MinimaxH3-全参生视频-加速-API专用_2096908346543665153.json, 视频生成/文生视频/MinimaxH3-首尾帧生视频-加速-API专用_2097606743491698689.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_330

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MinimaxH3-全参生视频-加速-API专用_2096908346543665153.json、视频生成/文生视频/MinimaxH3-首尾帧生视频-加速-API专用_2097606743491698689.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyAndNode`
- `ComfyMathExpression`
- `CreateVideo`
- `EasyCache`
- `EmptyImage`
- `KSamplerSelect`
- `Light-Tool: LoadImageFromURL`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `StringFromList`
- `StringLength`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy compare`
- `easy ifElse`
- `easy int`
- `easy lengthAnything`
- `easy promptLine`
- `easy string`

**可变部分**（部分 workflow 才有）：
- `EmptyAudio` —— 1/2 个有
- `MiniMaxH3ImageToVideo` —— 1/2 个有
- `MiniMaxH3ReferenceToVideo` —— 1/2 个有
- `VHS_LoadAudio` —— 1/2 个有
- `VHS_LoadVideoPath` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
