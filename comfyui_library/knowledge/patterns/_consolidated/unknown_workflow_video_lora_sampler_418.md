---
name: unknown_workflow_video_lora_sampler_418
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.873571
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelPreviewOverrideKJ, PreviewAny, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/H3最精准的动作迁移（支持多人）_2117882854582603778.json, 平台全量/H3角色替换提示词调整版_2113842946683523074.json, 平台全量/H3角色替换简易版_2110633674113896449.json, 平台全量/Viggle 6步Pika角色替换_2120437453331984385.json, 视频生成/图生视频/minimax-H3角色替换 动作迁移提示词调整版_2115034226574848002.json, 视频生成/图生视频/minimax-H3角色替换 动作迁移提示词调整版_2115040443187687426.json, 视频生成/视频生视频/Viggle 6步Pika视频编辑_2120743219825831937.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_418

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/H3最精准的动作迁移（支持多人）_2117882854582603778.json、平台全量/H3角色替换提示词调整版_2113842946683523074.json、平台全量/H3角色替换简易版_2110633674113896449.json、平台全量/Viggle 6步Pika角色替换_2120437453331984385.json、视频生成/图生视频/minimax-H3角色替换 动作迁移提示词调整版_2115034226574848002.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelPreviewOverrideKJ`
- `PreviewAny`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 6/7 个有
- `CM_FloatToInt` —— 5/7 个有
- `CreateVideo` —— 5/7 个有
- `MiniMaxH3PromptEnhancerT8` —— 5/7 个有
- `TextGenerate` —— 2/7 个有
- `BatchImagesNode` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `MiniMaxH3AddGuide` —— 1/7 个有
- `SmartImageConcat` —— 1/7 个有
- `SomethingToString` —— 1/7 个有
- `StringReplace` —— 1/7 个有
- `VHS_LoadVideoFFmpeg` —— 1/7 个有
- `VHS_SelectEveryNthImage` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
