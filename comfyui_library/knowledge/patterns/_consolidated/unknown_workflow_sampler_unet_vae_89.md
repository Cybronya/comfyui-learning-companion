---
name: unknown_workflow_sampler_unet_vae_89
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.551667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/AITUDOU-MiniMax+H3+T2V（文生视频）加速流_2085602340672987137.json, 视频生成/文生视频/DG_H3 文生视频 BF16高质量_2085624042417123330.json, 视频生成/文生视频/Fastvideo H3 快速文生视频ComfyUI工作流_2095113472886534146.json, 视频生成/文生视频/MiniMax H3 I2V 图生视频 1280分辨率加速工作流_2085953821150367746.json, 视频生成/文生视频/MiniMax H3 T2V（文生视频）_2084242586428067841.json, 视频生成/文生视频/MiniMax H3 手机取物换装 文生视频_2106940320041750529.json, 视频生成/文生视频/MiniMax H3文生视频+首尾帧生视频_2084121630451789825.json, 视频生成/文生视频/MiniMax H3文生视频+首尾帧生视频（LightX2V加速LORA）_2087364613808672770.json, 视频生成/文生视频/minimax h3六宫生视频_2085919188304093186.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_89

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/AITUDOU-MiniMax+H3+T2V（文生视频）加速流_2085602340672987137.json、视频生成/文生视频/DG_H3 文生视频 BF16高质量_2085624042417123330.json、视频生成/文生视频/Fastvideo H3 快速文生视频ComfyUI工作流_2095113472886534146.json、视频生成/文生视频/MiniMax H3 I2V 图生视频 1280分辨率加速工作流_2085953821150367746.json、视频生成/文生视频/MiniMax H3 T2V（文生视频）_2084242586428067841.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 8/9 个有
- `MiniMaxH3ImageToVideo` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/9 个有
- `VHS_VideoCombine` —— 7/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `LoadImage` —— 5/9 个有
- `CR Prompt Text` —— 4/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `Text` —— 4/9 个有
- `CreateVideo` —— 3/9 个有
- `Label (rgthree)` —— 3/9 个有
- `SaveVideo` —— 3/9 个有
- `MiniMaxH3SigmaShift` —— 2/9 个有
- `ModelAttentionBackend` —— 2/9 个有
- `PathchSageAttentionKJ` —— 2/9 个有
- `MiniMaxH3AVDecodeT8` —— 1/9 个有
- `MiniMaxH3ReferenceToVideo` —— 1/9 个有
- `ModelPreviewOverrideKJ` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `StringConcatenate` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
