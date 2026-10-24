---
name: unknown_workflow_sampler_106
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.821
common_nodes: [AudioCrop, Bjornulf_FreeVRAM, Demucs_Loader, Demucs_Sampler, LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MergeAudioNode, Music_AudioMixer, RunningHub SoulX-Singer Preprocess Pipeline, RunningHub SoulX-Singer Preprocessor, RunningHub SoulX-Singer SVS Loader, RunningHub SoulX-Singer SVS Processor, SaveAudio, Save_Audio]
problems: []
missing: [Demucs_Loader, Music_AudioMixer, Demucs_Sampler]
members: [音频生成/音频生成/一键翻唱爆款歌曲 声线迁移翻唱  音色替换翻唱_2054905399773548546.json, 音频生成/音频生成/一键翻唱爆款歌曲 声线迁移翻唱  音色替换翻唱_2059890167187591169.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_106

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/一键翻唱爆款歌曲 声线迁移翻唱  音色替换翻唱_2054905399773548546.json、音频生成/音频生成/一键翻唱爆款歌曲 声线迁移翻唱  音色替换翻唱_2059890167187591169.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `Bjornulf_FreeVRAM`
- `Demucs_Loader`
- `Demucs_Sampler`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MergeAudioNode`
- `Music_AudioMixer`
- `RunningHub SoulX-Singer Preprocess Pipeline`
- `RunningHub SoulX-Singer Preprocessor`
- `RunningHub SoulX-Singer SVS Loader`
- `RunningHub SoulX-Singer SVS Processor`
- `SaveAudio`
- `Save_Audio`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Demucs_Loader、Music_AudioMixer、Demucs_Sampler
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
