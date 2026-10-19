---
name: unknown_workflow_video_lora_sampler_320
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.913286
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/1951564879096434690.json, 视频生成/图生视频/2021217976392884225.json, 视频生成/图生视频/1974143667713781762.json, 视频生成/图生视频/1974129823239024642.json, 视频生成/图生视频/2067174890066763778.json, 视频生成/图生视频/1987880762861137921.json, 视频生成/图生视频/1983835133948174337.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_320

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1951564879096434690.json、视频生成/图生视频/2021217976392884225.json、视频生成/图生视频/1974143667713781762.json、视频生成/图生视频/1974129823239024642.json、视频生成/图生视频/2067174890066763778.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 6/7 个有
- `PrimitiveInt` —— 6/7 个有
- `WanVideoSetBlockSwap` —— 6/7 个有
- `WanVideoSetLoRAs` —— 6/7 个有
- `AILab_MiniCPM_4_V_Advanced` —— 5/7 个有
- `ShowText|pysssss` —— 5/7 个有
- `SimpleMath+` —— 3/7 个有
- `CM_IntToFloat` —— 1/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `HunyuanVideoFoley` —— 1/7 个有
- `MMAudioFeatureUtilsLoader` —— 1/7 个有
- `MMAudioModelLoader` —— 1/7 个有
- `MMAudioSampler` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
