---
name: unknown_workflow_sampler_clip_vae_63
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.91275
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptySD3LatentImage, KSampler, SaveImage, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/Flux 4K高清大图DyPE直出_2001499038975422465.json, 图片生成/文生图/Flux-双截棍 4K高清大图DyPE直出_2000808135889743873.json, 图片生成/文生图/去掉flux的AI 味er  flux krea_1951281909651419137.json, 图片生成/文生图/独特的美学风格和自然细节，避免 AI 外观，提供真实的图像质量。_1947211070849110017.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_63

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Flux 4K高清大图DyPE直出_2001499038975422465.json、图片生成/文生图/Flux-双截棍 4K高清大图DyPE直出_2000808135889743873.json、图片生成/文生图/去掉flux的AI 味er  flux krea_1951281909651419137.json、图片生成/文生图/独特的美学风格和自然细节，避免 AI 外观，提供真实的图像质量。_1947211070849110017.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 3/4 个有
- `DyPE_FLUX` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `VAEDecode` —— 2/4 个有
- `VAEDecodeTiled` —— 2/4 个有
- `LoadImage` —— 1/4 个有
- `NunchakuFluxDiTLoader` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 4 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/4 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，4 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：发现KSampler但没有VAEDecode
