---
name: text_to_image_sampler_clip_unet_124
type: Text To Image
frequency: 3
level: strong
coverage: 0.977667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, TTResolutionSelector, UNETLoader, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/Krea2-raw+turbo两次采样对比单采样turbo-_2074526672380063745.json, 图片生成/文生图/Krea2-色彩HDR增强VAE-对比原版VAE效果_2074188352772984834.json, 图片生成/文生图/Krea2四视图生成流（文生图）2608_2096857346608816129.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_124

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea2-raw+turbo两次采样对比单采样turbo-_2074526672380063745.json、图片生成/文生图/Krea2-色彩HDR增强VAE-对比原版VAE效果_2074188352772984834.json、图片生成/文生图/Krea2四视图生成流（文生图）2608_2096857346608816129.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TTResolutionSelector`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `VAEDecode` —— 2/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `VAEDecodeTiled` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 12 | 3 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 512 - 1024 | 3 | 72% |
| 高度 | 1024 | 512 - 1024 | 3 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 12，3 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1024，3 个样本
- 高度 中位数 1024，观测区间 512 - 1024，3 个样本
