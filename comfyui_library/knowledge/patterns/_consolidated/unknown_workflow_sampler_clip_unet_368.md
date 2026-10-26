---
name: unknown_workflow_sampler_clip_unet_368
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.866333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptySD3LatentImage, GetImageSize, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/千问Qwen-inpaint（局部重绘）_1958799757202317313.json, 图片生成/图生图/千问Qwen-inpaint（局部重绘）_2003855266217115649.json, 图片生成/图生图/千问反推出图_1954724393643589634.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_368

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/千问Qwen-inpaint（局部重绘）_1958799757202317313.json、图片生成/图生图/千问Qwen-inpaint（局部重绘）_2003855266217115649.json、图片生成/图生图/千问反推出图_1954724393643589634.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptySD3LatentImage`
- `GetImageSize`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelPatchLoader` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `QwenImageDiffsynthControlnet` —— 2/3 个有
- `ImageConcanate` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `Mask Fill Holes` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `TextBox` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 3.5 | 3 | 83% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 3.5，3 个样本，取值集中（一致性 83%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
