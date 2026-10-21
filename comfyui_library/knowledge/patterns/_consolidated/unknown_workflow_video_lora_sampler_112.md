---
name: unknown_workflow_video_lora_sampler_112
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.956143
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1913664774507327490.json, 视频生成/图生视频/1920904820126060546.json, 视频生成/图生视频/1922514213686886402.json, 视频生成/图生视频/1920925508526346241.json, 视频生成/图生视频/1945141161579225090.json, 视频生成/图生视频/1943857684569292801.json, 视频生成/图生视频/1909162790840639489.json, 视频生成/图生视频/1929451203611234306.json, 视频生成/图生视频/1928166272100352001.json, 视频生成/图生视频/1928158479809134593.json, 视频生成/图生视频/1901238900759609346.json, 视频生成/图生视频/1911273702397308929.json, 视频生成/图生视频/1910623040215154690.json, 视频生成/图生视频/1910235144152674306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_112

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/1913664774507327490.json、视频生成/图生视频/1920904820126060546.json、视频生成/图生视频/1922514213686886402.json、视频生成/图生视频/1920925508526346241.json、视频生成/图生视频/1945141161579225090.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 14 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 12/14 个有
- `WanVideoEnhanceAVideo` —— 12/14 个有
- `ImageResizeKJ` —— 11/14 个有
- `DownloadAndLoadGIMMVFIModel` —— 9/14 个有
- `GIMMVFI_interpolate` —— 9/14 个有
- `CR Upscale Image` —— 5/14 个有
- `WanVideoExperimentalArgs` —— 3/14 个有
- `WanVideoSLG` —— 3/14 个有
- `GetImageSize+` —— 1/14 个有
- `ImageScale` —— 1/14 个有
- `SaveImage` —— 1/14 个有
- `VHS_LoadVideo` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
