---
name: unknown_workflow_lora_sampler_unet_246
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.934667
common_nodes: [CLIPLoader, KSamplerSelect, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, RandomNoise, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-Image-2.1-一键抠图_图层拆分_2112447865481162754.json, 图片生成/文生图/Qwen image 2.1多参考生图工作流（短剧分镜制作、8步加速）_2112531337080037378.json, 平台全量/千问qwen2.1文生图工作流（超快、超好看、不可商用）_2119269537064509441.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_246

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-2.1-一键抠图_图层拆分_2112447865481162754.json、图片生成/文生图/Qwen image 2.1多参考生图工作流（短剧分镜制作、8步加速）_2112531337080037378.json、平台全量/千问qwen2.1文生图工作流（超快、超好看、不可商用）_2119269537064509441.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 2/3 个有
- `CFGGuider` —— 2/3 个有
- `EmptyLatentImage` —— 2/3 个有
- `ExtendIntermediateSigmas` —— 2/3 个有
- `BasicGuider` —— 1/3 个有
- `CustomSigmas` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `QwenImage21SageAttentionT8` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1260 | - | 2 | 86% |
| 高度 | 1920 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1260，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
