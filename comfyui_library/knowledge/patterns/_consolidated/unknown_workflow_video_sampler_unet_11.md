---
name: unknown_workflow_video_sampler_unet_11
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.861381
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1 minimax_h3_i2v_fastH3_raw_bigface_10s_2102562439794610177.json, 视频生成/图生视频/1图_multi_ref_minimax_h3_i2v_2094711687055241217.json, 视频生成/图生视频/2图_multi_ref_minimax_h3_i2v_2094710093471375361.json, 视频生成/图生视频/3图_multi_ref_minimax_h3_i2v_2092499319101415426.json, 视频生成/图生视频/8步加速官流_2108935132144037890.json, 视频生成/图生视频/AI短剧制作全流程_2111223881188077570.json, 视频生成/图生视频/MiNiMaxH3_六图+三音频参考_2111108549219799042.json, 视频生成/图生视频/Minimax H3三图参考+2参考音_2089300447696871426.json, 视频生成/图生视频/Minimax H3三图参考+三参考音_2089302046485864449.json, 视频生成/图生视频/Minimax H3单图参考+1参考音_2089270431596507137.json, 视频生成/图生视频/Minimax H3双图参考+1参考音【口播用】_2090260648876920833.json, 视频生成/图生视频/Minimax H3双图参考+1参考音【批量管理系统api用】_2093664402544353282.json, 视频生成/图生视频/Minimax H3双图参考+2参考音_2089282022698213377.json, 视频生成/图生视频/api竖屏768pH3官流_2110570859592249346.json, 视频生成/图生视频/api竖屏768pH3官流_2111012386319724545.json, 视频生成/图生视频/【MINIMAX H3】高动态_单采高清_2109286224707022849.json, 视频生成/图生视频/【MiniMax H3】短剧工作流_2110380691388194818.json, 视频生成/图生视频/【MiniMax_H3】短剧工作流_2110893565873311745.json, 视频生成/图生视频/【疯了的动态】Dasiwa_单采样25步无加速lora_2096793272898383874.json, 视频生成/图生视频/【阿良绘】MiniMax H3加速版｜速度与质量均衡V2_2109543805493014529.json, 视频生成/图生视频/名画自动写脚本直出视频H-3_2108343061192466434.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_11

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/1 minimax_h3_i2v_fastH3_raw_bigface_10s_2102562439794610177.json、视频生成/图生视频/1图_multi_ref_minimax_h3_i2v_2094711687055241217.json、视频生成/图生视频/2图_multi_ref_minimax_h3_i2v_2094710093471375361.json、视频生成/图生视频/3图_multi_ref_minimax_h3_i2v_2092499319101415426.json、视频生成/图生视频/8步加速官流_2108935132144037890.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 21 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 20/21 个有
- `BasicScheduler` —— 19/21 个有
- `LoraLoaderModelOnly` —— 16/21 个有
- `LoadAudio` —— 12/21 个有
- `ModelAttentionBackend` —— 12/21 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/21 个有
- `INTConstant` —— 10/21 个有
- `MiniMaxH3SigmaShift` —— 8/21 个有
- `ModelPreviewOverrideKJ` —— 8/21 个有
- `BlockSparseAttention` —— 7/21 个有
- `ManualSigmas` —— 6/21 个有
- `LoraLoaderBypassModelOnly` —— 5/21 个有
- `SolAttnMiniMax` —— 5/21 个有
- `PainterVRAM` —— 3/21 个有
- `PathchSageAttentionKJ` —— 3/21 个有
- `VHS_LoadVideo` —— 3/21 个有
- `YK_LoadImageFromURL` —— 3/21 个有
- `忽略多组孤海` —— 3/21 个有
- `EmptyImage` —— 1/21 个有
- `JjkText` —— 1/21 个有
- `MiniMaxH3ImageToVideo` —— 1/21 个有
- `PreviewImage` —— 1/21 个有
- `QWEN_TextDisplay` —— 1/21 个有
- `RHLLMChatNode` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
