---
name: unknown_workflow_video_lora_sampler_98
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.657111
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3 15秒卡点混剪工作流 像素幻想Lab_2090775624343445505.json, 视频生成/图生视频/MiniMaxH3巨构专用_图生视频_2115276904893870082.json, 视频生成/图生视频/MiniMaxH3首尾帧工作流 By 像素幻想Lab_2087128132951298049.json, 视频生成/图生视频/Minimax H3 图生视频_2084264368950304769.json, 视频生成/图生视频/Minimax H3 首尾帧_2089249903888392193.json, 视频生成/图生视频/MinimaxH3 海螺 4步lightx2v加速lora 多重提速 图生视频工作流_2084221979170795521.json, 视频生成/图生视频/【MINIMAX-H3】最强W版武戏-极速版_2111450852316770305.json, 视频生成/文生视频/15秒卡点混剪_2092720568926818306.json, 视频生成/文生视频/Minimax-H3剧情片工作台_2096851323793797122.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏-低配版_2100800495819517953.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏-高配版_2100787794460372994.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏_2094872667374571522.json, 视频生成/文生视频/【MINIMAX-H3】八月最强打斗武戏_2098355739667554306.json, 视频生成/文生视频/【MINIMAX-H3】八月最强文戏-低配版_2094683715619348482.json, 视频生成/文生视频/【MINIMAX-H3】八月最强文戏-低配版_2098599696725004290.json, 视频生成/文生视频/【MINIMAX-H3】打斗版-二采_2101165086437109761.json, 视频生成/文生视频/【二采-低配版】MinMaxh3日常短剧专用_2095180548556808193.json, 视频生成/文生视频/【二采】MinMaxh3动态打斗专用_2095187337885085698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_98

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3 15秒卡点混剪工作流 像素幻想Lab_2090775624343445505.json、视频生成/图生视频/MiniMaxH3巨构专用_图生视频_2115276904893870082.json、视频生成/图生视频/MiniMaxH3首尾帧工作流 By 像素幻想Lab_2087128132951298049.json、视频生成/图生视频/Minimax H3 图生视频_2084264368950304769.json、视频生成/图生视频/Minimax H3 首尾帧_2089249903888392193.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 16/18 个有
- `ResolutionSelector` —— 16/18 个有
- `H3SigmaRefiner` —— 14/18 个有
- `MiniMaxH3ReferenceToVideo` —— 13/18 个有
- `ModelAttentionBackend` —— 13/18 个有
- `CR Prompt Text` —— 11/18 个有
- `ExtendIntermediateSigmas` —— 11/18 个有
- `GetNode` —— 11/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/18 个有
- `LoadAudio` —— 11/18 个有
- `SetNode` —— 11/18 个有
- `忽略多组孤海` —— 11/18 个有
- `INTConstant` —— 10/18 个有
- `LTXVConcatAVLatent` —— 9/18 个有
- `LTXVSeparateAVLatent` —— 9/18 个有
- `MinimaxH3LatentUpscaler3D` —— 9/18 个有
- `PreviewImage` —— 8/18 个有
- `MiniMaxH3ImageToVideo` —— 5/18 个有
- `ShowText|pysssss` —— 5/18 个有
- `llama_cpp_instruct_adv` —— 4/18 个有
- `llama_cpp_model_loader` —— 4/18 个有
- `llama_cpp_parameters` —— 4/18 个有
- `MuyeTextEditOutput` —— 3/18 个有
- `PreviewAny` —— 3/18 个有
- `RH_LLMAPI_Pro_Node` —— 3/18 个有
- `ImageResizeKJv2` —— 2/18 个有
- `MiniMaxH3SigmaShift` —— 2/18 个有
- `CR Text` —— 1/18 个有
- `Label (rgthree)` —— 1/18 个有
- `StariAI-MiniMaxH3-Skill` —— 1/18 个有
- `XB_BatchImages` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
