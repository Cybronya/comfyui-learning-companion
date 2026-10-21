---
name: unknown_workflow_sampler_unet_vae_71
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8918
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 分镜成片 + IndexTTS 声音克隆配音｜剧本·角色图·分镜图一次出片（画_2087519875668471809.json, 视频生成/文生视频/MiniMax H3 图文生视频_2087784410467880961.json, 视频生成/文生视频/MiniMax H3 多图参考 开源版_2094392605172912129.json, 视频生成/文生视频/MiniMax H3 多图参考成片 V2｜官方六段式提示词 · 口型自然 · IndexTTS 声音克隆配音（画音合一）_2087523744918102018.json, 视频生成/文生视频/MiniMax H3 多模态参考生视频（SageAttention 加速版）_2085990402720616449.json, 视频生成/文生视频/MiniMax H3 多模态参考生视频（开源版）_2084993447697674241.json, 视频生成/文生视频/MiniMax H3 开源版-多参考图+IndexTTS参考音生视频_2087370253885067266.json, 视频生成/文生视频/MiniMax H3｜5图多参考快速出片｜5-15秒｜稳定版_2091107780571783170.json, 视频生成/文生视频/Minimax H3 多模态--综合应用流_2085249742157729793.json, 视频生成/文生视频/【5】全能多模态--多参视频生成（真正平替seedance）--ref2va模型_2087209584539820034.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_71

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 分镜成片 + IndexTTS 声音克隆配音｜剧本·角色图·分镜图一次出片（画_2087519875668471809.json、视频生成/文生视频/MiniMax H3 图文生视频_2087784410467880961.json、视频生成/文生视频/MiniMax H3 多图参考 开源版_2094392605172912129.json、视频生成/文生视频/MiniMax H3 多图参考成片 V2｜官方六段式提示词 · 口型自然 · IndexTTS 声音克隆配音（画音合一）_2087523744918102018.json、视频生成/文生视频/MiniMax H3 多模态参考生视频（SageAttention 加速版）_2085990402720616449.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
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
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 9/10 个有
- `VAEDecode` —— 9/10 个有
- `LoadAudio` —— 8/10 个有
- `VAEDecodeAudio` —— 7/10 个有
- `GetVideoComponents` —— 4/10 个有
- `LoadVideo` —— 4/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/10 个有
- `AudioCrop` —— 3/10 个有
- `IndexTTS2Run` —— 3/10 个有
- `MiniMaxH3BlockCacheT8` —— 3/10 个有
- `MultiLinePromptIndex` —— 3/10 个有
- `SaveAudioMP3` —— 3/10 个有
- `EasyCache` —— 2/10 个有
- `Label (rgthree)` —— 2/10 个有
- `LoraLoaderModelOnly` —— 2/10 个有
- `Text` —— 1/10 个有
- `VAEDecodeTiled` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
