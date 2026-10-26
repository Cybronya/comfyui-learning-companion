---
name: unknown_workflow_video_upscale_lora_11
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.87975
common_nodes: [GetImageRangeFromBatch, ImageResizeKJ, ImageUpscaleWithModel, ImpactFloat, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, RIFE VFI, UpscaleModelLoader, VHS_VideoCombine, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1 最新 FusionX 2分钟极速出视频_1942175633449578497.json, 视频生成/图生视频/Wan图生视频-FUSION版本_1933959648057675777.json, 视频生成/图生视频/Wan图生视频急速版_1935194153187999746.json, 视频生成/图生视频/【趣味】三味真火！_1934811553910693889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_11

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan2.1 最新 FusionX 2分钟极速出视频_1942175633449578497.json、视频生成/图生视频/Wan图生视频-FUSION版本_1933959648057675777.json、视频生成/图生视频/Wan图生视频急速版_1935194153187999746.json、视频生成/图生视频/【趣味】三味真火！_1934811553910693889.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `ImageResizeKJ`
- `ImageUpscaleWithModel`
- `ImpactFloat`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `RIFE VFI`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `WanVideoBlockSwap` —— 3/4 个有
- `WanVideoApplyNAG` —— 2/4 个有
- `WanVideoMagCache` —— 2/4 个有
- `WanVideoTextEncode` —— 2/4 个有
- `WanVideoTextEncodeSingle` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `Display Any (rgthree)` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `Text` —— 1/4 个有
- `Text Find and Replace` —— 1/4 个有
- `WanVideoEnhanceAVideo` —— 1/4 个有
- `WanVideoExperimentalArgs` —— 1/4 个有
- `WanVideoSLG` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
