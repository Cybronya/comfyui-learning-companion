---
name: unknown_workflow_sampler_clip_vae_20
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.9535
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/双节棍加速千问 image工作流_1965043199712612353.json, 图片生成/文生图/在线-Z-T2I-1128_1994378488129986561.json, 图片生成/文生图/基础文生海报_1932345808937807873.json, 图片生成/文生图/完美中文海报生成_2002018843826503681.json, 图片生成/文生图/文生图-极致自然-Z-Image-Base_2016417634937475073.json, 图片生成/文生图/文生图工作流购买的1 (1)_2045309169393209345.json, 图片生成/文生图/文生图工作流购买的1 (1)_2068998152438501378.json, 图片生成/文生图/文生图工作流购买的1_2047220596840341506.json, 图片生成/文生图/文生图工作流购买的1_2047619516003262466.json, 图片生成/文生图/文生图片工作流_2056608192112713729.json, 图片生成/文生图/海报生成器+QwenImage=艾橘溪_1954567812612288513.json, 图片生成/文生图/艺术字体生成器+QwenImage=B站艾橘溪_1954565922696654850.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_20

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/双节棍加速千问 image工作流_1965043199712612353.json、图片生成/文生图/在线-Z-T2I-1128_1994378488129986561.json、图片生成/文生图/基础文生海报_1932345808937807873.json、图片生成/文生图/完美中文海报生成_2002018843826503681.json、图片生成/文生图/文生图-极致自然-Z-Image-Base_2016417634937475073.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 11/12 个有
- `CR Text` —— 6/12 个有
- `easy cleanGpuUsed` —— 4/12 个有
- `DoubaoSizePreset` —— 1/12 个有
- `NunchakuQwenImageDiTLoader` —— 1/12 个有
- `SDXLAspectRatio` —— 1/12 个有
- `easy seed` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9.5 | 8 - 50 | 12 | 28% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 5 | 12 | 34% |
| 采样算法 | euler | - | 12 | 83% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9.5，观测区间 8 - 50，12 个样本，取值分散，一致性仅 28%
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 5，12 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，12 个样本，一致性 83%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（6/12 个样本）：Steps较低可能导致细节不足
