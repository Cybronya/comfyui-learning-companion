---
name: unknown_workflow_sampler_clip_unet_138
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.936556
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX文生图 大  快   不崩【中文输入】_1926971761274093569.json, 图片生成/文生图/FLUX文生图工作流+3LORA（一键运行）_1926928747302166529.json, 图片生成/文生图/FLUX文生图工作流+双LORA（中文输入）_1917149291704418305.json, 图片生成/文生图/Flux Schnell模型4步快速生图工作流_1896880774707093505.json, 图片生成/文生图/Flux Text-to-Image Workflow_2062531622062346242.json, 图片生成/文生图/Flux_人物一致性【小红书风美女lora】_1917393981133754370.json, 图片生成/文生图/Fluxmania-legacy 真实美图质感_1982900132742070274.json, 图片生成/文生图/Flux基础文生图_1904702749529845761.json, 图片生成/文生图/flux文生图标准版_在线生图_1892886267414392834.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_138

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/FLUX文生图 大  快   不崩【中文输入】_1926971761274093569.json、图片生成/文生图/FLUX文生图工作流+3LORA（一键运行）_1926928747302166529.json、图片生成/文生图/FLUX文生图工作流+双LORA（中文输入）_1917149291704418305.json、图片生成/文生图/Flux Schnell模型4步快速生图工作流_1896880774707093505.json、图片生成/文生图/Flux Text-to-Image Workflow_2062531622062346242.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 5/9 个有
- `PreviewImage` —— 4/9 个有
- `DetailDaemonSamplerNode` —— 2/9 个有
- `FluxGuidance` —— 2/9 个有
- `Label (rgthree)` —— 2/9 个有
- `RH_Translator` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `ArgosTranslateTextNode` —— 1/9 个有
- `NunchakuFluxDiTLoader` —— 1/9 个有
- `PatchModelAddDownscale` —— 1/9 个有
- `Text Concatenate` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.4 - 1 | 5 | 68% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 600 - 1536 | 9 | 75% |
| 高度 | 1024 | 720 - 2048 | 9 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.4 - 1，5 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 600 - 1536，9 个样本
- 高度 中位数 1024，观测区间 720 - 2048，9 个样本
