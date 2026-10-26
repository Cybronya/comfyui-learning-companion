---
name: unknown_workflow_sampler_clip_vae_66
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.958333
common_nodes: [CLIPLoader, CLIPTextEncode, SaveImage, TwinFlow_SM_KSampler, TwinFlow_SM_Model, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/TwinFlow-QI 基础流_2006183647942021122.json, 图片生成/文生图/TwinFlow-Z 基础流_2006774933891846146.json, 图片生成/文生图/zimage2步出图_2006767553821020161.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_66

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/TwinFlow-QI 基础流_2006183647942021122.json、图片生成/文生图/TwinFlow-Z 基础流_2006774933891846146.json、图片生成/文生图/zimage2步出图_2006767553821020161.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `SaveImage`
- `TwinFlow_SM_KSampler`
- `TwinFlow_SM_Model`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 2 | 2 - 2 | 3 | 100% |
| Prompt 约束强度(CFG) | 1.00482e+09 | 3.28647e+08 - 1.12825e+09 | 3 | 57% |
| 采样算法 | randomize | - | 3 | 100% |
| 调度器 | 0 | 0 - 0 | 3 | 100% |
| 重绘幅度 | all | - | 3 | 33% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.00482e+09，观测区间 3.28647e+08 - 1.12825e+09，3 个样本
- 采样算法 最常用 randomize，3 个样本，一致性 100%
- 调度器 中位数 0，观测区间 0 - 0，3 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 all，3 个样本，一致性 33%
- 风险：Prompt 约束强度(CFG) 观测到 1.12825e+09，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
