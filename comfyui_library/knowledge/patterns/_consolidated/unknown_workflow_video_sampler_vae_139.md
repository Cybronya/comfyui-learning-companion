---
name: unknown_workflow_video_sampler_vae_139
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8665
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoApplyNAG, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/图生视频FusionX+NAG_1934129997869142017.json, 视频生成/图生视频/图生视频快速稳定版_1943227383488921602.json, 视频生成/图生视频/大融合图生视频 FusionX I2V_1934261735870390274.json, 视频生成/图生视频/自己用：图生视频_1940690861510520833.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_139

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/图生视频FusionX+NAG_1934129997869142017.json、视频生成/图生视频/图生视频快速稳定版_1943227383488921602.json、视频生成/图生视频/大融合图生视频 FusionX I2V_1934261735870390274.json、视频生成/图生视频/自己用：图生视频_1940690861510520833.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoBlockSwap` —— 3/4 个有
- `WanVideoEnhanceAVideo` —— 3/4 个有
- `CLIPVisionLoader` —— 2/4 个有
- `ImageResizeKJ` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `WanVideoClipVisionEncode` —— 2/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LayerUtility: TextBox` —— 1/4 个有
- `WanVideoTorchCompileSettings` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
