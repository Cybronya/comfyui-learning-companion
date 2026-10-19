---
name: unknown_workflow_sampler_3
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.82375
common_nodes: [AudioMerge, AudioSeparation, Bjornulf_FreeVRAM, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, RunningHub SoulX-Singer Preprocess Pipeline, RunningHub SoulX-Singer Preprocessor, RunningHub SoulX-Singer SVS Loader, RunningHub SoulX-Singer SVS Processor, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/soulx-singer_多语言翻唱_2081217314275545089.json, 音频生成/音频生成/soulx-singer_歌曲声音转换_2027973593069527042.json, 音频生成/音频生成/一键翻唱爆款歌曲（普通话版）_2054373511006826498.json, 音频生成/音频生成/一键翻唱爆款歌曲（普通话版）_2054766006710620162.json, 音频生成/音频生成/歌曲音色转换_2025823310495358977.json, 音频生成/音频生成/音频分离与音色转化_2041523190177996801.json, 音频生成/音频生成/音频处理大集合（Supermate宝藏宝）_2081261037361393666.json, 音频生成/音频生成/音频改变音色音调 SoulX 歌曲音色转换 人声改变音色 音乐变人声音色_2027222941980692482.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_3

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（音频生成/音频生成/soulx-singer_多语言翻唱_2081217314275545089.json、音频生成/音频生成/soulx-singer_歌曲声音转换_2027973593069527042.json、音频生成/音频生成/一键翻唱爆款歌曲（普通话版）_2054373511006826498.json、音频生成/音频生成/一键翻唱爆款歌曲（普通话版）_2054766006710620162.json、音频生成/音频生成/歌曲音色转换_2025823310495358977.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `AudioMerge`
- `AudioSeparation`
- `Bjornulf_FreeVRAM`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `RunningHub SoulX-Singer Preprocess Pipeline`
- `RunningHub SoulX-Singer Preprocessor`
- `RunningHub SoulX-Singer SVS Loader`
- `RunningHub SoulX-Singer SVS Processor`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `FL_ChatterboxVC` —— 2/8 个有
- `SeedVCRun` —— 2/8 个有
- `TrimAudioDuration` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `Fast Groups Muter (rgthree)` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
