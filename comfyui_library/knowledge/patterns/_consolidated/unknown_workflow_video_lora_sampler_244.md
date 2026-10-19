---
name: unknown_workflow_video_lora_sampler_244
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.903
common_nodes: [CLIPTextEncode, CLIPVisionLoader, DualCLIPLoader, EmptyConditioning, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), ImageResizeKJ, KSampler, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoVRAMManagement, easy cleanGpuUsed]
problems: []
missing: [easy cleanGpuUsed]
members: [图片生成/文生图/1929089171099435010.json, 图片生成/文生图/1929150896092123137.json, 图片生成/文生图/1929433520668839938.json, 图片生成/文生图/1929452145547055105.json, 视频生成/图生视频/1929089171099435010.json, 视频生成/图生视频/1929150896092123137.json, 视频生成/图生视频/1929433520668839938.json, 视频生成/图生视频/1929452145547055105.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_244

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1929089171099435010.json、图片生成/文生图/1929150896092123137.json、图片生成/文生图/1929433520668839938.json、图片生成/文生图/1929452145547055105.json、视频生成/图生视频/1929089171099435010.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `EmptyConditioning`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJ`
- `KSampler`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoVRAMManagement`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | deis | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed
