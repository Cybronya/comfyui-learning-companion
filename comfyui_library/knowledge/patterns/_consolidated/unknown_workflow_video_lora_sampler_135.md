---
name: unknown_workflow_video_lora_sampler_135
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.602333
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, GetNode, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoScheduler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/动作舞蹈_骨骼迁移_不限时长版_2020834050457473026.json, 图片生成/文生图/腾讯最新开源SteadyDancer超完美动作迁移工作流_2006630138284351490.json, 视频生成/图生视频/2032112165968154626.json, 视频生成/图生视频/1996519049599270913.json, 视频生成/图生视频/1996568841872351234.json, 视频生成/图生视频/2017466618615439361.json, 视频生成/图生视频/2011405479620124674.json, 视频生成/图生视频/2011517668532162561.json, 视频生成/图生视频/1995783729840787458.json, 视频生成/图生视频/2039879176072732673.json, 视频生成/图生视频/2046114909657763841.json, 视频生成/图生视频/1996528847946399745.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_135

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/动作舞蹈_骨骼迁移_不限时长版_2020834050457473026.json、图片生成/文生图/腾讯最新开源SteadyDancer超完美动作迁移工作流_2006630138284351490.json、视频生成/图生视频/2032112165968154626.json、视频生成/图生视频/1996519049599270913.json、视频生成/图生视频/1996568841872351234.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoScheduler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 10/12 个有
- `ImageConcatMulti` —— 10/12 个有
- `WanVideoBlockSwap` —— 10/12 个有
- `WanVideoTorchCompileSettings` —— 9/12 个有
- `DrawViTPose` —— 8/12 个有
- `PoseAndFaceDetection` —— 8/12 个有
- `WanVideoSetBlockSwap` —— 8/12 个有
- `INTConstant` —— 5/12 个有
- `Int` —— 5/12 个有
- `PoseDetectionOneToAllAnimation` —— 4/12 个有
- `PrimitiveInt` —— 4/12 个有
- `PreviewImage` —— 3/12 个有
- `SimpleMath+` —— 3/12 个有
- `CR Text` —— 2/12 个有
- `Fast Groups Muter (rgthree)` —— 2/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/12 个有
- `TextInput_` —— 2/12 个有
- `Anything Everywhere3` —— 1/12 个有
- `CR Prompt Text` —— 1/12 个有
- `ImageConcanate` —— 1/12 个有
- `ImpactInt` —— 1/12 个有
- `JWInteger` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `LayerUtility: PurgeVRAM` —— 1/12 个有
- `MathExpression|pysssss` —— 1/12 个有
- `PrimitiveFloat` —— 1/12 个有
- `ToFloat` —— 1/12 个有
- `ttN float` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
