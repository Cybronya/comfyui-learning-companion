---
name: unknown_workflow_video_lora_sampler_182
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.720909
common_nodes: [GetNode, INTConstant, ImageConcatMulti, ImageResizeKJv2, LoadImage, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/【KJ加速版】wan2.2 Fun VACE图生视频_1967859229505761281.json, 视频生成/图生视频/KJ版 wan2.2-Fun-VACE动作迁移-美女跳舞_1968454947522138113.json, 视频生成/图生视频/wan2.2 Fun VACE 图生视频 KJ_1967866937906724865.json, 视频生成/图生视频/wan2.2 Fun VACE 舞蹈动作迁移 KJ_1967847816360001537.json, 视频生成/图生视频/wan2.2 Fun VACE首尾帧 KJ工作流_1967823701351739393.json, 视频生成/图生视频/wan2.2-Fun-VACE动作迁移-KJ_1967789727392890881.json, 视频生成/图生视频/wan2.2-Fun-VACE动作迁移-KJ_1968381285397868546.json, 视频生成/图生视频/wan2.2-Fun-VACE单图生视频-KJ版_1968419088865349633.json, 视频生成/图生视频/wan2.2-Fun-VACE突击侦查动作迁移-KJ_1967232757493534722.json, 视频生成/图生视频/wan2.2-Fun-VACE舞蹈动作迁移-KJ_1967220964087959554.json, 视频生成/图生视频/wan2.2-Fun-VACE首尾帧-KJ_1967848289393606658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_182

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/【KJ加速版】wan2.2 Fun VACE图生视频_1967859229505761281.json、视频生成/图生视频/KJ版 wan2.2-Fun-VACE动作迁移-美女跳舞_1968454947522138113.json、视频生成/图生视频/wan2.2 Fun VACE 图生视频 KJ_1967866937906724865.json、视频生成/图生视频/wan2.2 Fun VACE 舞蹈动作迁移 KJ_1967847816360001537.json、视频生成/图生视频/wan2.2 Fun VACE首尾帧 KJ工作流_1967823701351739393.json…）

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

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
