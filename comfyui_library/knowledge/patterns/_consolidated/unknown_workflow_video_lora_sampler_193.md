---
name: unknown_workflow_video_lora_sampler_193
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8728
common_nodes: [GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, PrimitiveInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-SmoothMix-V2文生视频，高动态_1979771248119025665.json, 视频生成/图生视频/Wan2.2-SmoothMix图生视频首中尾帧_1981252954491617282.json, 视频生成/图生视频/Wan2.2-SmoothMix图生视频首中尾帧自动提示词版_1979812385382895618.json, 视频生成/图生视频/Wan2.2SmoothMix高动态首尾帧自动提示词版_1979805991325831170.json, 视频生成/图生视频/Wan2.2取视频首尾帧生成视频自动提示词版_1974477475709366273.json, 视频生成/图生视频/Wan2.2图生视频首中尾帧自动提示词版_1976126127594975233.json, 视频生成/图生视频/Wan2.2提取视频首尾帧生成视频_1974460906073665538.json, 视频生成/图生视频/Wan2.2首尾帧自动提示词版_1975958977194405889.json, 视频生成/图生视频/全网首发首中尾无缝视频生成（自动反推首尾图提示词）_1982464473032212482.json, 视频生成/文生视频/MiniCPM4.5视频反推+图生视频+文生视频_2003004980099465217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_193

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-SmoothMix-V2文生视频，高动态_1979771248119025665.json、视频生成/图生视频/Wan2.2-SmoothMix图生视频首中尾帧_1981252954491617282.json、视频生成/图生视频/Wan2.2-SmoothMix图生视频首中尾帧自动提示词版_1979812385382895618.json、视频生成/图生视频/Wan2.2SmoothMix高动态首尾帧自动提示词版_1979805991325831170.json、视频生成/图生视频/Wan2.2取视频首尾帧生成视频自动提示词版_1974477475709366273.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `GetImageSizeAndCount`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 9/10 个有
- `WanVideoImageToVideoEncode` —— 9/10 个有
- `SimpleMath+` —— 8/10 个有
- `WanVideoTorchCompileSettings` —— 8/10 个有
- `AILab_MiniCPM_4_V_Advanced` —— 7/10 个有
- `ShowText|pysssss` —— 7/10 个有
- `ImageBatchMultiple+` —— 6/10 个有
- `CLIPVisionLoader` —— 5/10 个有
- `CR Text` —— 5/10 个有
- `WanVideoClipVisionEncode` —— 5/10 个有
- `WanVideoLoraSelect` —— 5/10 个有
- `ImageFromBatch+` —— 4/10 个有
- `WanVideoContextOptions` —— 4/10 个有
- `WanVideoEncodeLatentBatch` —— 4/10 个有
- `PreviewImage` —— 3/10 个有
- `SaveImage` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `VHS_VideoInfo` —— 2/10 个有
- `WanVideoEmptyEmbeds` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `INTConstant` —— 1/10 个有
- `LoadVideo` —— 1/10 个有
- `RH_Nano_Banana_Image2Image` —— 1/10 个有
- `ShellAgentPluginOutputText` —— 1/10 个有
- `Wan_video_prompt_generator` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
