---
name: unknown_workflow_video_upscale_latent_upscale_27
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.859692
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/H3 八步图生视频｜5秒预检版_2098722980808445953.json, 视频生成/图生视频/H3+6宫格故事板StoryBoard 生成10~15流畅视频_2093301213247922177.json, 视频生成/图生视频/H3-R2V 分镜故事板（一键全自动生成视频）_2094235413853589505.json, 视频生成/图生视频/H3全栈式短剧 自动生成二次采样 h3 i2v fastH3 trim latent upscale_2110526500184354818.json, 视频生成/图生视频/H3参考模式_10步+3步Latent Upscaler_2090620971345596417.json, 视频生成/图生视频/MiniMax FastH3 v2全能参考高清放大VSA加速生成_2099780057341456385.json, 视频生成/图生视频/MiniMax H3 首尾帧3步快速生成+2采放大_2099689978258345985.json, 视频生成/图生视频/MiniMax H3 首尾帧3步快速生成_2100766250199773186.json, 视频生成/图生视频/MiniMax-H3 ref2va单模型二采无编解码放大_2093541824198701058.json, 视频生成/文生视频/H3基础模式_10步+3步Latent Upscaler_2090818143013924865.json, 视频生成/文生视频/MiniMax H3 活人感多合一视频工作流_2103421922276106242.json, 视频生成/文生视频/MiniMax H3 活人爱神8步_2097733630738128897.json, 视频生成/文生视频/MiniMax H3一键直出活人感女友二采工作流_2098322238746480641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_27

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/H3 八步图生视频｜5秒预检版_2098722980808445953.json、视频生成/图生视频/H3+6宫格故事板StoryBoard 生成10~15流畅视频_2093301213247922177.json、视频生成/图生视频/H3-R2V 分镜故事板（一键全自动生成视频）_2094235413853589505.json、视频生成/图生视频/H3全栈式短剧 自动生成二次采样 h3 i2v fastH3 trim latent upscale_2110526500184354818.json、视频生成/图生视频/H3参考模式_10步+3步Latent Upscaler_2090620971345596417.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 12/13 个有
- `ManualSigmas` —— 12/13 个有
- `PrimitiveStringMultiline` —— 12/13 个有
- `LoraLoaderModelOnly` —— 9/13 个有
- `MiniMaxH3ReferenceToVideo` —— 9/13 个有
- `MiniMaxH3SigmaShift` —— 9/13 个有
- `SplitSigmas` —— 9/13 个有
- `UNETLoader` —— 9/13 个有
- `ModelPreviewOverrideKJ` —— 7/13 个有
- `CreateVideo` —— 6/13 个有
- `SaveVideo` —— 6/13 个有
- `CS-MultiImageLoader` —— 4/13 个有
- `DiffusionModelLoaderKJ` —— 4/13 个有
- `Fast Groups Bypasser (rgthree)` —— 4/13 个有
- `MiniMaxH3ImageToVideo` —— 4/13 个有
- `SaveImage` —— 4/13 个有
- `UniBlockSwap` —— 4/13 个有
- `Fast Groups Muter (rgthree)` —— 3/13 个有
- `Label (rgthree)` —— 3/13 个有
- `LoadAudio` —— 3/13 个有
- `VHS_LoadVideo` —— 3/13 个有
- `BlockSparseAttention` —— 2/13 个有
- `PixaromaDuration` —— 2/13 个有
- `CR Text` —— 1/13 个有
- `PixaromaSizes` —— 1/13 个有
- `RH_LLMAPI_Pro_Node` —— 1/13 个有
- `RH_RhartImageV1OfficialEdit` —— 1/13 个有
- `ShowText|pysssss` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
