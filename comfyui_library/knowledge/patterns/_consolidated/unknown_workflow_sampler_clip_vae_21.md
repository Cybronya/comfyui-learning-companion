---
name: unknown_workflow_sampler_clip_vae_21
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.957111
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Nunchaku-qwen image文生图_1965030044580069377.json, 图片生成/文生图/Nunchaku1.0正式版+ Qwen-Image：速度与质量的终极平衡！文生图_1965259047710674945.json, 图片生成/文生图/Nunchaku8步加速千问文生图_1962382351810564097.json, 图片生成/文生图/Nunchaku千问文生图_1959849718341906433.json, 图片生成/文生图/Nunchaku千问文生图超快_1959997422854418434.json, 图片生成/文生图/Nunchaku超级加速 Qwen Image文生图_1966409848168624130.json, 图片生成/文生图/image_qwen_Image_2512_2018879224546856962.json, 图片生成/文生图/千问文生图+双节棍（Qwen Nunchaku）_1964286433756332033.json, 图片生成/文生图/千问文生图极速生图双节棍 Qwen Nunchaku_1968509624422944769.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_21

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Nunchaku-qwen image文生图_1965030044580069377.json、图片生成/文生图/Nunchaku1.0正式版+ Qwen-Image：速度与质量的终极平衡！文生图_1965259047710674945.json、图片生成/文生图/Nunchaku8步加速千问文生图_1962382351810564097.json、图片生成/文生图/Nunchaku千问文生图_1959849718341906433.json、图片生成/文生图/Nunchaku千问文生图超快_1959997422854418434.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 5/9 个有
- `CR SDXL Aspect Ratio` —— 5/9 个有
- `EmptySD3LatentImage` —— 4/9 个有
- `Text` —— 3/9 个有
- `Text Multiline` —— 3/9 个有
- `JjkText` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `NunchakuQwenImageLoraStackV3` —— 1/9 个有
- `PreviewImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 30 | 9 | 45% |
| Prompt 约束强度(CFG) | 2 | 1 - 3.5 | 9 | 54% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 30，9 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 3.5，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
