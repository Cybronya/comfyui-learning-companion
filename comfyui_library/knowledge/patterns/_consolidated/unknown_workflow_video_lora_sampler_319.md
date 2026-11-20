---
name: unknown_workflow_video_lora_sampler_319
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.81625
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/【AI影视剧制作】MiniMaxH3-最优官流_2113081896400936962.json, 视频生成/图生视频/【MINIMAX H3】高动态_单采高清_2109286224707022849.json, 视频生成/图生视频/【MiniMax H3】短剧工作流_2110380691388194818.json, 视频生成/图生视频/【MiniMax H3】短剧工作流（批量跑剧版）_2113319585146560513.json, 视频生成/图生视频/【MiniMax_H3】短剧工作流_2110893565873311745.json, 视频生成/图生视频/【疯了的动态】Dasiwa_单采样25步无加速lora_2096793272898383874.json, 视频生成/图生视频/【阿良绘】MiniMax H3加速版｜速度与质量均衡V2_2109543805493014529.json, 视频生成/图生视频/名画自动写脚本直出视频H-3_2108343061192466434.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_319

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/【AI影视剧制作】MiniMaxH3-最优官流_2113081896400936962.json、视频生成/图生视频/【MINIMAX H3】高动态_单采高清_2109286224707022849.json、视频生成/图生视频/【MiniMax H3】短剧工作流_2110380691388194818.json、视频生成/图生视频/【MiniMax H3】短剧工作流（批量跑剧版）_2113319585146560513.json、视频生成/图生视频/【MiniMax_H3】短剧工作流_2110893565873311745.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
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
- `BasicScheduler` —— 7/8 个有
- `ModelPreviewOverrideKJ` —— 7/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/8 个有
- `LoraLoaderBypassModelOnly` —— 4/8 个有
- `ManualSigmas` —— 4/8 个有
- `SolAttnMiniMax` —— 4/8 个有
- `VHS_LoadVideo` —— 4/8 个有
- `BlockSparseAttention` —— 3/8 个有
- `INTConstant` —— 3/8 个有
- `LoadAudio` —— 3/8 个有
- `忽略多组孤海` —— 3/8 个有
- `ComfySwitchNode` —— 1/8 个有
- `EmptyImage` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `MiniMaxH3SigmaShift` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `PrimitiveBoolean` —— 1/8 个有
- `QWEN_TextDisplay` —— 1/8 个有
- `RHLLMChatNode` —— 1/8 个有
- `VHS_LoadAudioUpload` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
