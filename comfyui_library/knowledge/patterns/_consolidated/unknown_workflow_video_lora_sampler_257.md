---
name: unknown_workflow_video_lora_sampler_257
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.949667
common_nodes: [ImageResizeKJv2, LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2图生视频_1950137059535183873.json, 视频生成/图生视频/WAN2.2图生视频快速流KJ版i2V_1949391348926971905.json, 视频生成/图生视频/Wan2.2  高帧率高清｜图生视频稳定版_1950383603089891330.json, 视频生成/图生视频/Wan2.2 I2V KJ图生视频基础版 Borges_1951966233606434817.json, 视频生成/图生视频/Wan2.2一致性长视频_1950574501610311681.json, 视频生成/图生视频/Wan2.2图生视频-速度和质量的再一次提升_1950204585861365762.json, 视频生成/图生视频/Wan2.2图生视频吊打付费网站效果_1950068834109710337.json, 视频生成/图生视频/wan2.2_图生视频工作流  加速版_1962439638365376514.json, 视频生成/图生视频/wan2.2最好的360度旋转特效-可生成人物和物体一致性图片素材-附林黛玉写实_1986434223613636609.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_257

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/WAN2.2图生视频_1950137059535183873.json、视频生成/图生视频/WAN2.2图生视频快速流KJ版i2V_1949391348926971905.json、视频生成/图生视频/Wan2.2  高帧率高清｜图生视频稳定版_1950383603089891330.json、视频生成/图生视频/Wan2.2 I2V KJ图生视频基础版 Borges_1951966233606434817.json、视频生成/图生视频/Wan2.2一致性长视频_1950574501610311681.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 8/9 个有
- `LoadWanVideoT5TextEncoder` —— 8/9 个有
- `WanVideoTextEncode` —— 8/9 个有
- `CreateCFGScheduleFloatList` —— 5/9 个有
- `easy cleanGpuUsed` —— 5/9 个有
- `CLIPLoader` —— 4/9 个有
- `CLIPTextEncode` —— 4/9 个有
- `INTConstant` —— 4/9 个有
- `WanVideoTextEmbedBridge` —— 4/9 个有
- `CR Text` —— 3/9 个有
- `DownloadAndLoadGIMMVFIModel` —— 3/9 个有
- `GIMMVFI_interpolate` —— 3/9 个有
- `GetNode` —— 1/9 个有
- `JWStringMultiline` —— 1/9 个有
- `Note Plus (mtb)` —— 1/9 个有
- `Primitive integer [Crystools]` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `SetNode` —— 1/9 个有
- `SimpleMath+` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
