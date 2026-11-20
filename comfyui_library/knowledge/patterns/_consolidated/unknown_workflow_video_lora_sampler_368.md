---
name: unknown_workflow_video_lora_sampler_368
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.950286
common_nodes: [INTConstant, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2图生视频-植物生长蔓延-kijai版工作流_1959544112867389442.json, 视频生成/图生视频/Wan2.2电商产品旋转360度轨道镜头-任意物体三视图IP多角度v1.2_2005434183445086209.json, 视频生成/图生视频/Wan2.2超级首尾帧KJ版_1952197474423353346.json, 视频生成/图生视频/Wan2.2首尾帧KJ版_1952270588733804545.json, 视频生成/图生视频/Wan2.2首尾帧Kijai版-上传首尾帧图片运行工作流！高清流畅好用！_2040755258175004674.json, 视频生成/图生视频/Wan2.2首尾帧Kijai版-上传首尾帧图片运行工作流！高清流畅好用！_2044660138820247554.json, 视频生成/图生视频/Wan2.2首尾帧图视频720超清版加速出视频_1950913701371117569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_368

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Wan2.2图生视频-植物生长蔓延-kijai版工作流_1959544112867389442.json、视频生成/图生视频/Wan2.2电商产品旋转360度轨道镜头-任意物体三视图IP多角度v1.2_2005434183445086209.json、视频生成/图生视频/Wan2.2超级首尾帧KJ版_1952197474423353346.json、视频生成/图生视频/Wan2.2首尾帧KJ版_1952270588733804545.json、视频生成/图生视频/Wan2.2首尾帧Kijai版-上传首尾帧图片运行工作流！高清流畅好用！_2040755258175004674.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `INTConstant`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 6/7 个有
- `GetImageSizeAndCount` —— 6/7 个有
- `ImageResizeKJv2` —— 6/7 个有
- `Int` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `easy clearCacheAll` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `PrimitiveString` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `easy promptReplace` —— 1/7 个有
- `easy seed` —— 1/7 个有
- `ttN text` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
