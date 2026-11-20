---
name: unknown_workflow_video_sampler_vae_146
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8655
common_nodes: [ImageResizeKJ, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan_fun_control_官方工作流_文生视频t2v_K神版_1930315857648369666.json, 平台全量/通义万相wan2.1 Fun control视频转绘_1907331700114743297.json, 视频生成/图生视频/Uni3C运镜参考_1929726931179094017.json, 视频生成/文生视频/FUN 动作迁移稳定版_1909601709499580417.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_146

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Wan_fun_control_官方工作流_文生视频t2v_K神版_1930315857648369666.json、平台全量/通义万相wan2.1 Fun control视频转绘_1907331700114743297.json、视频生成/图生视频/Uni3C运镜参考_1929726931179094017.json、视频生成/文生视频/FUN 动作迁移稳定版_1909601709499580417.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 3/4 个有
- `GetImageSizeAndCount` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `WanVideoClipVisionEncode` —— 3/4 个有
- `WanVideoControlEmbeds` —— 3/4 个有
- `WanVideoEmptyEmbeds` —— 3/4 个有
- `WanVideoImageToVideoEncode` —— 3/4 个有
- `AIO_Preprocessor` —— 2/4 个有
- `WanVideoEnhanceAVideo` —— 2/4 个有
- `WanVideoVRAMManagement` —— 2/4 个有
- `AnimateDiffCombine` —— 1/4 个有
- `DWPreprocessor` —— 1/4 个有
- `DepthAnything_V2` —— 1/4 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImageBlend` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `WanVideoLoraSelect` —— 1/4 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/4 个有
- `WanVideoUni3C_embeds` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
