---
name: unknown_workflow_video_sampler_unet_74
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5848
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ImageResizeKJv2, KSamplerSelect, PT_H3ConcatAVLatent, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEEncode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MinimaxH3全能参考（二采高清放大）4步加速_2091790956046667778.json, 视频生成/文生视频/minimaxH3二采高清放大工作流_2086773185634197505.json, 视频生成/文生视频/一采lora1.0 turbo8 8步 0.5清晰度，match，二采8步0.3，int8，lanczos，crf16_2092168952892977153.json, 视频生成/文生视频/心然·寻源-Minimax H3 多模态参考生视频（双采加速版）_2087734113288679426.json, 视频生成/文生视频/海螺h3文生视频1080_2088596323753881602.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_74

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/MinimaxH3全能参考（二采高清放大）4步加速_2091790956046667778.json、视频生成/文生视频/minimaxH3二采高清放大工作流_2086773185634197505.json、视频生成/文生视频/一采lora1.0 turbo8 8步 0.5清晰度，match，二采8步0.3，int8，lanczos，crf16_2092168952892977153.json、视频生成/文生视频/心然·寻源-Minimax H3 多模态参考生视频（双采加速版）_2087734113288679426.json、视频生成/文生视频/海螺h3文生视频1080_2088596323753881602.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `PT_H3ConcatAVLatent`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `LoraLoaderBypassModelOnly` —— 4/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/5 个有
- `MiniMaxH3ReferenceToVideo` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `LoadAudio` —— 3/5 个有
- `MiniMaxH3AVDecodeT8` —— 3/5 个有
- `PrimitiveFloat` —— 3/5 个有
- `VHS_LoadVideo` —— 3/5 个有
- `ModelAttentionBackend` —— 2/5 个有
- `VAEDecode` —— 2/5 个有
- `VAEDecodeAudio` —— 2/5 个有
- `VAEEncodeAudio` —— 2/5 个有
- `CM_IntToFloat` —— 1/5 个有
- `EasyCache` —— 1/5 个有
- `FloatConstant` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `ImageFromBatch` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `MiniMaxH3AudioConditioningT8` —— 1/5 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
