---
name: unknown_workflow_clip_unet_vae_3
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.883077
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy cleanGpuUsed, easy clearCacheAll]
members: [图片生成/文生图/1944002361066946562.json, 图片生成/文生图/1944626515541676033.json, 图片生成/文生图/1946266988476030978.json, 图片生成/文生图/1950183203102441473.json, 图片生成/文生图/1950935703578419201.json, 图片生成/文生图/1951146831617175554.json, 图片生成/文生图/1951193822992773122.json, 图片生成/文生图/1951482093362688001.json, 图片生成/文生图/1951900115835498497.json, 图片生成/文生图/1952444989798330370.json, 图片生成/文生图/1954740605987504129.json, 图片生成/文生图/1960284703142129666.json, 图片生成/文生图/wan2.1真实感最强文生图_1899402301214248961.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_3

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/1944002361066946562.json、图片生成/文生图/1944626515541676033.json、图片生成/文生图/1946266988476030978.json、图片生成/文生图/1950183203102441473.json、图片生成/文生图/1950935703578419201.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 11/13 个有
- `KSampler` —— 8/13 个有
- `easy cleanGpuUsed` —— 8/13 个有
- `ModelSamplingSD3` —— 7/13 个有
- `KSamplerAdvanced` —— 5/13 个有
- `LoraLoader` —— 5/13 个有
- `WanVideoNAG` —— 4/13 个有
- `FastFilmGrain` —— 3/13 个有
- `Int` —— 3/13 个有
- `easy clearCacheAll` —— 3/13 个有
- `LoadImage` —— 2/13 个有
- `SaveAnimatedWEBP` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.6 - 1 | 5 | 83% |
| LoRA 文本强度 | 1 | 0.6 - 1 | 5 | 83% |
| 采样步数 | 10 | 5 - 20 | 8 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 20 | 13 | 0% |
| 采样算法 | euler | - | 13 | 54% |
| 调度器 | beta | - | 13 | 46% |
| 重绘幅度 | 1 | 0.3 - 1 | 8 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.6 - 1，5 个样本，取值集中（一致性 83%）
- LoRA 文本强度 中位数 1，观测区间 0.6 - 1，5 个样本，取值集中（一致性 83%）
- 采样步数 中位数 10，观测区间 5 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 20，13 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，13 个样本，一致性 54%
- 调度器 最常用 beta，13 个样本，一致性 46%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，8 个样本
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed、easy clearCacheAll
