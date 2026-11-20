---
name: unknown_workflow_inpaint_sampler_clip_54
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8276
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, GetImageSize, ImageFromBatch, MaskPreview, OpticalFlowLoader, RandomNoise, SAM3_Detect, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VOIDInpaintConditioning, VOIDSampler, VOIDWarpedNoise, VOIDWarpedNoiseSource]
problems: []
missing: []
members: [平台全量/utility_void_video_inpainting_2056029583681572865.json, 平台全量/void_inpainting视频擦除_2055608720196947970.json, 平台全量/视频移除物体｜及其引起的所有物理交互一并移除｜Netflix VOID_2058081868557410306.json, 数字人/数字人/Void_video_inpainting视频重绘V2V元素移除_2061983021380751361.json, 数字人/数字人/void_inpainting视频擦除_2085652354971553794.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_54

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/utility_void_video_inpainting_2056029583681572865.json、平台全量/void_inpainting视频擦除_2055608720196947970.json、平台全量/视频移除物体｜及其引起的所有物理交互一并移除｜Netflix VOID_2058081868557410306.json、数字人/数字人/Void_video_inpainting视频重绘V2V元素移除_2061983021380751361.json、数字人/数字人/void_inpainting视频擦除_2085652354971553794.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `GetImageSize`
- `ImageFromBatch`
- `MaskPreview`
- `OpticalFlowLoader`
- `RandomNoise`
- `SAM3_Detect`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VOIDInpaintConditioning`
- `VOIDSampler`
- `VOIDWarpedNoise`
- `VOIDWarpedNoiseSource`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 4/5 个有
- `ComfySwitchNode` —— 4/5 个有
- `PrimitiveBoolean` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `TrimAudioDuration` —— 4/5 个有
- `VHS_VideoCombine` —— 4/5 个有
- `VHS_LoadVideo` —— 3/5 个有
- `VHS_VideoInfo` —— 3/5 个有
- `CreateVideo` —— 2/5 个有
- `GetVideoComponents` —— 2/5 个有
- `LoadVideo` —— 2/5 个有
- `SaveVideo` —— 2/5 个有
- `INTConstant` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
