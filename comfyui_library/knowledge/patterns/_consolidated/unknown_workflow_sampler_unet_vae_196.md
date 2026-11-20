---
name: unknown_workflow_sampler_unet_vae_196
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.854
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 全能参考 自动提示词工作流_2084174326928076802.json, 视频生成/文生视频/MiniMax H3 全能参考生视频_2085373656615702530.json, 视频生成/文生视频/MiniMax H3 全能大合集工作流_2084920689999572993.json, 视频生成/文生视频/MiniMax H3 分镜成片 + IndexTTS 声音克隆配音｜剧本·角色图·分镜图一次出片（画_2087519875668471809.json, 视频生成/文生视频/MiniMax H3 多图参考成片 V2｜官方六段式提示词 · 口型自然 · IndexTTS 声音克隆配音（画音合一）_2087523744918102018.json, 视频生成/文生视频/MiniMax H3 开源版-多参考图+IndexTTS参考音生视频_2087370253885067266.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_196

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 全能参考 自动提示词工作流_2084174326928076802.json、视频生成/文生视频/MiniMax H3 全能参考生视频_2085373656615702530.json、视频生成/文生视频/MiniMax H3 全能大合集工作流_2084920689999572993.json、视频生成/文生视频/MiniMax H3 分镜成片 + IndexTTS 声音克隆配音｜剧本·角色图·分镜图一次出片（画_2087519875668471809.json、视频生成/文生视频/MiniMax H3 多图参考成片 V2｜官方六段式提示词 · 口型自然 · IndexTTS 声音克隆配音（画音合一）_2087523744918102018.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `AudioCrop` —— 3/6 个有
- `IndexTTS2Run` —— 3/6 个有
- `MiniMaxH3BlockCacheT8` —— 3/6 个有
- `MultiLinePromptIndex` —— 3/6 个有
- `SaveAudioMP3` —— 3/6 个有
- `VAEDecodeAudio` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `llama_cpp_instruct_adv` —— 1/6 个有
- `llama_cpp_model_loader` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
