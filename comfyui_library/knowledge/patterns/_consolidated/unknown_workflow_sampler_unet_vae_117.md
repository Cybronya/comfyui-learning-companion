---
name: unknown_workflow_sampler_unet_vae_117
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.880889
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 分镜成片 + IndexTTS 声音克隆配音｜剧本·角色图·分镜图一次出片（画_2087519875668471809.json, 视频生成/文生视频/MiniMax H3 图文生视频_2087784410467880961.json, 视频生成/文生视频/MiniMax H3 多图参考 开源版_2094392605172912129.json, 视频生成/文生视频/MiniMax H3 多图参考成片 V2｜官方六段式提示词 · 口型自然 · IndexTTS 声音克隆配音（画音合一）_2087523744918102018.json, 视频生成/文生视频/MiniMax H3 多模态参考生视频（开源版）_2084993447697674241.json, 视频生成/文生视频/MiniMax H3 开源版-多参考图+IndexTTS参考音生视频_2087370253885067266.json, 视频生成/文生视频/MiniMax H3 文图生视频、参考生视频多合一工作流-B站UP主@好奇漫步_2086134141166383105.json, 视频生成/文生视频/MiniMax H3多合一｜Turbo4 + Sage + T8 Stable 组合加速版｜B站UP主@好奇漫步_2086728037277720578.json, 视频生成/文生视频/MiniMax H3多合一｜V6_LightX2V官方Turbo4加速版｜B站UP主@好奇漫步_2086676399020142594.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_117

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 分镜成片 + IndexTTS 声音克隆配音｜剧本·角色图·分镜图一次出片（画_2087519875668471809.json、视频生成/文生视频/MiniMax H3 图文生视频_2087784410467880961.json、视频生成/文生视频/MiniMax H3 多图参考 开源版_2094392605172912129.json、视频生成/文生视频/MiniMax H3 多图参考成片 V2｜官方六段式提示词 · 口型自然 · IndexTTS 声音克隆配音（画音合一）_2087523744918102018.json、视频生成/文生视频/MiniMax H3 多模态参考生视频（开源版）_2084993447697674241.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
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
- `LoadAudio` —— 8/9 个有
- `PrimitiveStringMultiline` —— 8/9 个有
- `VAEDecodeAudio` —— 6/9 个有
- `GetVideoComponents` —— 4/9 个有
- `LoadVideo` —— 4/9 个有
- `AudioCrop` —— 3/9 个有
- `ComfySwitchNode` —— 3/9 个有
- `IndexTTS2Run` —— 3/9 个有
- `MiniMaxH3BlockCacheT8` —— 3/9 个有
- `MiniMaxH3ImageToVideo` —— 3/9 个有
- `MultiLinePromptIndex` —— 3/9 个有
- `PrimitiveInt` —— 3/9 个有
- `SaveAudioMP3` —— 3/9 个有
- `LoraLoaderBypassModelOnly` —— 2/9 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/9 个有
- `Text` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
