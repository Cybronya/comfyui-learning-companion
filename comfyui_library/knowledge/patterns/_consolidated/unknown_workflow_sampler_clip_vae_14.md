---
name: unknown_workflow_sampler_clip_vae_14
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.867417
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/QWEN image 引导版工作流  附多图像范例及提示词模板_1975853038126632962.json, 图片生成/文生图/Qwen-Image 超级加速简体中文版_1966547887809343490.json, 图片生成/文生图/Qwen-Image极速版文生图V1_1961312747210346498.json, 图片生成/文生图/Qwen-Image极速版文生图V1_2038788902223351809.json, 图片生成/文生图/Qwen千问反推生图，中文生成王者_1952795772553203714.json, 图片生成/文生图/Qwen千问文生图+lora_1953742275262251009.json, 图片生成/文生图/Qwen千问文生图8步lora加速_1954707955675480065.json, 图片生成/文生图/Qwen千问文生图，最佳中文生成_1952594396518780930.json, 图片生成/文生图/qwen-image文生图官方工作流_1953019372622311426.json, 图片生成/文生图/千问image2512文生图_2006334068803248129.json, 图片生成/文生图/千问image文生图_1973958786882908161.json, 图片生成/文生图/千问国庆中秋双节海报制作_1967092738313293826.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_14

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/QWEN image 引导版工作流  附多图像范例及提示词模板_1975853038126632962.json、图片生成/文生图/Qwen-Image 超级加速简体中文版_1966547887809343490.json、图片生成/文生图/Qwen-Image极速版文生图V1_1961312747210346498.json、图片生成/文生图/Qwen-Image极速版文生图V1_2038788902223351809.json、图片生成/文生图/Qwen千问反推生图，中文生成王者_1952795772553203714.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 11/12 个有
- `PreviewImage` —— 8/12 个有
- `UNETLoader` —— 8/12 个有
- `easy cleanGpuUsed` —— 8/12 个有
- `LoadImage` —— 7/12 个有
- `CR Text` —— 6/12 个有
- `LoraLoaderModelOnly` —— 5/12 个有
- `NunchakuQwenImageDiTLoader` —— 4/12 个有
- `LayerUtility: PurgeVRAM` —— 3/12 个有
- `CR SDXL Aspect Ratio` —— 1/12 个有
- `NunchakuQwenImageLoraLoader` —— 1/12 个有
- `RH_Captioner` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 17.5 | 8 - 20 | 12 | 64% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 12 | 50% |
| 采样算法 | euler | - | 12 | 83% |
| 调度器 | simple | - | 12 | 58% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 17.5，观测区间 8 - 20，12 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，12 个样本，取值分散，一致性仅 50%
- 采样算法 最常用 euler，12 个样本，一致性 83%
- 调度器 最常用 simple，12 个样本，一致性 58%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
