---
name: unknown_workflow_video_lora_sampler_309
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.656714
common_nodes: [GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageBatchMulti, LoadImage, LoadWanVideoT5TextEncoder, RepeatImageBatch, SetNode, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/SVI稳定长视频生成【无限循环】_1983506887171842049.json, 视频生成/图生视频/SVI长视频_1982104863096086530.json, 视频生成/图生视频/SVI长镜头分段提示词工作流_1981341961615474690.json, 视频生成/图生视频/Stable Video Infinity+Wan2.2：生成无限时长AI视频工作流实测！_2000388407983566850.json, 视频生成/图生视频/Stable Video Infinity，生成10分钟时长AI视频，ComfyUI工作流大公开！_1986760720148852738.json, 视频生成/图生视频/无限视频SVI-Wan22_1999143356380966913.json, 视频生成/文生视频/网红制造WanVideoWrapper_I2V_SVI_长视频工作流_1988840595856691202.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_309

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/SVI稳定长视频生成【无限循环】_1983506887171842049.json、视频生成/图生视频/SVI长视频_1982104863096086530.json、视频生成/图生视频/SVI长镜头分段提示词工作流_1981341961615474690.json、视频生成/图生视频/Stable Video Infinity+Wan2.2：生成无限时长AI视频工作流实测！_2000388407983566850.json、视频生成/图生视频/Stable Video Infinity，生成10分钟时长AI视频，ComfyUI工作流大公开！_1986760720148852738.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 7 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `RepeatImageBatch`
- `SetNode`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 6/7 个有
- `CLIPVisionLoader` —— 5/7 个有
- `InvertMask` —— 5/7 个有
- `WanVideoClipVisionEncode` —— 5/7 个有
- `WanVideoVACEStartToEndFrame` —— 5/7 个有
- `ColorMatch` —— 4/7 个有
- `WanVideoSetLoRAs` —— 4/7 个有
- `easy forLoopEnd` —— 3/7 个有
- `easy forLoopStart` —— 3/7 个有
- `Label (rgthree)` —— 2/7 个有
- `MathExpression|pysssss` —— 2/7 个有
- `PrimitiveStringMultiline` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `AudioCrop` —— 1/7 个有
- `CR Text Input Switch (4 way)` —— 1/7 个有
- `Int` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `LoadAudio` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `RIFE VFI` —— 1/7 个有
- `easy promptLine` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
