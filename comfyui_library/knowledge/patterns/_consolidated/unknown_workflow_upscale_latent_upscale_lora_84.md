---
name: unknown_workflow_upscale_latent_upscale_lora_84
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.861
common_nodes: [BasicGuider, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, GetVideoComponents, ImageFromBatch, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveAudio, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3_LTX2.5二次采样放大V0.1版_2092438276169879553.json, 视频生成/文生视频/MiniMaxH3_LTX2.5放大_2096200687985192962.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_84

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3_LTX2.5二次采样放大V0.1版_2092438276169879553.json、视频生成/文生视频/MiniMaxH3_LTX2.5放大_2096200687985192962.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `GetVideoComponents`
- `ImageFromBatch`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveAudio`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `PerturbedAttention` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
