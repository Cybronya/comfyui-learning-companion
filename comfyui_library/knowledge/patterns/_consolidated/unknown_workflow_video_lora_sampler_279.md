---
name: unknown_workflow_video_lora_sampler_279
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.888571
common_nodes: [BasicGuider, BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/反推提示词/H3单采_2106693127930212353.json, 图片生成/反推提示词/H3官流（终极版）_2105139266958487554.json, 图片生成/图生图/H3高清快速出视频_2110660601948233729.json, 视频生成/图生视频/H3工作流最优解_2104970789329133569.json, 视频生成/图生视频/Minimax H3视频 完美人物替换！_2109512582699769858.json, 视频生成/图生视频/平面户型图生长视频-H3_2111329378872418306.json, 视频生成/文生视频/H3官流（终极版）_2105121771757334530.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_279

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/H3单采_2106693127930212353.json、图片生成/反推提示词/H3官流（终极版）_2105139266958487554.json、图片生成/图生图/H3高清快速出视频_2110660601948233729.json、视频生成/图生视频/H3工作流最优解_2104970789329133569.json、视频生成/图生视频/Minimax H3视频 完美人物替换！_2109512582699769858.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
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
- `PrimitiveStringMultiline` —— 5/7 个有
- `CR Prompt Text` —— 4/7 个有
- `PreviewAny` —— 4/7 个有
- `BatchImagesNode` —— 2/7 个有
- `CreateVideo` —— 2/7 个有
- `JjkText` —— 2/7 个有
- `LTXVConcatAVLatent` —— 2/7 个有
- `LTXVSeparateAVLatent` —— 2/7 个有
- `LayerUtility: TextJoin` —— 2/7 个有
- `MiniMaxH3LatentUpscaleBy32T8` —— 2/7 个有
- `RH_LLMAPI_Pro_Node` —— 2/7 个有
- `SaveVideo` —— 2/7 个有
- `llama_cpp_instruct_adv` —— 2/7 个有
- `llama_cpp_model_loader` —— 2/7 个有
- `llama_cpp_parameters` —— 2/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
