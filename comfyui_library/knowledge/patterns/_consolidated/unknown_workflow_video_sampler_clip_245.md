---
name: unknown_workflow_video_sampler_clip_245
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7345
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, GetNode, INTConstant, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVScheduler, LTXVSeparateAVLatent, LoadAudio, PreviewAudio, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, TrimAudioDuration, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/ltx2_s2v_2011018464567234562.json, 视频生成/文生视频/ltx2_i2v_gguf-t2v生产力速度起飞_2011349638749622274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_245

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/ltx2_s2v_2011018464567234562.json、视频生成/文生视频/ltx2_i2v_gguf-t2v生产力速度起飞_2011349638749622274.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `PreviewAudio`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `TrimAudioDuration`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 1/2 个有
- `DualCLIPLoaderGGUF` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LTXVImgToVideoInplace` —— 1/2 个有
- `LTXVPreprocess` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MelBandRoFormerModelLoader` —— 1/2 个有
- `MelBandRoFormerSampler` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
