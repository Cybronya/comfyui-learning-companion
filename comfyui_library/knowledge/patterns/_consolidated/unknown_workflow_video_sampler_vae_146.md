---
name: unknown_workflow_video_sampler_vae_146
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.951
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.1-14B-FusionX-Image2video模型 图生视频工作流_1934961731435470849.json, 视频生成/文生视频/【Wan2.1系列】画质救星SLG技术_1918486985445675009.json, 视频生成/文生视频/【加速版】图生视频wan2.1万相2.1稳定效果强大_1945351110414540801.json, 视频生成/文生视频/丝丝顺滑】最新wan2.1 i2v 美女奔跑 lora_1928319038026596353.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_146

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/Wan2.1-14B-FusionX-Image2video模型 图生视频工作流_1934961731435470849.json、视频生成/文生视频/【Wan2.1系列】画质救星SLG技术_1918486985445675009.json、视频生成/文生视频/【加速版】图生视频wan2.1万相2.1稳定效果强大_1945351110414540801.json、视频生成/文生视频/丝丝顺滑】最新wan2.1 i2v 美女奔跑 lora_1928319038026596353.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 3/4 个有
- `WanVideoEnhanceAVideo` —— 3/4 个有
- `WanVideoSLG` —— 3/4 个有
- `WanVideoTeaCache` —— 3/4 个有
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `ImageResizeKJ` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `WanVideoLoraSelect` —— 2/4 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/4 个有
- `GIMMVFI_interpolate` —— 1/4 个有
- `LoadWanVideoClipTextEncoder` —— 1/4 个有
- `TextInput_` —— 1/4 个有
- `WanVideoExperimentalArgs` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
