---
name: unknown_workflow_video_lora_sampler_467
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.935
common_nodes: [CLIPTextEncode, CLIPVisionLoader, DualCLIPLoader, EmptyConditioning, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), ImageResizeKJ, KSampler, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoVRAMManagement, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/【老金驿站】WAN2.1史诗级英雄分镜生成工作流_1929452145547055105.json, 图片生成/文生图/【老金驿站】WAN2.1国家地理场景分镜生成工作流_1929433520668839938.json, 图片生成/文生图/【老金驿站】WAN2.1好莱坞人物分镜生成工作流_1929150896092123137.json, 图片生成/文生图/【老金驿站】WAN2.1车辆追逐场景分镜生成工作流_1929089171099435010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_467

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/【老金驿站】WAN2.1史诗级英雄分镜生成工作流_1929452145547055105.json、图片生成/文生图/【老金驿站】WAN2.1国家地理场景分镜生成工作流_1929433520668839938.json、图片生成/文生图/【老金驿站】WAN2.1好莱坞人物分镜生成工作流_1929150896092123137.json、图片生成/文生图/【老金驿站】WAN2.1车辆追逐场景分镜生成工作流_1929089171099435010.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
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
| 采样步数 | 25 | 25 - 25 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | deis | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
