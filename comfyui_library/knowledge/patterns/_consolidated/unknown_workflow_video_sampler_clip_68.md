---
name: unknown_workflow_video_sampler_clip_68
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.890444
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan-Fun视频首尾帧-KJ版_1905999669091307522.json, 视频生成/图生视频/Wan2.1 AI视频 首尾帧 丝滑动画过渡 工作流_1985915775540178945.json, 视频生成/图生视频/Wan2.1 AI视频首尾帧丝滑动画过渡工作流【AI小王子】_1918543439799975938.json, 视频生成/图生视频/Wan2.1 图生视频首尾帧_1919623628906758146.json, 视频生成/图生视频/Wan2.1+AI视频首尾帧丝滑动画过渡工作流【AI小王子】_1994010084806164482.json, 视频生成/图生视频/Wan2.1图生视频首尾帧_1905464146912006145.json, 视频生成/图生视频/通义万相Wan2.1Fun首尾帧图生视频TC加速_1907738859516342273.json, 视频生成/图生视频/首尾帧生视频 _ wan2.1（KJ）_1902281686166740993.json, 视频生成/文生视频/视频首尾帧过渡工作流_1937406270641225729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_68

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Wan-Fun视频首尾帧-KJ版_1905999669091307522.json、视频生成/图生视频/Wan2.1 AI视频 首尾帧 丝滑动画过渡 工作流_1985915775540178945.json、视频生成/图生视频/Wan2.1 AI视频首尾帧丝滑动画过渡工作流【AI小王子】_1918543439799975938.json、视频生成/图生视频/Wan2.1 图生视频首尾帧_1919623628906758146.json、视频生成/图生视频/Wan2.1+AI视频首尾帧丝滑动画过渡工作流【AI小王子】_1994010084806164482.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 8/9 个有
- `WanVideoTorchCompileSettings` —— 8/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `WanVideoEnhanceAVideo` —— 7/9 个有
- `easy cleanGpuUsed` —— 7/9 个有
- `easy imageSize` —— 7/9 个有
- `CR Text` —— 6/9 个有
- `EmptyImage` —— 6/9 个有
- `LayerUtility: PurgeVRAM` —— 6/9 个有
- `easy imageConcat` —— 6/9 个有
- `CR Simple Image Compare` —— 5/9 个有
- `ImageBatchRepeatInterleaving` —— 5/9 个有
- `ImageConcanate` —— 5/9 个有
- `WanVideoExperimentalArgs` —— 4/9 个有
- `ImageResizeKJ` —— 3/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `RH_Captioner` —— 1/9 个有
- `ShowText|pysssss` —— 1/9 个有
- `TextBox` —— 1/9 个有
- `TextInput_` —— 1/9 个有
- `Textbox` —— 1/9 个有
- `WanVideoFlowEdit` —— 1/9 个有
- `WanVideoLoopArgs` —— 1/9 个有
- `WanVideoVRAMManagement` —— 1/9 个有
- `easy textSwitch` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
