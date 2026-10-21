---
name: unknown_workflow_video_sampler_clip_71
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.87675
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1905999669091307522.json, 视频生成/图生视频/1985915775540178945.json, 视频生成/图生视频/1918543439799975938.json, 视频生成/图生视频/1919623628906758146.json, 视频生成/图生视频/1994010084806164482.json, 视频生成/图生视频/1907738859516342273.json, 视频生成/图生视频/1902281686166740993.json, 视频生成/文生视频/1937406270641225729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_71

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1905999669091307522.json、视频生成/图生视频/1985915775540178945.json、视频生成/图生视频/1918543439799975938.json、视频生成/图生视频/1919623628906758146.json、视频生成/图生视频/1994010084806164482.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
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
- `Int` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `WanVideoEnhanceAVideo` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `easy cleanGpuUsed` —— 7/8 个有
- `easy imageSize` —— 7/8 个有
- `CR Text` —— 6/8 个有
- `EmptyImage` —— 6/8 个有
- `LayerUtility: PurgeVRAM` —— 6/8 个有
- `easy imageConcat` —— 6/8 个有
- `CR Simple Image Compare` —— 5/8 个有
- `ImageBatchRepeatInterleaving` —— 5/8 个有
- `ImageConcanate` —— 5/8 个有
- `WanVideoExperimentalArgs` —— 3/8 个有
- `ImageResizeKJ` —— 2/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `RH_Captioner` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `TextBox` —— 1/8 个有
- `Textbox` —— 1/8 个有
- `WanVideoFlowEdit` —— 1/8 个有
- `WanVideoLoopArgs` —— 1/8 个有
- `WanVideoVRAMManagement` —— 1/8 个有
- `easy textSwitch` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
