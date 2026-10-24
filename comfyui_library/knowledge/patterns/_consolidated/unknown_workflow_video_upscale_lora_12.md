---
name: unknown_workflow_video_upscale_lora_12
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 1
common_nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, UpscaleImageWithModelIfNeed, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoEnhanceAVideo, WanVideoLoraSelect, WanVideoSEDecode, WanVideoSEImageClipEncode, WanVideoSEModelLoader, WanVideoSESampler, WanVideoSLG, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.1动态壁纸循环首尾帧_1918858509570473986.json, 视频生成/图生视频/wan2.1动态壁纸循环首尾帧，全尺寸支持+自动提示词_1914665456270278658.json, 视频生成/图生视频/wan2.1动态壁纸首尾帧循环版_1914595453097209857.json, 视频生成/图生视频/【动态逼真】万相动态壁纸循环首尾帧_1918851032598642689.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_12

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/WAN2.1动态壁纸循环首尾帧_1918858509570473986.json、视频生成/图生视频/wan2.1动态壁纸循环首尾帧，全尺寸支持+自动提示词_1914665456270278658.json、视频生成/图生视频/wan2.1动态壁纸首尾帧循环版_1914595453097209857.json、视频生成/图生视频/【动态逼真】万相动态壁纸循环首尾帧_1918851032598642689.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `UpscaleImageWithModelIfNeed`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoEnhanceAVideo`
- `WanVideoLoraSelect`
- `WanVideoSEDecode`
- `WanVideoSEImageClipEncode`
- `WanVideoSEModelLoader`
- `WanVideoSESampler`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadFlorence2Model` —— 3/4 个有
- `Florence2Run` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `StringFunction|pysssss` —— 3/4 个有
- `ImageResize+` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
