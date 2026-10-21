---
name: unknown_workflow_sampler_unet_vae_56
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.809727
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/video_minimax_h3_t2v_2084181061847838721.json, 视频生成/文生视频/video_minimax_h3_t2v_2084826081865068545.json, 视频生成/文生视频/video_minimax_h3_t2v_fast_2085226763852017665.json, 视频生成/文生视频/【开源】minimax_h3 文生视频_2084163370957234178.json, 视频生成/文生视频/【开源】minimax_h3 文生视频加速版_2085923601651425281.json, 视频生成/文生视频/【遇见AI】Minimax H3 的lightx2v正式版1.0加速lora，4步8步_2087808921359699970.json, 视频生成/文生视频/【遇见AI】Minimax H3官方提示词skill效果测试_2088103932554993666.json, 视频生成/文生视频/【遇见AI】Minimax H3，8大加速方案大对比_2086017355234234370.json, 视频生成/文生视频/一键工作流_2088139639545749506.json, 视频生成/文生视频/极速生成视频｜H3 FAST VSA + 真实人物 LoRA H3 Realism_2094205448344920065.json, 视频生成/视频生视频/_开源_minimax_h3 视频参考生视频加速版_2105631060909445122.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_56

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/video_minimax_h3_t2v_2084181061847838721.json、视频生成/文生视频/video_minimax_h3_t2v_2084826081865068545.json、视频生成/文生视频/video_minimax_h3_t2v_fast_2085226763852017665.json、视频生成/文生视频/【开源】minimax_h3 文生视频_2084163370957234178.json、视频生成/文生视频/【开源】minimax_h3 文生视频加速版_2085923601651425281.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ImageToVideo` —— 10/11 个有
- `CreateVideo` —— 7/11 个有
- `PathchSageAttentionKJ` —— 7/11 个有
- `SaveVideo` —— 7/11 个有
- `LoadImage` —— 6/11 个有
- `LoraLoaderModelOnly` —— 5/11 个有
- `EasyCache` —— 4/11 个有
- `SolAttnPatch` —— 4/11 个有
- `VHS_VideoCombine` —— 4/11 个有
- `ModelAttentionBackend` —— 3/11 个有
- `Text` —— 3/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/11 个有
- `MiniMaxH3ReferenceToVideo` —— 2/11 个有
- `PreviewAny` —— 2/11 个有
- `CLIPTextEncode` —— 1/11 个有
- `MuyeTextEditOutput` —— 1/11 个有
- `NotifyPixaroma` —— 1/11 个有
- `SolAttnMiniMax` —— 1/11 个有
- `SpectrumApplyMiniMaxH3` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
