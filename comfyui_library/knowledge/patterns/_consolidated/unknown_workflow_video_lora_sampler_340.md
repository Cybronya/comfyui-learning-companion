---
name: unknown_workflow_video_lora_sampler_340
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.854
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CR Text, EmptySD3LatentImage, GetImageSizeAndCount, ImageResizeKJv2, KSampler, LoadImage, LoadWanVideoT5TextEncoder, ModelSamplingAuraFlow, PreviewImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, easy cleanGpuUsed, CR Text Concatenate]
members: [图片生成/文生图/1953107742094520321.json, 图片生成/文生图/1976913869014765569.json, 图片生成/文生图/1979202770127458305.json, 视频生成/图生视频/1953107742094520321.json, 视频生成/图生视频/1976913869014765569.json, 视频生成/图生视频/1979202770127458305.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_340

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1953107742094520321.json、图片生成/文生图/1976913869014765569.json、图片生成/文生图/1979202770127458305.json、视频生成/图生视频/1953107742094520321.json、视频生成/图生视频/1976913869014765569.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Text`
- `EmptySD3LatentImage`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `AILab_MiniCPM_4_V_Advanced` —— 4/6 个有
- `ColorMatch` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `ShowText|pysssss` —— 4/6 个有
- `WanVideoBlockSwap` —— 4/6 个有
- `WanVideoTorchCompileSettings` —— 4/6 个有
- `CR Text Concatenate` —— 2/6 个有
- `ImageScale` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `RH_LLMAPI_NODE` —— 2/6 个有
- `String` —— 2/6 个有
- `easy showAnything` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 6 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 29% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | beta57 | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 beta57，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、easy cleanGpuUsed、CR Text Concatenate
