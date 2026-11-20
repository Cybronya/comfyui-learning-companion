---
name: unknown_workflow_video_lora_sampler_123
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.523933
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Our_H3_AudioTalking_2Image_1Audio_2103836296480378882.json, 视频生成/文生视频/YZ金鱼-MiniMax H3-多参考生视频-优化版_2092878871120142337.json, 视频生成/文生视频/YZ金鱼-MiniMax H3-多参考生视频-优化版（自用）_2094632571828260866.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏-低配版_2100800495819517953.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏-高配版_2100787794460372994.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏_2094872667374571522.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏_2098355739667554306.json, 视频生成/文生视频/【MINIMAX-H3】八月最强文戏-低配版_2094683715619348482.json, 视频生成/文生视频/【MINIMAX-H3】八月最强文戏-低配版_2098599696725004290.json, 视频生成/文生视频/【MINIMAX-H3】打斗版-二采_2101165086437109761.json, 视频生成/文生视频/【二采-低配版】MinMaxh3日常短剧专用_2095180548556808193.json, 视频生成/文生视频/【二采】MinMaxh3动态打斗专用_2095187337885085698.json, 视频生成/文生视频/【去油人脸一致】MiniMax H3全能多参考潜空间放大_2094826523541983233.json, 视频生成/文生视频/【终极版本】MiniMax H3 双采高清工作流 提速不降质【AI小王子】_2095420966586376194.json, 视频生成/文生视频/动漫短剧武戏最强工作流（模型、提示词二选一）_2095498147790417922.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_123

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/文生视频/Our_H3_AudioTalking_2Image_1Audio_2103836296480378882.json、视频生成/文生视频/YZ金鱼-MiniMax H3-多参考生视频-优化版_2092878871120142337.json、视频生成/文生视频/YZ金鱼-MiniMax H3-多参考生视频-优化版（自用）_2094632571828260866.json、视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏-低配版_2100800495819517953.json、视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏-高配版_2100787794460372994.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 14/15 个有
- `LTXVConcatAVLatent` —— 14/15 个有
- `LTXVSeparateAVLatent` —— 14/15 个有
- `LoadAudio` —— 14/15 个有
- `MinimaxH3LatentUpscaler3D` —— 14/15 个有
- `PrimitiveFloat` —— 14/15 个有
- `SetNode` —— 14/15 个有
- `VAEDecodeAudio` —— 14/15 个有
- `忽略多组孤海` —— 12/15 个有
- `ExtendIntermediateSigmas` —— 11/15 个有
- `H3SigmaRefiner` —— 11/15 个有
- `INTConstant` —— 11/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/15 个有
- `ModelAttentionBackend` —— 11/15 个有
- `CR Prompt Text` —— 10/15 个有
- `PreviewImage` —— 7/15 个有
- `PreviewAny` —— 4/15 个有
- `RH_LLMAPI_Pro_Node` —— 4/15 个有
- `SplitSigmas` —— 4/15 个有
- `Text` —— 4/15 个有
- `easy float` —— 4/15 个有
- `VHS_LoadVideo` —— 3/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `Int` —— 1/15 个有
- `LamSwitcherCase` —— 1/15 个有
- `LoraLoaderBypassModelOnly` —— 1/15 个有
- `SoundFlow_GetLength` —— 1/15 个有
- `Text Multiline` —— 1/15 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
