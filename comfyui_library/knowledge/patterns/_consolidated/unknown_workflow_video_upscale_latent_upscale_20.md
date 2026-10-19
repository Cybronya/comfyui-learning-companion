---
name: unknown_workflow_video_upscale_latent_upscale_20
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.847214
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3 八步图生视频｜5秒预检版_2098722980808445953.json, 视频生成/图生视频/H3+6宫格故事板StoryBoard 生成10~15流畅视频_2093301213247922177.json, 视频生成/图生视频/H3-R2V 分镜故事板（一键全自动生成视频）_2094235413853589505.json, 视频生成/图生视频/H3全栈式短剧 自动生成二次采样 h3 i2v fastH3 trim latent upscale_2110526500184354818.json, 视频生成/图生视频/H3参考模式_10步+3步Latent Upscaler_2090620971345596417.json, 视频生成/图生视频/MiniMax FastH3 v2全能参考高清放大VSA加速生成_2099780057341456385.json, 视频生成/图生视频/MiniMax H3 首尾帧3步快速生成+2采放大_2099689978258345985.json, 视频生成/图生视频/MiniMax H3 首尾帧3步快速生成_2100766250199773186.json, 视频生成/图生视频/MiniMax-H3 ref2va单模型二采无编解码放大_2093541824198701058.json, 视频生成/文生视频/MiniMax H3 活人感多合一视频工作流_2103421922276106242.json, 视频生成/文生视频/MiniMax H3 活人爱神8步_2097733630738128897.json, 视频生成/文生视频/MiniMax H3一键直出活人感女友二采工作流_2098322238746480641.json, 视频生成/文生视频/MiniMax+H3多参双采latent放大版_2090080342467235842.json, 视频生成/文生视频/MiniMax+H3文生视频双采latent放大版_2090080368669057026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_20

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/H3 八步图生视频｜5秒预检版_2098722980808445953.json、视频生成/图生视频/H3+6宫格故事板StoryBoard 生成10~15流畅视频_2093301213247922177.json、视频生成/图生视频/H3-R2V 分镜故事板（一键全自动生成视频）_2094235413853589505.json、视频生成/图生视频/H3全栈式短剧 自动生成二次采样 h3 i2v fastH3 trim latent upscale_2110526500184354818.json、视频生成/图生视频/H3参考模式_10步+3步Latent Upscaler_2090620971345596417.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 13/14 个有
- `ManualSigmas` —— 13/14 个有
- `PrimitiveStringMultiline` —— 13/14 个有
- `ModelAttentionBackend` —— 12/14 个有
- `LoraLoaderModelOnly` —— 10/14 个有
- `MiniMaxH3ReferenceToVideo` —— 10/14 个有
- `MiniMaxH3SigmaShift` —— 8/14 个有
- `SplitSigmas` —— 8/14 个有
- `UNETLoader` —— 8/14 个有
- `ModelPreviewOverrideKJ` —— 7/14 个有
- `DiffusionModelLoaderKJ` —— 6/14 个有
- `Fast Groups Bypasser (rgthree)` —— 6/14 个有
- `SaveImage` —— 6/14 个有
- `UniBlockSwap` —— 6/14 个有
- `CS-MultiImageLoader` —— 5/14 个有
- `CreateVideo` —— 5/14 个有
- `Label (rgthree)` —— 5/14 个有
- `SaveVideo` —— 5/14 个有
- `LoadAudio` —— 4/14 个有
- `MiniMaxH3ImageToVideo` —— 4/14 个有
- `VHS_LoadVideo` —— 4/14 个有
- `Fast Groups Muter (rgthree)` —— 3/14 个有
- `BlockSparseAttention` —— 2/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/14 个有
- `PixaromaDuration` —— 2/14 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 2/14 个有
- `ShowText|fofo` —— 2/14 个有
- `CR Text` —— 1/14 个有
- `PixaromaSizes` —— 1/14 个有
- `RH_LLMAPI_Pro_Node` —— 1/14 个有
- `RH_RhartImageV1OfficialEdit` —— 1/14 个有
- `ShowText|pysssss` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
