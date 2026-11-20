---
name: unknown_workflow_sampler_60
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.641667
common_nodes: [CreateVideo, JWInteger, JoyAI_Echo_SM_Clip, JoyAI_Echo_SM_Encoder, JoyAI_Echo_SM_KSampler, JoyAI_Echo_SM_Model, PreviewAny, SaveVideo]
problems: []
missing: []
members: [视频生成/文生视频/JoyAI Echo无限数字人_2063842945094209537.json, 视频生成/文生视频/Joyai_Echo智能单镜头文生数字人视频_2063868141255618562.json, 视频生成/文生视频/Joyai_Echo智能多镜头文生数字人视频_2063873351684280322.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_60

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/JoyAI Echo无限数字人_2063842945094209537.json、视频生成/文生视频/Joyai_Echo智能单镜头文生数字人视频_2063868141255618562.json、视频生成/文生视频/Joyai_Echo智能多镜头文生数字人视频_2063873351684280322.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateVideo`
- `JWInteger`
- `JoyAI_Echo_SM_Clip`
- `JoyAI_Echo_SM_Encoder`
- `JoyAI_Echo_SM_KSampler`
- `JoyAI_Echo_SM_Model`
- `PreviewAny`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `RH_LLMAPI_Pro_Node` —— 2/3 个有
- `Text` —— 2/3 个有
- `easy showAnything` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12345 | 12345 - 12345 | 3 | 100% |
| Prompt 约束强度(CFG) | fixed | - | 3 | 100% |
| 采样算法 | 121 | 121 - 121 | 3 | 100% |
| 调度器 | 24 | 24 - 24 | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12345，观测区间 12345 - 12345，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 最常用 fixed，3 个样本，一致性 100%
- 采样算法 中位数 121，观测区间 121 - 121，3 个样本，取值集中（一致性 100%）
- 调度器 中位数 24，观测区间 24 - 24，3 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 12345，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
