---
name: unknown_workflow_video_lora_sampler_148
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.718727
common_nodes: [GetNode, INTConstant, ImageConcatMulti, ImageResizeKJv2, LoadImage, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: [Text Multiline]
members: [图片生成/文生图/1967859229505761281.json, 视频生成/图生视频/1968454947522138113.json, 视频生成/图生视频/1967866937906724865.json, 视频生成/图生视频/1967847816360001537.json, 视频生成/图生视频/1967823701351739393.json, 视频生成/图生视频/1967789727392890881.json, 视频生成/图生视频/1968381285397868546.json, 视频生成/图生视频/1968419088865349633.json, 视频生成/图生视频/1967232757493534722.json, 视频生成/图生视频/1967220964087959554.json, 视频生成/图生视频/1967848289393606658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_148

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/1967859229505761281.json、视频生成/图生视频/1968454947522138113.json、视频生成/图生视频/1967866937906724865.json、视频生成/图生视频/1967847816360001537.json、视频生成/图生视频/1967823701351739393.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 11 个 workflow 都包含：
- `GetNode`
- `INTConstant`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoScheduler` —— 9/11 个有
- `CreateCFGScheduleFloatList` —— 7/11 个有
- `LayerUtility: TextJoin` —— 7/11 个有
- `RH_Captioner` —— 7/11 个有
- `DWPreprocessor` —— 6/11 个有
- `GetImageSizeAndCount` —— 6/11 个有
- `ImageBlend` —— 6/11 个有
- `VHS_LoadVideo` —— 6/11 个有
- `Zoe-DepthMapPreprocessor` —— 6/11 个有
- `WanVideoVACEStartToEndFrame` —— 5/11 个有
- `Text Multiline` —— 4/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `PrimitiveFloat` —— 2/11 个有
- `RH_Translator` —— 2/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `ImageStitch` —— 1/11 个有
- `LayerUtility: TextJoinV2` —— 1/11 个有
- `PreviewImage` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline
