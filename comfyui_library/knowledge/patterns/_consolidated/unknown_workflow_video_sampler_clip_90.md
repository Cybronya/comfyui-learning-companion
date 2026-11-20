---
name: unknown_workflow_video_sampler_clip_90
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.837429
common_nodes: [EmptyImage, Int, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy imageConcat, easy imageSize]
problems: []
missing: []
members: [平台全量/Wan2.1 首尾帧 （时间11分钟-5秒视频） 浮云12.17 备用_2001147373441122306.json, 视频生成/图生视频/Wan2.1 AI视频 首尾帧 丝滑动画过渡 工作流_1985915775540178945.json, 视频生成/图生视频/Wan2.1 AI视频首尾帧丝滑动画过渡工作流【AI小王子】_1918543439799975938.json, 视频生成/图生视频/Wan2.1 图生视频首尾帧_1919623628906758146.json, 视频生成/图生视频/Wan2.1+AI视频首尾帧丝滑动画过渡工作流【AI小王子】_1994010084806164482.json, 视频生成/图生视频/首尾帧生视频 _ wan2.1（KJ）_1902281686166740993.json, 视频生成/文生视频/视频首尾帧过渡工作流_1937406270641225729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_90

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/Wan2.1 首尾帧 （时间11分钟-5秒视频） 浮云12.17 备用_2001147373441122306.json、视频生成/图生视频/Wan2.1 AI视频 首尾帧 丝滑动画过渡 工作流_1985915775540178945.json、视频生成/图生视频/Wan2.1 AI视频首尾帧丝滑动画过渡工作流【AI小王子】_1918543439799975938.json、视频生成/图生视频/Wan2.1 图生视频首尾帧_1919623628906758146.json、视频生成/图生视频/Wan2.1+AI视频首尾帧丝滑动画过渡工作流【AI小王子】_1994010084806164482.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `EmptyImage`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy imageConcat`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CR Simple Image Compare` —— 6/7 个有
- `CR Text` —— 6/7 个有
- `ImageBatchRepeatInterleaving` —— 6/7 个有
- `ImageConcanate` —— 6/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `RH_Captioner` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `TextBox` —— 1/7 个有
- `Textbox` —— 1/7 个有
- `WanVideoExperimentalArgs` —— 1/7 个有
- `WanVideoFlowEdit` —— 1/7 个有
- `WanVideoLoopArgs` —— 1/7 个有
- `WanVideoVRAMManagement` —— 1/7 个有
- `easy textSwitch` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
