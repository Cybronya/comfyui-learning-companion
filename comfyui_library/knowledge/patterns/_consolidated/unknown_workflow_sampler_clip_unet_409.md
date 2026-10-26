---
name: unknown_workflow_sampler_clip_unet_409
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.983333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/美漫手绘故事FLUX + LORA 基础工作流_1955199580277280770.json, 图片生成/文生图/超高清  文生卡通图_1907499231920156674.json, 图片生成/文生图/风后文生图_1878760414459932673.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_409

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/美漫手绘故事FLUX + LORA 基础工作流_1955199580277280770.json、图片生成/文生图/超高清  文生卡通图_1907499231920156674.json、图片生成/文生图/风后文生图_1878760414459932673.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ModelSamplingFlux` —— 2/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `ImageUpscaleWithModelBatched` —— 1/3 个有
- `LatentToWidthHeight` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | - | 2 | 97% |
| 高度 | 1472 | - | 2 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1052，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 高度 中位数 1472，样本不足，未给区间，2 个样本
