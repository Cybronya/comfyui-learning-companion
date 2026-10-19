---
name: unknown_workflow_lora_sampler_unet_54
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.884333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, GetVideoComponents, KSamplerSelect, LoadImage, LoadVideo, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3 图生视频动作模仿ref turbo加速_2087775662382862337.json, 视频生成/图生视频/MiniMax-H3 图生视频动作迁移二采放大_2093997320298909698.json, 视频生成/文生视频/Minimax H3 多参数视频生成 768p 加速 LoRA 两步生成_2095762977566846977.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_54

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3 图生视频动作模仿ref turbo加速_2087775662382862337.json、视频生成/图生视频/MiniMax-H3 图生视频动作迁移二采放大_2093997320298909698.json、视频生成/文生视频/Minimax H3 多参数视频生成 768p 加速 LoRA 两步生成_2095762977566846977.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `GetVideoComponents`
- `KSamplerSelect`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `LTXVConcatAVLatent` —— 2/3 个有
- `LTXVSeparateAVLatent` —— 2/3 个有
- `LoadAudio` —— 2/3 个有
- `MiniMaxH3BlockCacheT8` —— 2/3 个有
- `MinimaxH3LatentUpscaler3D` —— 2/3 个有
- `ModelPreviewOverrideKJ` —— 2/3 个有
- `PixaromaDuration` —— 2/3 个有
- `PixaromaSizes` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `TrimAudioDuration` —— 2/3 个有
- `VRAM_Debug` —— 2/3 个有
- `Video Slice` —— 2/3 个有
- `ComfyMathExpression` —— 1/3 个有
- `ManualSigmas` —— 1/3 个有
- `MiniMaxH3SigmaShift` —— 1/3 个有
- `ModelAttentionBackend` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
