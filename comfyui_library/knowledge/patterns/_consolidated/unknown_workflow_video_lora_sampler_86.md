---
name: unknown_workflow_video_lora_sampler_86
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.954824
common_nodes: [INTConstant, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2图生视频-植物生长蔓延-kijai版工作流_1959544112867389442.json, 视频生成/图生视频/Wan2.2电商产品旋转360度轨道镜头-任意物体三视图IP多角度v1.2_2005434183445086209.json, 视频生成/图生视频/Wan2.2超级首尾帧KJ版_1952197474423353346.json, 视频生成/图生视频/Wan2.2首尾帧KJ版_1952270588733804545.json, 视频生成/图生视频/Wan2.2首尾帧Kijai版-上传首尾帧图片运行工作流！高清流畅好用！_2040755258175004674.json, 视频生成/图生视频/Wan2.2首尾帧Kijai版-上传首尾帧图片运行工作流！高清流畅好用！_2044660138820247554.json, 视频生成/图生视频/Wan2.2首尾帧图视频720超清版加速出视频_1950913701371117569.json, 视频生成/图生视频/wan2.2图生视频-标准版-(必收藏)_2059069738726285313.json, 视频生成/图生视频/wan2.2首尾帧kj图生视频+加速版=艾橘溪_1904943116204576769.json, 视频生成/图生视频/wan2.2首尾帧kj图生视频+加速版_2042949137406103554.json, 视频生成/图生视频/wan2.2首尾帧kj图生视频+加速版_2043184542202208257.json, 视频生成/图生视频/wan2.2首尾帧kj图生视频+加速版_2044662528826941441.json, 视频生成/图生视频/wan2.2首尾帧kj图生视频+加速版_2075046170388422658.json, 视频生成/图生视频/图生视频加速版-wan2.2首尾帧_2047121992129712129.json, 视频生成/图生视频/图生视频加速版-wan2.2首尾帧_2048604067320045570.json, 视频生成/图生视频/图生视频加速版-wan2.2首尾帧_2048924949674463234.json, 视频生成/图生视频/图生视频加速版-wan2.2首尾帧_2072871692606726146.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_86

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/Wan2.2图生视频-植物生长蔓延-kijai版工作流_1959544112867389442.json、视频生成/图生视频/Wan2.2电商产品旋转360度轨道镜头-任意物体三视图IP多角度v1.2_2005434183445086209.json、视频生成/图生视频/Wan2.2超级首尾帧KJ版_1952197474423353346.json、视频生成/图生视频/Wan2.2首尾帧KJ版_1952270588733804545.json、视频生成/图生视频/Wan2.2首尾帧Kijai版-上传首尾帧图片运行工作流！高清流畅好用！_2040755258175004674.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 17 个 workflow 都包含：
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 16/17 个有
- `ImageResizeKJv2` —— 16/17 个有
- `WanVideoTorchCompileSettings` —— 16/17 个有
- `easy cleanGpuUsed` —— 12/17 个有
- `Int` —— 11/17 个有
- `MathExpression|pysssss` —— 11/17 个有
- `easy clearCacheAll` —— 11/17 个有
- `CR Text` —— 10/17 个有
- `PrimitiveFloat` —— 10/17 个有
- `LayerUtility: PurgeVRAM` —— 9/17 个有
- `GetImageSizeAndCount` —— 6/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/17 个有
- `easy seed` —— 2/17 个有
- `LayerUtility: PurgeVRAM V2` —— 1/17 个有
- `PrimitiveString` —— 1/17 个有
- `ShowText|pysssss` —— 1/17 个有
- `easy promptReplace` —— 1/17 个有
- `ttN text` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
