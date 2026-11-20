---
name: unknown_workflow_sampler_unet_vae_381
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CFGGuider, CLIPLoader, EmptyHunyuanImageLatent, KSamplerSelect, ManualSigmas, QwenImage21Cache, RandomNoise, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/文生图｜Qwen-Image 2.1 完整 Turbo 模型（8 步）_2119357398690394114.json, 平台全量/文生图｜Qwen-Image 2.1 底模 + Turbo LoRA（8 步）_2119353186782900225.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_381

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/文生图｜Qwen-Image 2.1 完整 Turbo 模型（8 步）_2119357398690394114.json、平台全量/文生图｜Qwen-Image 2.1 底模 + Turbo LoRA（8 步）_2119353186782900225.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `EmptyHunyuanImageLatent`
- `KSamplerSelect`
- `ManualSigmas`
- `QwenImage21Cache`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
