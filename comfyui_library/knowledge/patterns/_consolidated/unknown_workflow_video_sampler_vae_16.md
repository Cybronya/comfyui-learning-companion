---
name: unknown_workflow_video_sampler_vae_16
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.929733
common_nodes: [GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2图生视频(更新优化版）_2019998989524934657.json, 视频生成/图生视频/WAN2.2图生视频_1950137059535183873.json, 视频生成/图生视频/WAN2.2图生视频快速流KJ版i2V_1949391348926971905.json, 视频生成/图生视频/Wan2.2 I2V KJ图生视频基础版 Borges_1951966233606434817.json, 视频生成/图生视频/Wan2.2图生视频720P高清版_1975403680918843394.json, 视频生成/图生视频/Wan2.2图生视频720P高清版自动提示词_1975197329210871809.json, 视频生成/图生视频/Wan2.2图生视频KJ加速版_1950013972280950785.json, 视频生成/图生视频/Wan2.2图生视频_1973774773308231682.json, 视频生成/图生视频/Wan2.2图生视频_2072884554280562690.json, 视频生成/图生视频/Wan2.2图生视频_2072885775900958721.json, 视频生成/图生视频/Wan2.2图生视频吊打付费网站效果_1950068834109710337.json, 视频生成/图生视频/Wan2.2首尾帧KJ版_1963509971877072897.json, 视频生成/图生视频/Wan2.2首尾帧工作流_1976854157967740929.json, 视频生成/图生视频/Wan2.2高动态图生视频Smooth_1977734210951729153.json, 视频生成/图生视频/【KJ加速版】Wan2.2 图生视频_1953401583553925122.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_16

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/WAN2.2图生视频(更新优化版）_2019998989524934657.json、视频生成/图生视频/WAN2.2图生视频_1950137059535183873.json、视频生成/图生视频/WAN2.2图生视频快速流KJ版i2V_1949391348926971905.json、视频生成/图生视频/Wan2.2 I2V KJ图生视频基础版 Borges_1951966233606434817.json、视频生成/图生视频/Wan2.2图生视频720P高清版_1975403680918843394.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 15 个 workflow 都包含：
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 14/15 个有
- `WanVideoSetLoRAs` —— 14/15 个有
- `CR Text` —— 13/15 个有
- `WanVideoTorchCompileSettings` —— 13/15 个有
- `CLIPVisionLoader` —— 11/15 个有
- `WanVideoClipVisionEncode` —— 11/15 个有
- `PrimitiveInt` —— 10/15 个有
- `SimpleMath+` —— 6/15 个有
- `DownloadAndLoadGIMMVFIModel` —— 4/15 个有
- `GIMMVFI_interpolate` —— 4/15 个有
- `ShowText|pysssss` —— 2/15 个有
- `AILab_MiniCPM_4_V_Advanced` —— 1/15 个有
- `AILab_QwenVL` —— 1/15 个有
- `AudioCrop` —— 1/15 个有
- `ImageFromBatch+` —— 1/15 个有
- `LoadAudio` —— 1/15 个有
- `Note Plus (mtb)` —— 1/15 个有
- `PrimitiveStringMultiline` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
