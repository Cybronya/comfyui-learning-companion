---
name: unknown_workflow_video_lora_sampler_271
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.8895
common_nodes: [GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1959544112867389442.json, 视频生成/图生视频/1975197329210871809.json, 视频生成/图生视频/1950013972280950785.json, 视频生成/图生视频/1973774773308231682.json, 视频生成/图生视频/2072884554280562690.json, 视频生成/图生视频/2072885775900958721.json, 视频生成/图生视频/1963509971877072897.json, 视频生成/图生视频/1975958977194405889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_271

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1959544112867389442.json、视频生成/图生视频/1975197329210871809.json、视频生成/图生视频/1950013972280950785.json、视频生成/图生视频/1973774773308231682.json、视频生成/图生视频/2072884554280562690.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
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
- `CLIPVisionLoader` —— 7/8 个有
- `PrimitiveInt` —— 7/8 个有
- `WanVideoClipVisionEncode` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `easy cleanGpuUsed` —— 7/8 个有
- `CR Text` —— 5/8 个有
- `SimpleMath+` —— 5/8 个有
- `ShowText|pysssss` —— 3/8 个有
- `AILab_MiniCPM_4_V_Advanced` —— 2/8 个有
- `AudioCrop` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `ImageBatchMultiple+` —— 1/8 个有
- `Int` —— 1/8 个有
- `LoadAudio` —— 1/8 个有
- `PrimitiveString` —— 1/8 个有
- `easy promptReplace` —— 1/8 个有
- `ttN text` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
