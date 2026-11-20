---
name: unknown_workflow_sampler_clip_unet_175
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.991125
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/千问文生图_1952243963510075394.json, 图片生成/文生图/千问文生图最新版工作流_2000925762351923202.json, 图片生成/文生图/千问文生图，极简加速版（Qwen4-8步））_1958431884814479361.json, 图片生成/文生图/古风男工作流_2051554347225497601.json, 图片生成/文生图/墨宝映画人物设定_2015364874955657217.json, 图片生成/文生图/帝企鹅工作流_1980164055954526209.json, 图片生成/文生图/性感情趣内衣亮亮丝袜_2024871763326275585.json, 图片生成/文生图/性感情趣内衣亮亮丝袜_2110944951742844929.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_175

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/千问文生图_1952243963510075394.json、图片生成/文生图/千问文生图最新版工作流_2000925762351923202.json、图片生成/文生图/千问文生图，极简加速版（Qwen4-8步））_1958431884814479361.json、图片生成/文生图/古风男工作流_2051554347225497601.json、图片生成/文生图/墨宝映画人物设定_2015364874955657217.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 7/8 个有
- `ModelSamplingAuraFlow` —— 7/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `CompressImages` —— 2/8 个有
- `FluxEmptyLatentSizePicker` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `ShowText` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 35 | 8 | 29% |
| Prompt 约束强度(CFG) | 1.26 | 1 - 4 | 8 | 37% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 832x1152 (0.96MP) - 3:4 | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 35，8 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1.26，观测区间 1 - 4，8 个样本，取值分散，一致性仅 37%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（5/8 个样本）：Steps较低可能导致细节不足
