---
name: unknown_workflow_video_sampler_vae_141
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9145
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1906626628410068994.json, 视频生成/文生视频/1934618185205522434.json, 视频生成/文生视频/1912089275754840066.json, 视频生成/文生视频/1913149731756015618.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_141

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/1906626628410068994.json、视频生成/文生视频/1934618185205522434.json、视频生成/文生视频/1912089275754840066.json、视频生成/文生视频/1913149731756015618.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoEnhanceAVideo` —— 3/4 个有
- `WanVideoExperimentalArgs` —— 3/4 个有
- `WanVideoSLG` —— 3/4 个有
- `WanVideoLoraSelect` —— 2/4 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/4 个有
- `GIMMVFI_interpolate` —— 1/4 个有
- `LoadAndResizeImage` —— 1/4 个有
- `Note _O` —— 1/4 个有
- `WanVideoImageToVideoEncode` —— 1/4 个有
- `WanVideoTorchCompileSettings` —— 1/4 个有
- `WanVideoVRAMManagement` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
