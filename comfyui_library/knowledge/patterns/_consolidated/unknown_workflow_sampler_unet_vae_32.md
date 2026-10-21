---
name: unknown_workflow_sampler_unet_vae_32
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.7965
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [数字人/数字人/MiniMax-H3伟大的开源模型  图片声音驱动数字人_2084654275631865857.json, 数字人/数字人/benson  声音克隆数字人_2097164489119588353.json, 数字人/数字人/最新MiniMax-H3 数字人说唱跳流畅自然_2085274986457157634.json, 视频生成/图生视频/(0713)MiniMaxH3 参考生视频（量化加速版） _ 文本 图像 音频 视频_2088910957308370946.json, 视频生成/图生视频/(0715)MiniMaxH3 参考生视频（量化加速版） _ 文本 图像 音频 视频_2088947852180545538.json, 视频生成/图生视频/(10Eros-Max V3)Minimax参考生视频BF16高质量加速版V3_2086185973813174274.json, 视频生成/图生视频/2倍速！加速版Minimax H3多参生视频sag+backend+block cache_2087475848759832577.json, 视频生成/图生视频/MiniMax H3 双角色+背景+自定义音频输入 视频生成工作流_2084953803597635586.json, 视频生成/图生视频/MiniMax H3+lightx2v 4步加速全能参考工作流2图_2086437276707545089.json, 视频生成/图生视频/漫剧林辰_2103760332870217729.json, 视频生成/图生视频/短剧漫剧参考图生视频_2103117172716429314.json, 视频生成/图生视频/自我介绍_2110222353635561474.json, 视频生成/图生视频/走秀_2110212966074376193.json, 视频生成/文生视频/260818002. MiniMax-H3 全能参考速生视频_2089370236645634050.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_32

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（数字人/数字人/MiniMax-H3伟大的开源模型  图片声音驱动数字人_2084654275631865857.json、数字人/数字人/benson  声音克隆数字人_2097164489119588353.json、数字人/数字人/最新MiniMax-H3 数字人说唱跳流畅自然_2085274986457157634.json、视频生成/图生视频/(0713)MiniMaxH3 参考生视频（量化加速版） _ 文本 图像 音频 视频_2088910957308370946.json、视频生成/图生视频/(0715)MiniMaxH3 参考生视频（量化加速版） _ 文本 图像 音频 视频_2088947852180545538.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 14 个 workflow 都包含：
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
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 10/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/14 个有
- `LoadAudio` —— 8/14 个有
- `LoraLoaderModelOnly` —— 8/14 个有
- `PrimitiveStringMultiline` —— 8/14 个有
- `CR Text` —— 6/14 个有
- `MiniMaxH3BlockCacheT8` —— 4/14 个有
- `VHS_LoadVideo` —— 4/14 个有
- `AudioCrop` —— 3/14 个有
- `ModelAttentionBackend` —— 3/14 个有
- `AILab_QwenVL` —— 2/14 个有
- `ComfyMiniMaxH3Director` —— 2/14 个有
- `JoinStrings` —— 2/14 个有
- `SolAttnMiniMax` —— 2/14 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/14 个有
- `SpectrumSDXL` —— 1/14 个有
- `TrimAudioDuration` —— 1/14 个有
- `VHS_LoadAudioUpload` —— 1/14 个有
- `孤海注释` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
