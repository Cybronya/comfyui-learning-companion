---
name: unknown_workflow_video_lora_sampler_259
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.909556
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2图生视频_1973774773308231682.json, 视频生成/图生视频/Wan2.2图生视频_2072884554280562690.json, 视频生成/图生视频/Wan2.2图生视频_2072885775900958721.json, 视频生成/图生视频/Wan2.2图生视频添加背景音版_1951564879096434690.json, 视频生成/图生视频/Wan2.2图生视频稳定快速优化版长视频_2021217976392884225.json, 视频生成/图生视频/Wan2.2图生视频自动提示词_1974143667713781762.json, 视频生成/图生视频/Wan2.2图生视频自动添加音效_1974129823239024642.json, 视频生成/图生视频/Wan2.2图生视频（优化版）_2067174890066763778.json, 视频生成/图生视频/Wan2.2图生视频（最新优化版）_1987880762861137921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_259

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Wan2.2图生视频_1973774773308231682.json、视频生成/图生视频/Wan2.2图生视频_2072884554280562690.json、视频生成/图生视频/Wan2.2图生视频_2072885775900958721.json、视频生成/图生视频/Wan2.2图生视频添加背景音版_1951564879096434690.json、视频生成/图生视频/Wan2.2图生视频稳定快速优化版长视频_2021217976392884225.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
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
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 8/9 个有
- `PrimitiveInt` —— 8/9 个有
- `WanVideoSetBlockSwap` —— 8/9 个有
- `WanVideoSetLoRAs` —— 8/9 个有
- `WanVideoTorchCompileSettings` —— 8/9 个有
- `SimpleMath+` —— 5/9 个有
- `AILab_MiniCPM_4_V_Advanced` —— 4/9 个有
- `ShowText|pysssss` —— 4/9 个有
- `AudioCrop` —— 1/9 个有
- `CM_IntToFloat` —— 1/9 个有
- `Fast Groups Muter (rgthree)` —— 1/9 个有
- `HunyuanVideoFoley` —— 1/9 个有
- `LoadAudio` —— 1/9 个有
- `MMAudioFeatureUtilsLoader` —— 1/9 个有
- `MMAudioModelLoader` —— 1/9 个有
- `MMAudioSampler` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
