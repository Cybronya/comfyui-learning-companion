---
name: unknown_workflow_lora_sampler_unet_129
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.866167
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/(8步加速-768P)Minimax图生视频V1_2085286536706351105.json, 视频生成/图生视频/(8步加速-768P)Minimax图生视频V1_2085553480567189505.json, 视频生成/图生视频/(fl)Minimax-H3官方8步极速工作流-V1正式版_2087281024626683906.json, 视频生成/图生视频/(fl)Minimax-H3官方8步极速工作流-V1正式版（自动反推版）_2087275070858289153.json, 视频生成/图生视频/(ref)Minimax-H3官方8步极速工作流-V1正式版(自动反推版)_2087167230646775810.json, 视频生成/图生视频/(ref)Minimax-H3官方8步极速工作流-V1正式版_2087271938422038530.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_129

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/(8步加速-768P)Minimax图生视频V1_2085286536706351105.json、视频生成/图生视频/(8步加速-768P)Minimax图生视频V1_2085553480567189505.json、视频生成/图生视频/(fl)Minimax-H3官方8步极速工作流-V1正式版_2087281024626683906.json、视频生成/图生视频/(fl)Minimax-H3官方8步极速工作流-V1正式版（自动反推版）_2087275070858289153.json、视频生成/图生视频/(ref)Minimax-H3官方8步极速工作流-V1正式版(自动反推版)_2087167230646775810.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 4/6 个有
- `SaveVideo` —— 4/6 个有
- `UniBlockSwap` —— 4/6 个有
- `VRAMReserver` —— 4/6 个有
- `CR Prompt Text` —— 2/6 个有
- `GetImageRangeFromBatch` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `LoadAudio` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `RHLLMChatNode` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `SaveVideoRGBA` —— 2/6 个有
- `StringFunction|pysssss` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `Vignette` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `BatchImagesNode` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
