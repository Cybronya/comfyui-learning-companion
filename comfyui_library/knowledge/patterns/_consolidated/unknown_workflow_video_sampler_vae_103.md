---
name: unknown_workflow_video_sampler_vae_103
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.889833
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoApplyNAG, WanVideoDecode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/图生视频快速稳定版_1943227383488921602.json, 视频生成/图生视频/自己用：图生视频_1940690861510520833.json, 视频生成/图生视频/高清图生视频工作流-Wan fusionX_1937875802723913730.json, 视频生成/图生视频/龙明wan2.1 图生视频fusionX+NAG_1935009209383886850.json, 视频生成/文生视频/CG迷-FusionX文生视频、图生视频工作流（KJ版本）_1936061298029285377.json, 视频生成/文生视频/Wan2.1FusionX-超高清文生视频_1934584295552163842.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_103

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/图生视频快速稳定版_1943227383488921602.json、视频生成/图生视频/自己用：图生视频_1940690861510520833.json、视频生成/图生视频/高清图生视频工作流-Wan fusionX_1937875802723913730.json、视频生成/图生视频/龙明wan2.1 图生视频fusionX+NAG_1935009209383886850.json、视频生成/文生视频/CG迷-FusionX文生视频、图生视频工作流（KJ版本）_1936061298029285377.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `WanVideoBlockSwap` —— 5/6 个有
- `WanVideoEnhanceAVideo` —— 5/6 个有
- `WanVideoImageToVideoEncode` —— 5/6 个有
- `DownloadAndLoadGIMMVFIModel` —— 4/6 个有
- `GIMMVFI_interpolate` —— 4/6 个有
- `ImageResizeKJ` —— 4/6 个有
- `PreviewImage` —— 3/6 个有
- `ImageScaleToMegapixels` —— 2/6 个有
- `UpscaleModelLoader` —— 2/6 个有
- `WanVideoEmptyEmbeds` —— 2/6 个有
- `CLIPVisionLoader` —— 1/6 个有
- `ImageSmartSharpen+` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/6 个有
- `WanVideoClipVisionEncode` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
