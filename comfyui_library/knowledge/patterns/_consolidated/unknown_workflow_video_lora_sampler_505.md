---
name: unknown_workflow_video_lora_sampler_505
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.967
common_nodes: [CLIPVisionLoader, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoUniAnimateDWPoseDetector, WanVideoUniAnimatePoseInput, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WanVideoUniAnimate动作迁移_1957361531111534593.json, 视频生成/图生视频/unianimate-dit(wan)动物拟人化跳舞_1917049756479328258.json, 视频生成/图生视频/图生视频-unianimate动画_2038418404205400065.json, 视频生成/图生视频/图生视频-unianimate动画_2046127380867059713.json, 视频生成/图生视频/视频转绘工作流（UniAnimate-DiT）_1913589244055515137.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_505

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/WanVideoUniAnimate动作迁移_1957361531111534593.json、视频生成/图生视频/unianimate-dit(wan)动物拟人化跳舞_1917049756479328258.json、视频生成/图生视频/图生视频-unianimate动画_2038418404205400065.json、视频生成/图生视频/图生视频-unianimate动画_2046127380867059713.json、视频生成/图生视频/视频转绘工作流（UniAnimate-DiT）_1913589244055515137.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
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
- `ImageConcanate` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `Bjornulf_FreeVRAM` —— 1/5 个有
- `CR SDXL Aspect Ratio` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `NunchakuFluxDiTLoader` —— 1/5 个有
- `PrimitiveString` —— 1/5 个有
- `VHS_VideoInfoLoaded` —— 1/5 个有
- `WanVideoApplyNAG` —— 1/5 个有
- `WanVideoContextOptions` —— 1/5 个有
- `WanVideoLoraSelectMulti` —— 1/5 个有
- `WanVideoTextEncodeSingle` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
