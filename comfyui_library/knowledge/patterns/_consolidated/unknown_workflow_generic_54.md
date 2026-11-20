---
name: unknown_workflow_generic_54
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.9857
common_nodes: [CR Prompt Text, RunningHub_VoxCPM_LoadModel, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/VoxCPM2 设计新的声音_2041869666791989249.json, 音频生成/音频生成/VoxCPM2人声声音设计-3.0_2046414147428032514.json, 音频生成/音频生成/VoxCPM2声音设计V3_2041782616201895938.json, 音频生成/音频生成/VoxCPM2声音设计_2047579813652729858.json, 音频生成/音频生成/VoxCPM2多人语音工作流（人数无上限）_2046148545018863618.json, 音频生成/音频生成/VoxCPM2语音克隆(四川话)_2047577873472561153.json, 音频生成/音频生成/VoxCPM2语音克隆+声音设计（天津话）V3_2041826223764021250.json, 音频生成/音频生成/VoxCPM2语音克隆+声音设计（广东话）V3_2041823275411574786.json, 音频生成/音频生成/VoxCPM2语音克隆+声音设计（河南话）V3_2041823297939185665.json, 音频生成/音频生成/VoxCPM2语音克隆（天津话）_2047581701450244098.json, 音频生成/音频生成/VoxCPM2语音克隆（广东话）_2047575508455530497.json, 音频生成/音频生成/VoxCPM2语音克隆（河南话）_2047580936384024578.json, 音频生成/音频生成/VoxCPM2语音极限克隆V2_2041822737211072514.json, 音频生成/音频生成/VoxCPM2语音极限克隆V2_2045487794499362817.json, 音频生成/音频生成/VoxCPM2长剧情音频克隆和设计_2046400394552676354.json, 音频生成/音频生成/VoxCPM语音克隆+音频设计V2_2041780714080833537.json, 音频生成/音频生成/VoxCPM语音克隆+音频设计_2047580106213822465.json, 音频生成/音频生成/VoxCPM语音克隆_2043262047881793538.json, 音频生成/音频生成/VoxCPM：最强语音克隆+音频设计_2042490156510355457.json, 音频生成/音频生成/（贞贞lora）VoxCPM2语音克隆+声音设计_2049724105854816257.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_54

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（音频生成/音频生成/VoxCPM2 设计新的声音_2041869666791989249.json、音频生成/音频生成/VoxCPM2人声声音设计-3.0_2046414147428032514.json、音频生成/音频生成/VoxCPM2声音设计V3_2041782616201895938.json、音频生成/音频生成/VoxCPM2声音设计_2047579813652729858.json、音频生成/音频生成/VoxCPM2多人语音工作流（人数无上限）_2046148545018863618.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 20 个 workflow 都包含：
- `CR Prompt Text`
- `RunningHub_VoxCPM_LoadModel`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `RunningHub_VoxCPM_Generate` —— 18/20 个有
- `LoadAudio` —— 15/20 个有
- `RunningHub_VoxCPM_MultiSpeaker_ListReference` —— 2/20 个有
- `Qwen3ASRLoader` —— 1/20 个有
- `Qwen3ASRTranscribe` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
