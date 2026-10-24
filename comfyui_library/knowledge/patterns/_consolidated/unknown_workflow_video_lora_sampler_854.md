---
name: unknown_workflow_video_lora_sampler_854
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.932
common_nodes: [CLIPVisionLoader, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wanunianimate舞蹈动作迁移_1913868726649978882.json, 视频生成/图生视频/可灵同款泼水变装特效_1935726272695689217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_854

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/wanunianimate舞蹈动作迁移_1913868726649978882.json、视频生成/图生视频/可灵同款泼水变装特效_1935726272695689217.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `Int` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `WanVideoEnhanceAVideo` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
