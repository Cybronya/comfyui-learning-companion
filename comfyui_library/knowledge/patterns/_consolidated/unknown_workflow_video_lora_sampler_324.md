---
name: unknown_workflow_video_lora_sampler_324
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.800714
common_nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1944806594343522306.json, 视频生成/图生视频/1945716479117447170.json, 视频生成/图生视频/1945116426497871874.json, 视频生成/图生视频/1913661782513385473.json, 视频生成/图生视频/1913309276788719618.json, 视频生成/图生视频/1917988631829745665.json, 视频生成/图生视频/2050270690158358530.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_324

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1944806594343522306.json、视频生成/图生视频/1945716479117447170.json、视频生成/图生视频/1945116426497871874.json、视频生成/图生视频/1913661782513385473.json、视频生成/图生视频/1913309276788719618.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoClipTextEncoder` —— 6/7 个有
- `WanVideoEnhanceAVideo` —— 6/7 个有
- `WanVideoExperimentalArgs` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `LayerUtility: PurgeVRAM V2` —— 5/7 个有
- `DownloadAndLoadGIMMVFIModel` —— 4/7 个有
- `GIMMVFI_interpolate` —— 4/7 个有
- `WanVideoVRAMManagement` —— 4/7 个有
- `WanVideoFreeInitArgs` —— 3/7 个有
- `WanVideoTeaCache` —— 3/7 个有
- `ImageBlur` —— 2/7 个有
- `SaveImage` —— 2/7 个有
- `SaveLatent` —— 2/7 个有
- `CLIPVisionLoader` —— 1/7 个有
- `CR Value` —— 1/7 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 1/7 个有
- `LayerUtility: PurgeVRAM` —— 1/7 个有
- `LayerUtility: TextBox` —— 1/7 个有
- `Text Multiline` —— 1/7 个有
- `WanVideoEasyCache` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
