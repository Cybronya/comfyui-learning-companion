---
name: unknown_workflow_sampler_clip_unet_356
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.854333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptySD3LatentImage, Image Comparer (rgthree), ModelSamplingAuraFlow, PiDFinalize, PiDKSamplerCapture, PiDPrepare, PiDSample, PiDTextPrompt, RunningHub Deepcleaner, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z-image Pid 图像模糊变高清放大2K版_2059489801124016130.json, 图片生成/文生图/Klein Pid文生图4K工作流_2059471562478284802.json, 图片生成/文生图/PiD Z-Image Turbo文生图一键4K_2061277338498850817.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_356

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z-image Pid 图像模糊变高清放大2K版_2059489801124016130.json、图片生成/文生图/Klein Pid文生图4K工作流_2059471562478284802.json、图片生成/文生图/PiD Z-Image Turbo文生图一键4K_2061277338498850817.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `ModelSamplingAuraFlow`
- `PiDFinalize`
- `PiDKSamplerCapture`
- `PiDPrepare`
- `PiDSample`
- `PiDTextPrompt`
- `RunningHub Deepcleaner`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorMatchV2` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `Float` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PDIMAGE_LongerSize` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `ShowAnything|Mie` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 50 | 3 | 4% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 0.2 - 1 | 3 | 49% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 50，3 个样本，取值分散，一致性仅 4%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，3 个样本，取值分散，一致性仅 49%
