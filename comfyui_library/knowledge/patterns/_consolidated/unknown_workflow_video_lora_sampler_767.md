---
name: unknown_workflow_video_lora_sampler_767
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6275
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, FloatToSigmas, ImageResizeKJ, KSamplerSelect, LTXVConditioning, LTXVLatentUpsampler, LTXVLatentUpsamplerModelLoader, LTXVLoopingSampler, LTXVTiledVAEDecode, LoraLoaderModelOnly, MultiPromptProvider, PrimitiveInt, PrintSigmas, RandomNoise, STGAdvancedPresets, STGGuiderAdvanced, Set VAE Decoder Noise, StringToFloatList, VAEEncode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1947704155776397313.json, 视频生成/图生视频/1947715360633040897.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_767

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1947704155776397313.json、视频生成/图生视频/1947715360633040897.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `FloatToSigmas`
- `ImageResizeKJ`
- `KSamplerSelect`
- `LTXVConditioning`
- `LTXVLatentUpsampler`
- `LTXVLatentUpsamplerModelLoader`
- `LTXVLoopingSampler`
- `LTXVTiledVAEDecode`
- `LoraLoaderModelOnly`
- `MultiPromptProvider`
- `PrimitiveInt`
- `PrintSigmas`
- `RandomNoise`
- `STGAdvancedPresets`
- `STGGuiderAdvanced`
- `Set VAE Decoder Noise`
- `StringToFloatList`
- `VAEEncode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
