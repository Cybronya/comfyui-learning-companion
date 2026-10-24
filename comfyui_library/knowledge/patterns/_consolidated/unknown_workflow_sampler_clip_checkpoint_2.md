---
name: unknown_workflow_sampler_clip_checkpoint_2
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.744667
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, ComfySwitchNode, EmptyLatentAudio, JsonExtractString, KSampler, PreviewAny, PrimitiveBoolean, PrimitiveFloat, PrimitiveStringMultiline, StringReplace, TextGenerate, VAEDecodeAudio]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Stable Audio 3 声音资产生成工作流_2058938930971635714.json, 音频生成/音频生成/Stable Audio 3 Medium 音乐制作基础版_2064536725820628994.json, 音频生成/音频生成/Stable Audio 3音乐音效VFXOneShot生成_2059069757013450754.json, 音频生成/音频生成/Stable audio 3纯音乐-音效-VFX-One-Shot音频工作流_2058858797854187521.json, 音频生成/音频生成/Stable audio 3纯音乐-音效-VFX-One-Shot音频工作流_2058933583804452866.json, 音频生成/音频生成/Stable audio 3音效生成官方工作流_2058187926873403394.json, 音频生成/音频生成/Stable-Audio-3_2094222954325430274.json, 音频生成/音频生成/audio_stable_audio_3_medium_2058366786768302081.json, 音频生成/音频生成/stable audio3纯音乐_2072513604150190081.json, 音频生成/音频生成/stable audio3纯音乐生成_2058516362439512066.json, 音频生成/音频生成/stable audio3纯音乐生成器_2059127739705286657.json, 音频生成/音频生成/stable audio3纯音乐生成器_2072517401828225026.json, 音频生成/音频生成/stable_audio_3_音乐创作—四种模式可选 自动扩展提示词_2059889777259925505.json, 音频生成/音频生成/stable_audio_3_音乐创作—四种模式可选 自动扩展提示词_2087402108919304193.json, 音频生成/音频生成/stable_audio_3（纯音乐生成）_2080834306892713985.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/Stable Audio 3 声音资产生成工作流_2058938930971635714.json、音频生成/音频生成/Stable Audio 3 Medium 音乐制作基础版_2064536725820628994.json、音频生成/音频生成/Stable Audio 3音乐音效VFXOneShot生成_2059069757013450754.json、音频生成/音频生成/Stable audio 3纯音乐-音效-VFX-One-Shot音频工作流_2058858797854187521.json、音频生成/音频生成/Stable audio 3纯音乐-音效-VFX-One-Shot音频工作流_2058933583804452866.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `EmptyLatentAudio`
- `JsonExtractString`
- `KSampler`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `StringReplace`
- `TextGenerate`
- `VAEDecodeAudio`

**可变部分**（部分 workflow 才有）：
- `SaveAudioMP3` —— 14/15 个有
- `CustomCombo` —— 12/15 个有
- `easy anythingIndexSwitch` —— 6/15 个有
- `SaveAudio` —— 4/15 个有
- `easy cleanGpuUsed` —— 4/15 个有
- `CR Prompt Text` —— 3/15 个有
- `CR Text` —— 3/15 个有
- `Int` —— 3/15 个有
- `ShowText|pysssss` —— 3/15 个有
- `SaveAudioAdvanced` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 60 | 60 - 60 | 15 | 100% |
| 高度 | 1 | 1 - 1 | 15 | 100% |
| 采样步数 | 8 | 8 - 50 | 15 | 17% |
| Prompt 约束强度(CFG) | 1 | 1 - 7 | 15 | 14% |
| 采样算法 | lcm | - | 15 | 73% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 15/15 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 9/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 60，观测区间 60 - 60，15 个样本，取值集中（一致性 100%）
- 高度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 50，15 个样本，取值分散，一致性仅 17%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 7，15 个样本，取值分散，一致性仅 14%
- 采样算法 最常用 lcm，15 个样本，一致性 73%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：发现KSampler但没有VAEDecode
- 高发问题（9/15 个样本）：Steps较低可能导致细节不足
