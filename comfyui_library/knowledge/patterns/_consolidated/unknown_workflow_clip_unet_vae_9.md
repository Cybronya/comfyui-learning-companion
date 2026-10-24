---
name: unknown_workflow_clip_unet_vae_9
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.946875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Instagirl Wan2.2_1954740605987504129.json, 图片生成/文生图/WAN2.1文生图_1946266988476030978.json, 图片生成/文生图/Wan2.1 文生图美学去AI感_1950183203102441473.json, 图片生成/文生图/Wan2.1文生图+真实感=艾橘溪_1944626515541676033.json, 图片生成/文生图/Wan2.2 文生图_1951184476380536834.json, 图片生成/文生图/Wan2.2文生图_1951193822992773122.json, 图片生成/文生图/wan2.2快速低燥文生图_2032451540241354753.json, 图片生成/文生图/图片-文生图-Instagirl_1960284703142129666.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_9

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Instagirl Wan2.2_1954740605987504129.json、图片生成/文生图/WAN2.1文生图_1946266988476030978.json、图片生成/文生图/Wan2.1 文生图美学去AI感_1950183203102441473.json、图片生成/文生图/Wan2.1文生图+真实感=艾橘溪_1944626515541676033.json、图片生成/文生图/Wan2.2 文生图_1951184476380536834.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/8 个有
- `easy cleanGpuUsed` —— 6/8 个有
- `KSampler` —— 5/8 个有
- `Int` —— 4/8 个有
- `ModelSamplingSD3` —— 4/8 个有
- `KSamplerAdvanced` —— 3/8 个有
- `LoraLoader` —— 3/8 个有
- `LoadImage` —— 2/8 个有
- `Float` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有
- `SaveAnimatedWEBP` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 采样步数 | 12 | 8 - 20 | 5 | 64% |
| Prompt 约束强度(CFG) | 2.25 | 1 - 20 | 8 | 0% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | simple | - | 8 | 38% |
| 重绘幅度 | 1 | 0.3 - 1 | 5 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 12，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 2.25，观测区间 1 - 20，8 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 38%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，5 个样本
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
