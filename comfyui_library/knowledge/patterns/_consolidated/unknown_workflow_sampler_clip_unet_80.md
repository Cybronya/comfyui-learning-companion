---
name: unknown_workflow_sampler_clip_unet_80
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.900875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Image Comparer (rgthree), ModelSamplingAuraFlow, PiDFinalize, PiDKSamplerCapture, PiDPrepare, PiDSample, PiDTextPrompt, RunningHub Deepcleaner, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Klein Pid文生图4K工作流_2059471562478284802.json, 图片生成/文生图/PiD Z-Image Turbo文生图一键4K_2061277338498850817.json, 图片生成/文生图/Z-image Pid 文生图4K版_2059462930655178754.json, 图片生成/文生图/Z-image Pid 文生图4K版_2059532072141807618.json, 图片生成/文生图/Z-image Turbo PiD直出4K_2061798580133916673.json, 图片生成/文生图/Z-image-turbo+Pid 4K高清放大版_2059609707664465921.json, 图片生成/文生图/Z-image-turbo+Pid_4K高清放大版_2095792042604580865.json, 图片生成/文生图/Z-image-turbo+Pid_4K高清放大版_2096148164293259266.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_80

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Klein Pid文生图4K工作流_2059471562478284802.json、图片生成/文生图/PiD Z-Image Turbo文生图一键4K_2061277338498850817.json、图片生成/文生图/Z-image Pid 文生图4K版_2059462930655178754.json、图片生成/文生图/Z-image Pid 文生图4K版_2059532072141807618.json、图片生成/文生图/Z-image Turbo PiD直出4K_2061798580133916673.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
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
- `CR Prompt Text` —— 7/8 个有
- `easy cleanGpuUsed` —— 7/8 个有
- `ConditioningZeroOut` —— 3/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `ColorMatchV2` —— 2/8 个有
- `MemoryCleaner` —— 1/8 个有
- `SeedVR2LoadDiTModel` —— 1/8 个有
- `SeedVR2LoadVAEModel` —— 1/8 个有
- `SeedVR2VideoUpscaler` —— 1/8 个有
- `Text` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 50 | 8 | 1% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 26% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 50，8 个样本，取值分散，一致性仅 1%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
