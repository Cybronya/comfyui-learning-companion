---
name: unknown_workflow_lora_sampler_unet_13
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7552
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3 15秒卡点混剪工作流 像素幻想Lab_2090775624343445505.json, 视频生成/图生视频/Minimax H3 人物替换 单人极速版_2109840033103568897.json, 视频生成/图生视频/Minimax H3 人物替换 双人极速版_2109844433255620610.json, 视频生成/图生视频/Minimax-动作迁移_2086299017864114177.json, 视频生成/图生视频/MinimaxH3 4步加速故事板九宫格分镜多参考图视频工作流_2084506449723617282.json, 视频生成/图生视频/【MINIMAX-H3】最强W版武戏-极速版_2111450852316770305.json, 视频生成/文生视频/15秒卡点混剪_2092720568926818306.json, 视频生成/文生视频/【MINIMAX-H3】八月最强文戏-低配版_2098599696725004290.json, 视频生成/文生视频/【二采-低配版】MinMaxh3日常短剧专用_2095180548556808193.json, 视频生成/文生视频/【二采】MinMaxh3动态打斗专用_2095187337885085698.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_13

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3 15秒卡点混剪工作流 像素幻想Lab_2090775624343445505.json、视频生成/图生视频/Minimax H3 人物替换 单人极速版_2109840033103568897.json、视频生成/图生视频/Minimax H3 人物替换 双人极速版_2109844433255620610.json、视频生成/图生视频/Minimax-动作迁移_2086299017864114177.json、视频生成/图生视频/MinimaxH3 4步加速故事板九宫格分镜多参考图视频工作流_2084506449723617282.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/10 个有
- `PrimitiveFloat` —— 8/10 个有
- `VHS_VideoCombine` —— 8/10 个有
- `H3SigmaRefiner` —— 6/10 个有
- `ModelAttentionBackend` —— 6/10 个有
- `CR Prompt Text` —— 4/10 个有
- `CreateVideo` —— 4/10 个有
- `ExtendIntermediateSigmas` —— 4/10 个有
- `GetNode` —— 4/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/10 个有
- `LoadAudio` —— 4/10 个有
- `MuyeTextEditOutput` —— 4/10 个有
- `PreviewImage` —— 4/10 个有
- `SetNode` —— 4/10 个有
- `忽略多组孤海` —— 4/10 个有
- `INTConstant` —— 3/10 个有
- `ShowText|pysssss` —— 3/10 个有
- `VHS_LoadVideo` —— 3/10 个有
- `llama_cpp_instruct_adv` —— 3/10 个有
- `llama_cpp_model_loader` —— 3/10 个有
- `llama_cpp_parameters` —— 3/10 个有
- `LTXVConcatAVLatent` —— 2/10 个有
- `LTXVSeparateAVLatent` —— 2/10 个有
- `MinimaxH3LatentUpscaler3D` —— 2/10 个有
- `SaveVideo` —— 2/10 个有
- `VHS_VideoInfoLoaded` —— 2/10 个有
- `PreviewAny` —— 1/10 个有
- `RH_LLMAPI_NODE` —— 1/10 个有
- `RH_LLMAPI_Pro_Node` —— 1/10 个有
- `XB_BatchImages` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
