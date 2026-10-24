---
name: unknown_workflow_sampler_clip_vae_18
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.872333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/ZIMAGE-Turbo文生图_图生图反推提示词 +写实光影LORA_2028301404321882114.json, 图片生成/图生图/Zimage base BF16一键反推出模特大片_2016385556543971329.json, 图片生成/图生图/Zimage base BF16一键反推出模特大片带提示词指令_2016404721153613825.json, 图片生成/图生图/Zimage base GGUF一键反推出模特大片_2016449692015534082.json, 图片生成/图生图/Zimage base GGUF一键反推出模特大片带提示词指令_2016410479102533634.json, 图片生成/图生图/Zimage base fp8一键反推出模特大片_2016385537959006209.json, 图片生成/图生图/Zimage base fp8一键反推出模特大片带提示词指令_2016402710362333185.json, 图片生成/图生图/图生图海报电商_2085391785551024129.json, 图片生成/图生图/高质量洗图 文生图 图生图自动_手动提示词 反推提示词 Z-Image Turbo  高清放大_2028735650962345986.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_18

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/ZIMAGE-Turbo文生图_图生图反推提示词 +写实光影LORA_2028301404321882114.json、图片生成/图生图/Zimage base BF16一键反推出模特大片_2016385556543971329.json、图片生成/图生图/Zimage base BF16一键反推出模特大片带提示词指令_2016404721153613825.json、图片生成/图生图/Zimage base GGUF一键反推出模特大片_2016449692015534082.json、图片生成/图生图/Zimage base GGUF一键反推出模特大片带提示词指令_2016410479102533634.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 7/9 个有
- `Text Multiline` —— 7/9 个有
- `UNETLoader` —— 7/9 个有
- `PathchSageAttentionKJ` —— 6/9 个有
- `PrimitiveStringMultiline` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `RH_Captioner` —— 2/9 个有
- `UnetLoaderGGUF` —— 2/9 个有
- `ttN concat` —— 2/9 个有
- `PreviewAny` —— 1/9 个有
- `ShowText|pysssss` —— 1/9 个有
- `Text Concatenate` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 10 - 30 | 9 | 60% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 9 | 53% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 10 - 30，9 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
