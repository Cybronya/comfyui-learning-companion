---
name: unknown_workflow_sampler_12
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 1
common_nodes: [LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler]
problems: []
missing: []
members: [图片生成/反推提示词/53fenlibanzou_2051271674208768002.json, 平台全量/人声与背景音分离_2120474755580129281.json, 音频生成/音频生成/人声 音乐分离_2075862276602683394.json, 音频生成/音频生成/人声 音乐分离_2079783956492410881.json, 音频生成/音频生成/人声伴奏分离_2023762226083012609.json, 音频生成/音频生成/分离人声伴奏_2032370394153361409.json, 音频生成/音频生成/无限画布-分离人声伴奏_2075086244081659906.json, 音频生成/音频生成/音色转换-Seed Voice Conversion_2052999260559429633.json, 音频生成/音频生成/音频分离人声和背景_2054841869460353025.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_12

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/53fenlibanzou_2051271674208768002.json、平台全量/人声与背景音分离_2120474755580129281.json、音频生成/音频生成/人声 音乐分离_2075862276602683394.json、音频生成/音频生成/人声 音乐分离_2079783956492410881.json、音频生成/音频生成/人声伴奏分离_2023762226083012609.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 9 个 workflow 都包含：
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`

**可变部分**（部分 workflow 才有）：
- `SaveAudio` —— 8/9 个有
- `SaveAudioAdvanced` —— 1/9 个有
- `SeedVCRun` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
