---
name: unknown_workflow_sampler_clip_unet_188
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.903714
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/2029744272278294529.json, 图片生成/文生图/87time #02 krea 默认生成_1955480075464577026.json, 图片生成/文生图/AI装饰画场景快速生成_1954389130199351298.json, 图片生成/文生图/FLUX.1 LoRA模型工作流搭建_2014635794983555074.json, 图片生成/文生图/FLUX.1+LoRA模型工作流_2055148110460006402.json, 图片生成/文生图/FLUX图生图LoRA工作流_2048670126542692354.json, 图片生成/文生图/latent大法工作流_1926584319706566658.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_188

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/2029744272278294529.json、图片生成/文生图/87time #02 krea 默认生成_1955480075464577026.json、图片生成/文生图/AI装饰画场景快速生成_1954389130199351298.json、图片生成/文生图/FLUX.1 LoRA模型工作流搭建_2014635794983555074.json、图片生成/文生图/FLUX.1+LoRA模型工作流_2055148110460006402.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `EmptyLatentImage` —— 3/7 个有
- `RH_Translator` —— 2/7 个有
- `DeepTranslatorTextNode` —— 1/7 个有
- `ImageUpscaleWithModel` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `LoraLoader` —— 1/7 个有
- `ModelMergeFlux1` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `SaveLatent` —— 1/7 个有
- `UpscaleModelLoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22 | 20 - 30 | 7 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 768 | 768 - 1024 | 3 | 86% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22，观测区间 20 - 30，7 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 1024，3 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
