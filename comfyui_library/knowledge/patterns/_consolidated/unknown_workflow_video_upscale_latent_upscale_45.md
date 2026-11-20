---
name: unknown_workflow_video_upscale_latent_upscale_45
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.894889
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, ManualSigmas, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3高清打斗_2092544929284317185.json, 视频生成/图生视频/minimax_h3_r2v_story_board_2091816381816860674.json, 视频生成/图生视频/minimax_h3_r2v_video_edit_2092169538497503233.json, 视频生成/图生视频/minmax潜空间放大姿势迁移_2097668196026372098.json, 视频生成/图生视频/参考故事版生成视频 minimax H3_2092780996881113090.json, 视频生成/文生视频/（0825）二采放大1080P12秒-提示词未自动优化_2092123279141195777.json, 视频生成/文生视频/（0826）万象二采放大1080P横屏12秒-提示词未自动优化（增加动态lora）_2092578809114619905.json, 视频生成/文生视频/（0826）万象二采放大1080P竖屏12秒-提示词未自动优化（增加动态lora）_2092617053390856194.json, 视频生成/视频生视频/Minimax+H3+多参角色替换Lora，二采放大_2106244704005345281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_45

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3高清打斗_2092544929284317185.json、视频生成/图生视频/minimax_h3_r2v_story_board_2091816381816860674.json、视频生成/图生视频/minimax_h3_r2v_video_edit_2092169538497503233.json、视频生成/图生视频/minmax潜空间放大姿势迁移_2097668196026372098.json、视频生成/图生视频/参考故事版生成视频 minimax H3_2092780996881113090.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 8/9 个有
- `PrimitiveFloat` —— 8/9 个有
- `PrimitiveStringMultiline` —— 7/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `Text` —— 2/9 个有
- `VHS_LoadVideo` —— 2/9 个有
- `CreateVideo` —— 1/9 个有
- `DF_Get_image_size` —— 1/9 个有
- `FlashVSR_SM_KSampler` —— 1/9 个有
- `FlashVSR_SM_Model` —— 1/9 个有
- `GetImageRangeFromBatch` —— 1/9 个有
- `JWInteger` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `MiniMaxH3TurboLoRA` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `SaveVideo` —— 1/9 个有
- `VideoCombineV2` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.81296e+09 | - | 1 | 100% |
| Prompt 约束强度(CFG) | randomize | - | 1 | 100% |
| 采样算法 | 2 | - | 1 | 100% |
| 调度器 | 3.5 | - | 1 | 100% |
| 重绘幅度 | 11 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：采样步数 观测到 1.81296e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
