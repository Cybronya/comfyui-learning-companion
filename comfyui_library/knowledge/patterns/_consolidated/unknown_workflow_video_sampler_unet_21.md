---
name: unknown_workflow_video_sampler_unet_21
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.774647
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/【MiniMax H3】短剧工作流_2110380691388194818.json, 视频生成/图生视频/【MiniMax_H3】短剧工作流_2110893565873311745.json, 视频生成/图生视频/【疯了的动态】Dasiwa_单采样25步无加速lora_2096793272898383874.json, 视频生成/图生视频/单图Minimax H3_2084901814679461889.json, 视频生成/图生视频/单图Minimax H3_2085688315197616129.json, 视频生成/图生视频/润哥教育IP数字人_H3_R2V_2111327138715623425.json, 视频生成/图生视频/（api）横屏640p坤坤H3官流无lora12步_2110413455923699713.json, 视频生成/图生视频/（api）竖屏608p坤坤H3官流无lora_2108200300300554241.json, 视频生成/图生视频/（api）竖屏768p坤坤H3官流_2108103067618070530.json, 视频生成/文生视频/H3-氛围感短视频_2096431562895220737.json, 视频生成/文生视频/H3-氛围感网红打卡点短视频制作_2096832540542857218.json, 视频生成/文生视频/H3无损融合单采【官方满血API画布级本地流】_2108739345095155713.json, 视频生成/文生视频/MiniMax H3  ref-多参考工作流（全接口开放内部开发版）_2094998770005135362.json, 视频生成/文生视频/MiniMax+H3+refV1.2Lora-多参考工作流（全接口开放内部开发版）_2096531122523033602.json, 视频生成/文生视频/MiniMax+H3+新ref V1.0 Lora 阿里8步版本-多参考工作流_2096537181975310338.json, 视频生成/文生视频/minimaxH3+访谈类数字人_2097651536854863873.json, 视频生成/文生视频/minimaxH3数字人工作流（音色参考）_2094688876832055298.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_21

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/【MiniMax H3】短剧工作流_2110380691388194818.json、视频生成/图生视频/【MiniMax_H3】短剧工作流_2110893565873311745.json、视频生成/图生视频/【疯了的动态】Dasiwa_单采样25步无加速lora_2096793272898383874.json、视频生成/图生视频/单图Minimax H3_2084901814679461889.json、视频生成/图生视频/单图Minimax H3_2085688315197616129.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
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
- `BasicScheduler` —— 16/17 个有
- `LoraLoaderModelOnly` —— 14/17 个有
- `ModelPreviewOverrideKJ` —— 12/17 个有
- `ModelAttentionBackend` —— 11/17 个有
- `LoadAudio` —— 8/17 个有
- `ManualSigmas` —— 7/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/17 个有
- `GetNode` —— 6/17 个有
- `SetNode` —— 6/17 个有
- `BlockSparseAttention` —— 5/17 个有
- `PathchSageAttentionKJ` —— 5/17 个有
- `MiniMaxH3SigmaShift` —— 4/17 个有
- `SolAttnMiniMax` —— 4/17 个有
- `VHS_LoadVideo` —— 4/17 个有
- `LoraLoaderBypassModelOnly` —— 3/17 个有
- `忽略多组孤海` —— 3/17 个有
- `AudioCrop` —— 2/17 个有
- `INTConstant` —— 2/17 个有
- `EmptyImage` —— 1/17 个有
- `PreviewImage` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
