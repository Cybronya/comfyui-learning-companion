---
name: unknown_workflow_video_sampler_vae_32
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.916455
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1934317213807505410.json, 视频生成/图生视频/1933551686864781313.json, 视频生成/图生视频/1933552260817534978.json, 视频生成/图生视频/1933824175960449025.json, 视频生成/图生视频/1934857703757914114.json, 视频生成/图生视频/1933852620643852289.json, 视频生成/图生视频/2034885482387083266.json, 视频生成/图生视频/1933192428583038978.json, 视频生成/图生视频/1941330850711814145.json, 视频生成/图生视频/1934449439467794433.json, 视频生成/图生视频/1940976707774136321.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_32

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/1934317213807505410.json、视频生成/图生视频/1933551686864781313.json、视频生成/图生视频/1933552260817534978.json、视频生成/图生视频/1933824175960449025.json、视频生成/图生视频/1934857703757914114.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Primitive integer [Crystools]` —— 10/11 个有
- `Text Multiline` —— 10/11 个有
- `WanVideoEnhanceAVideo` —— 10/11 个有
- `WanVideoTeaCache` —— 9/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/11 个有
- `WanVideoExperimentalArgs` —— 8/11 个有
- `WanVideoSLG` —— 8/11 个有
- `ColorMatch` —— 7/11 个有
- `JWInteger` —— 7/11 个有
- `CLIPVisionLoader` —— 6/11 个有
- `WanVideoClipVisionEncode` —— 6/11 个有
- `WanVideoImageToVideoEncode` —— 6/11 个有
- `ImageConcanate` —— 5/11 个有
- `WanVideoLoraSelect` —— 5/11 个有
- `WanVideoVACEEncode` —— 5/11 个有
- `WanVideoVACEStartToEndFrame` —— 5/11 个有
- `WanVideoTorchCompileSettings` —— 4/11 个有
- `ImageResizeKJ` —— 3/11 个有
- `WanVideoMagCache` —— 2/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `DF_Integer` —— 1/11 个有
- `GetImageSize` —— 1/11 个有
- `SimpleMath+` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
