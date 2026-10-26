---
name: unknown_workflow_inpaint_sampler_clip_82
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8295
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, ComfySwitchNode, GetImageSize, ImageFromBatch, MaskPreview, OpticalFlowLoader, PrimitiveBoolean, PrimitiveInt, RandomNoise, SAM3_Detect, SamplerCustomAdvanced, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VOIDInpaintConditioning, VOIDSampler, VOIDWarpedNoise, VOIDWarpedNoiseSource]
problems: []
missing: []
members: [数字人/数字人/Void_video_inpainting视频重绘V2V元素移除_2061983021380751361.json, 数字人/数字人/void_inpainting视频擦除_2085652354971553794.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_82

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/Void_video_inpainting视频重绘V2V元素移除_2061983021380751361.json、数字人/数字人/void_inpainting视频擦除_2085652354971553794.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `GetImageSize`
- `ImageFromBatch`
- `MaskPreview`
- `OpticalFlowLoader`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `SAM3_Detect`
- `SamplerCustomAdvanced`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VOIDInpaintConditioning`
- `VOIDSampler`
- `VOIDWarpedNoise`
- `VOIDWarpedNoiseSource`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `GetVideoComponents` —— 1/2 个有
- `LoadVideo` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
