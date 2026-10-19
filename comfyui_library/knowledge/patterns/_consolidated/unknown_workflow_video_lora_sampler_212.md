---
name: unknown_workflow_video_lora_sampler_212
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.640556
common_nodes: [GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageBatchMulti, LoadImage, LoadWanVideoT5TextEncoder, RepeatImageBatch, SetNode, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1992627593610588161.json, 视频生成/图生视频/1985341047272316930.json, 视频生成/图生视频/1985248262460481537.json, 视频生成/图生视频/2057618532237664258.json, 视频生成/图生视频/1998600702769422338.json, 视频生成/图生视频/1983506887171842049.json, 视频生成/图生视频/1982104863096086530.json, 视频生成/文生视频/6窗口-svi-film长视频生产_1983866504603172866.json, 视频生成/文生视频/网红制造WanVideoWrapper_I2V_SVI_长视频工作流_1988840595856691202.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_212

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1992627593610588161.json、视频生成/图生视频/1985341047272316930.json、视频生成/图生视频/1985248262460481537.json、视频生成/图生视频/2057618532237664258.json、视频生成/图生视频/1998600702769422338.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 9 个 workflow 都包含：
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
- `ImageResizeKJv2` —— 8/9 个有
- `CLIPVisionLoader` —— 7/9 个有
- `WanVideoClipVisionEncode` —— 7/9 个有
- `InvertMask` —— 6/9 个有
- `WanVideoVACEStartToEndFrame` —— 6/9 个有
- `WanVideoSetLoRAs` —— 5/9 个有
- `ColorMatch` —— 4/9 个有
- `easy showAnything` —— 3/9 个有
- `CLIPLoader` —— 2/9 个有
- `CLIPTextEncode` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `MathExpression|pysssss` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `PrimitiveStringMultiline` —— 2/9 个有
- `VRAM_Debug` —— 2/9 个有
- `WanVideoTextEmbedBridge` —— 2/9 个有
- `easy forLoopEnd` —— 2/9 个有
- `easy forLoopStart` —— 2/9 个有
- `AudioCrop` —— 1/9 个有
- `CR Text Input Switch (4 way)` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `Int` —— 1/9 个有
- `LoadAudio` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `RIFE VFI` —— 1/9 个有
- `String Literal` —— 1/9 个有
- `Text Load Line From File` —— 1/9 个有
- `easy promptLine` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
