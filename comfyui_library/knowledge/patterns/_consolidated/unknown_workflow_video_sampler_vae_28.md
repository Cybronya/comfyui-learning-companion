---
name: unknown_workflow_video_sampler_vae_28
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.881231
common_nodes: [GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, PrimitiveInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-SmoothMix-V2文生视频，高动态_1979771248119025665.json, 视频生成/图生视频/Wan2.2-SmoothMix图生视频首中尾帧_1981252954491617282.json, 视频生成/图生视频/Wan2.2-SmoothMix图生视频首中尾帧自动提示词版_1979812385382895618.json, 视频生成/图生视频/Wan2.2SmoothMix高动态首尾帧自动提示词版_1979805991325831170.json, 视频生成/图生视频/Wan2.2取视频首尾帧生成视频自动提示词版_1974477475709366273.json, 视频生成/图生视频/Wan2.2图生视频720P高清版_1975403680918843394.json, 视频生成/图生视频/Wan2.2图生视频KJ加速版_1950013972280950785.json, 视频生成/图生视频/Wan2.2图生视频首中尾帧自动提示词版_1976126127594975233.json, 视频生成/图生视频/Wan2.2提取视频首尾帧生成视频_1974460906073665538.json, 视频生成/图生视频/Wan2.2首尾帧KJ版_1963509971877072897.json, 视频生成/图生视频/Wan2.2首尾帧自动提示词版_1975958977194405889.json, 视频生成/图生视频/Wan2.2高动态图生视频Smooth_1977734210951729153.json, 视频生成/图生视频/全网首发首中尾无缝视频生成（自动反推首尾图提示词）_1982464473032212482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_28

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-SmoothMix-V2文生视频，高动态_1979771248119025665.json、视频生成/图生视频/Wan2.2-SmoothMix图生视频首中尾帧_1981252954491617282.json、视频生成/图生视频/Wan2.2-SmoothMix图生视频首中尾帧自动提示词版_1979812385382895618.json、视频生成/图生视频/Wan2.2SmoothMix高动态首尾帧自动提示词版_1979805991325831170.json、视频生成/图生视频/Wan2.2取视频首尾帧生成视频自动提示词版_1974477475709366273.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
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
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 12/13 个有
- `SimpleMath+` —— 12/13 个有
- `WanVideoImageToVideoEncode` —— 12/13 个有
- `WanVideoSetLoRAs` —— 12/13 个有
- `WanVideoTorchCompileSettings` —— 11/13 个有
- `CLIPVisionLoader` —— 8/13 个有
- `CR Text` —— 8/13 个有
- `WanVideoClipVisionEncode` —— 8/13 个有
- `WanVideoLoraSelect` —— 7/13 个有
- `AILab_MiniCPM_4_V_Advanced` —— 6/13 个有
- `ImageBatchMultiple+` —— 6/13 个有
- `ShowText|pysssss` —— 6/13 个有
- `WanVideoContextOptions` —— 4/13 个有
- `WanVideoEncodeLatentBatch` —— 4/13 个有
- `ImageFromBatch+` —— 3/13 个有
- `PreviewImage` —— 3/13 个有
- `VHS_LoadVideo` —— 2/13 个有
- `VHS_VideoInfo` —— 2/13 个有
- `RH_Nano_Banana_Image2Image` —— 1/13 个有
- `SaveImage` —— 1/13 个有
- `WanVideoEmptyEmbeds` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
