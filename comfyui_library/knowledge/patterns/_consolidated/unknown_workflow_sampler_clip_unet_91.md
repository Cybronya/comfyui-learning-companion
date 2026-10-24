---
name: unknown_workflow_sampler_clip_unet_91
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.951273
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图 FLUX 3 Image Klein-_2112067114927480834.json, 图片生成/文生图/文生图Flux2-Klein_2080293479414059009.json, 图片生成/文生图/文生图工作流购买的1 (1)_2045309169393209345.json, 图片生成/文生图/文生图工作流购买的1 (1)_2068998152438501378.json, 图片生成/文生图/文生图工作流购买的1_2047220596840341506.json, 图片生成/文生图/文生图工作流购买的1_2047619516003262466.json, 图片生成/文生图/文生图片工作流_2056608192112713729.json, 图片生成/文生图/文生图超真实+去除AI味_2043505519566000130.json, 图片生成/文生图/文生图（自定义lora版）Z-image-base_2018558734011736066.json, 图片生成/文生图/智趣云课（文生图学员练习版）_2046152098273828865.json, 图片生成/文生图/泠月luna_固定人物出图。Z-image Base_luna_v4_ckpt16_2043661655762014209.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_91

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/文生图 FLUX 3 Image Klein-_2112067114927480834.json、图片生成/文生图/文生图Flux2-Klein_2080293479414059009.json、图片生成/文生图/文生图工作流购买的1 (1)_2045309169393209345.json、图片生成/文生图/文生图工作流购买的1 (1)_2068998152438501378.json、图片生成/文生图/文生图工作流购买的1_2047220596840341506.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 8/11 个有
- `EmptySD3LatentImage` —— 8/11 个有
- `ModelSamplingAuraFlow` —— 8/11 个有
- `TTResolutionSelector` —— 3/11 个有
- `CR Text Concatenate` —— 2/11 个有
- `EmptyFlux2LatentImage` —— 2/11 个有
- `LoraLoaderModelOnly` —— 2/11 个有
- `CR SDXL Aspect Ratio` —— 1/11 个有
- `Text Multiline` —— 1/11 个有
- `workflow>lora pipe` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 50 | 11 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 11 | 34% |
| 采样算法 | euler | - | 11 | 73% |
| 调度器 | simple | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 50，11 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，11 个样本，一致性 73%
- 调度器 最常用 simple，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（8/11 个样本）：Steps较低可能导致细节不足
