---
name: unknown_workflow_sampler_unet_vae_76
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.7775
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 文生视频 _ 图生视频  首尾帧_1934647540794990594.json, 视频生成/文生视频/MiniMax H3 文生视频-comfyui版_2084188214616739841.json, 视频生成/文生视频/MiniMax H3 文生视频_2085450682408194050.json, 视频生成/文生视频/MiniMax H3 文生视频（SageAttention 加速版）_2085990359359909889.json, 视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086288381553762305.json, 视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086407187261378562.json, 视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086413769206489090.json, 视频生成/文生视频/MiniMax H3文生视频KJ加速版_2085281989065793537.json, 视频生成/文生视频/MiniMax-H3_插帧图生视频_2084843609874067458.json, 视频生成/文生视频/Minimax H3 图生视频 最新8步增速工作流+全节点注释_2088628478857015297.json, 视频生成/文生视频/Minimax H3 文生视频 最新8步增速工作流_2087823188460920833.json, 视频生成/文生视频/文生视频_图生视频MiniMax+H3_2084798105811251201.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_76

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 文生视频 _ 图生视频  首尾帧_1934647540794990594.json、视频生成/文生视频/MiniMax H3 文生视频-comfyui版_2084188214616739841.json、视频生成/文生视频/MiniMax H3 文生视频_2085450682408194050.json、视频生成/文生视频/MiniMax H3 文生视频（SageAttention 加速版）_2085990359359909889.json、视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086288381553762305.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 10/12 个有
- `KSamplerSelect` —— 10/12 个有
- `PrimitiveFloat` —— 10/12 个有
- `ResolutionSelector` —— 9/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/12 个有
- `LoadImage` —— 5/12 个有
- `LoraLoaderBypassModelOnly` —— 5/12 个有
- `CR Text` —— 4/12 个有
- `easy showAnything` —— 4/12 个有
- `GoohaiUniversalSlider` —— 2/12 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/12 个有
- `PreviewImage` —— 2/12 个有
- `VHS_VideoCombine` —— 2/12 个有
- `孤海图像缩放按像素` —— 2/12 个有
- `孤海注释` —— 2/12 个有
- `忽略多组孤海` —— 2/12 个有
- `GetImageSize+` —— 1/12 个有
- `RIFE VFI` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
