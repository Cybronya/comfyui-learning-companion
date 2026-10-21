---
name: unknown_workflow_lora_sampler_unet_47
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7495
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MultiRateSamplerEXPT8, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveAudioAdvanced, UNETLoader, VAEDecodeAudio, VAELoader, easy ifElse, easy seed]
problems: []
missing: []
members: [音频生成/音频生成/MiniMax H3 TTS _ 文生音频 _ 音频克隆 _ 开源版SeedAudio_2086469576803569665.json, 音频生成/音频生成/MiniMax_H3_双人对话_2100869700593999874.json, 音频生成/音频生成/MiniMax_H3_双人对话_2101136318687436802.json, 音频生成/音频生成/minimax-H3-纯文生语音_2099494195999371266.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_47

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/MiniMax H3 TTS _ 文生音频 _ 音频克隆 _ 开源版SeedAudio_2086469576803569665.json、音频生成/音频生成/MiniMax_H3_双人对话_2100869700593999874.json、音频生成/音频生成/MiniMax_H3_双人对话_2101136318687436802.json、音频生成/音频生成/minimax-H3-纯文生语音_2099494195999371266.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MultiRateSamplerEXPT8`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveAudioAdvanced`
- `UNETLoader`
- `VAEDecodeAudio`
- `VAELoader`
- `easy ifElse`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 3/4 个有
- `MiniMaxH3AudioConditioningT8` —— 3/4 个有
- `easy isNone` —— 3/4 个有
- `StringReplace` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
