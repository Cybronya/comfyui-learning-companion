---
name: unknown_workflow_sampler_clip_vae_29
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.935857
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptySD3LatentImage, KSampler, SaveImage, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/Flux 4K高清大图DyPE直出_2001499038975422465.json, 图片生成/文生图/Flux-双截棍 4K高清大图DyPE直出_2000808135889743873.json, 图片生成/文生图/flux1_krea_dev 很漂亮_1954159231169642497.json, 图片生成/文生图/flux1_krea_dev满血版出图_1951839776326537218.json, 图片生成/文生图/【茗翠Ai】F.1 krea文生图_1952021213906415618.json, 图片生成/文生图/去掉flux的AI 味er  flux krea_1951281909651419137.json, 图片生成/文生图/独特的美学风格和自然细节，避免 AI 外观，提供真实的图像质量。_1947211070849110017.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_29

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Flux 4K高清大图DyPE直出_2001499038975422465.json、图片生成/文生图/Flux-双截棍 4K高清大图DyPE直出_2000808135889743873.json、图片生成/文生图/flux1_krea_dev 很漂亮_1954159231169642497.json、图片生成/文生图/flux1_krea_dev满血版出图_1951839776326537218.json、图片生成/文生图/【茗翠Ai】F.1 krea文生图_1952021213906415618.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 6/7 个有
- `VAEDecode` —— 5/7 个有
- `DyPE_FLUX` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `VAEDecodeTiled` —— 2/7 个有
- `LoadImage` —— 1/7 个有
- `NunchakuFluxDiTLoader` —— 1/7 个有
- `RH_Captioner` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 7 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/7 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，7 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
