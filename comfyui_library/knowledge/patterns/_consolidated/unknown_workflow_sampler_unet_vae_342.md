---
name: unknown_workflow_sampler_unet_vae_342
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.964333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3Easy, MiniMaxH3EasyModelAdapter, MiniMaxH3EasyOutput, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [音频生成/音频生成/AI视频模型转音频模型_2089669249060134913.json, 音频生成/音频生成/MINIMAX视频模型转音频模型_2090695139621695490.json, 音频生成/音频生成/Minimax H3-AI音乐+声音克隆工作流（超长生成、多音频参考）_2090786847566946305.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_342

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/AI视频模型转音频模型_2089669249060134913.json、音频生成/音频生成/MINIMAX视频模型转音频模型_2090695139621695490.json、音频生成/音频生成/Minimax H3-AI音乐+声音克隆工作流（超长生成、多音频参考）_2090786847566946305.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyModelAdapter`
- `MiniMaxH3EasyOutput`
- `ModelAttentionBackend`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveAudioAdvanced` —— 2/3 个有
- `easy promptList` —— 2/3 个有
- `LoadAudio` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `MiniMaxH3TurboLoRA` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `SpectrumApplyMiniMaxH3` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
