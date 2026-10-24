---
name: unknown_workflow_sampler_clip
type: Unknown Workflow
frequency: 10
level: weak
coverage: 0.9067
common_nodes: [CLIPTextEncode, PiDFinalize, PiDKSamplerCapture, PiDPrepare, PiDSample, PiDTextPrompt, SaveImage]
problems: []
missing: []
members: [图片生成/文生图/FLUX.1 Dev｜PiD直出4K_2059961777689030657.json, 图片生成/文生图/FLUX.2 Dev｜PiD直出4K_2059961769686294530.json, 图片生成/文生图/SD3.5 Large｜PiD直出4K_2059961785033256961.json, 图片生成/文生图/Z-Image Turbo｜PiD直出4K极速版_2059961793564471298.json, 图片生成/文生图/Z-image Pid 文生图4K版_2059462930655178754.json, 图片生成/文生图/Z-image Pid 文生图4K版_2059532072141807618.json, 图片生成/文生图/Z-image Turbo PiD直出4K_2061798580133916673.json, 图片生成/文生图/Z-image-turbo+Pid 4K高清放大版_2059609707664465921.json, 图片生成/文生图/Z-image-turbo+Pid_4K高清放大版_2095792042604580865.json, 图片生成/文生图/Z-image-turbo+Pid_4K高清放大版_2096148164293259266.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/FLUX.1 Dev｜PiD直出4K_2059961777689030657.json、图片生成/文生图/FLUX.2 Dev｜PiD直出4K_2059961769686294530.json、图片生成/文生图/SD3.5 Large｜PiD直出4K_2059961785033256961.json、图片生成/文生图/Z-Image Turbo｜PiD直出4K极速版_2059961793564471298.json、图片生成/文生图/Z-image Pid 文生图4K版_2059462930655178754.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `PiDFinalize`
- `PiDKSamplerCapture`
- `PiDPrepare`
- `PiDSample`
- `PiDTextPrompt`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 9/10 个有
- `VAEDecode` —— 9/10 个有
- `CLIPLoader` —— 8/10 个有
- `UNETLoader` —— 8/10 个有
- `VAELoader` —— 8/10 个有
- `ModelSamplingAuraFlow` —— 7/10 个有
- `Image Comparer (rgthree)` —— 6/10 个有
- `RunningHub Deepcleaner` —— 6/10 个有
- `easy cleanGpuUsed` —— 6/10 个有
- `CR Prompt Text` —— 5/10 个有
- `ConditioningZeroOut` —— 3/10 个有
- `LoraLoaderModelOnly` —— 3/10 个有
- `CheckpointLoaderSimple` —— 2/10 个有
- `FluxGuidance` —— 2/10 个有
- `EmptyFlux2LatentImage` —— 1/10 个有
- `MemoryCleaner` —— 1/10 个有
- `Text` —— 1/10 个有
- `VAEDecodeTiled` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17.5 | 8 - 50 | 10 | 27% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.4 | 10 | 32% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | beta | - | 10 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 17.5，观测区间 8 - 50，10 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.4，10 个样本，取值分散，一致性仅 32%
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
