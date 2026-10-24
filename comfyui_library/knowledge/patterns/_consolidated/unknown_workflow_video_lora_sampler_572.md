---
name: unknown_workflow_video_lora_sampler_572
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.929
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CR Text, EmptySD3LatentImage, GetImageSizeAndCount, ImageResizeKJv2, KSampler, LoadImage, LoadWanVideoT5TextEncoder, ModelSamplingAuraFlow, PreviewImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen千问文生图+Wan2.2图生视频，强强联合_1953107742094520321.json, 图片生成/文生图/Wan2.2+千问剪纸风格视频生成_1976913869014765569.json, 图片生成/文生图/文生动态表情包微信动态表情制作_1979202770127458305.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_572

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen千问文生图+Wan2.2图生视频，强强联合_1953107742094520321.json、图片生成/文生图/Wan2.2+千问剪纸风格视频生成_1976913869014765569.json、图片生成/文生图/文生动态表情包微信动态表情制作_1979202770127458305.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
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
- `AILab_MiniCPM_4_V_Advanced` —— 2/3 个有
- `ColorMatch` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `WanVideoBlockSwap` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `String` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta57 | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta57，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
