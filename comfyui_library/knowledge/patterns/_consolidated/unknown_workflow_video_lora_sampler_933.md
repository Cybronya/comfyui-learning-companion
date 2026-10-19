---
name: unknown_workflow_video_lora_sampler_933
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.976
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, GetVideoComponents, ImageScaleToMaxDimension, KSamplerSelect, LTXAVTextEncoderLoader, LTXVConditioning, LTXVLoopingSampler, LTXVSpatioTemporalTiledVAEDecode, LoadVideo, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SaveVideo, VAEEncodeTiled, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [视频生成/文生视频/LTX 2.3 循环采样放大优化_2041055276513628161.json, 视频生成/文生视频/LTX-2视频放大_2010029707667968001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_933

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/LTX 2.3 循环采样放大优化_2041055276513628161.json、视频生成/文生视频/LTX-2视频放大_2010029707667968001.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `GetVideoComponents`
- `ImageScaleToMaxDimension`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVConditioning`
- `LTXVLoopingSampler`
- `LTXVSpatioTemporalTiledVAEDecode`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SaveVideo`
- `VAEEncodeTiled`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/2 个有
- `DisTorchPurgeVRAMV2` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `DualCLIPLoaderGGUF` —— 1/2 个有
- `LTX2_NAG` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `VAELoaderKJ` —— 1/2 个有
- `VRAMReserver` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
