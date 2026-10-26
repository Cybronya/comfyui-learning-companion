---
name: unknown_workflow_video_lora_sampler_230
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.875667
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PrimitiveInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/反推提示词/MiniCPM4.5视频反推提示词+图生视频_1966696077435056130.json, 图片生成/反推提示词/MiniCPM4.5视频反推提示词_2072539419097264129.json, 图片生成/反推提示词/MiniCPM4.5视频反推提示词_2072540868833267714.json, 图片生成/反推提示词/MiniCPM4.5视频反推提示词_2072550656325537793.json, 视频生成/图生视频/WAN2.2图生视频(更新优化版）_2019998989524934657.json, 视频生成/图生视频/Wan2.2图生视频720P高清版自动提示词_1975197329210871809.json, 视频生成/图生视频/Wan2.2首尾帧工作流_1976854157967740929.json, 视频生成/图生视频/发布Wan2.2图生视频——优化版_1983835133948174337.json, 视频生成/文生视频/MiniCPM4.5视频反推+图生视频+文生视频_2003004980099465217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_230

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/MiniCPM4.5视频反推提示词+图生视频_1966696077435056130.json、图片生成/反推提示词/MiniCPM4.5视频反推提示词_2072539419097264129.json、图片生成/反推提示词/MiniCPM4.5视频反推提示词_2072540868833267714.json、图片生成/反推提示词/MiniCPM4.5视频反推提示词_2072550656325537793.json、视频生成/图生视频/WAN2.2图生视频(更新优化版）_2019998989524934657.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 8/9 个有
- `ShowText|pysssss` —— 8/9 个有
- `WanVideoTorchCompileSettings` —— 8/9 个有
- `AILab_MiniCPM_4_V_Advanced` —— 7/9 个有
- `Fast Groups Bypasser (rgthree)` —— 5/9 个有
- `INTConstant` —— 5/9 个有
- `ImageFromBatch+` —— 5/9 个有
- `LoadVideo` —— 5/9 个有
- `SaveImage` —— 5/9 个有
- `ShellAgentPluginOutputText` —— 5/9 个有
- `WanVideoEmptyEmbeds` —— 5/9 个有
- `Wan_video_prompt_generator` —— 5/9 个有
- `AILab_QwenVL` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
