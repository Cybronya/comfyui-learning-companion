---
name: unknown_workflow_video_sampler_vae_168
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.75825
common_nodes: [CLIPVisionLoader, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/抖音蜜蜂宝宝_1933541518860800001.json, 视频生成/图生视频/抖音骑上我心爱的小摩托_1933704774371954690.json, 视频生成/文生视频/WAN_FusionX_LoRa_文图生视频_1943843153860497410.json, 视频生成/文生视频/【Wan2.1系列】CFG-Zero Star技术提升视频质量N个档次_1918878513657479170.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_168

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/抖音蜜蜂宝宝_1933541518860800001.json、视频生成/图生视频/抖音骑上我心爱的小摩托_1933704774371954690.json、视频生成/文生视频/WAN_FusionX_LoRa_文图生视频_1943843153860497410.json、视频生成/文生视频/【Wan2.1系列】CFG-Zero Star技术提升视频质量N个档次_1918878513657479170.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 3/4 个有
- `Int` —— 3/4 个有
- `MathExpression|pysssss` —— 3/4 个有
- `WanVideoEnhanceAVideo` —— 3/4 个有
- `WanVideoLoraSelect` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `WanVideoEmptyEmbeds` —— 2/4 个有
- `WanVideoExperimentalArgs` —— 2/4 个有
- `WanVideoVRAMManagement` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `WanVideoSLG` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
