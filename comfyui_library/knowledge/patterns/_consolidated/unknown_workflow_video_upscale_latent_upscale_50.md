---
name: unknown_workflow_video_upscale_latent_upscale_50
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.948
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CR Text, CreateVideo, DualCLIPLoader, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, Int, KSamplerSelect, LTX2_NAG, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PIP_IntegerCalculator, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, VRAMReserver, easy cleanGpuUsed, easy convertAnything]
problems: []
missing: []
members: [视频生成/图生视频/2072859139281342465.json, 视频生成/文生视频/LTX2.3文生视频_2072522403787399169.json, 视频生成/文生视频/LTX2.3文生视频【切镜头优化版4】_2065674485692461057.json, 视频生成/文生视频/LTX2.3文生视频【切镜头优化版4】_2066698425961369602.json, 视频生成/文生视频/LTX2.3文生视频【切镜头优化版4】_2071506679061106690.json, 视频生成/文生视频/LTX2.3文生视频【切镜头优化版4】_2071853403160014850.json, 视频生成/文生视频/LTX2.3文生视频【切镜头优化版】_2066428134618124289.json, 视频生成/文生视频/LTX2.3文生视频【根据时间写剧情】_2067564577201672194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_50

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2072859139281342465.json、视频生成/文生视频/LTX2.3文生视频_2072522403787399169.json、视频生成/文生视频/LTX2.3文生视频【切镜头优化版4】_2065674485692461057.json、视频生成/文生视频/LTX2.3文生视频【切镜头优化版4】_2066698425961369602.json、视频生成/文生视频/LTX2.3文生视频【切镜头优化版4】_2071506679061106690.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `Int`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PIP_IntegerCalculator`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VRAMReserver`
- `easy cleanGpuUsed`
- `easy convertAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 8 | 100% |
| 高度 | 25 | 25 - 25 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，8 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
