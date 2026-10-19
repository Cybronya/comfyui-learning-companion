---
name: unknown_workflow_video_lora_sampler_32
type: Unknown Workflow
frequency: 25
level: moderate
coverage: 0.4508
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3官方工作流 _ 首尾帧生成视频_2090003109429989378.json, 视频生成/图生视频/MiniMax+H3  9 图_2088611634561503233.json, 视频生成/图生视频/MiniMax+H3+lightx2v+8step_2088449363017293825.json, 视频生成/图生视频/MiniMax+H3-8.24_2091826993972203521.json, 视频生成/图生视频/MiniMax+H3只保留多参数（文+图+音频+视频）生视频+二次高清放大视频（简约实用）_2087117739247890433.json, 视频生成/图生视频/MiniMax+H3私有化数字人系统（多参数版本）_2087100457863962625.json, 视频生成/图生视频/MiniMax+H3超级多合_2090252973527097346.json, 视频生成/图生视频/MiniMax+H3超级多合一工作流-官方版V2_2089267137377558529.json, 视频生成/图生视频/MiniMax+H3（文+图+音频+视频）生视频+二次高清放大视频_官方_关闭二阶版本_2087456299859660802.json, 视频生成/图生视频/MiniMax+H3（文+图+音频+视频）生视频+二次高清放大视频_官方本地版本_2087385271133364226.json, 视频生成/图生视频/MiniMax+H3（文+图+音频+视频）生视频+二次高清放大视频_官方本地版本_2087633586324336641.json, 视频生成/图生视频/MiniMax+H3（文+图+音频+视频）生视频+二次高清放大视频_官方本地版本_2087652786140962818.json, 视频生成/图生视频/MiniMax+H3（文+图+音频+视频）生视频+二次高清放大视频_官方本地版本_2087668195007221762.json, 视频生成/图生视频/MiniMax+H3（文+图+音频+视频）生视频+二次高清放大视频_官方版本_2087204342389624833.json, 视频生成/图生视频/MiniMax+H3（文+图+音频+视频）生视频_官方本地版本_关闭二阶版本_2087470453815336961.json, 视频生成/图生视频/MiniMaxH38高动态加速流_2091799612456783873.json, 视频生成/图生视频/多参考-MiniMax H3工作流_2087919826470793218.json, 视频生成/图生视频/开源MiniMax H3学习_2086616197088505858.json, 视频生成/图生视频/李哈哈自用2_2087374892856594433.json, 视频生成/图生视频/李哈哈自用2_2087377495900377089.json, 视频生成/图生视频/李哈哈自用4_2089313154718322689.json, 视频生成/图生视频/李哈哈自用_2087353819746361346.json, 视频生成/图生视频/自用minimax_2087019527124119553.json, 视频生成/文生视频/Fenglairh-MiniMax H3完整工作流集合最新加速-官方版_2087770654929145857.json, 视频生成/文生视频/Fenglairh-MiniMax H3完整工作流集合最新加速-官方版_2089022849863471105.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_32

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3官方工作流 _ 首尾帧生成视频_2090003109429989378.json、视频生成/图生视频/MiniMax+H3  9 图_2088611634561503233.json、视频生成/图生视频/MiniMax+H3+lightx2v+8step_2088449363017293825.json、视频生成/图生视频/MiniMax+H3-8.24_2091826993972203521.json、视频生成/图生视频/MiniMax+H3只保留多参数（文+图+音频+视频）生视频+二次高清放大视频（简约实用）_2087117739247890433.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 25 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Text` —— 24/25 个有
- `VAEDecode` —— 24/25 个有
- `LoadAudio` —— 23/25 个有
- `Fast Groups Bypasser (rgthree)` —— 22/25 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 22/25 个有
- `PreviewImage` —— 22/25 个有
- `PrimitiveFloat` —— 22/25 个有
- `RunningHub Deepcleaner` —— 21/25 个有
- `VHS_LoadVideo` —— 21/25 个有
- `ImageResizeKJv2` —— 20/25 个有
- `PT_H3ConcatAVLatent` —— 20/25 个有
- `VAEEncode` —— 20/25 个有
- `VAEEncodeAudio` —— 20/25 个有
- `孤海注释` —— 18/25 个有
- `MiniMaxH3AVDecodeT8` —— 15/25 个有
- `VAEDecodeAudio` —— 10/25 个有
- `MiniMaxH3ImageToVideo` —— 7/25 个有
- `FL_Audio_BPM_Analyzer` —— 2/25 个有
- `FL_Audio_Drum_Detector` —— 2/25 个有
- `Float` —— 2/25 个有
- `JWFloatToString` —— 2/25 个有
- `LoadAudioUI` —— 2/25 个有
- `ModelAttentionBackend` —— 2/25 个有
- `PreviewAny` —— 2/25 个有
- `Qwen3ASRLoader_DFT` —— 2/25 个有
- `Qwen3ASRTranscribe_DFT` —— 2/25 个有
- `RHLLMChatNode` —— 2/25 个有
- `SigmasGraph` —— 2/25 个有
- `TextCombinerSix` —— 2/25 个有
- `TextCombinerTwo` —— 2/25 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/25 个有
- `CRTFirstLastFrameSelector` —— 1/25 个有
- `FloatConstant` —— 1/25 个有
- `HAIGC_VideoLastFrame` —— 1/25 个有
- `Mesh2MotionExplore` —— 1/25 个有
- `PixaromaGroupSwitch` —— 1/25 个有
- `PrimitiveStringMultiline` —— 1/25 个有
- `RTXVideoSuperResolution` —— 1/25 个有
- `SaveImage` —— 1/25 个有
- `Text Multiline` —— 1/25 个有
- `easy clearCacheAll` —— 1/25 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
