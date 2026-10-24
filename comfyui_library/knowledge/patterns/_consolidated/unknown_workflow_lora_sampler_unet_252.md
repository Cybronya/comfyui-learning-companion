---
name: unknown_workflow_lora_sampler_unet_252
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.902
common_nodes: [CFGGuider, CLIPLoader, KSamplerSelect, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, RandomNoise, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen-Image-2.1-一键抠图_图层拆分_2112447865481162754.json, 图片生成/文生图/Qwen image 2.1多参考生图工作流（短剧分镜制作、8步加速）_2112531337080037378.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_252

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-2.1-一键抠图_图层拆分_2112447865481162754.json、图片生成/文生图/Qwen image 2.1多参考生图工作流（短剧分镜制作、8步加速）_2112531337080037378.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
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
- `BasicScheduler` —— 1/2 个有
- `CustomSigmas` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `ExtendIntermediateSigmas` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `QwenImage21SageAttentionT8` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1440 | - | 1 | 100% |
| 高度 | 1920 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
