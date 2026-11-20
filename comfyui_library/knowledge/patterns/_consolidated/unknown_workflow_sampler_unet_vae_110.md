---
name: unknown_workflow_sampler_unet_vae_110
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.817545
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, LoadImage, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/video_minimax_h3_r2v_turbo 多参加速_2100758868111486978.json, 视频生成/图生视频/video_minimax_h3_r2v_turbo_4ref_2102954009563848706.json, 视频生成/图生视频/【开源】minimax_h3 音频参考生MV_2084184318896857090.json, 视频生成/图生视频/【老金驿站】MinimaxH3多参考视频工作流_2084270884050792449.json, 视频生成/图生视频/主要_2092662832407076865.json, 视频生成/图生视频/加速升级版！ MiniMax-H3 图生视频！_2088799409717997570.json, 视频生成/图生视频/加速版Minimax多参生视频BF16高质量-sage+Block Cache (T8)_2085374592817909762.json, 视频生成/图生视频/加速高质开源MiniMax+H3+FL2VA开源版-首尾帧参考生视频+++_2084152775365189633.json, 视频生成/图生视频/参考生视频_MiniMax H3_2084453784557809665.json, 视频生成/图生视频/无参考视频-新加速高质开源MiniMax H3 RE2VA开源版_2087442373067501569.json, 视频生成/文生视频/多图参考H3广告_2085248140055236609.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_110

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/video_minimax_h3_r2v_turbo 多参加速_2100758868111486978.json、视频生成/图生视频/video_minimax_h3_r2v_turbo_4ref_2102954009563848706.json、视频生成/图生视频/【开源】minimax_h3 音频参考生MV_2084184318896857090.json、视频生成/图生视频/【老金驿站】MinimaxH3多参考视频工作流_2084270884050792449.json、视频生成/图生视频/主要_2092662832407076865.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `LoadImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 10/11 个有
- `KSamplerSelect` —— 9/11 个有
- `LoadAudio` —— 7/11 个有
- `PathchSageAttentionKJ` —— 6/11 个有
- `VHS_LoadVideo` —— 5/11 个有
- `MiniMaxH3BlockCacheT8` —— 4/11 个有
- `LoraLoaderModelOnly` —— 3/11 个有
- `PreviewAny` —— 3/11 个有
- `RHLLMChatNode` —— 3/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/11 个有
- `MiniMaxH3TurboLoRA` —— 2/11 个有
- `MiniMaxH3TurboSampler` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `MiniMaxH3ImageToVideo` —— 1/11 个有
- `TrimAudioDuration` —— 1/11 个有
- `VHS_VideoInfo` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
