---
name: unknown_workflow_video_sampler_unet_43
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.520222
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, ImageResizeKJv2, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PT_H3ConcatAVLatent, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEEncode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/lora1.0，match，二采0.35，一采turbo4_2092441692577288193.json, 图片生成/文生图/一采lora1.0 turbo4 8步 0.5 match 二采8步0.3 -时长修正版_2092183943792648194.json, 视频生成/图生视频/H3全能参考+二采放大_2086611990604238849.json, 视频生成/图生视频/H3全能参考+提示词全自动+二采+加速_2091371802969862145.json, 视频生成/图生视频/H3全能参考（二采高清放大）4步加速Lora_2087357939664379905.json, 视频生成/图生视频/【官模】H3单图案例：自媒体文案配视频_2089348331234484226.json, 视频生成/图生视频/【官模】双模型双采样：Lightx2v+8步加速 _ 自动反推提词+单图_2088972692887269377.json, 视频生成/文生视频/MiniMAX参数优化版_2089184857632100354.json, 视频生成/文生视频/MiniMax+H3多合一加速工作流，提示词优化，二采放大，多参，图生，文生，首尾帧_2087914357572325377.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_43

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/lora1.0，match，二采0.35，一采turbo4_2092441692577288193.json、图片生成/文生图/一采lora1.0 turbo4 8步 0.5 match 二采8步0.3 -时长修正版_2092183943792648194.json、视频生成/图生视频/H3全能参考+二采放大_2086611990604238849.json、视频生成/图生视频/H3全能参考+提示词全自动+二采+加速_2091371802969862145.json、视频生成/图生视频/H3全能参考（二采高清放大）4步加速Lora_2087357939664379905.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PT_H3ConcatAVLatent`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 8/9 个有
- `LoraLoaderBypassModelOnly` —— 8/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/9 个有
- `LoadAudio` —— 7/9 个有
- `PrimitiveFloat` —— 7/9 个有
- `VHS_LoadVideo` —— 7/9 个有
- `CR Prompt Text` —— 6/9 个有
- `MiniMaxH3AVDecodeT8` —— 5/9 个有
- `ModelAttentionBackend` —— 4/9 个有
- `VAEDecode` —— 4/9 个有
- `VAEDecodeAudio` —— 4/9 个有
- `VAEEncodeAudio` —— 4/9 个有
- `easy showAnything` —— 4/9 个有
- `CR Text` —— 3/9 个有
- `RHLLMChatNode` —— 3/9 个有
- `StringFunction|pysssss` —— 3/9 个有
- `easy clearCacheAll` —— 3/9 个有
- `ImageFromBatch` —— 2/9 个有
- `Label (rgthree)` —— 2/9 个有
- `LoraLoaderModelOnly` —— 2/9 个有
- `PrimitiveStringMultiline` —— 2/9 个有
- `AILab_ImageStitch` —— 1/9 个有
- `CreateVideo` —— 1/9 个有
- `FastGroupsBypassSwitch` —— 1/9 个有
- `INTConstant` —— 1/9 个有
- `ImpactSwitch` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `MiniMaxH3ImageToVideo` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `RH_LLMAPI_Pro_Node` —— 1/9 个有
- `Text Multiline` —— 1/9 个有
- `easy promptConcat` —— 1/9 个有
- `llama_cpp_instruct_adv` —— 1/9 个有
- `llama_cpp_model_loader` —— 1/9 个有
- `llama_cpp_parameters` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
