---
name: unknown_workflow_sampler_clip_unet_207
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.929143
common_nodes: [BasicScheduler, CLIPTextEncode, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/image_omnigen2_文生图_1939949487580160001.json, 图片生成/文生图/image_omnigen2_文生图_1943503078144286722.json, 图片生成/文生图/pipi-anima高级采样器工作流_2078243608947412994.json, 图片生成/文生图/人猫合影_1891781898589384705.json, 图片生成/文生图/小红书人物一致性9宫格文生图工作流_1923215248826748929.json, 图片生成/文生图/文生图 krea适用于亚马逊_1985963732088041473.json, 图片生成/文生图/文生图_FLUX_FP16+Teacache_1893650144414351362.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_207

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/image_omnigen2_文生图_1939949487580160001.json、图片生成/文生图/image_omnigen2_文生图_1943503078144286722.json、图片生成/文生图/pipi-anima高级采样器工作流_2078243608947412994.json、图片生成/文生图/人猫合影_1891781898589384705.json、图片生成/文生图/小红书人物一致性9宫格文生图工作流_1923215248826748929.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 5/7 个有
- `EmptySD3LatentImage` —— 5/7 个有
- `FluxGuidance` —— 5/7 个有
- `DualCLIPLoader` —— 4/7 个有
- `CLIPLoader` —— 3/7 个有
- `ModelSamplingFlux` —— 3/7 个有
- `DualCFGGuider` —— 2/7 个有
- `EmptyLatentImage` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `Lora Loader Stack (rgthree)` —— 1/7 个有
- `TeaCacheForImgGen` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 944 | - | 2 | 92% |
| 高度 | 1488 | - | 2 | 97% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 944，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 高度 中位数 1488，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
