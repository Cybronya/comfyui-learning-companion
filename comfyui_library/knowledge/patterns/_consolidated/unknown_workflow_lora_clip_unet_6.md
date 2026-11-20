---
name: unknown_workflow_lora_clip_unet_6
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 1
common_nodes: [CLIPLoaderGGUF, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/zib+zit双采_2041551392782950402.json, 图片生成/文生图/文生图虚实之间-写真风格_2061334205283524609.json, 图片生成/文生图/虚实之间-写真风格（偏raw）v2_2059308512265728002.json, 图片生成/文生图/虚实之间-写真风格（偏精修）v5_2053493793466404865.json, 图片生成/文生图/随地大小拍-手机随拍感_2037514128289439745.json, 图片生成/文生图/随地大小拍—手机摄影v3_2040675977839251457.json, 图片生成/文生图/随地大小拍—手机摄影v3_2105573480929517569.json, 图片生成/文生图/随地大小拍—手机摄影v3_2108010331879600130.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_6

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/zib+zit双采_2041551392782950402.json、图片生成/文生图/文生图虚实之间-写真风格_2061334205283524609.json、图片生成/文生图/虚实之间-写真风格（偏raw）v2_2059308512265728002.json、图片生成/文生图/虚实之间-写真风格（偏精修）v5_2053493793466404865.json、图片生成/文生图/随地大小拍-手机随拍感_2037514128289439745.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 7/8 个有
- `KSampler` —— 4/8 个有
- `KSamplerAdvanced` —— 4/8 个有
- `LayerColor: BrightnessContrastV2` —— 4/8 个有
- `ModelSamplingAuraFlow` —— 4/8 个有
- `VAEEncode` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 6.5 | 1 - 12 | 8 | 15% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | dpmpp_2m_sde_gpu | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 6.5，观测区间 1 - 12，8 个样本，取值分散，一致性仅 15%
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m_sde_gpu，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/8 个样本）：Steps较低可能导致细节不足
