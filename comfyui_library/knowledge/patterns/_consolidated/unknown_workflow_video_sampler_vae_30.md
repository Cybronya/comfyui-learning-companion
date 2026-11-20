---
name: unknown_workflow_video_sampler_vae_30
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.907167
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/图生动态表情包微信动态表情制作_1979420581047209986.json, 视频生成/图生视频/Wan2.2图生视频720P高清版自动提示词_1975197329210871809.json, 视频生成/图生视频/Wan2.2图生视频KJ加速版_1950013972280950785.json, 视频生成/图生视频/Wan2.2图生视频_1973774773308231682.json, 视频生成/图生视频/Wan2.2图生视频_2072884554280562690.json, 视频生成/图生视频/Wan2.2图生视频_2072885775900958721.json, 视频生成/图生视频/Wan2.2图生视频添加背景音版_1951564879096434690.json, 视频生成/图生视频/Wan2.2图生视频稳定快速优化版长视频_2021217976392884225.json, 视频生成/图生视频/Wan2.2图生视频自动提示词_1974143667713781762.json, 视频生成/图生视频/Wan2.2图生视频自动添加音效_1974129823239024642.json, 视频生成/图生视频/Wan2.2首尾帧KJ版_1963509971877072897.json, 视频生成/图生视频/Wan2.2高动态图生视频Smooth_1977734210951729153.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_30

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（平台全量/图生动态表情包微信动态表情制作_1979420581047209986.json、视频生成/图生视频/Wan2.2图生视频720P高清版自动提示词_1975197329210871809.json、视频生成/图生视频/Wan2.2图生视频KJ加速版_1950013972280950785.json、视频生成/图生视频/Wan2.2图生视频_1973774773308231682.json、视频生成/图生视频/Wan2.2图生视频_2072884554280562690.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoBlockSwap` —— 11/12 个有
- `WanVideoLoraSelect` —— 11/12 个有
- `WanVideoSetLoRAs` —— 11/12 个有
- `easy cleanGpuUsed` —— 11/12 个有
- `PrimitiveInt` —— 10/12 个有
- `WanVideoTorchCompileSettings` —— 10/12 个有
- `CR Text` —— 9/12 个有
- `SimpleMath+` —— 7/12 个有
- `AILab_MiniCPM_4_V_Advanced` —— 4/12 个有
- `ShowText|pysssss` —— 4/12 个有
- `AudioCrop` —— 1/12 个有
- `ColorMatch` —— 1/12 个有
- `HunyuanVideoFoley` —— 1/12 个有
- `ImageScale` —— 1/12 个有
- `LoadAudio` —— 1/12 个有
- `MMAudioFeatureUtilsLoader` —— 1/12 个有
- `MMAudioModelLoader` —— 1/12 个有
- `MMAudioSampler` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
