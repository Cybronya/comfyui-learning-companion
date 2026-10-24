---
name: unknown_workflow_lora_sampler_unet_310
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.889
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfySwitchNode, CreateVideo, Fast Groups Bypasser (rgthree), GetVideoComponents, ImageConcatMulti, ImageResizeKJv2, KSamplerSelect, LoadAudio, LoadImage, LoadVideo, LoraLoaderModelOnly, MiniMaxH3BlockCacheT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PixaromaDuration, PixaromaSizes, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VRAM_Debug, Video Slice]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3 图生视频动作模仿ref turbo加速_2087775662382862337.json, 视频生成/图生视频/MiniMax-H3 图生视频动作迁移二采放大_2093997320298909698.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_310

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3 图生视频动作模仿ref turbo加速_2087775662382862337.json、视频生成/图生视频/MiniMax-H3 图生视频动作迁移二采放大_2093997320298909698.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfySwitchNode`
- `CreateVideo`
- `Fast Groups Bypasser (rgthree)`
- `GetVideoComponents`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3BlockCacheT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PixaromaDuration`
- `PixaromaSizes`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VRAM_Debug`
- `Video Slice`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 1/2 个有
- `LTXVSeparateAVLatent` —— 1/2 个有
- `ManualSigmas` —— 1/2 个有
- `MinimaxH3LatentUpscaler3D` —— 1/2 个有
- `ModelPreviewOverrideKJ` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
