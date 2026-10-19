---
name: unknown_workflow_video_sampler_unet_37
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.688875
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, LoadImage, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/H3文生视频，首尾帧+放大_2086693311015907329.json, 视频生成/文生视频/H3极速二采高质量图_文生视频(胸部大小可控)_2090731045871251457.json, 视频生成/文生视频/H3极速二采高质量图_文生视频_2086494938853892097.json, 视频生成/文生视频/MiniMax H3｜参考图生视频+Pass2 二采精修_2087873476030984194.json, 视频生成/文生视频/MinimaxH3全能参考（二采高清放大）4步加速_2091790956046667778.json, 视频生成/文生视频/Minimax多参(双时钟8步高质量极速)V1_2085629759433822210.json, 视频生成/文生视频/minimaxH3二采高清放大工作流_2086773185634197505.json, 视频生成/文生视频/一采lora1.0 turbo8 8步 0.5清晰度，match，二采8步0.3，int8，lanczos，crf16_2092168952892977153.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_37

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/H3文生视频，首尾帧+放大_2086693311015907329.json、视频生成/文生视频/H3极速二采高质量图_文生视频(胸部大小可控)_2090731045871251457.json、视频生成/文生视频/H3极速二采高质量图_文生视频_2086494938853892097.json、视频生成/文生视频/MiniMax H3｜参考图生视频+Pass2 二采精修_2087873476030984194.json、视频生成/文生视频/MinimaxH3全能参考（二采高清放大）4步加速_2091790956046667778.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 7/8 个有
- `ImageResizeKJv2` —— 7/8 个有
- `KSamplerSelect` —— 7/8 个有
- `LoraLoaderBypassModelOnly` —— 7/8 个有
- `PT_H3ConcatAVLatent` —— 7/8 个有
- `PrimitiveFloat` —— 7/8 个有
- `VAEEncode` —— 7/8 个有
- `MiniMaxH3AudioConditioningT8` —— 5/8 个有
- `MiniMaxH3DualClockSamplerT8` —— 5/8 个有
- `CR Prompt Text` —— 4/8 个有
- `GetNode` —— 4/8 个有
- `LoadAudio` —— 4/8 个有
- `SetNode` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `VHS_LoadVideo` —— 3/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `MiniMaxH3ReferenceToVideo` —— 2/8 个有
- `CLIPTextEncode` —— 1/8 个有
- `ImageFromBatch` —— 1/8 个有
- `MiniMaxH3ImageToVideo` —— 1/8 个有
- `MuyeTextEditOutput` —— 1/8 个有
- `Text Multiline` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
