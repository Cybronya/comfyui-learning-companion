---
name: unknown_workflow_sampler_67
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.909
common_nodes: [LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, SaveAudioMP3]
problems: []
missing: []
members: [音频生成/音频生成/人声分离背景音去除提取人声去除杂音-方便克隆_2061002830537912321.json, 音频生成/音频生成/人声和音乐分离_2041783462037823490.json, 音频生成/音频生成/声音分离_2000428461267316737.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_67

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/人声分离背景音去除提取人声去除杂音-方便克隆_2061002830537912321.json、音频生成/音频生成/人声和音乐分离_2041783462037823490.json、音频生成/音频生成/声音分离_2000428461267316737.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `SaveAudioMP3`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/3 个有
- `Bjornulf_FreeVRAM` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
