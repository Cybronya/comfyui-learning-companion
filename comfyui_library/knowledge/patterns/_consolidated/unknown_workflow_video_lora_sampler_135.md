---
name: unknown_workflow_video_lora_sampler_135
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.608733
common_nodes: [CLIPVisionLoader, DrawViTPose, GetImageRangeFromBatch, GetNode, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/动作迁移视频生视频_2042064025676156929.json, 平台全量/最新动作迁移动物美女舞蹈必备 超强一致性_2042037980784762881.json, 数字人/数字人/最新SteadyDancer动作迁移动物美女舞蹈必备 超强一致性_1996288612700397569.json, 视频生成/图生视频/SteadDancer （KJ版）视频姿势参考_1996519049599270913.json, 视频生成/图生视频/SteadDancer动作迁移_1996568841872351234.json, 视频生成/图生视频/SteadDancer自适应骨骼绑定动作迁移_1995783729840787458.json, 视频生成/图生视频/SteadDancer自适应骨骼绑定动作迁移，超级Nice!好用到爆!_2039879176072732673.json, 视频生成/图生视频/SteadDancer自适应骨骼绑定动作迁移，超级Nice!好用到爆!_2046114909657763841.json, 视频生成/图生视频/SteadDancer视频姿势参考（KJ）_1996528847946399745.json, 视频生成/图生视频/SteadDancer视频自适应绑定动作迁移_1996396266479296514.json, 视频生成/图生视频/SteadyDancer动作迁移_1995679581803778050.json, 视频生成/图生视频/SteadyDancer动作迁移_2073284965781032961.json, 视频生成/图生视频/SteadyDancer动作迁移视频生视频_1996042760450981890.json, 视频生成/图生视频/SteadyDancer动作迁移视频生视频_2069666439010807809.json, 视频生成/图生视频/动作模仿-动作迁移-和谐连贯的人像动画与首帧保留_1996439442132975617.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_135

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（平台全量/动作迁移视频生视频_2042064025676156929.json、平台全量/最新动作迁移动物美女舞蹈必备 超强一致性_2042037980784762881.json、数字人/数字人/最新SteadyDancer动作迁移动物美女舞蹈必备 超强一致性_1996288612700397569.json、视频生成/图生视频/SteadDancer （KJ版）视频姿势参考_1996519049599270913.json、视频生成/图生视频/SteadDancer动作迁移_1996568841872351234.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 14/15 个有
- `WanVideoContextOptions` —— 14/15 个有
- `WanVideoScheduler` —— 13/15 个有
- `WanVideoTextEncodeCached` —— 13/15 个有
- `WanVideoTorchCompileSettings` —— 12/15 个有
- `INTConstant` —— 10/15 个有
- `ImageConcatMulti` —— 10/15 个有
- `WanVideoSetBlockSwap` —— 10/15 个有
- `WanVideoSetLoRAs` —— 10/15 个有
- `easy cleanGpuUsed` —— 6/15 个有
- `easy clearCacheAll` —— 6/15 个有
- `PreviewImage` —— 4/15 个有
- `AddLabel` —— 2/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/15 个有
- `LoadWanVideoT5TextEncoder` —— 2/15 个有
- `MathExpression|pysssss` —— 2/15 个有
- `WanVideoTextEncode` —— 2/15 个有
- `Anything Everywhere3` —— 1/15 个有
- `DF_Int_to_Float` —— 1/15 个有
- `ImageConcanate` —— 1/15 个有
- `ImpactInt` —— 1/15 个有
- `PrimitiveInt` —— 1/15 个有
- `ToFloat` —— 1/15 个有
- `WanVideoImageResizeToClosest` —— 1/15 个有
- `easy int` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
