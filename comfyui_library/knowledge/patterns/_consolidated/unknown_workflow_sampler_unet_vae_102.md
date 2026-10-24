---
name: unknown_workflow_sampler_unet_vae_102
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8537
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 文生视频（开源版）_2084993426063450113.json, 视频生成/文生视频/MiniMax H3 首尾帧图生视频_2084850865038520322.json, 视频生成/文生视频/MiniMax H3+ 新4步LoRa + 参考图图生视频工作流_2092505916875829250.json, 视频生成/文生视频/MiniMax H3_文生视频工作流_2084504955460866050.json, 视频生成/文生视频/MiniMax H3全能参考工作流_2084202154499338242.json, 视频生成/文生视频/MiniMax H3参考生视频6倍加速48GB高配版_2086459494866968577.json, 视频生成/文生视频/MiniMax H3参考生视频6倍加速80GB满配版_2086411609148313601.json, 视频生成/文生视频/MiniMax+H3+R2V-02：纯视频参考_2084850819463208962.json, 视频生成/文生视频/MiniMax+H3+R2V-03：人物图＋动作视频_2084850873976578049.json, 视频生成/文生视频/R2V-06：人物图＋动作视频＋新音频_2084910702598381569.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_102

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 文生视频（开源版）_2084993426063450113.json、视频生成/文生视频/MiniMax H3 首尾帧图生视频_2084850865038520322.json、视频生成/文生视频/MiniMax H3+ 新4步LoRa + 参考图图生视频工作流_2092505916875829250.json、视频生成/文生视频/MiniMax H3_文生视频工作流_2084504955460866050.json、视频生成/文生视频/MiniMax H3全能参考工作流_2084202154499338242.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
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
- `LoadImage` —— 9/10 个有
- `PathchSageAttentionKJ` —— 9/10 个有
- `PrimitiveStringMultiline` —— 8/10 个有
- `LoadAudio` —— 7/10 个有
- `MiniMaxH3ReferenceToVideo` —— 7/10 个有
- `EasyCache` —— 6/10 个有
- `ImageResizeKJv2` —— 6/10 个有
- `GetVideoComponents` —— 4/10 个有
- `LoadVideo` —— 4/10 个有
- `LoraLoaderModelOnly` —— 4/10 个有
- `SolAttnPatch` —— 4/10 个有
- `MiniMaxH3ImageToVideo` —— 3/10 个有
- `TrimAudioDuration` —— 3/10 个有
- `Video Slice` —— 3/10 个有
- `MiniMaxH3BlockCacheT8` —— 1/10 个有
- `ModelPatchTorchSettings` —— 1/10 个有
- `SpectrumSDXLBatch` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
