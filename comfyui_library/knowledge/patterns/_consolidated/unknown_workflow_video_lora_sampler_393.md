---
name: unknown_workflow_video_lora_sampler_393
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.743333
common_nodes: [ApplyFaceProcessor, FaceProcessorLoader, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/wanvideo_Stand-In_高级用法_1956565549708967937.json, 数字人/数字人/最强视频换脸 wan stand in vace 版_1958711325885100034.json, 数字人/数字人/最强视频换脸 wan stand in_1958073826179428353.json, 数字人/数字人/视频换脸，视频重绘（Wan2.1+Standin+Vace）_1965963887017455617.json, 视频生成/图生视频/Stand-In+VACE一致性视频生成_1958065173116366849.json, 视频生成/图生视频/Stand-In+VACE视频换脸_1959340354166272002.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_393

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/wanvideo_Stand-In_高级用法_1956565549708967937.json、数字人/数字人/最强视频换脸 wan stand in vace 版_1958711325885100034.json、数字人/数字人/最强视频换脸 wan stand in_1958073826179428353.json、数字人/数字人/视频换脸，视频重绘（Wan2.1+Standin+Vace）_1965963887017455617.json、视频生成/图生视频/Stand-In+VACE一致性视频生成_1958065173116366849.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 6 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 5/6 个有
- `SimpleMath+` —— 5/6 个有
- `WanVideoVACEEncode` —— 5/6 个有
- `WanVideoVACEModelSelect` —— 5/6 个有
- `GetNode` —— 4/6 个有
- `INTConstant` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `WanVideoTorchCompileSettings` —— 4/6 个有
- `Anything Everywhere` —— 3/6 个有
- `WanVideoVACEStartToEndFrame` —— 3/6 个有
- `AIO_Preprocessor` —— 2/6 个有
- `CR Text` —— 2/6 个有
- `ImageFromBatch+` —— 2/6 个有
- `ImpactInt` —— 2/6 个有
- `JjkText` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `OpenposePreprocessor` —— 2/6 个有
- `TrimVideoLatent` —— 2/6 个有
- `VideoInputPreprocessor` —— 2/6 个有
- `easy imageRemBg` —— 2/6 个有
- `CM_IntToFloat` —— 1/6 个有
- `Int` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `Text` —— 1/6 个有
- `WanVideoEmptyEmbeds` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
