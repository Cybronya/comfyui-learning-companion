---
name: unknown_workflow_sampler_clip_unet_101
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.906143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图-产品创意海报_2059206447187193858.json, 图片生成/文生图/文生图-极致自然-Z-Image-Base_2016417634937475073.json, 图片生成/文生图/电商生成多镜头图片 qwen2512_2017062093035413506.json, 图片生成/文生图/红潮造相ZImage+LoRA文生图+VAE增加细节_2009818930566664194.json, 图片生成/文生图/赛博玄幻修仙者｜墨渊·文生图_2093285763407507458.json, 图片生成/文生图/赛博玄幻修仙者｜燕青·文生图_2093374844577599489.json, 图片生成/文生图/超可爱的q版3d风格动画角色设计_2067581459497578498.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_101

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/文生图-产品创意海报_2059206447187193858.json、图片生成/文生图/文生图-极致自然-Z-Image-Base_2016417634937475073.json、图片生成/文生图/电商生成多镜头图片 qwen2512_2017062093035413506.json、图片生成/文生图/红潮造相ZImage+LoRA文生图+VAE增加细节_2009818930566664194.json、图片生成/文生图/赛博玄幻修仙者｜墨渊·文生图_2093285763407507458.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `JjkText` —— 2/7 个有
- `CR SDXL Aspect Ratio` —— 1/7 个有
- `LatentUpscaleBy` —— 1/7 个有
- `TextCombinerTwo` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 25 | 7 | 50% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 7 | 27% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 25，7 个样本，取值分散，一致性仅 50%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，7 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
