---
name: unknown_workflow_video_lora_sampler_951
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9745
common_nodes: [CR Text, CreateCFGScheduleFloatList, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetImageSizeAndCount, INTConstant, ImageFromBatch+, LoadImage, LoadWanVideoT5TextEncoder, ShowText|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/文生视频/1950563765865598978.json, 视频生成/文生视频/1951548166669807618.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_951

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/1950563765865598978.json、视频生成/文生视频/1951548166669807618.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `CreateCFGScheduleFloatList`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageFromBatch+`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `MMAudioFeatureUtilsLoader` —— 1/2 个有
- `MMAudioModelLoader` —— 1/2 个有
- `MMAudioSampler` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `Wan_video_prompt_generator` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
