---
name: unknown_workflow_video_lora_sampler_271
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.89525
common_nodes: [BasicGuider, BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/反推提示词/H3单采_2106693127930212353.json, 图片生成/反推提示词/H3官流（终极版）_2105139266958487554.json, 图片生成/图生图/H3官流（单采极速文戏）_2112910766088220674.json, 图片生成/图生图/H3高清快速出视频_2110660601948233729.json, 图片生成/图生图/道真数字人多场景通用版_2112188090025598978.json, 视频生成/图生视频/H3工作流最优解_2104970789329133569.json, 视频生成/图生视频/Minimax H3视频 完美人物替换！_2109512582699769858.json, 视频生成/文生视频/H3官流（终极版）_2105121771757334530.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_271

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/反推提示词/H3单采_2106693127930212353.json、图片生成/反推提示词/H3官流（终极版）_2105139266958487554.json、图片生成/图生图/H3官流（单采极速文戏）_2112910766088220674.json、图片生成/图生图/H3高清快速出视频_2110660601948233729.json、图片生成/图生图/道真数字人多场景通用版_2112188090025598978.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ManualSigmas` —— 6/8 个有
- `PreviewAny` —— 6/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `CR Prompt Text` —— 4/8 个有
- `BatchImagesNode` —— 2/8 个有
- `CreateVideo` —— 2/8 个有
- `ExtendIntermediateSigmas` —— 2/8 个有
- `LTXVConcatAVLatent` —— 2/8 个有
- `LTXVSeparateAVLatent` —— 2/8 个有
- `MiniMaxH3LatentUpscaleBy32T8` —— 2/8 个有
- `MiniMaxH3SigmaShift` —— 2/8 个有
- `RH_LLMAPI_Pro_Node` —— 2/8 个有
- `SaveVideo` —— 2/8 个有
- `llama_cpp_instruct_adv` —— 2/8 个有
- `llama_cpp_model_loader` —— 2/8 个有
- `llama_cpp_parameters` —— 2/8 个有
- `JjkText` —— 1/8 个有
- `LayerUtility: TextJoin` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
