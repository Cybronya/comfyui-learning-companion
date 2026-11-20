---
name: unknown_workflow_sampler_checkpoint_vae_10
type: Unknown Workflow
frequency: 11
level: strong
coverage: 1
common_nodes: [CR Text, CheckpointLoaderSimple, ConditioningZeroOut, KSampler, LoadImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/29itifast_2049490245002993665.json, 图片生成/反推提示词/92dantucy_2056714574065393665.json, 图片生成/图生图/Qwen-Rapid-AIO_2047923784266555393.json, 图片生成/图生图/图生图一键工作_2001323637812625410.json, 图片生成/图生图/图生图一键工作_2045091323006427138.json, 图片生成/图生图/图生图工作流_2037530314460893185.json, 图片生成/文生图/Qwen-Rapid-AIO_2054565798374584322.json, 图片生成/文生图/YYEMOJI 图生图一键工作_2056537190146076674.json, 图片生成/文生图/图生图一键工作_2049476537925242881.json, 图片生成/文生图/通义千问文生图_2064587610374361089.json, 平台全量/一句话改图_1956406306309591041.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_10

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/反推提示词/29itifast_2049490245002993665.json、图片生成/反推提示词/92dantucy_2056714574065393665.json、图片生成/图生图/Qwen-Rapid-AIO_2047923784266555393.json、图片生成/图生图/图生图一键工作_2001323637812625410.json、图片生成/图生图/图生图一键工作_2045091323006427138.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 11 个 workflow 都包含：
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/11 个有
- `easy cleanGpuUsed` —— 10/11 个有
- `easy clearCacheAll` —— 10/11 个有
- `SaveImage` —— 7/11 个有
- `CompressImages` —— 6/11 个有
- `SaveLatent` —— 6/11 个有
- `RTXVideoSuperResolution` —— 2/11 个有
- `TT_img_enc` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 11 | 74% |
| 采样算法 | er_sde | - | 11 | 55% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，11 个样本
- 采样算法 最常用 er_sde，11 个样本，一致性 55%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
