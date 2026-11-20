---
name: unknown_workflow_sampler_55
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8635
common_nodes: [LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, SaveAudioMP3]
problems: []
missing: []
members: [数字人/数字人/烟嗓版翻唱必备人声分离_2117072683547578370.json, 音频生成/音频生成/人声分离背景音去除提取人声去除杂音-方便克隆_2061002830537912321.json, 音频生成/音频生成/人声和音乐分离_2041783462037823490.json, 音频生成/音频生成/声音分离_2000428461267316737.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_55

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/烟嗓版翻唱必备人声分离_2117072683547578370.json、音频生成/音频生成/人声分离背景音去除提取人声去除杂音-方便克隆_2061002830537912321.json、音频生成/音频生成/人声和音乐分离_2041783462037823490.json、音频生成/音频生成/声音分离_2000428461267316737.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `SaveAudioMP3`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 2/4 个有
- `Bjornulf_FreeVRAM` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
