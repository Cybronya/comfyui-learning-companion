---
name: unknown_workflow_video_lora_sampler_757
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9325
common_nodes: [ImageResizeKJv2, LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/LongCat图生视频30秒_1985890878952747009.json, 视频生成/图生视频/【遇见AI】wan2.1 Skyreels V3 V2V视频延长_2067528007627141122.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_757

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LongCat图生视频30秒_1985890878952747009.json、视频生成/图生视频/【遇见AI】wan2.1 Skyreels V3 V2V视频延长_2067528007627141122.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `ImageBatchExtendWithOverlap` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
