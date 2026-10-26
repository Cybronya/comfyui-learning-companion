---
name: unknown_workflow_video_lora_sampler_922
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7755
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ImageScaleToTotalPixelsX, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, ModelAttentionBackend, PathchSageAttentionKJ, PreviewAny, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/minimax-h3-首尾无缝循环视频_2085721665069211650.json, 视频生成/图生视频/poster animation_2108798159089651714.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_922

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/minimax-h3-首尾无缝循环视频_2085721665069211650.json、视频生成/图生视频/poster animation_2108798159089651714.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ImageScaleToTotalPixelsX`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `EasyCache` —— 1/2 个有
- `GetVideoComponents` —— 1/2 个有
- `ImageBatchExtendWithOverlap` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LayerUtility: TextJoin` —— 1/2 个有
- `LoadVideo` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `VHS_SplitImages` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
