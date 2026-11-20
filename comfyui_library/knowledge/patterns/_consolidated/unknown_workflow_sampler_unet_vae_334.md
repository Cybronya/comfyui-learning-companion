---
name: unknown_workflow_sampler_unet_vae_334
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.767333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyAndNode, ComfyMathExpression, CreateVideo, EasyCache, EmptyImage, KSamplerSelect, Light-Tool: LoadImageFromURL, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, StringFromList, StringLength, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy compare, easy ifElse, easy int, easy lengthAnything, easy promptLine, easy string]
problems: []
missing: []
members: [平台全量/全能H3-建议API+Agent调用_2119037964423622658.json, 视频生成/文生视频/MinimaxH3-全参生视频-加速-API专用_2096908346543665153.json, 视频生成/文生视频/MinimaxH3-首尾帧生视频-加速-API专用_2097606743491698689.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_334

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/全能H3-建议API+Agent调用_2119037964423622658.json、视频生成/文生视频/MinimaxH3-全参生视频-加速-API专用_2096908346543665153.json、视频生成/文生视频/MinimaxH3-首尾帧生视频-加速-API专用_2097606743491698689.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
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
- `EmptyAudio` —— 2/3 个有
- `MiniMaxH3ReferenceToVideo` —— 2/3 个有
- `VHS_LoadAudio` —— 2/3 个有
- `VHS_LoadVideoPath` —— 2/3 个有
- `MiniMaxH3ImageToVideo` —— 1/3 个有
- `PreviewVideoNode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
