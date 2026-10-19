---
name: unknown_workflow_generic_894
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.807
common_nodes: [AudioSeparation, LoadAudio, SaveAudio, SeedVCRun, VHS_LoadVideo]
problems: []
missing: []
members: [音频生成/音频生成/语音音色克隆STS_2074124382586359809.json, 音频生成/音频生成/音色迁移_2026843563522265089.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_894

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/语音音色克隆STS_2074124382586359809.json、音频生成/音频生成/音色迁移_2026843563522265089.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioSeparation`
- `LoadAudio`
- `SaveAudio`
- `SeedVCRun`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
