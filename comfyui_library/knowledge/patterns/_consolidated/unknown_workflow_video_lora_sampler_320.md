---
name: unknown_workflow_video_lora_sampler_320
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.976429
common_nodes: [CLIPVisionLoader, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoUniAnimateDWPoseDetector, WanVideoUniAnimatePoseInput, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1957361531111534593.json, 视频生成/图生视频/1917049756479328258.json, 视频生成/图生视频/2038418404205400065.json, 视频生成/图生视频/2046127380867059713.json, 视频生成/图生视频/1913589244055515137.json, 视频生成/图生视频/1921566992392978434.json, 视频生成/图生视频/1934795083336065026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_320

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1957361531111534593.json、视频生成/图生视频/1917049756479328258.json、视频生成/图生视频/2038418404205400065.json、视频生成/图生视频/2046127380867059713.json、视频生成/图生视频/1913589244055515137.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoUniAnimateDWPoseDetector`
- `WanVideoUniAnimatePoseInput`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 3/7 个有
- `PreviewImage` —— 2/7 个有
- `Bjornulf_FreeVRAM` —— 1/7 个有
- `CR SDXL Aspect Ratio` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `NunchakuFluxDiTLoader` —— 1/7 个有
- `PrimitiveString` —— 1/7 个有
- `VHS_VideoInfoLoaded` —— 1/7 个有
- `WanVideoApplyNAG` —— 1/7 个有
- `WanVideoContextOptions` —— 1/7 个有
- `WanVideoLoraSelectMulti` —— 1/7 个有
- `WanVideoTextEncodeSingle` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
