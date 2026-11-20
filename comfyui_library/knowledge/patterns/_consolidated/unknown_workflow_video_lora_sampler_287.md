---
name: unknown_workflow_video_lora_sampler_287
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9706
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2图生视频_1950137059535183873.json, 视频生成/图生视频/WAN2.2图生视频快速流KJ版i2V_1949391348926971905.json, 视频生成/图生视频/Wan2.2  高帧率高清｜图生视频稳定版_1950383603089891330.json, 视频生成/图生视频/Wan2.2 I2V KJ图生视频基础版 Borges_1951966233606434817.json, 视频生成/图生视频/Wan2.2 Kj-图生视频工作流_1956914143121039362.json, 视频生成/图生视频/Wan2.2 图生视频一键工作流_2032825101573431298.json, 视频生成/图生视频/Wan2.2-KJ-6步加速图生视频_1950400282711736322.json, 视频生成/图生视频/Wan2.2图生视频吊打付费网站效果_1950068834109710337.json, 视频生成/图生视频/wan2.2图生视频-标准版-(必收藏)_2059069738726285313.json, 视频生成/图生视频/【KJ加速版】Wan2.2 图生视频_1953401583553925122.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_287

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/WAN2.2图生视频_1950137059535183873.json、视频生成/图生视频/WAN2.2图生视频快速流KJ版i2V_1949391348926971905.json、视频生成/图生视频/Wan2.2  高帧率高清｜图生视频稳定版_1950383603089891330.json、视频生成/图生视频/Wan2.2 I2V KJ图生视频基础版 Borges_1951966233606434817.json、视频生成/图生视频/Wan2.2 Kj-图生视频工作流_1956914143121039362.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 10 个 workflow 都包含：
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
- `GetImageSizeAndCount` —— 8/10 个有
- `ImageResizeKJv2` —— 8/10 个有
- `WanVideoTorchCompileSettings` —— 7/10 个有
- `easy cleanGpuUsed` —— 6/10 个有
- `CreateCFGScheduleFloatList` —— 5/10 个有
- `CR Text` —— 4/10 个有
- `DownloadAndLoadGIMMVFIModel` —— 4/10 个有
- `GIMMVFI_interpolate` —— 4/10 个有
- `INTConstant` —— 4/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/10 个有
- `CLIPVisionLoader` —— 2/10 个有
- `MathExpression|pysssss` —— 2/10 个有
- `PrimitiveStringMultiline` —— 2/10 个有
- `easy seed` —— 2/10 个有
- `DF_Integer` —— 1/10 个有
- `ImageFromBatch+` —— 1/10 个有
- `Note Plus (mtb)` —— 1/10 个有
- `PrimitiveFloat` —— 1/10 个有
- `WanVideoClipVisionEncode` —— 1/10 个有
- `WanVideoLoraSelectMulti` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
