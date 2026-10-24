---
name: unknown_workflow_video_lora_sampler_409
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7036
common_nodes: [GetImageSizeAndCount, GetNode, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, OnnxDetectionModelLoader, PoseDetectionOneToAllAnimation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddOneToAllPoseEmbeds, WanVideoAddOneToAllReferenceEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/OneToAllAnimation 姿势迁移，Q版人物骨骼适配_1998982182737694722.json, 视频生成/图生视频/OneToAll视频姿势参考（骨骼绑定）_1998661075665047553.json, 视频生成/图生视频/OneToAll视频姿势参考（骨骼绑定）_1998721650784919553.json, 视频生成/图生视频/OneToAll视频姿势参考（骨骼绑定）_1999765252109631490.json, 视频生成/图生视频/OneToAll视频姿势参考（骨骼绑定）_2000385748819902466.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_409

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/OneToAllAnimation 姿势迁移，Q版人物骨骼适配_1998982182737694722.json、视频生成/图生视频/OneToAll视频姿势参考（骨骼绑定）_1998661075665047553.json、视频生成/图生视频/OneToAll视频姿势参考（骨骼绑定）_1998721650784919553.json、视频生成/图生视频/OneToAll视频姿势参考（骨骼绑定）_1999765252109631490.json、视频生成/图生视频/OneToAll视频姿势参考（骨骼绑定）_2000385748819902466.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 5 个 workflow 都包含：
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseDetectionOneToAllAnimation`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddOneToAllPoseEmbeds`
- `WanVideoAddOneToAllReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 4/5 个有
- `ImageConcatMulti` —— 4/5 个有
- `ImpactInt` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `Anything Everywhere` —— 1/5 个有
- `CR Prompt Text` —— 1/5 个有
- `DrawViTPose` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `PoseAndFaceDetection` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
